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
4. **Reference Data Table** — structured table for quick lookup

### 2. Reference Data Table

Include as **Section 4** of `references.md`. Format:

| Paper Name | Authors | arXiv | Bib Key |
|---|---|---|---|
| Planck 2018 results... | Aghanim et al. | 1807.06209 | `Aghanim:2018eyx` |
| Gamma-ray evidence... | Belotsky et al. | 1212.6087 | `2014GrCo...20...47B` |
| Some missing paper... | Smith et al. | 2401.12345 | **N/A** |

**Bib key lookup procedure**:
1. Extract the arXiv number from the NotebookLM response
2. Search `bibliography.bib` for the arXiv number using: `grep_search(query="<arxiv_number>", SearchPath="bibliography.bib", Includes=["*.bib"])`
3. If found, extract the bib key (the string after `@article{` or `@book{` etc.)
4. If NOT found, write **N/A** — this signals the user needs to add the entry

### 3. Knowledge Insights

Save key insights as standalone `.md` files in `.agent/knowledge/`. Use descriptive filenames:
- `dark_matter_evidence_overview.md`
- `indirect_detection_current_limits.md`
- `nfw_profile_definition.md`

Each file should contain:
- A brief summary of the insight
- The source references (with arXiv numbers)
- The context in which it was gathered (which chapter/section)

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
