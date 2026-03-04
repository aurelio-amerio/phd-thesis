---
description: Write thesis prose for a specific section or subsection. Usage: /draft X.Y or /draft X.Y.Z (e.g., /draft 1.2.3)
---

# Draft Workflow

**Usage**: `/draft X.Y` or `/draft X.Y.Z`

Examples: `/draft 1.2` (subsection), `/draft 1.2.3` (subsubsection)

## Instructions

1. **Parse the section identifier** from the user's command.
   - `X.Y` → subsection mode (chapter X, section Y)
   - `X.Y.Z` → subsubsection mode (chapter X, section Y, subsection Z)

2. **Set the target chapter directory** to `chapter_0X` (zero-padded, e.g., `chapter_01`).

3. **Load and execute the `section_drafting` skill** at `.agent/skills/section_drafting/SKILL.md`.

4. **Follow all steps** defined in the skill:
   - Step 0: Parse input and determine mode
   - Step 1: Context loading
   - Step 2: Source registry
   - Step 3: Knowledge retrieval
   - Step 4: Targeted NotebookLM research
   - Step 5: Draft writing (three-layer pipeline)
   - Step 6: Self-review
   - Step 7: Coherence check
   - Step 8: Output and iteration

## Writing Pipeline

The skill uses a three-layer writing pipeline:

1. **`scientific-writing`** — primary prose driver (load skill before writing)
2. **`humanizer`** — anti-AI post-processing pass
3. **Personal style adaptation** — author's voice, softened for clarity
