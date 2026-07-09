# Resumen de la Tesis — Design

**Date:** 2026-07-09
**Status:** Approved structure, pending user review of this spec
**Deliverable:** `resumen/resumen_en.tex` (English draft, ≥5000 words ≈ 12 pages), later translated into `resumen/resumen.tex` (Spanish)

## Purpose

Spanish universities require an extended summary (resumen) of a thesis written in English. The model is the "Resumen de la Tesis" of the Loayza thesis (`PhD_Thesis_Loayza.pdf`, pp. 226–243, ~6,500 words): an unnumbered chapter after the bibliography with the arc *preface → background → objectives → methodology → results → conclusions*. We write the summary first in English, iterate until satisfied, then translate to Spanish.

## Ground rules

1. **Source of truth is the written thesis.** Every claim, number, and future direction in the resumen comes from prose already written in chapters 1–8, the abstract, or the frontmatter. No new content is invented. Chapter 9 (GenSBI) does not exist and is never mentioned.
2. **No bullet points.** Objectives and future directions are flowing prose, per the thesis convention, even though Loayza used bullet lists.
3. **Moderate equation density.** Only punchline equations (roughly 5–10 total): relic abundance / thermal cross section, the master annihilation-flux equation with the J-factor, the dN/dS definition, and at most a couple of methodological statements (e.g. the SBI posterior estimator, the cross-correlation spectrum). No derivations.
4. **Sparse citations.** `\cite` only where a specific measurement or claim demands it (e.g. Planck abundance, 4FGL, the five thesis papers), reusing existing `bibliography.bib` keys exclusively. No new bib entries.
5. **Numbers are verified, not recalled.** Every quantitative statement (luminosity function parameters, flux limits, percentages) is checked against the actual chapter text before being written.

## LaTeX setup

- Content lives in `resumen/resumen_en.tex` under the existing `\chapter*{Summary of the thesis}` header; `resumen/resumen.tex` keeps the Spanish `\chapter*{Resumen de la Tesis}` header and receives the translation later.
- Internal headings are `\section*` (unnumbered, matching Loayza); only the chapter appears in the TOC (already handled by `\addcontentsline`).
- Equations use the thesis `\be`/`\ee` macros.
- No glossary/acronym macros (`\gls` etc.): acronyms are spelled out at first use inside the resumen so the chapter is self-contained and the Spanish translation is not tied to English glossary expansions.
- While drafting, `main.tex:137` imports `resumen/resumen_en.tex`; when the Spanish translation is done, it switches back to `resumen/resumen.tex`.

## Structure and word budgets (~6,000 words total)

### Preface (~700 words, no equations)
Expansion of the abstract's opening: the evidence for dark matter and its unknown particle nature; WIMPs annihilating into Standard Model states; gamma rays as privileged messengers; fifteen years of Fermi-LAT and the maturity problem (bright targets exhausted, remaining signals faint, blended, or sub-threshold); the thesis claim that progress now depends on statistical and machine-learning methods recovering information where thresholding fails; the narrative arc (decreasing signal strength, increasing methodological sophistication); closes by naming the five works integrated in the thesis and the public deliverables (the gPCS catalog), as Loayza closes his preface naming CosmoLattice.

### The dark matter problem (~650 words, 2–3 equations)
Compressed chapter 1: the pillars of evidence (rotation curves, clusters, lensing, CMB); ΛCDM and the measured abundance; the WIMP hypothesis with the relic-abundance punchline (thermal cross section ⟨σv⟩ ≈ 3×10⁻²⁶ cm³/s); the detection strategies in one paragraph; indirect detection via the master annihilation-flux equation with the J-factor; the target hierarchy it implies (Galactic Center → dwarfs and subhalos → extragalactic web), which prefigures the arc of the results.

### The gamma-ray sky and Fermi-LAT (~550 words, 0–1 equations)
Compressed chapter 2: the LAT as a pair-conversion telescope (energy range, all-sky cadence, angular resolution); the decomposition of the GeV sky (Galactic diffuse emission, resolved point sources dominated by blazars and pulsars, isotropic unresolved background); the 4FGL catalog and the detection-threshold concept; ends on the two blind spots that motivate the thesis — unassociated sources and the sub-threshold population.

### Objectives (~200 words, prose)
A single prose passage enumerating the goals: testing the millisecond-pulsar interpretation of the Galactic Center Excess through the globular-cluster luminosity function; constraining a dark-matter-subhalo component among the unassociated Fermi-LAT sources; reconstructing the source-count distribution dN/dS below the detection threshold; extending the catalogs probabilistically below threshold; forecasting CTAO sensitivity to the cross-correlation of gamma rays with galaxy catalogs; and, across all of these, developing statistical and machine-learning methodology transferable to future instruments.

### Methodology: statistics and machine learning for faint signals (~950 words, 2–4 equations)
Unified tour of the toolbox, organized with bold paragraph lead-ins in the thesis style, each closing with a pointer to the results section that uses it: Bayesian inference and the intractable-likelihood problem in high-dimensional photon data; simulation-based inference and neural posterior estimation; quantification learning (estimating class prevalences rather than labels, with prior and covariate shift corrections); deep learning on sky maps (convolutional networks); probabilistic cataloging; the cross-correlation angular power spectrum. Content drawn from chapter 3 and the methodological parts of chapters 4–8.

### Results (~2,250 words, one subsection of ~450 words per paper)
One `\section*` or bold-led block per paper, in thesis order (decreasing signal strength), each stating problem, method, and quantitative outcome as written in the corresponding chapter:

1. **The MSP luminosity function and the GCE** (ch. 4): hierarchical measurement in globular clusters; ⟨L_γ⟩ ~ (1–8)×10³³ erg/s, σ_L ~ 1.4–2.8; the prediction that Fermi-LAT should already have resolved roughly 17–37 pulsars against 3 known candidates, straining the pulsar interpretation.
2. **Dark matter subhalos among unassociated sources** (ch. 5): generative mixture model of unassociated sources at |b| > 10°, quantification learning with prior/covariate shift correction; no significant subhalo component; 95% CL upper limits on ⟨σv⟩ in the b b̄ channel for masses 10 GeV–1 TeV.
3. **The source-count distribution below threshold** (ch. 6): CNN trained on ~10⁶ synthetic sky maps, applied to 14 years of data between 1 and 10 GeV; reconstruction reaching a factor ~50 below the Fermi-LAT threshold; dN/dS ∝ S⁻² down to ~5×10⁻¹² cm⁻² s⁻¹.
4. **Probabilistic cataloging** (ch. 7): per-direction likelihood of hosting a sub-threshold source; roughly 50% more candidate directions than 4FGL-DR3; public gPCS catalog suited to cross-correlation studies.
5. **Cross-correlations with CTAO** (ch. 8): forecast of the gamma-ray–galaxy cross-correlation with a dense low-redshift catalog (2MASS-like) and ~50 h of observation; sensitivity to annihilating and decaying dark matter competitive with dwarf-galaxy and cluster analyses.

Exact figures above are indicative (taken from the current abstract); at drafting time each is re-verified against the chapter text.

### Conclusions and future directions (~650 words, prose)
Synthesis restating the arc: no confirmed detection, but a coherent demonstration that the limiting factor in indirect detection has shifted from photon statistics to analysis methodology. Future directions in flowing prose, sourced exclusively from the prospects already discussed in the written chapters (chapter 8's outlook and the concluding discussions of chapters 4–7) — no invented outlook material.

## Drafting workflow (for the implementation plan)

1. Gather per-section source material from the actual chapter texts (numbers, claims, prospects).
2. Draft section by section via the `scientific-prose-writer` pipeline with self-contained briefs, following the thesis style guide (CLAUDE.md).
3. Review passes (humanizer / referee) dispatched in fresh-context subagents.
4. Compile check with `main.tex` importing `resumen_en.tex`.
5. Once the English version is approved by the author: translate to Spanish into `resumen/resumen.tex` (separate task, same structure), then restore the `main.tex` import.

## Out of scope

- The Spanish (and any Valencian) translation — follows after the English draft is approved.
- The short abstracts (`frontmatter/abstract_es.tex`, `abstract_vlc.tex`, `abstract_3000.md`) — separate deliverables.
- Any change to thesis chapters, bibliography, or glossary.
