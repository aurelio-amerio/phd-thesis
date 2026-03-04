---
name: literature_research
description: General-purpose research skill for establishing state of the art, defining concepts, and collecting references for thesis chapters. Produces structured references.md files with data tables and bib-key lookups.
---

# Thesis Literature & Context Research

A unified research skill for gathering **state-of-the-art context**, **theoretical foundations**, and **specific references** for thesis chapters. This skill merges the capabilities of the former `literature_review` and `theory_context` skills.

## Target Notebook

- **Name**: `thesis references`
- **ID**: `1b7df790-7858-4fc8-879c-39f41238c4ae`
- **Strict Rule**: Exclusively use this notebook. Do not query other notebooks.

## When to Use This Skill

Use this skill when:

- **Establishing the state of the art** (e.g., "What is the evidence for Dark Matter?")
- **Defining a concept or standard physics** (e.g., "What is WIMP annihilation?", "How is the J-factor defined?")
- **Reviewing the current landscape** (e.g., "What are the current limits on WIMP annihilation?")
- **Collecting references for a chapter section** (e.g., "Find reviews and key papers for Chapter 1")
- **Citing standard results** (e.g., "Who first calculated the Tremaine-Gunn bound?")

**Do NOT use this skill** for extracting details from the author's own papers (`001)`). Use `paper_analysis` instead.
**Do NOT use this skill** for deep extraction from review articles (`002)`). Use `review_analysis` instead. This skill *identifies* relevant reviews; `review_analysis` *extracts* from them.

## Prerequisites

1. **Run `source_registry` first** to obtain the **Review Articles** (`002)`) source IDs.
2. This skill uses a **two-phase query strategy** (see below).

## Two-Phase Query Strategy

Research follows two phases: start narrow with curated reviews, then widen to all sources for gap-filling.

### Phase 1: Reviews Only (Big Picture)

Query **only Review Articles** (`002)` source IDs from `source_registry`) to establish the big picture, consensus definitions, and structural context.

```
mcp_notebooklm_notebook_query(
    notebook_id="1b7df790-7858-4fc8-879c-39f41238c4ae",
    query="<your question>",
    source_ids=<review_002_ids>  # only the ~8 review source IDs
)
```

**Why reviews first?** Reviews are curated, authoritative, and provide the "big picture." Starting here ensures the foundation is built on consensus before drilling into specifics.

### Phase 2: All Sources (Gap-Filling & Specifics)

For follow-up questions, clarifications, or finding specific papers that reviews mentioned but didn't detail — query **all sources** by simply **omitting `source_ids`** (defaults to the entire notebook).

```
mcp_notebooklm_notebook_query(
    notebook_id="1b7df790-7858-4fc8-879c-39f41238c4ae",
    query="<your follow-up or specific question>",
    conversation_id=<previous_conversation_id>  # maintains context from Phase 1
)
```

**Why omit `source_ids`?** With 170+ general references, passing them individually is impractical. Omitting the parameter lets NotebookLM search the entire corpus, which naturally includes reviews + all specific papers.

### When to Use Each Phase

| Phase | Use when... | `source_ids` |
|---|---|---|
| **Phase 1** (Reviews) | Establishing concepts, definitions, state of the art, structural guidance | `review_002_ids` only |
| **Phase 2** (All) | Finding specific papers, getting arXiv numbers, clarifying details, filling gaps | Omit entirely |

### Conversation Continuity

Use `conversation_id` (returned by each query) for follow-up questions. This is especially useful for the Phase 1 → Phase 2 transition:

1. **Phase 1**: "What are the main approaches to indirect DM detection?" → get `conversation_id`
2. **Phase 2**: "For each approach you mentioned, list specific papers with arXiv numbers" → pass `conversation_id`, omit `source_ids`

## Source Provenance Classification

Every reference identified during research falls into one of two categories:

| Type | Symbol | Meaning | Implication |
|---|---|---|---|
| **Direct Source** | ✅ | Paper is an individual source in the NotebookLM notebook | Content is directly queryable; we can extract details, equations, and context |
| **Referenced Source** | ❌ | Paper is only **cited within** a review or other notebook source | Content is NOT directly queryable; we must cite via the review that discusses it |

### How to Determine Provenance

1. Run `source_registry` — this gives the full list of notebook sources with titles (usually containing arXiv IDs)
2. For each reference found during queries, check whether its arXiv ID appears as a separate notebook source filename
3. If it does → ✅ Direct Source. If not → ❌ Referenced Source

### Why This Matters

When writing thesis text, we can only paraphrase and build arguments from sources we can actually read. For ❌ Referenced Sources, we rely on the review's discussion of that paper. The "Cited In" column in the data table tells us which review(s) to query for context about that paper.

### Lightweight Context via InspireHEP (Optional)

For ❌ Referenced Sources, you can use `mcp_inspirehep_get_paper_details` to retrieve metadata such as the **abstract**, author list, citation count, and publication info. This is useful when:

- **Evaluating whether a paper is worth citing** — the abstract helps judge relevance without needing full text
- **Disambiguating papers** — when a review mentions a result but doesn't specify which paper
- **Checking citation impact** — citation count helps gauge significance

```
# Wrap arXiv ID in URL to avoid numeric parsing issues:
mcp_inspirehep_get_paper_details(arxiv_id="https://arxiv.org/abs/1503.02641")
# Old-format IDs work directly (they contain letters):
mcp_inspirehep_get_paper_details(arxiv_id="hep-ph/0512090")
# Returns: title, authors, abstract, citation_count, publication info, etc.
```

> **⚠️ Guardrails**: This is a **triage tool**, not a content source. Use it to *decide* whether to cite a paper, not to *write* based on it. The abstract alone is insufficient for paraphrasing results or building arguments. For that, always rely on the review(s) that discuss the paper (listed in "Cited In"), or add the paper to the NotebookLM notebook as a full source.

## Citation Preference Hierarchy

When citing a claim or result, follow this priority order:

1. **Prefer review papers** (✅ Direct Sources, `002)` prefix) — they provide authoritative, synthesized context that is directly queryable
2. **Complement with the specific original paper** (often ❌ Referenced) — adds scholarly precision and credit to the original work
3. **Use notebook general references** (✅ Direct Sources without `002)`) when available — these give us direct content access
4. **Last resort**: cite a paper only mentioned in passing in a review, without detailed discussion

### Non-Peer-Reviewed Source Policy

> **Rule:** PhD theses and unpublished preprints must NEVER be the sole citation for a specific claim. Always pair with the original peer-reviewed paper.

| Source Type | Reliability | Usage |
|---|---|---|
| **Published books** (Hooper, Dodelson) | ✅ Fully reliable | Can be cited as sole reference for standard results and derivations |
| **PhD theses** (e.g., Pinetti 2021) | ⚠️ Not peer-reviewed | Cite for structural guidance, but always pair with original peer-reviewed paper |
| **Large preprints** (e.g., Cirelli 2024) | ⚠️ Widely cited but unpublished | Acceptable as review reference; complement with original papers for specific claims |

**Example citation pattern** (LaTeX):
```
The NFW profile~\cite{Navarro:1996gj} is the standard parametrization
for CDM halos (see~\cite{Cirelli:2024ssz} for a review).
```
Here `Cirelli:2024ssz` is ✅ (we can query it for details), while `Navarro:1996gj` is ❌ (cited within Cirelli). Both are cited, but the review provides processable context.

## Query Best Practices

1. **Granular Querying**: Never ask for an entire chapter at once. Break requests by sub-section (e.g., "1.1 Cosmological Context", "1.2 Particle Nature").

2. **Specific Prompt Engineering**:
   - **Dual-Reference Standard**: Always request **at least 2 distinct references** for each topic — complementary perspectives (e.g., Theory vs. Observation, or two contrasting reviews).
   - **Corpus Priority**: Prioritize sources **already in the NotebookLM corpus** (review articles, books) over external textbooks from general knowledge. Only cite external sources if the notebook lacks coverage.
   - **arXiv Numbers**: Explicitly ask for **"Specific Papers with arXiv numbers"** to get primary sources for citation.
   - **Relevance Justification**: Ask **"Why is it relevant?"** to ensure each source fits the narrative.
   - **Additional Sources**: Always request a list of **5–8 Additional Sources** per subsection, including authors, year, arXiv number, and a 5–10 word summary.

3. **Follow-up Queries**: Use `conversation_id` across both phases. For example:
   - Phase 1: "List relevant reviews on Indirect Detection" (with `source_ids=<review_ids>`)
   - Phase 2: "For the reviews you just listed, which specific papers do they cite for gamma-ray line searches?" (omit `source_ids`)

## Output

### 1. `references.md`

Save to `chapter_XX/references.md`. Follow the structure in `resources/references_structure.md`:

1. **Reviews & Textbooks** — general consensus
2. **Key Specific Papers** — primary sources
3. **References Breakdown by Section** — detailed mapping
4. **Reference Data Table** — structured table with **provenance tracking**

### 2. Reference Data Table

Include as **Section 4** of `references.md`. Format:

| Paper Name | Bib Key | In NB | Cited In |
|---|---|---|---|
| **Section Header** | | | |
| Planck 2018 VI | `Aghanim:2018eyx` | ✅ | — |
| NFW Profile | `Navarro:1996gj` | ❌ | Cirelli, Hooper, Pinetti |
| Some missing paper | **N/A** | ❌ | Cirelli |

**Column definitions**:
- **Bib Key**: looked up from `bibliography.bib` (or use InspireHEP MCP). **N/A** = needs adding.
- **In NB**: ✅ = separate source in NotebookLM, ❌ = only cited within a review
- **Cited In**: for ❌ papers, which review(s) discuss this paper (short names: Cirelli, Hooper, Dodelson, Pinetti, Bullock, etc.)

**Bib key lookup procedure**:
1. Extract the arXiv number from the NotebookLM response
2. Search `bibliography.bib` for the arXiv number using: `grep_search(query="<arxiv_number>", SearchPath="bibliography.bib", Includes=["*.bib"])`
3. If found, extract the bib key (the string after `@article{` or `@book{` etc.)
4. If NOT found, use `mcp_inspirehep_get_bibtex` to fetch the entry and append to `bibliography.bib`
5. If InspireHEP also fails, write **N/A** — this signals the user needs to add the entry manually

**Provenance lookup procedure**:
1. Get notebook sources from `source_registry` output
2. For each reference, check if its arXiv ID appears in any source title
3. Mark ✅ if found, ❌ if not
4. For ❌ entries, note which review(s) cited the paper based on the query response

### 3. Knowledge Insights

**REQUIRED**: After producing `references.md`, use the `knowledge` skill (save mode) to persist key insights to `.agent/knowledge/`. The `knowledge` skill defines the standard file format (YAML frontmatter + body) and handles deduplication.

## Usage Examples

### Scenario: Finding General Reviews
- **User**: "Find reviews on Indirect Detection."
- **Query**: `"List the most relevant review articles and books on Indirect Detection of Dark Matter. For each, explain why it is relevant."`

### Scenario: Finding Specific Citations
- **User**: "Who established the limits on neutrino masses?"
- **Query**: `"Provide a list of specific papers establishing limits on neutrino masses (e.g., Tremaine-Gunn), including arXiv numbers and a summary of the finding."`

### Scenario: Defining Standard Physics
- **User**: "Write the equations for the NFW profile."
- **Query**: `"Provide the mathematical definition of the NFW density profile and explain its parameters using standard references."`

### Scenario: Full Chapter Research
- **User**: "Research sources for Chapter 1."
- **Action**:
    1. Read `outline.md` to identify sub-topics for Chapter 1.
    2. Iterate through each sub-topic (1.1, 1.2, 1.3...).
    3. For each, run a query combining the strategies above.
    4. Compile into `chapter_01/references.md` with data table.
    5. Save key insights to `.agent/knowledge/`.
