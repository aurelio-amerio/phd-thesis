# citecheck — Citation Pertinence Review Plugin

**Status:** design draft
**Date:** 2026-05-18
**Author:** Aurelio Amerio

## Problem

A LaTeX research thesis can contain 1000–2000 `\cite` references across many `.tex`
files. Some of these citations may be mistakenly inserted, swapped with an unrelated
key, or hallucinated entirely (e.g. inserted by an LLM-assisted draft). Manual
verification at this scale is infeasible.

We want a coarse, automated pertinence check that scores each `\cite` 1–10 against
the abstract of the cited paper, flagging citations that are not on-topic so the
author can review them by hand. The check is intentionally not a strict referee —
it is a cheap filter to surface obvious mistakes.

## Scope

- Input: one `.tex` file at a time (max ~100 citations per file in practice). The
  user invokes the skill repeatedly across files.
- Output: a markdown report + JSON sidecar at `.citecheck/{tex_basename}.{md,json}`.
- Sources of truth for abstracts: InspireHEP REST API (preferred — bibliography is
  physics-dominated) with the arXiv API as a fallback for entries Inspire does not
  index (ML / CS papers in particular). Non-arXiv, non-Inspire entries gracefully
  degrade to "no abstract".
- The skill does **not** modify the `.tex` file or `bibliography.bib`.

## Non-goals

- Field-specific quality scoring (e.g. citation impact, journal tier).
- Catching subtle mis-attribution where the abstract genuinely overlaps with the
  paragraph but the paper does not actually support the claim. This is a coarse
  filter, not a referee.
- Bibliography deduplication or key rewriting. Use the existing `fixref` skill for
  that.

## Packaging

`citecheck` is delivered as a standalone Claude Code plugin with its own marketplace
manifest, so it can later be published as an independent git repo.

```
citecheck-plugin/                              # plugin root, eventually its own git repo
  .claude-plugin/
    plugin.json
    marketplace.json
  agents/
    citecheck-scorer.md
  commands/
    citecheck.md
  skills/
    citecheck/
      SKILL.md
      scripts/
        extract_citations.py
        parse_bib.py
        fetch_abstracts.py
        collate_report.py
  README.md
  LICENSE
  .gitignore
```

While iterating it lives at `/Users/aure/Documents/Github/phd-thesis/citecheck-plugin/`.

`plugin.json`:
```json
{
  "name": "citecheck",
  "version": "0.1.0",
  "description": "Pertinence review for \\cite references in LaTeX research documents: parallel haiku scoring against InspireHEP abstracts to flag mistakenly inserted or hallucinated citations.",
  "author": { "name": "Aurelio Amerio" }
}
```

`marketplace.json` lives in the same repo and lists the plugin as a single entry, so
a `git clone` makes the repo browsable as a marketplace and installable as a plugin.

## Architecture overview

The plugin pairs:

- An **orchestrator skill** (Opus-class, `skills/citecheck/SKILL.md`) that handles
  bib parsing, citation extraction, abstract fetching, batching, dispatch, and
  collation — all via small deterministic Python helpers.
- A **scoring subagent** (Haiku, `agents/citecheck-scorer.md`) restricted to `Read`
  and `Write` tools, whose sole job is to read one input batch JSON and write one
  output batch JSON. No MCP, no Bash, no Edit.

This keeps Opus tokens off the per-citation work and removes any risk of subagent
side-effects.

```
/citecheck <file>
        │
        ▼
  [orchestrator]
        │
        ├─ parse_bib.py          (bibliography.bib → bib_index.json)
        ├─ extract_citations.py  (tex → citations.json with paragraph + heading)
        ├─ fetch_abstracts.py    (parallel HTTPS to Inspire → .citecache/)
        ├─ partition into batches of 15–20
        │
        ├─ Agent × N (haiku citecheck-scorer, parallel)
        │     └─ each reads batch_n_input.json, writes batch_n_output.json
        │
        └─ collate_report.py     (batches → .citecheck/{basename}.{md,json})
```

## Components

### 1. Citation extraction (`extract_citations.py`)

- Input: a single `.tex` file.
- Match only the bare `\cite` command (`grep` over the thesis confirms zero use of
  `\citep` / `\citet` / etc., and zero multi-line `\cite{...}`).
- Regex: `\\cite\s*\{([^}]+)\}`. Optional preceding `~` is naturally ignored.
- Strip LaTeX comments first (drop everything after an unescaped `%` to EOL) so
  commented-out citations are not picked up.
- Split the captured group on `,`, trim whitespace; emit one entry per key with the
  same line number for all keys in a `\cite{a,b,c}`.
- Per citation, record:
  - `bibkey`, `line` (1-indexed), `tex_file`
  - `paragraph`: enclosing block of non-blank lines (paragraph boundary = blank line
    or `\section{...}` / `\subsection{...}` / `\paragraph{...}`), capped at ~600
    chars
  - `section_heading`: nearest preceding `\section` / `\subsection` /
    `\subsubsection` (deepest of the three), as a one-line string

### 2. Bibliography parsing (`parse_bib.py`)

- Lightweight regex parser, no `bibtexparser` dependency.
- Split into entries by `^@\w+\{key,` headers; per entry extract `title`, `eprint`
  (arXiv ID), `doi`, `archiveprefix`, `year`, first `author`.
- Output: `{ bibkey: {title, arxiv_id, doi, year, first_author} }`.
- Cached on `bibliography.bib` mtime; only rebuilt when the bib file changes.

### 3. Abstract fetching (`fetch_abstracts.py`)

Input: list of bibkeys with no `.citecache/abstracts/{bibkey}.json` yet, joined with
their bib metadata.

Resolution order per key (first hit wins), Inspire preferred, arXiv as fallback so
ML / CS papers absent from Inspire are still resolved:

1. **Inspire by arXiv ID** → `GET https://inspirehep.net/api/literature?q=arxiv:{id}&fields=titles,authors,abstracts,arxiv_eprints,external_system_identifiers`
2. **Inspire by DOI** → `q=doi:{doi}`
3. **Inspire by title** → `q=title:{quoted_title}` — accept only if top hit's
   normalized title similarity to the bib title is ≥ 0.90.
4. **arXiv by arXiv ID** → `GET https://export.arxiv.org/api/query?id_list={id}`
   (Atom XML; parse `<title>` and `<summary>` from the single entry).
5. **arXiv by title** → `GET https://export.arxiv.org/api/query?search_query=ti:{quoted_title}&max_results=3` —
   accept only if a hit has normalized title similarity ≥ 0.90.

If all five paths fail, write `source: "not_found"`.

**Optional cross-check** (off by default, `--cross-check` flag): when the Inspire
result has `title_match: "mismatch"`, also query arXiv with the same ID. If arXiv's
title matches the bib title closely, prefer the arXiv abstract and mark
`source: "arxiv_xref"` with a `cross_check_note` field. This catches the case where
an Inspire arXiv-ID lookup happens to point at a different paper than the bib entry
intends.

Concurrency: `concurrent.futures.ThreadPoolExecutor` with 8 workers, 100 ms jitter,
one retry on 429/5xx with 500 ms backoff. The arXiv API has its own rate limit
(roughly 1 request/3 s recommended for bulk); the fetcher applies a per-host token
bucket so arXiv calls stay polite even when Inspire calls run hot.

**Title validation runs after every successful fetch** regardless of which path
matched, since a wrong arXiv ID in the bib entry would silently fetch the wrong
abstract:

- Normalization: lowercase, strip LaTeX (`{`, `}`, `\textit{}`, etc.), collapse
  whitespace, drop punctuation.
- Similarity: `difflib.SequenceMatcher.ratio()`.
- Thresholds:
  - `≥ 0.90` → `title_match: "ok"`
  - `0.70–0.90` → `title_match: "fuzzy"` (accept but flag)
  - `< 0.70` → `title_match: "mismatch"` (accept but flag prominently)

Cache file shape `.citecache/abstracts/{bibkey}.json`:

```json
{
  "bibkey": "2024JCAP...03..035A",
  "title": "CosmiXs: cosmic messenger spectra...",
  "authors_short": "Arina et al.",
  "year": 2024,
  "arxiv_id": "2312.01153",
  "inspire_id": "2729450",
  "doi": "10.1088/1475-7516/2024/03/035",
  "abstract": "We present...",
  "source": "inspire_arxiv",
  "title_match": "ok",
  "title_similarity": 0.97,
  "bib_title": "CosmiXs: cosmic messenger spectra...",
  "fetched_title": "CosmiXs: cosmic messenger spectra for indirect dark matter searches",
  "fetched_at": "2026-05-18T10:23:00Z"
}
```

`source` values: `inspire_arxiv` | `inspire_doi` | `inspire_title` | `arxiv_id` |
`arxiv_title` | `arxiv_xref` | `not_found` | `fetch_error`.

Not-found entries are still written so dead keys are not re-queried; a `--refresh`
flag forces re-fetch of `not_found` and `fetch_error` rows.

### 4. Scoring subagent (`agents/citecheck-scorer.md`)

```markdown
---
name: citecheck-scorer
description: Scores citation pertinence 1-10 for a JSON batch of \cite references with paragraph context and fetched abstracts. Reads input JSON path, writes output JSON path, takes no other actions.
tools: Read, Write
model: haiku
color: cyan
---

You are a citation-pertinence classifier for academic research documents.
You receive a JSON batch where each entry has the paragraph in which a
\cite was used, the surrounding section heading, the cited paper's title,
and its abstract. Your job is to judge whether the cited paper is a
reasonable reference for the claim being made in that paragraph.

Procedure:
1. Read the input JSON file at <input_path>.
2. For each citation, assign an integer score from 1 to 10 using the rubric.
3. Write the array of results to <output_path>. Do nothing else.

Rubric:
- 9-10: Abstract directly supports the specific claim in the paragraph.
- 7-8:  Same sub-topic; plausibly supports the claim but not the sharpest reference.
- 5-6:  Same broad research area; relevant background but not the specific claim.
- 3-4:  Adjacent field; tenuous connection to the paragraph.
- 1-2:  Off-topic; likely a wrong key, swapped citation, or hallucination.

Special cases:
- abstract_status == "not_found"  → score: null, reason: "no_abstract".
- abstract_status == "mismatch"   → score: null, reason: "title_mismatch".
- abstract_status == "fuzzy"      → score normally + flag: "fuzzy_title".

Output schema per citation: {id, bibkey, score, reason, flag?}
"reason" is one sentence, ≤ 140 chars, explaining the score.
Do not call any tool other than Read and Write. Do not edit any file
other than <output_path>.
```

### 5. Batch input/output schema

`batch_{n}_input.json`:
```json
{
  "batch_id": 3,
  "citations": [
    {
      "id": "c042",
      "bibkey": "2024JCAP...03..035A",
      "line": 187,
      "section_heading": "3.1.2 Likelihood-based inference",
      "paragraph": "The likelihood function describes ... \\cite{2024JCAP...03..035A} ...",
      "bib_title": "CosmiXs: cosmic messenger spectra...",
      "abstract": "We present an updated set of...",
      "abstract_status": "ok"
    }
  ]
}
```

`abstract_status` ∈ {`ok`, `fuzzy`, `mismatch`, `not_found`, `missing_bib_entry`,
`no_bib_metadata`, `fetch_error`}.

`batch_{n}_output.json`: array of `{id, bibkey, score, reason, flag?}`.

### 6. Orchestrator flow (`skills/citecheck/SKILL.md`)

1. Resolve target: validate `$ARGUMENTS` is an existing `.tex` file; walk up to find
   `bibliography.bib` (override `--bib <path>`).
2. Run `parse_bib.py` → `bib_index.json` (skipped if mtime unchanged).
3. Run `extract_citations.py <tex_file>` → `citations.json`. Bail with a clear
   message if zero citations.
4. Compute missing abstracts: for each unique bibkey check
   `.citecache/abstracts/{bibkey}.json`; build `missing_keys.json` for the rest.
5. Run `fetch_abstracts.py` to populate the cache (parallel HTTPS, title validation).
6. Build batches of 15–20 citations → `batch_{n}_input.json`. For each citation the
   orchestrator sets `abstract_status` as follows: `missing_bib_entry` if the bibkey
   is absent from `bib_index.json`; `no_bib_metadata` if the bib entry has no
   arXiv/DOI/title; otherwise it is read directly from the cache file
   (`ok` / `fuzzy` / `mismatch` / `not_found` / `fetch_error`). The corresponding
   abstract text is inlined when present.
7. Dispatch haiku scorers in parallel: one single message with N
   `Agent({subagent_type: "citecheck-scorer", ...})` calls.
8. Validate batch outputs (schema check); retry malformed/missing batches once.
9. Run `collate_report.py` → `.citecheck/{tex_basename}.md` and `.json`.
10. Wipe `.citecheck/.tmp/`. Print a one-line summary:
    `N citations · M needing review · K title-match issues · report at <path>`.

**Concurrency budget:** at most 8 parallel `Agent` calls per dispatch wave. For
files with >8 batches (>~160 citations), dispatch in waves of 8.

**Exit conditions:** the skill terminates after writing the report. It does not
modify the `.tex` file or `bibliography.bib`.

### 7. Slash command (`commands/citecheck.md`)

```markdown
---
description: Review citation pertinence in a LaTeX file against InspireHEP abstracts using parallel haiku scoring.
argument-hint: <path-to-tex-file>
---

Run the citecheck workflow on $ARGUMENTS. Use the `citecheck` skill.
```

### 8. Output report (`collate_report.py`)

Merges all `batch_*_output.json` and writes two artifacts:

`.citecheck/{tex_basename}.md` (human-readable, three sections in priority order):

```markdown
# Citation review: chapter_03/sections/3.1_inference.tex

**Total citations:** 23
**Average score:** 7.4
**Scored 1-4 (review):** 3
**Scored 5-6 (borderline):** 4
**Unscored:** 1 (no_abstract: 1, title_mismatch: 0)

---

## Title-match issues (manual check)

| line | bibkey       | bib title | fetched title       | similarity |
|------|--------------|-----------|---------------------|------------|
| 187  | Smith:2020   | "Foo bar" | "Wholly different"  | 0.31       |

## Citations needing review (score ≤ 4 first)

### line 42 — score 2 — bibkey `Jones:2019`
**Section:** 3.1.2 Likelihood-based inference
**Paragraph:** The likelihood function describes ... \cite{Jones:2019} ...
**Cited title:** *Quantum gravity in 11 dimensions*
**Reason:** Paper is about quantum gravity; paragraph is about Bayesian likelihoods — likely wrong key.

## Citations OK (score ≥ 5)

| line | score | bibkey       | title                       |
|------|-------|--------------|-----------------------------|
| 12   | 9     | CosmiXs:2024 | CosmiXs: cosmic messenger…  |
```

`.citecheck/{tex_basename}.json` mirrors the markdown with all structured fields per
citation: score, reason, abstract_status, similarity, paragraph excerpt, line.

## Re-run behaviour and caching

- Abstract cache `.citecache/abstracts/{bibkey}.json` is persistent across runs and
  files; this is the only thing that survives between invocations.
- Scoring is **never cached**: every run re-scores every `\cite` from scratch, since
  scores depend on the surrounding paragraph, which changes as the author edits.
- `.citecheck/.tmp/` is ephemeral, wiped at end of every successful run. A crashed
  run leaves it behind; the next run overwrites.
- The bib parser cache is keyed by `bibliography.bib` mtime.

## Failure modes

| Failure | Detection | Behaviour |
|---|---|---|
| Bibkey in `\cite{}` but not in `bibliography.bib` | bib index lookup misses | `score: null, reason: "missing_bib_entry"`, no Inspire call |
| Bib entry has no arXiv / DOI / title | parse_bib fields empty | `score: null, reason: "no_bib_metadata"`, flagged |
| Inspire returns no hit on any path | fetch resolution exhausted | Cache `source: "not_found"`, downstream `score: null, reason: "no_abstract"` |
| Inspire hit but title similarity < 0.70 | post-fetch validator | Cache `title_match: "mismatch"`, downstream `score: null, reason: "title_mismatch"`; top report section |
| Inspire HTTP 429 / 5xx | fetcher | One retry with 500 ms backoff; on second failure `source: "fetch_error"` |
| Subagent malformed JSON | orchestrator schema validates | Retry batch once; second failure → `score: null, reason: "scoring_failed"` for that batch |
| `bibliography.bib` not found by walk-up | resolver | Skill fails fast with explicit error |
| Zero citations in file | extractor empty | Skill exits cleanly with "no citations found"; no report written |
| Cached `source: "fetch_error"` | cache reader | Treated as miss; re-fetched |
| Cached `source: "not_found"` | cache reader | Treated as hit; user can pass `--refresh-missing` to retry |

## Configuration knobs (initial)

- `--bib <path>` — override the walk-up resolver.
- `--refresh` — re-fetch all abstracts ignoring cache.
- `--refresh-missing` — re-fetch only `not_found` and `fetch_error` rows.
- `--cross-check` — enable Inspire-vs-arXiv cross-check on title mismatches.
- `--no-arxiv-fallback` — restrict resolution to Inspire only.
- `--batch-size <n>` — default 15.
- `--parallel <n>` — default 8.

## Smoke test

Initial validation target: `chapter_03/sections/3.1_inference.tex` (~13 citations
on the current revision; manageable for spot-checking). Acceptance: report exists,
all citations scored or flagged, ≥ 1 citation surfaced as a known case the author
can adjudicate by eye in under five minutes.

## Out of scope (future work)

- Acting on findings — replacing wrong keys, removing hallucinated entries. Stays
  manual or delegated to `fixref`.
- Cross-file deduplication / global bib audit. Skill stays single-file.
- Additional sources beyond Inspire and arXiv (ADS, CrossRef, Semantic Scholar) for
  entries indexed by neither — books, software, blog posts, conference proceedings
  not on arXiv.
- Score caching by `(bibkey, paragraph hash)` for incremental re-runs.
