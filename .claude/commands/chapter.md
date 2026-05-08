---
description: Generate a detailed chapter outline for a specific thesis chapter. Usage: /chapter N (e.g., /chapter 5)
---

# Chapter Outline Workflow

**Usage**: `/chapter N` where N is the chapter number (e.g., `/chapter 5`)

## Instructions

1. **Parse the chapter number** from the user's command (the number after `/chapter`).
2. **Invoke the `chapter_outline` skill** using the Skill tool.
3. **Set the target chapter directory** to `chapter_XX` (zero-padded, e.g., `chapter_05` for chapter 5).
4. **Follow all 8 steps** defined in the `chapter_outline` skill:
   - Step 1: Context Analysis (read `outline.md` for the specific chapter)
   - Step 2: Source Registry
   - Step 3: Literature Research
   - Step 4: Review Analysis
   - Step 5: Paper Analysis (if applicable)
   - Step 6: Structural Research
   - Step 7: Draft `chapter_outline.md`
   - Step 8: Review and Refine

## Chapter-to-Number Mapping

Refer to `outline.md` for the full structure. Key mappings:

| Chapter | Title | Inserted Paper |
|---------|-------|----------------|
| 1 | The Dark Matter Problem | — |
| 2 | The Gamma-Ray Sky and Fermi-LAT | — |
| 3 | Statistical Methods for Noise-Dominated Regimes | — |
| 4 | The Galactic Center Excess (GCE) | Paper 3 |
| 5 | Searching for Dark Matter Substructures | Paper 4 |
| 6 | From Individual Sources to Populations | Paper 1 |
| 7 | Probabilistic Cataloging | Paper 2 |
| 9 | Generative Models for SBI (provisional) | Paper 6 |
| 10 | Cross-Correlations and Future Prospects | Paper 5 |
| 11 | Summary and Outlook | — |
