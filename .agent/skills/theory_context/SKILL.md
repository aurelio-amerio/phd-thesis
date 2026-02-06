---
name: theory_context
description: Research assistant for gathering general theoretical context and field consensus. Prioritizes Review Articles (002).
---

# Thesis Theory & Context Research

**Target Notebook**: `thesis references` (ID: `1b7df790-7858-4fc8-879c-39f41238c4ae`)
**Strict Rule**: Exclusively use the above notebook. Do not query other notebooks.

## When to Use This Skill
Use this skill when you need to **gather general information** or describe the **"State of the Art"**. It is context-driven, not chapter-driven.

*   **Are we defining a concept?** (e.g., "What is WIMP annihilation?")
*   **Are we reviewing the field?** (e.g., "What are the current limits on GCE?")
*   **Are we establishing specific physical backgrounds?** (e.g., "How is the J-factor defined?")

## Source Hierarchy

1.  **Primary: Review Articles (002)**
    *   **Goal**: Establish the "Big Picture" and generally accepted definitions.
    *   **Rule**: ALWAYS start queries here to get the consensus view.

2.  **Secondary: General References**
    *   **Goal**: Fill in technical details (derivations, specific experiments) mentioned in reviews.
    *   **Rule**: Use these to "drill down" after establishing the context.

3.  **Excluded: Author Papers (001)**
    *   **Rule**: Do not use `001)` papers to define general theory. Use them only if you specifically need to mention standard physics *as cited/used* in the papers (but even then, a general ref is usually better for the definition itself).

## Usage Examples

### Scenario: Setting the Stage
*   **User**: "I need to write the section introducing the Galactic Center Excess."
*   **Action**: Query `002)` reviews to get the history, the main interpretations (Dark Matter vs. Pulsars), and the current controversy.
*   **Prompt**: "Based on review articles '002)', outline the history and leading interpretations of the Galactic Center Excess."

### Scenario: Defining Standard Physics
*   **User**: "Write the equations for the NFW profile."
*   **Action**: Query General References (or Reviews) for the standard formula.
*   **Prompt**: "Provide the mathematical definition of the NFW density profile and explain its parameters using standard references."

### Scenario: Broad Comparison
*   **User**: "What are the typical uncertainties in this field?"
*   **Action**: Query `002)` for a high-level summary of systematic uncertainties.
*   **Prompt**: "According to the reviews, what are the dominant systematic uncertainties in gamma-ray dark matter searches?"
