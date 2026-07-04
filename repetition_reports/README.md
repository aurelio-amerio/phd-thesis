# Intra-Chapter Repetition Reports

Detection-only reports enumerating **intra-chapter** redundancy — the same
concept, fact, or number restated across multiple sections of the *same*
chapter. Cross-chapter repetition is out of scope (repeating a concept in a
different chapter is acceptable and is not reported here).

These reports **do not rewrite anything**. Consolidation is a separate task the
author performs, guided by each report. Imported paper prose (`paper_*/`) is
read-only reference material and is never edited or proposed for edit.

Generated per the plan
`docs/superpowers/plans/2026-07-03-intra-chapter-repetition-detection.md`, one
fresh-context subagent per chapter (per CLAUDE.md's "review in fresh context"
rule).

**Verification pass (2026-07-03).** Every report was independently re-verified
by a second round of fresh-context subagents: each claimed occurrence was
located in the current `.tex` sources, severities were re-judged, and each
recommendation was stress-tested against a *balanced* de-duplication philosophy
(each section should still stand alone with a one-line recap + cross-reference;
neither gut a section nor leave near-verbatim duplication). Reports were
updated in place: entries carry `Verification:` verdicts
(CONFIRMED / PARTIAL / FALSE-POSITIVE), revised recommendations are marked, new
overlaps found during the sweep were appended as new entries, and false
positives are struck through but retained for the record. Each report opens
with a summary of what changed. Non-repetition defects surfaced during
verification (wrong cross-references, numeric inconsistencies, stale wrapper
comments) are recorded in the C-sections.

## Report structure

Each `chapter_0X_overlaps.md` contains:

- **A. Narrative-vs-narrative overlaps [PRIMARY]** — redundancy among the
  hand-written narrative sections. This is what the task aims to reduce.
- **B. Narrative-vs-paper over-anticipation [FLAG ONLY]** — narrative that
  reproduces in heavy detail what the integrated paper already details; suggest
  condensing the *narrative* to a summary + pointer. Paper untouched.
- **C. Structural notes / borderline cases** — orphan files, numbering gaps,
  judgment calls.

## Severity

- **High** — near-verbatim / full-detail restatement in 2+ narrative sections.
- **Medium** — same concept explained twice with moderate detail overlap.
- **Low** — light thematic overlap or legitimate signposting/recap.

## Recommendation vocabulary

- `KEEP-primary / CUT-secondary` — pick the best location, delete the echo.
- `MERGE` — fold two partial treatments into one.
- `CONDENSE→xref` — keep one full treatment, shrink the other to a cross-reference.
- `CONDENSE→paper` — (Section B only) shrink over-detailed narrative to a
  summary + pointer to the paper section. Paper untouched.

## Index

| Chapter | Report | Title |
|---------|--------|-------|
| 1 | [chapter_01_overlaps.md](chapter_01_overlaps.md) | The Dark Matter Problem |
| 2 | [chapter_02_overlaps.md](chapter_02_overlaps.md) | The Gamma-Ray Sky and Fermi-LAT |
| 3 | [chapter_03_overlaps.md](chapter_03_overlaps.md) | Statistical Methods for Noise-Dominated Regimes |
| 4 | [chapter_04_overlaps.md](chapter_04_overlaps.md) | The Galactic Center Excess |
| 5 | [chapter_05_overlaps.md](chapter_05_overlaps.md) | Searching for Dark Matter Substructures |
| 6 | [chapter_06_overlaps.md](chapter_06_overlaps.md) | Extracting the Source-Count Distribution with Deep Learning |
| 7 | [chapter_07_overlaps.md](chapter_07_overlaps.md) | Probabilistic Cataloging |
| 8 | [chapter_08_overlaps.md](chapter_08_overlaps.md) | Cross-Correlations and Future Prospects |
