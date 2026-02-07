---
name: literature_review
description: Research assistant that generates structured `references.md` reports for thesis chapters. It identifies reviews, key papers, and section-specific additional sources via NotebookLM.
---

# Thesis Literature & Context Research

**Target Notebook**: `thesis references` (ID: `1b7df790-7858-4fc8-879c-39f41238c4ae`)
**Strict Rule**: Exclusively use the above notebook.

## When to Use This Skill
Use this skill when we are **establishing the state of the art**. It focuses on what *others* have done and the general consensus of the field.

*   **Are we writing an introduction?** (e.g., "What is the evidence for Dark Matter?")
*   **Are we describing the current landscape?** (e.g., "What are the current limits on WIMP annihilation?")
*   **Are we citing standard results?** (e.g., "Who first calculated the Tremaine-Gunn bound?")

## Strategy & Best Practices

1.  **Granular Querying**: Do not ask for an entire chapter at once. Break requests down by sub-section (e.g., "1.1 Cosmological Context", "1.2 Particle Nature").
2.  **Specific Prompt Engineering**:
    *   **Dual-Reference Standard:** Always propose **at least 2 distinct references** for each topic in the "Breakdown" section to provide complementary perspectives (e.g., Theory vs. Observation, or two contrasting reviews), prioritizing review articles and/or books. 
    *   **Crucial:** Prioritize Review Articles and books that are **already included in the NotebookLM corpus** (e.g., Physics Reports, Annual Reviews) over external textbooks proposed by general knowledge. Only cite external textbooks if the notebook lacks specific coverage.
    *   Explicitly ask for **"Specific Papers with arXiv numbers"** to get the primary sources for detailed citation.
    *   Ask **"Why is it relevant?"** to ensure the source fits the specific narrative argument.
    *   **Always** ask for a list of **"Additional Sources"** (5-8 papers) for each subsection, including authors, year, arXiv number, and a brief 5-10 word summary.
3.  **Structured Output**: Compile findings into a Markdown file that strictly follows the template provided in `resources/references_structure.md`.
    *   **Structure**:
        1.  **Reviews & Textbooks**: General consensus.
        2.  **Key Specific Papers**: Primary sources.
        3.  **References Breakdown by Section**: Detailed mapping of sections.
    *   **Location**: Always save the output to `chapter_XX/references.md` (e.g., `chapter_01/references.md`).

## Usage Examples

### Scenario: Finding General Reviews
*   **User**: "Find reviews on Indirect Detection."
*   **Action**: Query to find high-level summaries.
*   **Prompt**: "List the most relevant review articles and books on Indirect Detection of Dark Matter. For each, explain why it is relevant."

### Scenario: Finding Specific Citations
*   **User**: "Who established the limits on neutrino masses?"
*   **Action**: Query for specific papers.
*   **Prompt**: "Provide a list of specific papers establishing limits on neutrino masses (e.g., Tremaine-Gunn), including arXiv numbers and a summary of the finding."

### Scenario: Full Chapter Research
*   **User**: "Research sources for Chapter 1."
*   **Action**:
    1.  Read `outline.md` to identify sub-topics.
    2.  Iterate through each sub-topic (1.1, 1.2, 1.3...).
    3.  For each, run a prompt combining the above strategies: "List relevant reviews and specific papers (with arXiv numbers) for [Topic], explaining their relevance."
