---
name: paper_analysis
description: Research assistant for extracting specific methodology and results from the author's papers. Prioritizes Author Papers (001).
---

# Thesis Paper & Contribution Research

Extracts specific methodology, results, and justifications from **the author's own published papers** (`001)` sources). These papers are included **verbatim** in the thesis LaTeX, so this skill focuses on extracting precise details for cross-referencing — not for rewriting content.

## Target Notebook

- **Name**: `thesis references`
- **ID**: `1b7df790-7858-4fc8-879c-39f41238c4ae`
- **Strict Rule**: Exclusively use this notebook.

## When to Use This Skill

Use this skill when:

- **Describing the author's methodology** (e.g., "How did we train the network in Paper 1?")
- **Reporting the author's results** (e.g., "What was the specific exclusion limit we found?")
- **Explaining the author's specific choices** (e.g., "Why did we choose this specific ROI?")
- **Building transitions** between a contextual chapter and the inserted paper

**Do NOT use this skill** for general theory or definitions — use `literature_research` instead.
**Do NOT use this skill** for review article content — use `review_analysis` instead.

## Key Principle: Internal References, Not External Citations

The author's papers are included as-is in the thesis LaTeX. Therefore:

- **Do NOT** rewrite or summarize what the paper already says
- **DO** extract specific facts, numbers, and methods to reference from contextual chapters
- **DO** use internal references: "See Chapter 6, Sec. 6.2" or "as detailed in the following paper"
- **DO** identify the key contributions to highlight in the introductory paragraphs before each paper

## Author Papers Mapping

| Source Name | Thesis Location | Topic |
|---|---|---|
| `001) paper 1 - 2302.01947.pdf` | Chapter 6 (after) | Source-count distribution via SBI + Deep Learning |
| `001) paper 2 - 2306.16483.pdf` | Chapter 7 (after) | Probabilistic cataloging with sub-threshold info |
| `001) paper 3 - 2412.05220.pdf` | Chapter 4 (after) | MSPs in Globular Clusters → GCE implications |
| `001) paper 4 - 2503.14584v1.pdf` | Chapter 5 (after) | DM subhalos among unassociated sources + dataset shift |
| `001) paper 5 - 2505.20383.pdf` | Chapter 8 (after) | CTA sensitivity via cross-correlations |

## Prerequisites

1. **Run `source_registry` first** to obtain `001)` source IDs.

## MCP Tool Usage

### Querying Author Papers

```
mcp_notebooklm_notebook_query(
    notebook_id="1b7df790-7858-4fc8-879c-39f41238c4ae",
    query="<your question>",
    source_ids=<author_001_ids>,  # from source_registry, only 001) sources
    conversation_id=<previous_id>  # for follow-up drilling
)
```

### Targeting a Specific Paper

When you need details from a single paper, pass only that paper's source ID:

```
mcp_notebooklm_notebook_query(
    notebook_id="1b7df790-7858-4fc8-879c-39f41238c4ae",
    query="Detail the domain adaptation methodology used in this paper.",
    source_ids=["<paper_4_source_id>"]
)
```

## Query Strategy

1. **Methodology Extraction**: Ask for step-by-step methods.
   - *Prompt*: `"Based on '001) paper 4', detail the domain adaptation methodology used to handle dataset shift. List the specific steps and techniques."`

2. **Results Extraction**: Ask for specific numbers and figures.
   - *Prompt*: `"Retrieve the forecasted sensitivity to Dark Matter from '001) paper 5'. What are the exact numerical limits?"`

3. **Choice Justification**: Ask why specific decisions were made.
   - *Prompt*: `"Summarize the motivation for targeting unassociated sources as described in the author's papers."`

4. **Key Contributions**: Extract the main takeaway for chapter introductions.
   - *Prompt*: `"What is the single most important contribution of '001) paper 1'? Summarize in 2-3 sentences suitable for an introductory paragraph."`

5. **Comparison with Literature**: Compare author results against the field.
   - *Prompt*: `"How do the results in '001) paper 3' compare to previous constraints on the MSP luminosity function?"`

## Output

### Internal Reference Notes

Structure output as notes for writing contextual chapters:

```markdown
## Paper [N] — Key Extractions

### Methodology Summary
- [Step 1]: [brief description] → detailed in Sec X.X of the paper
- [Step 2]: [brief description]

### Key Results
- [Result 1]: [exact value/limit]
- [Result 2]: [comparison with prior work]

### Contribution Statement (for chapter intro)
"[2-3 sentence summary of what this paper achieves and why it matters]"

### Transition Points
- **From context chapter to paper**: [how the introductory chapter leads into this paper]
- **From paper to next chapter**: [how this paper's conclusions set up the next chapter]
```

### Knowledge Saving

Save methodology insights to `.agent/knowledge/`:
- `paper1_sbi_methodology.md`
- `paper4_domain_adaptation_approach.md`
- `paper5_cross_correlation_sensitivity.md`

## Usage Examples

### Scenario: Describing Methodology
- **User**: "Explain how we handled the dataset shift in Paper 4."
- **Action**: Query `001) paper 4` specifically.
- **Query**: `"Based on '001) paper 4', detail the domain adaptation methodology used to handle dataset shift."`

### Scenario: Reporting Results
- **User**: "What was the final sensitivity we achieved for the CTA analysis?"
- **Action**: Query `001) paper 5`.
- **Query**: `"Retrieve the forecasted sensitivity to Dark Matter from '001) paper 5'."`

### Scenario: Building a Chapter Introduction
- **User**: "Write the introduction for Chapter 6, before Paper 1 is inserted."
- **Action**: Query `001) paper 1` for key contributions.
- **Query**: `"What is the key contribution and motivation of '001) paper 1'? What existing gap does it fill?"`
