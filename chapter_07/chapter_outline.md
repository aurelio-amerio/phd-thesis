---
title: "Chapter 7 — Probabilistic Cataloging"
date: 2026-03-26
source_skill: chapter_outline
chapter: chapter_07
status: outline
tags: [probabilistic-catalog, firing-pixels, quality-factor, ks-test, sub-threshold, fermi-lat, gpcs, dnds]
---

# Chapter 7 — Probabilistic Cataloging

**Estimated length:** 5–8 pages (introduction, §7.1–7.3) + paper body
**Page ceiling:** 10 pages for introduction

This chapter is the second chapter of Part III and contains Paper 2 (`dNdS_catalog`, arXiv:2306.16483). It is a compact extension of Chapter 6: Paper 1 recovered the dN/dS (the flux distribution of sub-threshold sources); Paper 2 complements it with spatial information (where those sources are). The introduction should be SHORT — all heavy lifting (dN/dS formalism, SBI methodology, Fermi-LAT data pipeline) was done in Ch. 6. The paper is included in near-entirety.

---

## Connections

- **Previous Chapter (Ch. 6):** Chapter 6 recovered the sub-threshold dN/dS using SBI and deep learning — proving that one can measure how many faint sources exist at each flux. However, the dN/dS provides *zero* spatial information: it says nothing about where individual sources are located. Chapter 7 bridges this gap by using the dN/dS as input to generate ensembles of synthetic skies, then comparing their pixel-wise TS distributions against the real Fermi-LAT sky to identify source candidates.
- **Next Chapter (Ch. 8):** The extended probabilistic catalog (gPCS) produced here has a globally homogeneous TS scale, making it especially suited for cross-correlation studies. Chapter 8 uses cross-correlations between gamma-ray maps and galaxy catalogs to search for collective DM emission in unresolved large-scale structure — the gPCS catalog provides a larger statistical sample for such analyses.
- **Inserted Paper:** Paper 2 (arXiv:2306.16483), "Deepening gamma-ray point-source catalogues with sub-threshold information." Key contribution: a frequentist framework using simulated-sky comparison and a KS test to identify "firing pixels" — source candidate positions below the nominal Fermi-LAT detection threshold. Delivers ~50% more candidate directions than the 4FGL-DR3 catalog.

---

## 7.0 Chapter Introduction

**Goal:** Provide a brief, untitled opening (2–3 paragraphs) that orients the reader before the first numbered section. This text appears at the start of the chapter with no section heading.

**Narrative:** Follow a funnel structure:
- Opening context: Chapter 6 demonstrated that the sub-threshold dN/dS is recoverable from photon-count statistics via deep learning. The result tells us the statistical flux distribution of faint sources — but it tells us nothing about where any individual source is located. The natural follow-up question is whether this population-level information can be leveraged to extract spatial information.
- Central question: can one use the dN/dS to identify specific sky directions that are likely to host sub-threshold sources?
- Chapter roadmap: §7.1 examines why fixed TS thresholds lose information and produce spatially inconsistent catalogs; §7.2 presents the conceptual framework for complementing the dN/dS with spatial information via simulated-sky comparison; §7.3 transitions to the paper.
- Bridge to the thesis: the probabilistic catalog constructed here is a natural input for cross-correlation analyses (Ch. 8), where a larger statistical sample of source directions — even if probabilistically defined — outweighs a sub-leading fraction of spurious directions.

**Cross-references:** Ch. 6 (dN/dS recovery); Ch. 3 §3.2 (SBI paradigm); Ch. 8 (cross-correlations).

---

## 7.1 The Limits of Fixed-Threshold Cataloging (~2.5 pages)

**Purpose:** Motivate why fixed TS thresholds are insufficient and why sub-threshold information is scientifically valuable. This section establishes the *problem* that the rest of the chapter solves.

### 7.1.1 The Standard Catalog-Construction Paradigm

**Key points:**
- The Fermi-LAT 4FGL catalog identifies point sources via a likelihood-ratio test statistic, TS = 2 ln(ℒ/ℒ₀), requiring TS > 25 for inclusion (corresponding nominally to ~4σ). Cite [`Fermi-LAT:2019yla`], [`Fermi-LAT:2022byn`].
- This procedure is necessarily *local*: TS values are computed in individual regions of interest, with energy-dependent background re-normalizations applied independently in each region. The resulting TS scale is therefore not globally uniform — the same TS value at different sky locations corresponds to different underlying source significances, because the background level and structure vary across the sky.
- The fixed threshold is a binary gate: a source is either "in" (TS ≥ 25) or "out." All sub-threshold information is discarded, regardless of how close to the threshold a pixel's TS may be.
- Cross-ref Ch. 2 §2.3 (Fermi-LAT data reduction), Ch. 6 §6.2 (dN/dS as the bridge between resolved and unresolved regimes).

### 7.1.2 The Information Below Threshold

**Key points:**
- The unresolved gamma-ray background (UGRB) is known to contain a large population of sub-threshold point sources — blazars, MSPs, star-forming galaxies — whose cumulative emission is detectable but whose individual signals fall below the catalog threshold. Cross-ref Ch. 6 §6.2.3.
- The dN/dS recovered in Chapter 6 extends as ~S⁻² down to fluxes ~50× below the Fermi-LAT threshold. This implies a substantial population of sources just below TS = 25 that carry real astrophysical information.
- This sub-threshold population is relevant for several science cases: (i) constraining faint astrophysical populations, (ii) multi-wavelength source identification campaigns, and (iii) cross-correlation studies (Ch. 8) where statistical power scales with sample size.
- **The gap left by Chapter 6:** the dN/dS tells us the *number of sources per unit flux* — a one-dimensional flux distribution. It provides no information about where on the sky any specific source is located. The challenge is to complement this population-level statistical knowledge with positional information.
- **Transition:** A globally defined, simulation-calibrated TS scale could overcome both limitations — the spatial inconsistency of fixed thresholds and the loss of sub-threshold information. The next section describes such a framework.

---

## 7.2 From Population Statistics to Spatial Information (~2.5 pages)

**Purpose:** Present the conceptual leap from the dN/dS (a population statistic with no spatial content) to a probabilistic catalog (a list of sky directions with associated source probabilities). This section introduces the *idea* at a qualitative level; the paper body contains the full mathematical treatment.

### 7.2.1 The Core Idea: Simulated-Sky Comparison

**Key points:**
- The framework is conceptually simple: if the dN/dS is known, one can *generate* realistic synthetic skies by drawing source fluxes from the dN/dS and placing them at uniformly random positions. Each synthetic sky is a plausible realization of the sub-threshold source population.
- By generating thousands of such synthetic skies (5000 in the analysis) and computing a pixel-wise TS for each — quantifying how much each pixel's photon count deviates from the background-only expectation — one obtains an ensemble of TS distributions that encodes what the sky *should look like* if the dN/dS is correct.
- Comparing the TS distribution of the real Fermi-LAT sky against this ensemble determines the TS threshold down to which the simulations remain statistically compatible with the data. Pixels in the real sky whose TS exceeds this threshold are labeled "firing pixels" — candidate source directions.
- **Key distinction from Ch. 6:** the dN/dS provides the *input* (population statistics); this chapter provides the *output* (positional information). The two are complementary halves of the same program.
- Other approaches to probabilistic gamma-ray cataloging have been attempted (e.g. Daylan et al. 2017), though applied to limited sky regions.

### 7.2.2 A Frequentist Framework: TS, KS Test, and Quality Factor

**Key points:**
- The framework is entirely frequentist. There is no Bayesian prior in the usual sense — the dN/dS acts as a *generative model* for synthetic sky simulations, not as a prior on source properties.
- **The TS as a "signal interest label":** A Pearson-like statistic TS_i = (x_i − λ_i)² / λ_i is computed per pixel, where λ_i is the background-only model prediction and x_i is the observed (or simulated) photon count. This is inspired by Pearson's χ² test for Poisson-distributed counts. Importantly, no particular probability distribution is assumed for the TS values — its statistical meaning is derived entirely from the simulated ensemble.
- **The KS two-sample test:** For a given minimum TS threshold TS★, the normalized cumulative TS distributions of the real sky and each simulated sky (both restricted to TS > TS★) are compared via a two-sample Kolmogorov–Smirnov test. The KS test determines the lowest TS★ above which the simulations remain statistically compatible with the data at a chosen significance level α.
- **The Quality Factor (QF):** Since 5000 synthetic skies are generated, not all will pass the KS test at a given TS★. The QF is defined as the fraction of simulations that pass the test. A higher QF demands stricter compatibility (fewer firing pixels, lower false-positive rate); a lower QF relaxes the criterion (more firing pixels, deeper catalog). QF is thus a second meta-parameter alongside α.
- **The depth/purity trade-off:** The pair (α, QF) controls the operating point of the probabilistic catalog. The paper explores the full (α, QF) plane, providing the user with the flexibility to choose the trade-off appropriate to their science case.
- **A globally homogeneous TS scale:** Unlike the Fermi-LAT catalog's locally computed TS, the TS defined here is a single, globally consistent quantity. This homogeneity is advantageous for global statistical analyses such as cross-correlations (Ch. 8).
- **Firing pixels vs. sources:** At the chosen pixel resolution (N_side = 512, ~0.12°), a single source may produce multiple firing pixels (PSF spreading) and multiple faint sources may share a pixel. The output is therefore a map of firing *pixels*, not a traditional source catalog. The paper body discusses the pixel resolution choice in detail.
- **Transition:** the paper presents the full methodology, applies it to 14 years of Fermi-LAT data, validates the procedure against the 4FGL-DR3 catalog, and delivers the publicly available gPCS probabilistic catalog.

---

## 7.3 Transition to the Paper (~0.5 page)

**Purpose:** Bridge into the paper body with a summary of what the reader should expect.

**Key points:**
- The remainder of this chapter presents the analysis in full.
- Main results: for reasonable choices of the meta-parameters (α, QF), the procedure identifies ~50% more firing pixels than one would infer from the 4FGL-DR3 catalog alone. As a sanity check, the vast majority of bright cataloged sources are recovered as firing pixels.
- The results are publicly available as the gPCS (gamma-ray Photon Count Statistics) Python package and accompanying FITS files.
- **Outlook (one sentence):** The extended probabilistic catalog is especially suited for cross-correlation studies (Ch. 8), where the statistical advantage of a larger sample outweighs a sub-leading fraction of spurious directions.
- **Transition:** "The remainder of this chapter presents the analysis in full."

---

## Paper Body — §7.4 onward

**Source:** Paper 2 (`dNdS_catalog`, arXiv:2306.16483) — included from Section 2 onward.

| Thesis Section | Paper Section | Content |
|---|---|---|
| §7.4 | Section 2 | Data selection and model components: 14-year Fermi-LAT dataset, null- and alternative-hypothesis models (𝓑, 𝓚, 𝓜), background fitting |
| §7.5 | Section 3 | Problem setting and statistical framework: TS definition, KS two-sample test, Quality Factor, firing pixel identification, pixel resolution choice |
| §7.6 | Section 4 | Results: TS★ tables, firing pixel counts, 4FGL recovery validation, background model robustness, gPCS package and code |
| §7.7 | Section 5 | Discussion and conclusions: future directions (energy-dependent extension, low-latitude extension, constrained simulations) |

> [!NOTE]
> The paper has no appendices. The code snippet for the gPCS package (Paper §4) is retained in the paper body as-is.

---

## 7.8 Summary (~0.5 page)

**Key points:**
- The dN/dS recovered in Chapter 6 was used to generate ensembles of synthetic Fermi-LAT skies, enabling a frequentist comparison of pixel-wise TS distributions between simulated and real data.
- A two-parameter framework (KS significance α and Quality Factor QF) controls the depth/purity trade-off of the resulting probabilistic catalog.
- For reasonable meta-parameter choices, the procedure identifies ~50% more candidate source directions than the 4FGL-DR3 catalog, while recovering the vast majority of known bright sources as a sanity check.
- The globally homogeneous TS scale — in contrast to the locally defined Fermi-LAT catalog TS — makes the probabilistic catalog especially suited for global statistical analyses.
- The results are publicly available via the gPCS Python package.
- **Connection forward:** the extended catalog provides a larger statistical sample for cross-correlation studies between gamma-ray maps and tracers of large-scale structure — the subject of Chapter 8, where the collective DM signal in unresolved structure is the target.

---

## Structural Notes

- **Figures in introduction:** No paper figures are duplicated in the introduction. Consider including a conceptual schematic (not from the paper) showing the pipeline: dN/dS → simulated skies → TS comparison → firing pixels → probabilistic catalog. This would be a new thesis-original figure, not a reproduction.
- **No repeated figures:** Paper figures stay in the paper body (§7.4–§7.7).
- **Tone:** Scholarly, neutral. Present the method as a proof of concept — a methodological first step, not a definitive replacement for Fermi-LAT catalogs. The gPCS catalog is "probabilistically defined" and "useful for statistical applications."
- **Precision of language:** Use "firing pixels" (not "source candidates"), "meta-parameters" (not "hyperparameters"), "Quality Factor" (not "quality score").
- **Relationship to Ch. 6:** The introduction assumes the reader has read Ch. 6. Do not re-derive the dN/dS formalism or the SBI methodology. Cross-reference freely.
- **Length budget:** §7.0 (0.5p) + §7.1 (2.5p) + §7.2 (2.5p) + §7.3 (0.5p) = **~6 pages**, well within the 10-page ceiling while remaining lean.
