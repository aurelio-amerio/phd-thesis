---
title: "Chapter 5 — Searching for Dark Matter Substructures"
date: 2026-03-26
source_skill: chapter_outline
chapter: chapter_05
status: outline
tags: [dm-subhalos, fermi-lat, unassociated-sources, dataset-shift, quantification-learning, domain-adaptation]
---

# Chapter 5 — Searching for Dark Matter Substructures

**Estimated length:** ~13 pages (introduction, Sections 5.1–5.6) + paper body (dm_halos)

This chapter opens with a pedagogical introduction to dark matter subhalo searches among Fermi-LAT unassociated sources, then transitions into the author's published analysis (Paper 4 = `dm_halos`, arXiv:2503.14584). The introduction replaces the paper's abstract and Section 1.

---

## 5.1 Introduction (~0.5 page)

**Purpose:** Frame subhalo searches as the second prong of Part II. After Chapter 4's resolved GCE analysis, this chapter seeks individual DM objects among cataloged sources — a fundamentally different strategy.

**Key points:**
- Chapter 4 examined the brightest expected DM signal; the Galactic Center Excess remains unresolved. This chapter shifts to a complementary approach: searching for individual dark matter subhalos among Fermi-LAT point sources.
- The conceptual leap: rather than analyzing a known excess, we ask whether *any* cataloged gamma-ray sources could be dark matter subhalos.
- Preview: ΛCDM predicts an enormous population of dark subhalos → a fraction may be detectable in gamma rays → they would appear as unassociated Fermi-LAT sources → identifying them requires a statistical framework that accounts for the mismatch between training and target data.

**Cross-references:** Ch. 4 (GCE debate); Ch. 1 §1.4.3 (density profiles, J-factors); Ch. 2 (Fermi-LAT source classes).

---

## 5.2 Dark Matter Substructure in ΛCDM (~2 pages)

**Purpose:** Establish the theoretical foundation — why dark subhalos exist and what ΛCDM predicts for the Milky Way's subhalo population.

### 5.2.1 Hierarchical Structure Formation

**Key points:**
- ΛCDM predicts bottom-up hierarchical assembly: small halos merge to form larger ones, retaining a population of gravitationally bound subhalos (substructure).
- N-body cosmological simulations (Millennium, Via Lactea II [`2007ApJ...667..859D`], Aquarius [`2008Natur.454..735D`], FIRE) resolve subhalos down to ~10⁴ M☉; extrapolation below the resolution limit extends to ~10⁻¹ M☉.
- The subhalo mass function dN/dM ∝ M^{−α} with α ≈ 1.9 — the MW should host O(10¹⁵–10¹⁶) total subhalos.

### 5.2.2 Luminous Satellites vs. Dark Subhalos

**Key points:**
- Subhalos above ~10⁸ M☉ can retain baryons → observed as dwarf spheroidal galaxies (dSphs). ~60 known MW satellites.
- The vast majority of subhalos (below ~10⁸ M☉) are "dark": no stars, no gas, no electromagnetic counterpart except potentially from DM annihilation.
- The "missing satellite problem" and its resolution through baryonic physics and detection limits — but the dark subhalo population remains largely unconstrained observationally.
- Cross-ref Ch. 1 §1.4.3 for density profiles (NFW, concentration-mass relation) and the J-factor formalism that determines gamma-ray visibility.

---

## 5.3 Dark Matter Subhalos as Gamma-Ray Targets (~2 pages)

**Purpose:** Connect the theoretical subhalo population to observable gamma-ray signatures and explain why dark subhalos are uniquely compelling DM targets.

### 5.3.1 Expected Gamma-Ray Properties

**Key points:**
- Gamma-ray flux from DM annihilation: Φ_DM ∝ (⟨σv⟩ / 2m²_DM) × J × (dN_γ/dE). The J-factor is the line-of-sight integral of ρ² (cross-ref Ch. 1 §1.4.4).
- For thermal relic cross-sections (⟨σv⟩ ~ 3×10⁻²⁶ cm³/s), only the brightest (most massive, nearest) subhalos produce detectable gamma-ray fluxes.
- Spectral shape: determined by the annihilation channel (bb̄ → peaked at ~m_DM/20; τ⁺τ⁻ → harder spectrum). All subhalos with the same DM mass share the same spectral shape → distinctive population signature.
- Angular extent: the brightest subhalos may subtend 0.2°–0.3° (Coronado-Blázquez et al. 2022), marginally resolvable by Fermi-LAT; fainter ones are point-like.
- Spatial distribution: approximately isotropic for subhalos at |b| > 10°, in contrast to Galactic source populations concentrated near the plane.

### 5.3.2 Detection Prospects

**Key points:**
- J-factor distributions from N-body simulations (Aguirre-Santaella et al. 2024 [`2024MNRAS.530.2496A`]): two prescriptions based on M_sub and V_max, spanning current uncertainties in subhalo structural modeling.
- Expected number of detectable subhalos as a function of (m_DM, ⟨σv⟩): at thermal relic cross-section, O(0–30) subhalos could exceed the Fermi-LAT detection threshold (TS > 25) depending on J-factor model.
- Why dark subhalos are uniquely clean: no astrophysical emission to confuse the DM signal (unlike the GCE, which is contaminated by MSPs, diffuse emission, cosmic-ray interactions). A dark subhalo is a "pure" DM laboratory.
- However, distinguishing a DM subhalo from an unidentified astrophysical source based on gamma-ray properties alone is the central challenge.

---

## 5.4 The Unassociated Source Problem (~2 pages)

**Purpose:** Introduce the observational landscape — the Fermi-LAT catalog, the nature of unassociated sources, and prior efforts to identify DM candidates among them.

### 5.4.1 The Fermi-LAT Source Catalogs

**Key points:**
- The 4FGL-DR4 catalog contains ~7200 sources; 2428 (~33%) are unassociated — no identified counterpart at other wavelengths.
- "Association" requires positional coincidence with a known source in radio, optical, or X-ray catalogs; association completeness depends on source brightness, localization, and Galactic latitude.
- Cross-ref Ch. 2 §2.2 and §2.3 for source classes (blazars, pulsars) and the Fermi-LAT instrument.

### 5.4.2 What Are the Unassociated Sources?

**Key points:**
- Majority are expected to be astrophysical: faint AGNs lacking counterparts (below the sensitivity of radio/optical surveys), pulsars with unfavorable beaming geometry, or sources in confused regions near the Galactic plane.
- At |b| > 10° (the region relevant for subhalo searches): 1282 unassociated sources. The composition is not directly measurable.
- No unassociated source has been confirmed as a DM subhalo.

### 5.4.3 Previous DM Subhalo Searches

**Key points:**
- **Hand-crafted approaches** [`2010PhRvD..82f3501B`, `2012A&A...538A..93Z`, `2015JCAP...12..035B`, `2017PhRvD..96f3009C`, `2019JCAP...07..020C`, `2019JCAP...11..045C`]: select candidates based on spectral/spatial properties consistent with DM (no variability, no association, spectral curvature consistent with annihilation). Coronado-Blázquez et al. (2019) identified 16 candidates in 3FGL.
- **ML classification approaches** [`2016ApJ...825...69M`, `2023JCAP...07..033B`, `2023MNRAS.520.1348G`]: train classifiers on labeled sources (AGN/pulsar/DM) and apply to unassociated sources. Butter et al. (2023) reported 281 candidates in most conservative scenario.
- **Common strategy:** "classify-and-count" — identify N candidates, then assume N_DM ≤ N candidates to derive upper bounds on ⟨σv⟩.
- **Fundamental limitation:** the classify-and-count approach relies on ad hoc probability thresholds, balanced training sets that do not reflect actual class prevalences, and the assumption that training and target distributions are identical. These limitations motivate the methodological development in §5.5.

---

## 5.5 From Classification to Quantification: The Dataset Shift Challenge (~5–6 pages)

**Purpose:** Present the key methodological innovation as a pedagogical narrative. This section builds on the general formalism introduced in Ch. 3 §3.4 and develops the specific application to DM subhalo searches in depth.

> **Scope note:** Ch. 3 §3.4 introduces the mathematical framework of dataset shift (covariate shift, prior shift, combined shift) in ~2.5 pages. This section focuses on *why* these shifts matter specifically for subhalo searches, *how* standard approaches fail, *what* quantification learning is and why it resolves the problem, and *how* the mixture model connects these ideas. The mathematical equations from Ch. 3 §3.4 are cross-referenced rather than re-derived.

### 5.5.1 Why Standard Classification Fails for DM Subhalo Searches (~1.5 pages)

**Key points:**
- Recap the setup (cross-ref Ch. 3 §3.4): classifiers are trained on associated sources (known labels) and applied to unassociated sources (unknown labels). The fundamental assumption p_train(x,k) = p_target(x,k) is violated.
- **The training set problem:** There are zero confirmed DM subhalos → the "DM" class has no real training data. Simulated DM spectra are used as surrogates, but the simulation-to-reality gap is uncontrolled.
- **The balanced class fallacy:** standard ML practice balances classes (50/50 AGN/pulsar, or 33/33/33 AGN/pulsar/DM). This has nothing to do with the actual prevalences. Among associated sources at |b| > 10°, AGNs outnumber pulsars ~10:1. Using balanced classes artificially inflates the predicted fraction of rare classes.
- **The threshold arbitrariness:** the number of DM candidates depends entirely on the probability threshold chosen (e.g., p_DM > 0.5 vs. p_DM > 0.9). The threshold is not derived from any statistical principle; it is a free parameter that directly determines the final constraint.
- **Concrete example:** Butter et al. (2023) find 281 candidates (conservative) — a number so large that the resulting ⟨σv⟩ bounds are extremely weak. A different threshold would give a different number and different bounds. Neither threshold is "correct."

### 5.5.2 Dataset Shift in the Fermi-LAT Context (~1.5 pages)

**Key points:**
- The distributions of associated and unassociated sources *are* measurably different (Figure from paper: α and β histograms). Cross-ref Ch. 3 §3.4, Figure 3.X for the visual evidence.
- **Prior shift manifestation:** the fraction of Galactic sources (mostly pulsars) among unassociated sources (~29%) is much higher than among associated sources (~6%) at |b| > 10°. This is expected: pulsars in unfavorable beaming geometry remain unassociated, while bright blazars are easily associated.
- **Covariate shift manifestation:** even within a single source class, the feature distributions differ between associated and unassociated populations. Unassociated sources are systematically fainter (harder to associate) and have larger spectral uncertainties.
- **The degeneracy:** the same observed mismatch can be explained by prior shift, covariate shift, or the presence of a genuinely new source class (DM subhalos). This degeneracy is the central statistical challenge (cross-ref Ch. 3 §3.4, "Combined shift").
- **Why ignoring the shift is dangerous:** a classifier that assumes p_train = p_target will misattribute the excess of pulsar-like unassociated sources either to pulsars (underestimating DM) or, worse, to DM (overestimating DM) depending on the training choices.

### 5.5.3 Quantification Learning: From p(k|x) to p(x|k) (~1.5 pages)

**Key points:**
- **The classification paradigm:** standard ML estimates p(k|x) — "what is the probability that source x is class k?" This is useful for individual classification but does not give a coherent model of the population.
- **The quantification paradigm:** instead, estimate p(x|k) — "what is the distribution of features x for class k?" — and then determine the class prevalences p(k) by fitting the mixture model to the target data. This is called *quantification learning* (González et al. 2017, Esuli et al. 2023, Moreo et al. 2024).
- **Key advantage:** quantification learning directly estimates class prevalences without assuming they match the training set. The prevalences (including a potential new DM class) are free parameters fit to the data.
- **Connection to template fitting in astrophysics:** the approach is analogous to fitting photon count maps as linear combinations of spatial templates (e.g., gas maps, IC maps, isotropic background) — a standard technique in Fermi-LAT analyses. Here, the "templates" are the spectral parameter distributions of each source class.
- **Generative vs. discriminative:** this is a generative model (estimates p(x,k) = p(x|k)p(k)) rather than a discriminative model (estimates p(k|x) directly). Generative models can be sampled to produce mock data for validation, and they yield a well-defined likelihood function — essential for statistical hypothesis testing.

### 5.5.4 The Mixture Model Concept (~1 page)

**Key points:**
- The unassociated source distribution is modeled as a mixture:
  p_unas(x) = [Σ_k π_k p_assoc(x|k)] C̃(x; θ_cov) + π_DM p_DM(x; θ_DM)
  (reference equation from Ch. 3 §3.4; the full derivation appears in the paper's Section 2.3).
- **Three components:** Galactic astrophysical, extragalactic astrophysical, and (hypothetical) DM subhalos.
- **Prior shift:** handled by fitting the class prevalences π_k — they need not match the training set.
- **Covariate shift:** handled by the modulation function C̃(x), modeled as a product of sigmoid functions (cross-ref Ch. 3 §3.4, Eq. 3.XX) — one monotonic function per feature dimension.
- **DM component:** derived from Monte Carlo simulations using J-factor distributions from N-body simulations and Fermi-LAT instrument response functions. Not a free-form template; fully determined by DM physics parameters (m_DM, ⟨σv⟩, channel).
- **Likelihood:** the product of p_unas(x_i) over all unassociated sources yields a well-defined likelihood → can maximize to find best-fit parameters → can profile to set upper bounds on ⟨σv⟩.
- **Why this is better than classify-and-count:**
  1. No ad hoc probability threshold.
  2. Natural handling of both prior and covariate shifts.
  3. The DM contribution is determined by maximum likelihood, not by counting candidates.
  4. Statistical significance and upper bounds are derived from the likelihood ratio (Wilks' theorem), giving them a rigorous statistical interpretation.
- **Transition:** "The remainder of this chapter presents the full analysis, beginning with the data selection and the detailed construction of the mixture model."

---

## 5.6 The Search for Dark Matter Subhalos Among Fermi-LAT Unassociated Sources

**Source:** Paper 4 (`dm_halos`, arXiv:2503.14584) — included in near-entirety.

The paper's abstract and introduction (Section 1) are replaced by the material above (§5.1–5.5). The paper body begins from its Section 2 (Statistical Analysis / Data Selection).

**Paper sections as thesis sections:**
- 5.6 → Paper Section 2 (Statistical analysis: data selection, covariate/prior shifts, statistical model)
- 5.7 → Paper Section 3 (DM subhalos model: J-factors, gamma-ray emission simulation)
- 5.8 → Paper Section 4 (Mixture model results and DM annihilation limits)
- 5.9 → Paper Section 5 (Discussion and conclusions)
- Appendices A–E → included as thesis appendices or inline

---

## 5.10 Summary

**Key points:**
- No significant excess of DM subhalos is found among Fermi-LAT unassociated sources.
- 95% CL upper bounds on ⟨σv⟩ are derived for the bb̄ channel across m_DM = 10 GeV – 1 TeV.
- The quantification learning approach provides the first maximum-likelihood upper bounds on DM from subhalo searches — a well-defined statistical framework compared to classify-and-count.
- The bounds are competitive with but ~1 order of magnitude weaker than dSph limits, primarily because subhalo positions/J-factors are unknown (unlike dSphs).
- Outlook: velocity-dependent cross-sections (Sommerfeld enhancement) could make nearby low-mass subhalos more visible; future surveys (LSST, SKA) may enable multiwavelength confirmation of DM subhalo candidates.
- Connection forward: the limitations of individual source identification motivate the population-level approach of Part III (Chapters 6–7), where sub-threshold sources are probed statistically rather than individually.

---

## Structural Notes

- **Figures for introduction:** Consider including:
  - Subhalo mass function and/or N-body simulation visualization (from VL-II or Aquarius)
  - α–β distributions for associated vs. unassociated sources (Fig. 1 from Paper 4, already used in Ch. 3 §3.4 — check if same figure can be reused or a variant is needed)
  - Conceptual schematic: O(10^16) subhalos → O(10²–10³) above Fermi-LAT threshold → subhalo candidates among ~1300 unassociated sources at |b| > 10°
  - Classify-and-count vs. quantification learning comparison diagram
- **Tone:** Scholarly and neutral. Frame the methodological contribution as a natural evolution of the field, not a revolution. The dataset shift problem is presented as a known issue in ML (not discovered by the author) that had not been addressed in this astrophysical context.
- **Length budget:** §5.1 (0.5p) + §5.2 (2p) + §5.3 (2p) + §5.4 (2p) + §5.5 (5.5p) + §5.6 transition (0.5p) = **~12.5 pages**, within the 15-page ceiling.
- **Relationship to Ch. 3 §3.4:** The introduction references Ch. 3 §3.4 for the mathematical definitions (Eqs. 3.XX–3.XX) and uses the same notation. Chapter 5's treatment is primarily *contextual* and *applied* — why these shifts matter for this specific physics problem — while Ch. 3 provides the *formal* framework.
