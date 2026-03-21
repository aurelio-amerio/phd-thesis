---
description: Critical review of thesis sections or chapters. Usage: /review X.Y (section) or /review X (chapter)
---

# Review Workflow

**Usage**: `/review X.Y` (section review) or `/review X` (chapter review)

Examples: `/review 1.2` (review Section 1.2), `/review 1` (review all of Chapter 1)

## Instructions

1. **Parse the identifier** from the user's command.
   - `X.Y` → section review mode
   - `X` → chapter review mode

2. **Set the target chapter directory** to `chapter_0X` (zero-padded, e.g., `chapter_01`).

3. **Load and execute the `review` skill** at `.agent/skills/referee/SKILL.md`.

4. **Follow all steps** defined in the skill:
   - Step 1: Load context (outline, chapter_outline, references, draft files)
   - Step 2: Dimension-by-dimension review (rigor, citations, writing, structure, integration)
   - Step 3: Produce review report
   - Step 4: Present to user

## Review Dimensions

The skill evaluates five dimensions, drawing from `scientific-critical-thinking` and `scientific-writing`:

1. **Scientific Rigor** — claim evaluation, logical flow, fallacy detection
2. **Citation Quality** — coverage, specificity, recency, balance
3. **Writing Quality** — clarity, conciseness, precision, anti-AI check
4. **Structure & Transitions** — internal coherence, inter-section flow
5. **Thesis Integration** — outline alignment, cross-references, paper setup
