# Chapter 7 — Repetition Reduction Design

**Date:** 2026-07-04
**Source report:** `repetition_reports/chapter_07_overlaps.md`
**Chapter:** 7 — Probabilistic Cataloging

## Goal

Reduce intra-chapter redundancy in Chapter 7, acting on the actionable
overlaps the verification-passed report flags. Explicit KEEPs and optional
polish are left untouched. Both narrative-vs-narrative (A) and
narrative-vs-paper over-anticipation (B) are in scope this pass.

## Scope

**In scope:** A1, A2, A3, A5, A7, A8, A9 (narrative-vs-narrative) + B1, B2,
B3, B4 (narrative over-anticipates the paper) + the low-severity duplicate
signpost note.

**Out of scope:** A4 (optional polish, KEEP-as-is), A6 (report verdict KEEP,
no action); the PCAT digression and QF-definition `\aure` open decisions
(left for the author); orphan `7.3_transition_to_paper.tex` (unbuilt); all
`paper_dnds_catalog/` files (read-only reference).

## Mechanics protocol (applies to every edit)

- **Removed text** → comment the old line(s) with `%`. Never delete; the old
  prose stays in the file for recoverability. Section files are one-sentence-
  per-line, so commenting is per-sentence and clean.
- **New / replacement text** → wrapped in `\blue{...}` (`\textcolor{blue}`,
  defined in `macros.tex:58`) so the change is visible in the rendered PDF.
- **Pure cut, no replacement** → comment the line only; nothing to blue.
- `\aure{}` WIP markers stay in place (house style).
- Design records structural decisions and target lines only. The actual
  `\blue{}` prose is authored at implementation time (drafter's job), not
  pre-written here.

## Editing order

Apply the 7.2 B-condensations (B1, B2/B3, B4) conceptually together with the
overlapping A-trims that share their blocks, so the collapsed prose composes.
Editing is by exact-string match, not line number, so the report's line-drift
warning does not apply. Line numbers below are report anchors — locate by
content.

## Edit plan

### `7.0_introduction.tex` (2 edits)
- **A1** (~L5): drop the "roughly 50 times" factor; keep the qualitative
  shape (`extends as ~S^-2 well below the nominal detection threshold`). The
  numeric factor lives in §7.1.2.
- **A3** (~L10): condense the core-idea sentence to a lighter *preview* — the
  method is developed in §7.2. Keep the hook, shed the mechanism detail.
- KEEP: A2 (L6), A4 apposition (L5) — 7.0 is their primary home.

### `7.1_limits_of_threshold.tex` (1 edit)
- **A8** (~L37–38): MERGE the two "Ch-6 dN/dS directly confirms/quantifies
  the sub-threshold population" statements. Line 34's parenthetical stays;
  comment L37–38, replace with one sentence keeping the full flux number
  (per A1 KEEP-primary here) + folding in "quantifies directly", dropping the
  duplicate Ch-6 re-reference.
- KEEP: A1 number (L38 primary), A4 (L35), A6 (L41–42).

### `7.2_population_to_spatial.tex` (5 blocks)
1. **Signpost** (~L13): comment out the second "Full details appear in the
   paper body" — L11 already carries the deferral + `\ref`.
2. **A1-occ3 + A2** (~L18–19): collapse to one disambiguated sentence
   (report's suggestion) — "Since the dN/dS carries no spatial content
   (Section~ref{sec:threshold_limits}), the question is how to leverage it to
   identify specific sky directions likely to host sub-threshold sources."
   Drops the restated 50× factor and the restated what/where.
3. **A3-occ3 + B1** (~L21–26): condense the full synthetic-sky recipe. Keep
   the *idea* (draw fluxes from dN/dS → random positions → same instrument
   pipeline → repeat many times); defer per-bin Poisson, exposure, GP, and
   the "5000" count to `sec:dnds_catalog_paper`. Drops the L22 restatement of
   the generative-model idea.
4. **Frequentist trio** (~L54–64, = B2 + B3): preview each of the three
   quantities in one conceptual sentence (§7.2 intro L12 promises the trio).
   Keep L55's local-vs-global TS *contrast* (A5's single narrative home).
   Lighten L56's near-verbatim "signal interest label" phrase (B3). Strip the
   operational QF-as-fraction definition and the α grid (B2) → defer to
   `statistical_framework.tex`. `\aure{check again the definition of the QF}`
   stays.
5. **"Two features" paragraph** (~L66–69, = A5 + B4 + A9): at L67 delete only
   the em-dash contrast insert (duplicates L55), keeping the advantage claim.
   At L68 drop the specific `Nside=512`/`0.12°` values (B4) → paper. Collapse
   the firing-pixel-map conclusion at L69 (A9) into the shortened L68–69 as
   one sentence; primary stays at L43.

## Verification

After edits: `latexmk`/`pdflatex` compiles clean; every commented line has a
`\blue{}` replacement (or is a deliberate pure cut); no `\aure` marker lost;
each section still stands alone with a one-line recap + cross-reference.
