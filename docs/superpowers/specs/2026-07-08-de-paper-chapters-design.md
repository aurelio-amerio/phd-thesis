# De-paper-ing chapters 4–8 — design & subagent brief

**Date:** 2026-07-08
**Goal:** Chapters 4–8 reproduce the author's own papers almost verbatim. Reword every place the reproduced text refers to itself *as a standalone paper* so nothing reads as a lifted paper, and normalize each chapter's hand-off sentence to a canonical, properly-cited bridge. This is a wording pass only — no scientific content changes.

## Scope

- **In scope:** chapters 4, 5, 6, 7, 8 (the paper-integrated chapters), including their `paper_*/` subdirectories, tables, and figure captions.
- **Out of scope:** chapters 1–3, introduction, conclusion (hand-written review material with no reproduced paper). Do not touch.

## Execution model

Five **parallel Sonnet 5 subagents**, one per chapter. Each reads its **entire chapter** into context (the 1M window fits a full chapter comfortably) rather than doing a keyword grep, so it judges every self-reference with full context and catches implicit standalone-document framing a filter scan would miss.

The orchestrator collects the five reports into one consolidated summary. The author reviews the `\blue{}` diff in the compiled PDF.

## What each agent does

### 1. Scrub own-paper self-references
Rewrite every place the reproduced text refers to itself *as a paper*:
- Literal `this paper`, `in this paper`, `throughout this paper`, `the present paper`.
- Any equivalent standalone-document framing surfaced by the full read (e.g. "we present here…", "our results below…", section-structure sentences that describe the paper's own layout).

Replacement is **context-dependent** — the agent picks the best fit:
- `this chapter` for structural / section-layout / cross-reference sentences.
- `this work` / `this analysis` for methodological or results sentences.

Wrap each swapped fragment in `\blue{...}`.

### 2. Standardize the bridge sentence
Normalize the chapter's hand-off line (thesis narrative → reproduced content) to:

> The remainder of this chapter is based on `\cite{KEY}` and presents the analysis in full.

Bib keys (all already present in `bibliography.bib` — do **not** fetch or fabricate):

| Chapter | Key |
|---------|-----|
| 4 | `Amerio:2024qor` |
| 5 | `Amerio:2025fhz` |
| 6 | `Amerio:2023uet` |
| 7 | `Amerio:2023rjn` |
| 8 | `Pinetti:2025hgd` |

Notes:
- Ch7 currently says "presents the **original research paper**" — priority rewrite.
- Some chapters have more than one bridge-like sentence (e.g. ch7 has lines in `7.0_introduction`, `7.2_population_to_spatial`, `7.3_transition_to_paper`). Reconcile them so exactly one clean canonical bridge remains and the others don't re-introduce "paper" framing.
- Wrap the reworded bridge sentence in `\blue{...}`.

### 3. Hard exclusions (must not touch)
- **Third-party paper mentions** — any "paper" referring to someone else's work (e.g. `their companion paper~\cite{Leane:2020pfc}`, "Leane and Slatyer", "Buschmann et al."). Leave verbatim.
- **Commented-out lines** (`%` … ) — skip entirely.
- Already-acceptable self-reference words (`work`, `analysis`, `study`) — leave alone unless the sentence still frames the text as a standalone document.
- No scientific-content, number, or citation-key changes beyond the bridge normalization.

### 4. Report back
Return a markdown report with:
- **Changes table:** `file:line` · before → after (one row per edit).
- **Skipped third-party hits:** `file:line` · the phrase · why skipped — so the author can audit the judgment calls in one place.
- Bridge sentence: note the final form and which redundant bridge lines (if any) were removed.

## Marking convention
All reworded fragments wrapped in `\blue{...}` per the repo's revision convention, so the author and supervisor see exactly what changed in the compiled PDF. Applied directly to the files (no separate approval gate before editing).

## Safeguards / risks
- The main risk is a false positive on a third-party "paper" reference. Full-chapter context + the explicit skipped-hits report mitigate this; the author audits before accepting the `\blue` diff.
- Agents run in isolation on disjoint chapters → no write conflicts.
