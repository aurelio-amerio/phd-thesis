# Plan: Intra-Chapter Repetition Detection (Chapters 1–8)

## Context

The thesis integrates six papers across eight chapters. Because chapters were
drafted section-by-section (and several wrap externally-authored paper prose),
the same concept, fact, or number can end up **restated across multiple
sections of the *same* chapter** with only small variations. Cross-chapter
repetition of a concept is fine and expected — the concern is *intra-chapter*
redundancy that makes a chapter read as if it is circling the same point.

This task **detects and reports** that redundancy. It does **not** rewrite
anything — the author handles consolidation separately, guided by the reports.
Papers are read-only reference material; we never edit imported paper prose.

Goal: for each chapter 1→8, produce one markdown report enumerating every
overlap cluster with locations, severity, and a concrete handling suggestion.

## Scope decisions (confirmed with author)

- **Primary target — narrative vs. narrative:** overlaps *among the
  hand-written narrative sections* of a chapter (the `N.x_*.tex` files listed in
  the chapter wrapper). This is what we aim to reduce.
- **Secondary — narrative vs. paper (flag only):** the narrative legitimately
  *anticipates* the integrated paper, so some overlap is fine. But when a
  narrative section reproduces in heavy detail what the paper already details,
  flag it and suggest condensing the narrative to a short summary + a pointer to
  the paper section. **Never propose edits to the paper itself.**
- **Cross-chapter overlap is out of scope** — repeating a concept in a
  different chapter is acceptable and will not be reported.
- **Deliverable is a report only.** No `.tex` edits in this task.

## Per-chapter file map (what to read, what to skip)

Each chapter has narrative sections (READ + analyze) and an imported paper
subtree (READ as reference only, for the secondary flag; never edit).

| Ch | Narrative sections to analyze (in wrapper order) | Paper subtree (reference only) |
|----|--------------------------------------------------|--------------------------------|
| 1 | `1.0_introduction`, `1.1_evidence_for_dark_matter`, `1.2_wimp_paradigm`, `1.3_searching_for_dark_matter`, `1.4_indirect_detection`, `1.5_summary` | — (no paper) |
| 2 | `2.0_introduction`, `2.1_production_mechanisms`, `2.2_astrophysical_sky`, `2.3_fermi_lat`, `2.4_summary` | — |
| 3 | `3.0_introduction`, `3.1_inference`, `3.2_sbi`, `3.3_ml_astrophysics`, `3.4_domain_shift`, `3.5_cross_correlations`, `3.6_summary` | — |
| 4 | `4.0_introduction`, `4.1_discovery_and_characterization`, `4.2_msp_hypothesis`, `4.3_systematics_stalemate`, `4.4_breaking_the_stalemate` | `sections/paper_msp/sections/*` |
| 5 | `5.1_introduction`, `5.2_dark_matter_substructure`, `5.3_dm_subhalos_gamma_ray_targets`, `5.4_unassociated_sources` | `sections/paper_dm_halos/sections/*` |
| 6 | `6.0_introduction`, `6.1_limits_individual`, `6.2_source_count`, `6.3_sbi_cnn`, `6.4_transition` | `sections/paper_dnds/sections/*` |
| 7 | `7.0_introduction`, `7.1_limits_of_threshold`, `7.2_population_to_spatial` | `paper_dnds_catalog/sections/*` |
| 8 | `8.0_introduction`, `8.1_from_resolved_to_cosmic_web`, `8.2_cross_correlation_technique`, `8.3_ctao` | `paper_xcorr/sections/*` |

All paths relative to each `chapter_0X/` directory unless noted (Ch7/Ch8 paper
subtrees sit at the chapter root, not under `sections/`).

**Exclude entirely (do not read/analyze):**
- `chapter_01/sections/1.2_wimp_paradigm.backup.tex` — stale backup.
- `chapter_07/sections/7.3_transition_to_paper.tex` — orphaned, not built (but
  note its existence in the Ch7 report as a structural observation).
- `chapter_06/sections/paper_dnds/appendix/appendix_A.tex` — empty stub.
- `chapter_04/sections/paper_msp/tables/*.tex` — numeric tables.
- Standalone paper wrappers `paper_1.tex … paper_5.tex` — they re-`\input` the
  same leaf section files as the thesis bridges; analyze each leaf file once,
  via the thesis wrapper path, to avoid double-counting.

## Detection method

For each chapter, dispatch **one fresh-context subagent** (no drafting-session
familiarity bias, per CLAUDE.md's "review in fresh context" rule). The subagent:

1. Reads **all** of the chapter's narrative section `.tex` files in one context
   (each chapter is 6k–22k words — fits comfortably).
2. Reads the chapter's paper subtree section files as **reference only** (for the
   secondary narrative-vs-paper flag).
3. Performs a **semantic** comparison — catches paraphrased restatements with
   small variations, not just verbatim duplication. No automated lexical
   pre-scan (author chose the pure LLM reading pass).
4. Writes the per-chapter report (schema below).

Run **one chapter at a time**, sequentially. After each report, the author
reviews and does the actual consolidation as a separate task before we move to
the next chapter.

### Severity rubric (applied consistently across chapters)

- **High** — near-verbatim or full-detail restatement of the same
  fact/argument/number in 2+ narrative sections; a reader notices déjà vu.
- **Medium** — same concept explained twice with moderate detail overlap;
  consolidatable to one primary location + a cross-reference.
- **Low** — light thematic overlap or legitimate signposting/recap; noted but
  usually kept.

Calibration note: an introduction previewing and a summary recapping the
chapter is *expected* — flag intro/summary material only when it re-derives or
re-argues in substantive detail rather than signposting.

### Recommendation vocabulary

- `KEEP-primary / CUT-secondary` — pick the best location, delete the echo.
- `MERGE` — fold two partial treatments into one.
- `CONDENSE→xref` — keep one full treatment, shrink the other to a
  cross-reference (`as discussed in Section X.Y`).
- `CONDENSE→paper` — (secondary flag) narrative over-details paper content;
  shrink to a summary + pointer to the paper section. Paper untouched.

## Report schema (one markdown file per chapter)

Written to `repetition_reports/chapter_0X_overlaps.md`. Structure:

```
# Chapter X — Intra-Chapter Overlap Report

## Sections analyzed / excluded
(list of narrative files read; excluded files noted)

## A. Narrative-vs-narrative overlaps  [PRIMARY]
### A1. <short concept label>   — Severity: High/Med/Low
- Occurrence 1: <file> · Section X.Y · ~line N — "<short quote>"
- Occurrence 2: <file> · Section X.Z · ~line M — "<short quote>"
- Recommendation: <KEEP-primary/MERGE/CONDENSE→xref> — which stays, what changes
### A2. ...

## B. Narrative-vs-paper over-anticipation  [FLAG ONLY]
### B1. <concept> — Severity
- Narrative: <file> · Section X.Y — "<quote>"
- Paper covers in full: <paper section file>
- Recommendation: CONDENSE→paper (narrative only; paper untouched)

## C. Structural notes / borderline cases
(orphan files, numbering gaps, judgment calls left to author)
```

## Execution order

1. Create `repetition_reports/` at repo root (+ a short `README.md` index).
2. Chapter 1 → dispatch detection subagent → write `chapter_01_overlaps.md` →
   author reviews.
3. Repeat for chapters 2–8, one at a time, pausing for author review/rewrite
   between chapters.

## Critical files / references

- Chapter wrappers `chapter_0X/chapter_X.tex` — authoritative section order
  (already extracted; see the map above).
- CLAUDE.md — "Review in fresh context" rule (mandates the fresh subagent per
  chapter) and the chapter↔paper mapping.
- Reuse the `referee` skill's critical-reading posture as a model for the
  subagent brief, but the output here is an overlap inventory, not a full
  referee report.

## Verification

Repetition detection is a judgment task, so verification is review-based:
- Each report must cite **≥2 concrete locations** (file + section + quote) per
  cluster — a claim with a single location is not an overlap and must be dropped.
- Spot-check 2–3 flagged clusters per chapter by opening the cited `.tex` lines
  and confirming the quotes and locations are accurate (no hallucinated overlaps).
- Confirm no report proposes edits to any `paper_*/` file (papers are read-only).
- Confirm excluded files (backups, tables, orphans, standalone wrappers) do not
  appear as overlap sources.
