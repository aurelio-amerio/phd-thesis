---
name: paper_analysis
description: Research assistant for extracting specific methodology and results from the author's papers. Prioritizes Author Papers (001).
---

# Thesis Paper & Contribution Research

**Target Notebook**: `thesis references` (ID: `1b7df790-7858-4fc8-879c-39f41238c4ae`)
**Strict Rule**: Exclusively use the above notebook. Do not query other notebooks.

## When to Use This Skill
Use this skill when we are **making a statement concerning *my* research**. It focuses on what *your* thesis contributes to the field.

*   **Are we describing *my* methodology?** (e.g., "How did we train the network in Paper 1?")
*   **Are we reporting *my* results?** (e.g., "What was the specific exclusion limit we found?")
*   **Are we explaining *my* specific choices?** (e.g., "Why did we choose this specific ROI?")

## Source Hierarchy

1.  **Primary: Author Papers (001)**
    *   **Goal**: Extract the specific details of the work done in the thesis.
    *   **Rule**: ALWAYS prioritize these files. These contain the "Truth" of the thesis contribution.

2.  **Secondary: Comparison References**
    *   **Goal**: Compare *your* results to others.
    *   **Rule**: Only use General References to contrast against the Author Papers (e.g., "Our results are better than X because...").

## Usage Examples

### Scenario: Describing Methodology
*   **User**: "Explain how we handled the dataset shift in Paper 4."
*   **Action**: Query `001) paper 4` specifically to extract the domain adaptation technique used.
*   **Prompt**: "Based on '001) paper 4', detail the domain adaptation methodology used to handle dataset shift."

### Scenario: Reporting Results
*   **User**: "What was the final sensitivity we achieved for the CTA analysis?"
*   **Action**: Query `001) paper 5` for the specific sensitivity curve/value.
*   **Prompt**: "Retrieve the forecasted sensitivity to Dark Matter from '001) paper 5'."

### Scenario: Justifying Choices
*   **User**: "Why did we focus on unassociated sources?"
*   **Action**: Query `001)` papers to find the motivation written by the author.
*   **Prompt**: "Summarize the motivation for targeting unassociated sources as described in the author's papers '001)'."
