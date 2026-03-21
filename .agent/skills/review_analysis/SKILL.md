---
name: review_analysis
description: Research assistant for extracting detailed information from review articles (002). Produces citation-ready content with bib-key lookups for thesis incorporation.
---

# Thesis Review Article Analysis

Extracts detailed information from **review articles** (`002)` sources) for incorporation into the thesis text. Unlike `literature_research` (which *identifies* relevant reviews), this skill *extracts and structures* content from specific review articles for direct use in writing.

## Target Notebook

- **Name**: `thesis references`
- **ID**: `1b7df790-7858-4fc8-879c-39f41238c4ae`
- **Strict Rule**: Exclusively use this notebook.

## When to Use This Skill

Use this skill when:

- **Incorporating review content into thesis text** — the review is NOT included directly in the thesis, so its information must be paraphrased and cited
- **Extracting the narrative structure** of a review (e.g., "How does Cirelli (2024) structure the argument for indirect detection?")
- **Getting precise definitions or derivations** from review articles
- **Understanding how a topic transitions** from one concept to another in expert exposition

**Do NOT use this skill** for general reference gathering — use `literature_research` instead.
**Do NOT use this skill** for the author's own papers — use `paper_analysis` instead.

## Key Principle

Review articles are **external** to the thesis. Their content must be:
1. **Paraphrased** — never copy text directly
2. **Cited** — every claim needs a `\cite{bib_key}` reference
3. **Integrated** — woven into the thesis narrative, not just summarized

## Prerequisites

1. **Run `source_registry` first** to obtain `002)` source IDs.
2. Typically called **after** `literature_research` has identified which reviews are most relevant.

## MCP Tool Usage

### Querying Specific Reviews

```
mcp_notebooklm_notebook_query(
    notebook_id="1b7df790-7858-4fc8-879c-39f41238c4ae",
    query="<your question>",
    source_ids=<review_002_ids>,  # from source_registry, only 002) sources
    conversation_id=<previous_id>  # for follow-up drilling
)
```

**Filtering strategy**: Pass only the `002)` review source IDs to focus the AI on review literature. If you need a specific review, pass only that single source ID.

### Targeted Single-Source Queries

When you need to extract from a **specific** review article:

```
mcp_notebooklm_notebook_query(
    notebook_id="1b7df790-7858-4fc8-879c-39f41238c4ae",
    query="Based on this review, detail the structure and key arguments about [topic]",
    source_ids=["<single_review_source_id>"]
)
```

## Query Strategy

1. **Structure Extraction**: Ask for the table of contents or argument flow of a specific review.
   - *Prompt*: `"What is the detailed structure of [Review X] regarding [Topic]? List section headers and summarize the argumentation flow."`

2. **Concept Definitions**: Extract how the review defines standard concepts.
   - *Prompt*: `"How does [Review X] define [Concept]? Include any key equations or parameters."`

3. **Narrative Flow**: Understand how experts transition between ideas.
   - *Prompt*: `"How does [Review X] transition from [Concept A] to [Concept B]? What logical steps connect them?"`

4. **Specific Claims with Citations**: Get precise statements that can be paraphrased.
   - *Prompt*: `"What specific claims does [Review X] make about [Topic]? For each, note the section number and any papers they cite."`

5. **Comparative Views**: Compare how different reviews cover the same topic.
   - *Prompt*: `"Compare how [Review A] and [Review B] present [Topic]. What differences in emphasis or interpretation exist?"`

6. **Figure Identification**: Identify key figures from papers cited in the review that illustrate core concepts.
   - *Prompt*: `"Which figures from the papers discussed in [Review X] are considered canonical illustrations of [Topic]? For each, provide the paper's arXiv ID, figure number, and a brief description of what it shows."`
   - This feeds into `section_drafting` Step 4b and `paper_lookup` Recipe 3 for actual downloads.

## Output

### Citation-Ready Notes

Structure extracted content as:

```markdown
## [Topic] — from [Review Author (Year)]

### Key Points
- [Paraphrased claim 1] → `\cite{bib_key}`, Sec X.X
- [Paraphrased claim 2] → `\cite{bib_key}`, Sec Y.Y

### Definitions
- **[Term]**: [definition as given in review] → `\cite{bib_key}`

### Narrative Structure
1. The review begins by establishing...
2. It then transitions to...
3. The argument concludes with...

### Key Figures
- **Fig. N** from [arXiv:XXXX.XXXXX]: [description of what it shows] → illustrates [concept]
- **Fig. M** from [arXiv:YYYY.YYYYY]: [description] → illustrates [concept]
```

### Bib Key Lookup

For every reference extracted:
1. Get the arXiv number from the review's citations
2. Search `bibliography.bib`: `grep_search(query="<arxiv_number>", SearchPath="bibliography.bib")`
3. If found → use the bib key for `\cite{}`
4. If NOT found → flag as **N/A** and note the full reference so the user can add it

### Knowledge Saving

**REQUIRED**: Use the `knowledge` skill (save mode) to persist extracted insights to `.agent/knowledge/`. The `knowledge` skill defines the standard file format and handles deduplication.

## Usage Examples

### Scenario: Setting the Stage
- **User**: "I need to write the section introducing the Galactic Center Excess."
- **Action**: Query `002)` reviews to get the history, main interpretations (DM vs. Pulsars), and current controversy.
- **Query**: `"Based on the review articles, outline the history and leading interpretations of the Galactic Center Excess. Include specific section references."`

### Scenario: Defining Standard Physics
- **User**: "Write the equations for the NFW profile."
- **Action**: Query reviews for the standard formula and parameters.
- **Query**: `"Provide the mathematical definition of the NFW density profile and explain its parameters, citing the specific sections from the reviews."`

### Scenario: Broad Comparison
- **User**: "What are the typical uncertainties in this field?"
- **Action**: Query `002)` reviews for a high-level summary.
- **Query**: `"According to the reviews, what are the dominant systematic uncertainties in gamma-ray dark matter searches? List them with section references."`
