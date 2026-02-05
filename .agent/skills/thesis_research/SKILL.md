---
name: thesis_research
description: Research assistant for PhD thesis using NotebookLM. Enforces specific workflows for interacting with author's papers (001), reviews (002), and general references.
---

# Thesis Research Assistant

This skill manages interactions with the "Thesis Research & References" NotebookLM notebook. It enforces strict prioritization and logical flows based on file categories.

## Source Categories
1.  **Author's Papers (001)**: Files starting with `001)`. These are the core contributions.
2.  **Review Articles (002)**: Files starting with `002)`. High-level field overviews (Dark Matter, Cosmology).
3.  **General References**: All other files. Deep-dive, domain-specific details.

## Research Workflows

### 1. The "Author-First" Flow (Drafting & Specifics)
**Goal**: Write introductions or explain specific physics concepts used in your work.
*   **Step 1**: Query **ONLY** files starting with `001)`.
*   **Step 2**: Identify citations or referenced concepts within the retrieval.
*   **Step 3**: Perform a **Follow-up Query** on the "General References" to fetch details for those specific citations.
*   **Prompt Pattern**: "Based on papers '001)', explain [Topic]. Then, finding the references cited for [Topic], summarize their specific contribution from the general files."

### 2. The "Context-First" Flow (Integration & Reviews)
**Goal**: Integrate new information or understand the broader landscape.
*   **Step 1**: Query **ONLY** files starting with `002)`. Get the "Big Picture".
*   **Step 2**: Identify gaps where the review is too high-level.
*   **Step 3**: "Drill down" into "General References" to fill those gaps.
*   **Prompt Pattern**: "Using review articles '002)', outline the current state of [Topic]. Then, use the other references to provide specific experimental details on [Sub-topic]."

## Critical Rules
*   **Never** prioritize a General Reference over an Author Paper (001) for defining *your* methodology.
*   **Always** check `002)` reviews before claiming a statement is "universally accepted".
*   If a user asks about a specific paper title that isn't `001` or `002`, treat it as a General Reference lookup.
