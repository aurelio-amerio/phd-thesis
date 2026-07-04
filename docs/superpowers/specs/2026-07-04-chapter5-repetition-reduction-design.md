# Chapter 5 Revision: Repetition Reduction

**Date:** 2026-07-04
**Scope:** `chapter_05/sections/5.3` and `5.4` (narrative only). One resolved paper-intro trim, described below, was already made by the author.
**Inputs:** `repetition_reports/chapter_05_overlaps.md` (verified 2026-07-03), user directives from this session.

## Context: the wrapper contradiction is already resolved

The report flags (four times) that `5.6_paper_dmhalos.tex:1–3` claims the paper introduction is "replaced by the pedagogical introduction above," while `5.6:8` still `\input`s it — so the paper intro rendered, doubling the pedagogical §5.4. **The author has resolved this** by `%`-commenting the *pedagogical* portion of `paper_dm_halos/sections/introduction.tex` (lines 3–56: subhalo physics, 4FGL census, classify-and-count critique + three flaws, quantification-learning definition). The *concrete* paper setup (lines 58–92: "in this paper we construct a mixture model…", the formal $p(\bx|k)$ construction, and the paper roadmap) still renders and is deliberately kept — it is the hand-off into the paper body.

**Consequences for the report's B-cluster:**
- **B1** (classify-and-count + three flaws) — eliminated; the paper-intro copy is now commented, so §5.4.2 is correctly the sole full treatment.
- **B3** (4FGL census) — eliminated; paper-intro copy commented.
- **B4 part 1** (quantification definition / template matching) — eliminated; paper-intro copy commented.
- **B4 residual / B2** — the still-active paper intro (lines 67–81) and paper body (`statistical_analysis.tex`) remain, so §5.4.3's generative/mixture tail and its sigmoid-implementation detail still double them. These are in scope (author chose the aggressive §5.4.3 cleanup).

## Goals

Reduce intra-chapter redundancy per the report's A-cluster (narrative-vs-narrative) and the surviving B-residual, without gutting any section — each section must still stand alone with a one-line recap plus a cross-reference. No advocacy or physics content changes.

## Editing conventions (per Chapter 4 precedent)

- All new/modified text wrapped in `\blue{...}` (`macros.tex:58`). Per sentence/clause — `\blue{}` must not span paragraph breaks or contain `%`.
- Replaced sentences are **not deleted**: keep the original as a `%`-commented line directly above the replacement.
- Pure deletions (condensed repetition, no replacement) → comment out.
- Citations: existing bib keys only (all cite keys involved are already used in §5.4). No new BibTeX.
- **Preserve every `\aure{}` marker** in the touched passages (§5.4.1 line 17, line 25; §5.4.2 line 31, line 39).
- Prose wording is the implementer's decision; this spec fixes only *what* changes and *why*.

## Per-edit plan

All line numbers are current-source references; the implementer re-locates by content.

### A1 — CONDENSE→xref · `5.3_dm_subhalos_gamma_ray_targets.tex` (~line 33)
The "no stars/gas below ~10⁸ M☉ → emission is pure DM annihilation" premise is stated three times (§5.1 preview, §5.2.2 primary, §5.3). Keep §5.2.2 (`sec:5.2.2`, the dedicated "Luminous Satellites vs. Dark Subhalos" treatment) as primary; leave §5.1 (legitimate intro preview). In §5.3, **keep the distinct "exceptionally clean target vs. the Galactic Center" point** but drop the re-asserted no-stars/gas premise (and the ~10⁸ M☉ figure), replacing it with a cross-reference to `sec:5.2.2`.

### A2 — CONDENSE (keep formula, strip re-derivation) · `5.4_unassociated_sources.tex` (~line 57, §5.4.3)
The "posterior absorbs training-set prevalences" mechanism is stated in full in both §5.4.2 (verbal, primary) and §5.4.3. Keep §5.4.2 (lines 40–43) as the primary verbal mechanism. In §5.4.3 line 57: **keep the load-bearing Bayes decomposition** $p(k|\bx)\propto p(\bx|k)\,p(k)$ (it is the pivot that introduces $p(\bx|k)$, the subsection's subject) but strip the surrounding re-derivation prose, and **re-point the back-reference from `sec:3.4.2` to `sec:5.4.2`** so the two §5.4 subsections consolidate rather than both citing Chapter 3.

### A3 — back-reference add · `5.4_unassociated_sources.tex` (~line 38, §5.4.2)
"No DM subhalo has ever been identified" recurs across §5.4.1/5.4.2/5.4.3. Keep §5.4.1 line 24 as primary (carries the `\aure{}` about contested claims). At §5.4.2 line 38 the sentence is load-bearing as the first flaw — **keep it, add only a back-reference to `sec:5.4.1`**. Preserve the `\aure{review this statement}` on line 39.

### B4 residual — CONDENSE tail · `5.4_unassociated_sources.tex` (~lines 65–69, §5.4.3)
The generative-model / mixture / product-likelihood exposition now doubles the still-active paper intro (lines 67–81). Condense the five sentences to ~two: **retain the one-line mixture formula** $\tilde p_\mathrm{unas}(\bx)=\sum_k \pi_k\,p(\bx|k)$ (the chapter's conceptual crux) and **the new-class / free-prevalence argument** (the core of the quantification pitch), thin the generative-vs-discriminative re-explanation, and hand off to the paper. This edit also absorbs A3-occurrence-3 (the "class never observed" clause at line 66).

### B2 — CONDENSE→paper · `5.4_unassociated_sources.tex` (~lines 75–77, §5.4.3)
The shared-sigmoid covariate-shift *implementation* detail ($\tilde C(\bx;\btheta_\mathrm{cov})$, joint fitting) is pure paper-body material. **Keep the covariate-shift concept** (bright/high-latitude association bias) but drop the explicit sigmoid notation, replacing it with a pointer to the paper's `sec:stat-model` (verified to exist at `statistical_analysis.tex:101`).

## Out of scope / untouched

- A4 (ΛCDM "vast population" signposting) — expected preview→develop→recap, no action.
- §5.1 intro preview and §5.2.2 (the A1 primary).
- §5.4.2 classify-and-count full detail — now correct as the sole treatment (paper-intro copy commented).
- §5.4.3 results preview (lines 78–79) — legitimate roadmap anticipation; keep numbers in sync with the paper if ever touched.
- Stale commented block at `5.4:71–73` — already commented, not rendered; leave.
- The author's paper-intro commenting — already done, not re-litigated here.
- `paper_dm_halos/` prose (read-only), the 5.6 wrapper, tables, figures, other chapters.

## Verification

1. `latexmk` compile: no broken refs/labels (new xrefs `sec:5.2.2`, `sec:5.4.2`, `sec:5.4.1`, `sec:stat-model` all resolve); `\blue{}` balanced, none spanning paragraph breaks or containing `%`.
2. Fresh-context referee subagent reads revised §5.3/§5.4 cold: (a) each condensed passage still flows and no cross-reference is orphaned; (b) §5.4.3 still reads as self-contained motivation and the mixture crux survives; (c) the hand-off into the paper body still lands.
3. Diff review: every changed line is either a `%`-commented original or `\blue{}`-wrapped new text; every `\aure{}` marker preserved.
