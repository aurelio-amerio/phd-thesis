# Chapter 8 — Repetition Reduction Design

**Date:** 2026-07-04
**Source report:** `repetition_reports/chapter_08_overlaps.md`
**Chapter:** 8 — Cross-Correlations and Future Prospects

## Goal

Reduce intra-chapter redundancy in Chapter 8, acting on the actionable
overlaps the verification-passed report flags. Full pass: both
narrative-vs-narrative (A) and narrative-vs-paper over-anticipation (B) are in
scope. Delisted false positives and explicit KEEPs are left untouched.

## Scope

**In scope:** A1, A2, A3, A4, A6, A7, A9, A10, A11 (narrative-vs-narrative) +
B1, B2, B3, B4 (narrative over-anticipates the paper) + the C5 paper-typo
`\aure` flag (narrative only).

**Out of scope:** A5, A8 (delisted FALSE POSITIVES); C1/C2 as standalone
items (absorbed into the A-trims below); the paper subtree
(`paper_xcorr/` — read-only reference, never edited); `8.4_paper_xcorr.tex`
(standalone paper wrapper).

## Mechanics protocol (applies to every edit)

- **Removed text** → comment the old line(s) with `%`. Never delete; the old
  prose stays in the file for recoverability. Section files are
  one-sentence-per-line, so commenting is per-sentence and clean.
- **New / replacement text** → wrapped in `\blue{...}` (`\textcolor{blue}`,
  defined in `macros.tex`) so the change is visible in the rendered PDF.
- **Pure append/insert (an xref, no removal)** → add the inline `\blue{(cf. …)}`
  fragment only; nothing to comment, existing sentence untouched.
- **Pure cut, no replacement** → comment the line only; nothing to blue.
- `\aure{}` WIP markers stay in place (house style).
- Design records structural decisions and target lines only. The actual
  `\blue{}` prose is authored at implementation time (drafter's job), not
  pre-written here.

**Blue-block wrinkle.** Much of Chapter 8's duplication already sits inside
`\blue{}` WIP blocks (§8.2.3 L97–99; §8.3 L21, L26, L28–29, L47–48).
Compressing those blocks keeps the replacement blue — consistent with the
convention, no conflict. Commenting the old blue lines is fine.

## Keystone edit

**A10** is the chapter's highest-value consolidation: §8.1.2's closing
paragraph (L74–81) is a preview-in-full of §8.2.1, including a duplicate
walk-through of the *same figure* (`fig:window_main`). Collapsing it to two
sentences + an xref resolves the §8.1.2 side of A2, A3, **and** A7 in one
coherent move rather than three independent trims.

## Editing order

Editing is by exact-string match, not line number, so the report's line-drift
warning does not apply. Line numbers below are report/source anchors — locate
by content. Apply the §8.3 B-condensations (B1, B2, B3) together with the
overlapping A-trims that share their blocks (A3, A11), so the collapsed prose
composes.

## Edit plan

### `8.0_introduction.tex` (1 edit)
- **A11** (~L21): reword the hand-off clause so it does not triple with §8.3
  L57 and the paper bridge — vary the phrasing (e.g. "…quantifies what this
  combination can achieve").
- KEEP: A1-occ1 (L12–13, intro premise), A4-occ1 (L18, intro preview); A5/A8
  delisted.

### `8.1_from_resolved_to_cosmic_web.tex` (6 edits, all §8.1.2)
- **A1** (~L40): reword to break the "inside every gravitationally bound
  structure" verbatim echo of §8.0 L12–13. Keep a physics-motivated opening
  for §8.1 (L42 is a consequence clause, not a scene-setter).
- **A2** (~L70): drop the parenthetical "(because the flux is proportional to
  $\rho^2$ and thus weights dense, nearby structures more heavily)" — restates
  L49. Keep the sentence's main clause.
- **A6** (~L51): drop the "20–30\%" figure → pointer to §8.2.3 (the number's
  primary home, L82, where the argument consumes it).
- **A4** (~L68): inline-append a forward xref to §8.2.2 — L68 is the section's
  thesis statement, do not trim it further.
- **A9** (~L63–66): condense to one sentence per limitation, keeping **both**
  named (shot-noise mixing + no redshift resolution — the motivation climax
  needs both); repoint the existing L65 xref to also point to §8.2.2.
- **A10** (~L74–81): compress the `fig:window_main` walk-through to two
  sentences (qualitative "DM emission is local, blazar emission is not; a local
  catalog therefore selects the DM window") + "Section~\ref{sec:8.2.1} makes
  this argument quantitative (Fig.~\ref{fig:window_main})." Subsumes A2-L75,
  A3-L79, A7-L76.
- KEEP: A2-primary L49 (first full statement), A3 bare mention L71
  ("peaks at $z \sim 0.3$–0.4", carries §8.1.2's argument).

### `8.2_cross_correlation_technique.tex` (4 edits)
- **B4** (~L20): drop the $(1+z)^3\,e^{-\tau(E,z)}$ factors from the DM window
  expression; keep the load-bearing $\langle\sigma v\rangle\,\Delta^2(z)/m_\chi^2$
  (needed for the tomography argument at L21) and defer the full form to the
  appendix. **Verify the appendix label** (report cites `app:WDM` /
  `appendix_formalism.tex` L209–213) at implementation before writing the xref.
- **A2** (~L21–22): keep as the one-line recap (the window-function formula
  lives here and needs its conclusion stated); inline-append
  "(cf. Section~\ref{sec:8.1.2})".
- **A3** (~L28): trim the duplicated "$z \sim 0.4$–0.5 at 50 GeV" number —
  already stated at L25 ("$z \sim 0.3$–0.5 at $50\,\mathrm{GeV}$").
- **A7 + A3** (blue block ~L97–99): collapse to one sentence covering both the
  2MASS/2MRS-with-CTAO point and the EBL-horizon point (report's suggested
  wording: "the case for 2MASS and 2MRS is even stronger with CTAO: at TeV
  energies the EBL horizon (Section~\ref{sec:8.2.1}) removes the distant blazars
  while local DM photons arrive unabsorbed."). Subsumes A3-L99 and A7-L97/98.
- KEEP: A6-primary L82 (20–30\% figure lives here; optionally harmonize its
  `Ajello:2015mfa` citation with L51's `DGRB-review` when editing A6),
  A7-L31 (functional example in the overlap-integral argument), A7-L75–77
  (2MASS/2MRS catalog description).

### `8.3_ctao.tex` (5 edits + 1 flag)
- **B1** (~L21–22 + L42): keep the qualitative picture (two arrays, three
  telescope types, atmosphere-as-calorimeter, TeV reach, order-of-magnitude
  over current IACTs); drop the exact FoV enumeration
  ($4.3^\circ$/$7.5$–$7.7^\circ$/$8.8^\circ$) → paper §CTA. At L42, replace the
  repeated FoV values with "the wide, overlapping telescope fields of view
  (Section~\ref{sec:CTA})". Retain the LST/MST-for-extragalactic role used at
  L27.
- **B2** (~L38–43): highest-value cut — near-verbatim numeric duplication of
  paper §CTA (the narrative even cites "see Section~\ref{sec:CTA}" while
  restating every number). Compress to a qualitative sentence (~quarter-sky,
  $|b|>5^\circ$, ~uniform ~3 h exposure over three years, cf. §CTA); defer the
  pointing-grid/$400$ h/$600$ h/$0.51$ h/$1.11$ h/~10\% numbers to the paper.
- **B3** (~L47–49): state the off-source scenario in one sentence; drop the
  "~25×" and "factor ~4" quantitatives → paper/appendix (narrative already
  points to App.~\ref{app:expo}).
- **A3** (~L26 & L29): these duplicate each other *and* §8.2.1's EBL numbers;
  trim to "(cf. Section~\ref{sec:8.2.1})" + keep the one new point at L29
  (blazars remain the dominant TeV background). Remove the L26/L29
  number-for-number restatement.
- **A11** (~L57): shrink to "The paper that follows~\cite{Pinetti:2025hgd}
  applies this framework to forecast CTAO's dark matter sensitivity."
- **C5** (~L49, flag only): add an `\aure{}` flagging the likely "5 hrs → 50
  hrs" typo in the paper's `sensitivity_forecast.tex` L110. Narrative only;
  paper source untouched.

## Verification

After edits:
- `latexmk`/`pdflatex` compiles clean (no undefined refs from the new xrefs;
  confirm `app:WDM`, `app:expo`, `sec:CTA`, `sec:8.2.1`, `sec:8.2.2`,
  `sec:8.2.3`, `sec:8.1.2` all resolve).
- Every commented line has a `\blue{}` replacement, or is a deliberate pure cut
  (A2-L70 parenthetical, A3-L28 number, A3-L26 number).
- No `\aure` marker lost; C5 `\aure` added.
- Each section still stands alone with a one-line recap + cross-reference;
  §8.1.2's motivation climax (A9) still names both limitations.
