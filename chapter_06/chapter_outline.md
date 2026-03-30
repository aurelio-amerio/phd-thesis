---
title: "Chapter 6 — From Individual Sources to Populations"
date: 2026-03-26
source_skill: chapter_outline
chapter: chapter_06
status: outline
tags: [dnds, source-count-distribution, 1ppdf, sbi, cnn, healpix, fermi-lat, unresolved-background]
---

% TODO: need to review this outline, it's very rough

# Chapter 6 — From Individual Sources to Populations

**Estimated length:** 5–15 pages (introduction, §6.1–6.5) + paper body
**Page ceiling:** 10 pages for introduction

This chapter opens **Part III: The Unresolved Sky** and contains Paper 1 (`dNdS`, arXiv:2302.01947). The introduction replaces the paper's abstract and Section 1. The paper body begins from its Section 2 (Data selection).

---

## Connections

- **Previous Chapter (Ch. 5):** Part II concluded with the search for individual DM subhalos among unassociated sources. The analysis yielded upper limits on ⟨σv⟩ but found no statistically significant DM contribution — illustrating the fundamental limits of source-by-source identification. This chapter picks up that thread: if individual identification is inherently limited, the solution is to study the *population* collectively.
- **Next Chapter (Ch. 7):** The dN/dS recovered in this chapter feeds directly into Chapter 7, where it is used as a prior for probabilistic source cataloging — deepening the Fermi catalog below the standard detection threshold.
- **Ch. 8 (Cross-Correlations):** While Chapters 6–7 characterize the *astrophysical* unresolved source population, the search for a collective DM signal in the unresolved sky is deferred to Ch. 8, where cross-correlations with galaxy catalogs provide sensitivity to DM annihilation in unresolved large-scale structure.
- **Inserted Paper:** Paper 1 (arXiv:2302.01947), "Extracting the gamma-ray source-count distribution below the Fermi-LAT detection limit with deep learning." Key contribution: proof-of-principle CNN-based recovery of the extragalactic dN/dS down to fluxes 50× below the Fermi-LAT threshold.

---

## 6.0 Chapter Introduction

**Goal:** Provide a brief, untitled opening (2–4 paragraphs) that orients the reader before the first numbered section. This text appears at the start of the chapter with no section heading.

**Narrative:** Follow a funnel structure:
- Opening context: Part II examined DM in specific, resolved targets — the Galactic Center and individual subhalo candidates. Both approaches encountered fundamental limitations, motivating a shift in strategy.
- Central question: can the statistical properties of the *entire* faint source population — including sources below the detection threshold — be recovered from the collective photon-count distribution?
- Chapter roadmap: §6.1 builds the conceptual argument for population studies; §6.2 introduces the source-count distribution as the key observable; §6.3 presents the SBI methodology for recovering it; §6.4 provides the transition to the paper.
- Bridge to the thesis: this chapter's results provide the foundation for probabilistic cataloging (Ch. 7). While characterizing the astrophysical source population is the primary goal of Part III, the methodology also lays groundwork for future DM-sensitive extensions.

**Cross-references:** Ch. 4 (GCE); Ch. 5 (subhalo searches); Ch. 3 §3.2 (SBI paradigm); Ch. 2 §2.2 (astrophysical source populations).

---

## 6.1 The Limits of Individual Detection (~1.5 pages)

**Purpose:** Transitional argument connecting Part II to Part III. This is the thesis's key conceptual pivot: from resolved targets to population statistics.

**Goal:** Convince the reader that after the frustrations of individual-source identification, the natural next step is to abandon the question "is this source DM?" and instead ask "what is the statistical distribution of the entire faint source population?"

**Narrative:**

### 6.1.1 The Resolved-Source Paradigm and Its Boundaries

**Key points:**
- Part II investigated DM through two complementary strategies, both targeting *individual* resolved structures:
  - **The Galactic Center (Ch. 4):** The strongest expected DM signal, but the GCE remains unresolved after 15+ years due to irreducible systematic uncertainties — competing IEM models, morphological degeneracies (NFW vs. stellar bulge), and the NPTF crisis. The signal is there, but attributing it to any single origin is confounded by the complex Galactic foreground environment. Cross-ref Ch. 4 §4.4.
  - **Dark matter subhalos (Ch. 5):** A cleaner environment (no astrophysical confusion), but no statistically significant DM contribution was found among Fermi-LAT unassociated sources. Individual subhalo identification is limited by: (i) sensitivity — only the brightest subhalos would be detectable, and (ii) the look-elsewhere effect — any single candidate drawn from a catalog of ~2400 unassociated sources requires extraordinary evidence. Cross-ref Ch. 5 §5.4–5.5.
- The common thread: individual-source methods rely on *identifying* a specific target or *classifying* individual sources. Both strategies are fundamentally constrained by the gap between the detector threshold and the true source population.

### 6.1.2 The Population Alternative

**Key points:**
- The conceptual shift: rather than asking "is *this* source DM?", we ask "what is the statistical distribution of all sources — including those too faint to detect individually?"
- Below the Fermi-LAT detection threshold lies a vast population of unresolved sources whose cumulative emission forms the unresolved gamma-ray background (UGRB). These sources are invisible individually, but their collective photon statistics encode recoverable information about the population.
- This approach is complementary to Part II: resolved-source methods probe the bright end of the population; population methods probe the faint end. Together, they provide a complete picture.
- **Scope of Part III:** Chapters 6–7 focus on characterizing the *general* unresolved source population (primarily astrophysical: blazars, MSPs, star-forming galaxies). The search for a collective DM signal in the unresolved gamma-ray sky — via cross-correlations with tracers of large-scale structure — is the subject of Ch. 8, which uses a complementary approach (angular cross-correlations) rather than the dN/dS framework developed here.
- **Transition:** The key observable for characterizing the sub-threshold source population is the source-count distribution, dN/dS, which we define in the next section.

---

## 6.2 The Source-Count Distribution (~2.0 pages)

**Purpose:** Define the dN/dS formally, explain its physical content, and establish why it is a powerful observable for studying sub-threshold populations.

### 6.2.1 Definition and Physical Meaning

**Key points:**
- The **differential source-count distribution** dN/dS gives the number of sources per unit solid angle per unit flux at a given integral photon flux S. It is the fundamental observable describing the abundance of point sources as a function of brightness.
- For bright sources (above the catalog detection threshold), dN/dS is directly measured by counting cataloged objects. Cross-ref Ch. 2 §2.2.
- Below the threshold, the true dN/dS must be *inferred* from the statistical properties of the photon-count map — this is the central challenge of this chapter.
- dN/dS is the observational projection of the **luminosity function**: the LF gives the intrinsic number density of sources per unit luminosity and volume; integrating over redshift and spectral properties yields the flux distribution observed from Earth. Cite [`Fornasa:2015qua`] (UGRB review 1502.02866), Eq. (3).
- **Figure**: Consider including a schematic showing how dN/dS bridges the resolved catalog (bright end, measured directly) and the unresolved background (faint end, inferred statistically). → Conceptual diagram, not from a specific paper.

### 6.2.2 The 1-Point Photon-Count Distribution

**Scope note:** This subsection provides a *conceptual* overview of the 1pPDF — enough to understand the approach and its role as a benchmark — without going into derivation details.

**Key points:**
- The photon-count distribution (1pPDF, or pixel-count distribution) is the histogram of the number of pixels containing exactly k photons. The core idea: different source populations leave distinct imprints on this distribution — bright, rare sources produce non-Poissonian tails, while faint, numerous sources (and diffuse emission) produce a Poissonian distribution. Analyzing these tails reconstructs the properties of sub-threshold populations.
- **Key literature** (brief summary of the development, not detailed methodology):
  - **Malyshev & Hogg (2011)** [`Malyshev:2011zi`]: pioneered the 1pPDF for gamma rays; decomposed the sky into point sources, Galactic foreground, and isotropic background.
  - **Cuoco et al. (2015)** [`Cuoco-1pdf`]: pixel-dependent improvement incorporating spatial variation of foreground and exposure; measured dN/dS down to ~1 order of magnitude below threshold.
  - **Zechlin et al. (2016), Lisanti et al. (2016)** [`Zechlin:2015wdz`, `Lisanti:2016jub`]: energy-dependent extensions to multiple bands (1–171 GeV).
- **Passing remark on NPTF:** The same pixel-statistics formalism was adapted for the NPTF framework applied to the GCE (cross-ref Ch. 4 §4.4.1), demonstrating the versatility of photon-count methods across different science cases.

### 6.2.3 Why dN/dS Is a Powerful Observable

**Key points:**
- dN/dS bridges two regimes: the bright end is anchored by catalog measurements (4FGL); the faint end encodes the composition and abundance of unresolved populations.
- Different source classes (blazars, MSPs, star-forming galaxies, potentially DM) contribute to different flux ranges. Decomposing dN/dS by population probes the composition of the UGRB. Cite [`Korsmeier:2022cwp`, `Manconi:2019ynl`, `DiMauro:2017ing`] for blazar decomposition.
- Integrating the sub-threshold dN/dS yields the total contribution of unresolved point sources to the UGRB — a key input for multi-messenger studies.
- **Transition:** The analytical 1pPDF approach has been remarkably successful but operates under restrictive assumptions. The next section introduces a simulation-based alternative that relaxes these assumptions.

---

## 6.3 Simulation-Based Inference for dN/dS (~2.5 pages)

**Purpose:** Motivate *why* the analytical 1pPDF method has limitations, present the SBI/CNN approach as the solution, and address the specific technical challenge of ML on spherical data. This section merges the methodological motivation with the spherical geometry discussion. A key motivation is that the 1pPDF is *not amortized* — each new dataset or parameter configuration requires a full re-convergence of the likelihood, which is computationally expensive.

### 6.3.1 Limitations of the Analytical Approach

**Key points:**
- The analytical 1pPDF likelihood requires:
  1. **Neglecting PSF spatial correlations:** the generating-function formalism treats each pixel independently, but the PSF spreads photons across multiple pixels, introducing inter-pixel correlations that are not captured.
  2. **Discarding energy information:** the standard 1pPDF operates in a single broad energy band (e.g., 1–10 GeV). Energy-dependent extensions exist [`Zechlin:2015wdz`, `Lisanti:2016jub`], but they treat each band independently rather than exploiting energy correlations.
  3. **Assuming a parametric dN/dS form:** the analytical approach models dN/dS as a broken power-law with a fixed number of breaks, limiting flexibility.
  4. **Slow convergence and no amortization:** the generating-function formalism is computationally demanding, especially in its pixel-dependent version. Crucially, the method is *not amortized*: each new dataset or parameter configuration requires a full re-convergence of the likelihood from scratch.
- **Note on our work:** The present analysis uses a single energy bin (1–10 GeV) to enable direct comparison with the 1pPDF benchmark of Zechlin et al. However, the CNN-based approach naturally extends to multiple energy bins simultaneously — a key advantage for future work.
- These limitations motivate an alternative approach: rather than writing down and evaluating the likelihood analytically, one can *simulate* the forward model and let a neural network learn the mapping from photon-count maps to dN/dS parameters.

### 6.3.2 The SBI Approach: Learning from Simulated Maps

**Key points:**
- The key insight is that the forward model — from dN/dS parameters to a photon-count map — is straightforward to simulate: draw source fluxes from the dN/dS, place them on the sky, convolve with the PSF, add foregrounds and isotropic backgrounds, apply exposure, and add Poisson noise. This is a classic simulation-based inference setup (cross-ref Ch. 3 §3.2).
- A CNN is trained on a large set (~10⁶) of synthetic Fermi-LAT-like maps generated from diverse dN/dS realizations. The network learns to extract the output dN/dS (discretized in 20 flux bins) and the isotropic flux F_iso directly from the input map.
- **Advantages over the analytical 1pPDF:**
  - The CNN implicitly accounts for PSF correlations through the spatial structure of the training maps — no explicit correlation model is needed.
  - The methodology naturally extends to multiple energy bins and energy correlations (a stated future direction).
  - The dN/dS is recovered non-parametrically in flux bins rather than as a parametric power-law.
  - Once trained, inference is extremely fast (single forward pass), enabling efficient uncertainty quantification.
- Error estimation: the CNN uses a heteroscedastic Gaussian cost function (Bayesian error estimation) combined with concrete dropout, providing per-bin uncertainties that naturally widen at very low and very high fluxes where the network reaches its confusion limit. Cross-validated with a frequentist error estimation procedure.
- Cross-ref Ch. 3 §3.2 for the SBI framework; Ch. 3 §3.3 for ML in astrophysics.

### 6.3.3 Inference on Spherical Data

**Scope note:** Keep this subsection *compact* — the full algorithm is described in the paper body (§6.7). The introduction should only convey the key idea and motivation.

**Key points:**
- Fermi-LAT data are naturally represented as HEALPix maps on the sphere. Standard planar CNNs applied to flattened projections introduce geometric distortions. Fully spherical architectures [`Cohen:2018`, `Perraudin:2019`, `Krachmalnicoff:2019`] exist but are slower and less mature.
- This work introduces the **map2patches** strategy: the HEALPix sphere is subdivided into 12 equal-area base patches, each mapped to a flat 2D image without resampling. Patches are padded with pixels from neighbouring patches to preserve boundary information during convolutions. Standard 3D convolutions then treat the patch index as the third dimension, enabling the use of highly optimized architectures (EfficientNet V2M) with >10× speedup over fully spherical convolutions.
- Full details (architecture, training, validation, cross-check against DeepSphere) are in the paper body (§6.7).

---

## 6.4 Transition to the Paper (~0.5 page)

**Purpose:** Motivate what the dN/dS recovery enables and bridge into the paper.

**Key points:**
- Recovering the sub-threshold dN/dS with deep learning is not merely a methodological exercise — it opens several scientific doors:
  - **(a) Constraining faint astrophysical populations:** the sub-threshold dN/dS reveals the composition and abundance of sources too faint to be individually cataloged (blazars, star-forming galaxies, misaligned AGNs). This is the primary science goal of Part III.
  - **(b) Providing priors for probabilistic cataloging:** the dN/dS measured in this chapter is used in Chapter 7 as a prior for the source detection step, enabling the construction of probabilistic catalogs that extend below the standard detection threshold.
  - **(c) Future prospects — DM in the dN/dS:** a natural extension of this methodology would include a DM component in the dN/dS model, enabling a statistical search for DM subhalos as a faint population. Energy-dependent dN/dS decomposition would further sharpen this capability. This remains a future goal — the present analysis characterizes the total source population without attempting DM decomposition. A complementary approach to searching for unresolved DM is provided by the cross-correlation analysis of Ch. 8, which exploits the spatial correlation between the UGRB and tracers of DM large-scale structure.
- The methodology presented here serves as a proof of principle: it validates the CNN approach by recovering a dN/dS fully consistent with catalog measurements in the resolved regime and with the independent 1pPDF results in the unresolved regime.
- **Transition:** "The remainder of this chapter presents the analysis in full."

---

## Paper Body — §6.5 onward

**Source:** Paper 1 (`dNdS`, arXiv:2302.01947) — included from Section 2 onward.

| Thesis Section | Paper Section | Content |
|---|---|---|
| §6.5 | Section 2 | Data selection: 14-year Fermi-LAT dataset, IRFs, HEALPix maps |
| §6.6 | Section 3 | Synthetic map generation: dN/dS parametrization (MBPL), Galactic foreground, isotropic background |
| §6.7 | Section 4 | Neural network architecture and training: map2patches, EfficientNet V2M, Bayesian error estimation, validation |
| §6.8 | Section 5 | Results: baseline dN/dS recovery, stability tests (latitude cuts, foreground models) |
| §6.9 | Section 6 | Conclusions |

## Appendices (at end of chapter)

Paper appendices included as thesis chapter appendices:

| Appendix | Content |
|---|---|
| 6.A | Further tests: flat dN/dS, UltraCleanVeto selection |
| 6.B | Multipole analysis for foreground stability |
| 6.C | Variation of foreground normalization A_gal |
| 6.D | Full spherical convolution cross-check |

---

## 6.10 Summary (~0.5 page)

**Key points:**
- The CNN recovers a dN/dS extending as ~S⁻² over almost four orders of magnitude in flux, down to 5 × 10⁻¹² cm⁻² s⁻¹ — a factor of ~50 below the Fermi-LAT detection threshold.
- In the resolved regime, the CNN result agrees with catalog-derived source counts (4FGL-DR3); in the unresolved regime, it is consistent with the independent analytical 1pPDF measurement of Cuoco et al. (2015).
- The methodology is robust against systematics: stable across latitude cuts (30°, 40°, 50°), foreground models (v05, v07), and event selections (SOURCEVETO, ULTRACLEANVETO).
- The map2patches approach enables efficient CNN training on spherical data, with >10× speedup over fully spherical architectures and equivalent accuracy.
- **Outlook:** the framework naturally extends to multiple energy bins, enabling energy-dependent dN/dS decomposition — a prerequisite for identifying the contributions of specific source classes. In the future, this could be extended to search for spectral signatures of a DM annihilation component, although the present analysis focuses on characterizing the total source population.
- **Connection forward:** the recovered dN/dS serves as the empirical prior for the probabilistic cataloging framework developed in Chapter 7, where sub-threshold source information is extracted source-by-source. The complementary search for collective DM emission in the unresolved sky is addressed through cross-correlations in Ch. 8.

---

## Structural Notes

- **Figures for introduction:** Consider including:
  - A conceptual schematic showing dN/dS bridging the resolved catalog and unresolved background (§6.2.1)
  - Possibly the 4FGL-DR3 dN/dS data points (from Fig. 1 of the paper) to ground the discussion — but check whether this duplicates a paper figure
- **No repeated figures:** Do not duplicate Paper 1's figures in the introduction. The dN/dS result figure (Paper Fig. 12) stays in the paper body.
- **NPTF treatment:** Passing remark only (§6.2.2). The primary methodological comparison is with the analytical 1pPDF (Malyshev & Hogg 2011, Cuoco et al. 2015), not NPTF.
- **Spherical ML:** Absorbed into §6.3.3 as a subsection of the SBI methodology, not a standalone section. The paper body (§6.7) contains the full technical detail.
- **Tone:** Scholarly, neutral. Present the CNN approach as a proof of principle (the paper itself uses this framing), not as a definitive replacement for analytical methods. The 1pPDF and CNN approaches are complementary.
- **Length budget:** §6.0 (0.5p) + §6.1 (1.5p) + §6.2 (2p) + §6.3 (2.5p) + §6.4 (0.5p) = **~7 pages**, within the 5–10 page target.
