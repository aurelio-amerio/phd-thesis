# Eckner substantive pass — design

Date: 2026-08-28
Input: `reply_eckner.md` (8 deferred items: E-3.1, E-4.1, E-4.3, E-4.5, E-4.6, E-4.8, E-6.4, E-6.7) + author Review Mode annotations on that file.
Approved by author in chat (2026-08-28). Branch: `eckner-quick-pass` (continue; one review unit).

Conventions for the whole pass:
- All new/reworded prose wrapped in `\blue{}` (including reworded headings — use plain optional short title for TOC/bookmarks).
- Structural decisions only in this spec; final prose is drafted at implementation via `scientific-prose-writer` subagents (Fable/Opus only) for WP3, inline for mechanical WPs.
- Anything unverifiable gets `\aure{}`, never a guess.
- Bib entries only via InspireHEP/arXiv fetch.
- Update `reply_eckner.md` item statuses + summary table as each item lands; commit per work package.

## WP1 — Chapter 3 terminology rename (E-3.1)

Author decision: full rename, "background-dominated" is the preferred term.

- Chapter title → *Statistical Methods for Background-Dominated Regimes* (`chapter_03/chapter_3.tex:1`).
- Sweep thesis prose occurrences of "noise-dominated": `frontmatter/abstract_en.tex`, `resumen/resumen_en.tex`, `conclusion/conclusion.tex`, Ch. 3 intro, any cross-references in other chapters (full grep at implementation, incl. unhyphenated variants).
- Add a short defining passage at the top of `chapter_03/sections/3.0_introduction.tex`: photons plentiful; limitation is systematic uncertainty of astrophysical components → background/systematics-dominated, not statistics-limited. Addresses Eckner's "explain the term right at the start".
- Keep: `chapter_08/paper_xcorr/sections/appendix_formalism.tex:127` — technical shot-noise sense inside published paper text.

## WP2 — Small dN/dS-paper additions (E-6.4, E-6.7)

Both are thesis-side notes on published paper text; `\blue{}`-wrapped.

- E-6.4 (`chapter_06/sections/paper_dnds/sections/synthetic_map_generation.tex:179`): small footnote (author's preferred form) stating what "better stability" meant: fewer simulations needed for convergence; faster convergence to simulation ground truth; NN's own A_gal uncertainty larger than the Poisson-fit determination, so fixing it loses little. Source: author's annotation.
- E-6.7 (`chapter_06/sections/paper_dnds/sections/nn_architecture_training.tex`, preprocessing subsubsection): one clarifying sentence on negative-pixel handling, verified in the paper code (`thesis_project/mapGen/tfUtils.py _process_map`; `model_trainer_HL_v5.py find_min_max_counts_dataset`): no clipping; constant offset `1 − min_counts` (dataset-minimum scan) added before log10 — shifted logarithm mapping the most oversubtracted pixel to ≈1; oversubtracted pixels retain information at the low end.

## WP3 — Chapter 4 substantive rebalance (E-4.1, E-4.3+E-4.6, E-4.5, E-4.8)

One coherent pass; drafted section by section by prose subagents; fresh-context referee/humanizer review at the end (project rule).

- §4.1.4 (E-4.1): drop "prediction" framing. Structure: spectrum fixes (m, channel) — particle physics; morphology *measured*, fitted contracted NFW credible because N-body simulations of DM accretion independently produce steep, near-spherical halos (author's unpack point); single ⟨σv⟩ near thermal accounts for flux. Frame as internal consistency + economy, not prediction. Delete "No tuning of separate parameters" sentence; reword "three independent observables… could be described" line; keep "interpreted with care" pivot.
- §4.2.1 + §4.3 (E-4.3/E-4.6): author-specified order — introduce fixed-template analyses with the common-vulnerability critique first, then skyFACT as mitigating morphology mis-specification by construction, with its own caveats (regularization strength, input-template anchoring). Sweep §4.3 for blanket "all template-based" claims. Bib: arXiv:1705.04065 (skyFACT) if absent.
- §4.2.2 (E-4.5): deposition-mechanism paragraph where MSP-origin hypothesis is introduced (author-chosen placement): infalling GCs disrupt and deposit MSPs (Gnedin:2013cda, Brandt:2015ula, Fragione:2017rsp); NSC largely assembled from same disrupted clusters (self-consistency); therefore surviving GCs = natural calibration sample → chapter's strategy. One preview sentence in 4.0 roadmap. Coordinate with applied E-4.4 text (no duplicate density/channel argument).
- §4.3.3 (E-4.8): caveats paragraph on List et al. mirroring NPTF critique symmetry: (i) inherited diffuse templates; (ii) diffuse-model sensitivity (Fig. S12) with the worse-fit counterweight stated honestly; (iii) shared-spectrum simulator. Author framing: approximations + robustness remains to be demonstrated; move this framing before the result. Align §4.4 convergence claims and thesis conclusion.

## WP4 — Bookkeeping

- `reply_eckner.md`: statuses ⏳→✅, refresh counts line and summary table.
- Commit per WP; recompile check at end (chapter title change touches TOC).
