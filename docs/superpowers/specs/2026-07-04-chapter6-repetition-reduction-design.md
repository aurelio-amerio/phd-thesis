# Chapter 6 — Repetition Reduction Design

**Date:** 2026-07-04
**Source report:** `repetition_reports/chapter_06_overlaps.md`
**Chapter:** 6 — Extracting the Source-Count Distribution with Deep Learning

## Goal

Reduce intra-chapter redundancy in Chapter 6, acting on the High/Medium
overlaps the verification-passed report flags as needing action. Explicit
KEEPs and Low-severity borderline cases are left untouched.

## Scope

**In scope:** A1, A2, A4, A8, A9, A10 (narrative-vs-narrative) + B1, B4
(narrative over-anticipates the paper).

**Out of scope:** A3, A5, A6, A7 (report marks KEEP / no-action); B2, B3
(Low, borderline-acceptable); all paper subtree files (`paper_dnds/`, read-only).

## Mechanics protocol (applies to every edit)

- **Removed text** → comment the old line(s) with `%`. Never delete; the old
  prose stays in the file for recoverability. Section files are formatted
  one-sentence-per-line, so commenting is per-sentence and clean.
- **New / replacement text** → wrapped in `\blue{...}` (`\textcolor{blue}`,
  defined in `macros.tex:58`) so the change is visible in the rendered PDF.
- **Pure cut, no replacement** → comment the line only; nothing to blue.
- Design records structural decisions and target lines only. The actual
  `\blue{}` prose is authored at implementation time (drafter's job), not
  pre-written here.

## Edit plan

Line numbers are from the report; treat as approximate anchors and locate by
content.

### A1 + A2 — coupled, §6.0 intro (High)
- `6.0_introduction.tex` ~L9–12: comment the population-shift paragraph
  (the "vast population below the detection threshold" sentence + the "asking
  whether any specific source is a dark matter subhalo" pivot). Replace with a
  shorter `\blue{}` preview that forward-refs §6.1.2 and does **not** reuse
  either verbatim construction.
- §6.1.2 remains the KEEP-primary anchor for both facts.

### A1 — §6.2.1 duplicated UGRB definition (High)
- `6.2_source_count.tex` L19: comment the second parenthesized UGRB definition
  ("cumulative emission … forms the unresolved gamma-ray background (UGRB)")
  and the "inferred from statistical properties of the photon-count map" clause.
  `\blue{}` replace with a pointer — "the UGRB (Section~\ref{sec:6.1.2})" —
  keeping only the regime-ladder content specific to §6.2.1.

### A2 — §6.1.1 closing pivot (supporting, High cluster)
- `6.1_limits_individual.tex` L28: light condense of the "develop methods that
  extract population-level information" restatement so §6.1.2's opening
  (L33–34) is not pre-made one paragraph earlier. §6.1.2 stays the anchor.

### A4 — "empirical prior for Ch.7" bookend (Medium)
- `6.0_introduction.tex` ~L18: comment the "empirical prior for the
  probabilistic cataloging framework developed in Chapter 7" sentence. `\blue{}`
  replace with a bookend that drops the duplicated phrase (e.g. "feeds into the
  cataloging framework of Chapter~\ref{ch:7}"). §6.4 keeps the fuller version.

### A8 — §6.1.2 handoff merge (Low)
- `6.1_limits_individual.tex` L46–47: MERGE the two sentences (the "primary
  observable … is the source-count distribution" role-definition + "We define
  this distribution…") into one `\blue{}` handoff sentence that names $dN/dS$
  and points to §6.2. Removes the role-definition that the §6.2 opener restates
  without orphaning L47.

### A9 — §6.2 "central problem" repeats (Medium)
- `6.2_source_count.tex` L20: CUT (comment) — pure repeat of L6 fourteen lines
  later.
- L38: condense the "must be reconstructed statistically from the collective
  imprint" clause to "…reconstructed statistically (Section~\ref{sec:6.2.2})"
  in `\blue{}`. (Handled jointly with A10.)
- KEEP L6 (opener signposting) and L46 (launches §6.2.2).

### A10 — §6.2.1 double regime-ladder (Medium)
- `6.2_source_count.tex` L36–39: MERGE. Keep the first ladder (L16–20) as
  primary. In the synthesis paragraph (L36–39) comment the repeated
  catalog-measurement and statistical-reconstruction clauses; retain only the
  genuinely new quantitative anchors ($S^{-2}$ vs Euclidean $S^{-5/2}$ slope;
  $S_\mathrm{th}\sim 2\times10^{-10}$ cm$^{-2}$ s$^{-1}$). New connective prose
  in `\blue{}`.

### B1 — exact CNN training numbers (Medium)
- `6.3_sbi_cnn.tex` L46–47: comment the exact numbers (20 flux bins, flux range
  $[5\times10^{-12},10^{-7}]$, 21 outputs, $9\times10^5$ maps). `\blue{}` a
  one-line qualitative statement ("discretized non-parametric output; large
  simulated training ensemble") that defers the numbers to the paper body.
- **Preserve L48** — the conceptual "discretized representation is critical …
  non-parametrically" sentence carries the argument and stays.

### B4 — §6.4 proof-of-principle recitation (Medium)
- `6.4_transition.tex` L14–15: comment the "proof of principle" phrase and the
  trained-CNN / 14-year / 1–10 GeV recitation (the paper's rendered intro
  fragment restates all of it). `\blue{}` a single sentence keeping only the
  factor-50 headline, which the paper intro fragment does **not** state.

## Ordering / conflict notes

- **A9 + A10** both touch `6.2_source_count.tex` L36–39 — do them as one
  combined edit on that synthesis paragraph.
- **A1 + A2** both live at the §6.0 / §6.1.1-close / §6.1.2-open junction — one
  intro-paragraph rewrite handles both; §6.1.2 stays KEEP-primary throughout.
- Backups already exist (`*.bak0`) alongside each section file.

## Verification

- Compile the chapter with `latexmk` / `pdflatex` after edits; confirm no
  broken refs and that `\ref{sec:6.1.2}` / `\ref{sec:6.2.2}` / `\ref{ch:7}`
  resolve.
- Eyeball the rendered blue diffs to confirm each replacement reads cleanly and
  no `\aure{}` WIP markers were disturbed.
