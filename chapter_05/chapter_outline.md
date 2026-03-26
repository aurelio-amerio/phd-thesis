---
title: "Chapter 5 — Searching for Dark Matter Substructures"
date: 2026-03-26
source_skill: chapter_outline
chapter: chapter_05
status: outline
tags: [dm-subhalos, fermi-lat, unassociated-sources, dataset-shift, quantification-learning, domain-adaptation]
---

# Chapter 5 — Searching for Dark Matter Substructures

**Estimated length:** ~12 pages (introduction, §5.1–5.5) + paper body + appendices
**Page ceiling:** 15 pages for introduction

This chapter opens with a pedagogical introduction, then transitions into Paper 4 (`dm_halos`, arXiv:2503.14584). The introduction replaces the paper's abstract and Section 1.

---

## 5.1 Introduction (~0.5 page)

**Purpose:** Frame subhalo searches as the second prong of Part II.

**Key points:**
- Chapter 4 examined the brightest expected DM signal (GCE); this chapter shifts to a complementary approach: searching for individual dark matter subhalos among Fermi-LAT point sources.
- The conceptual leap: rather than analyzing a known excess, we ask whether *any* cataloged gamma-ray sources could be dark matter subhalos.
- Preview the narrative arc: ΛCDM predicts an enormous dark subhalo population → a fraction may produce detectable gamma rays → they would appear as unassociated sources → identifying them requires handling the mismatch between labeled and unlabeled data.

**Cross-references:** Ch. 4 (GCE); Ch. 1 §1.4.3 (density profiles, J-factors); Ch. 2 (Fermi-LAT source classes).

---

## 5.2 Dark Matter Substructure in ΛCDM (~2 pages)

**Purpose:** Establish why dark subhalos exist and what ΛCDM predicts for the Milky Way's subhalo population. Covers the mass function and its slope, the simulation resolution floor, and the impact of baryonic effects on subhalo survival.

### 5.2.1 Hierarchical Structure Formation

**Key points:**
- ΛCDM predicts bottom-up hierarchical assembly; smaller halos merge to form larger ones, retaining gravitationally bound subhalos.
- N-body simulations (Via Lactea II, Aquarius) resolve subhalos down to ~10⁴ M☉; extrapolation extends to ~10⁻¹ M☉ via repopulation techniques.
- The subhalo mass function dN/dM ∝ M^{−α} with α ≈ 1.9 — the MW should host O(10¹⁵–10¹⁶) total subhalos.

### 5.2.2 Luminous Satellites vs. Dark Subhalos

**Key points:**
- Subhalos above ~10⁸ M☉ can retain baryons → observed as dwarf spheroidal galaxies. ~60 known MW satellites.
- The vast majority (below ~10⁸ M☉) are "dark": no stars, no gas, no EM counterpart except potentially from DM annihilation.
- The "missing satellite problem" and its resolution through baryonic physics and detection limits.
- Paragraph on baryonic effects: tidal stripping, disk shocking modify the subhalo population, especially in the inner Galaxy. Hydrodynamical simulations (FIRE, Auriga) don't resolve below ~10⁶ M☉ — low-mass survival remains uncertain.
- Cross-ref Ch. 1 §1.4.3 for density profiles (NFW, concentration-mass) and the J-factor formalism.

**Figures:**
- **Fig. 5.1:** N-body simulation visualization (VL-II or Aquarius subhalo distribution) — establishes the "sea of subhalos" visually. Source from the literature; find a suitable published figure during drafting.

---

## 5.3 Dark Matter Subhalos as Gamma-Ray Targets (~1.5 pages)

**Purpose:** Connect the subhalo population to observable gamma-ray signatures. Present the wide range of detectability predictions across the parameter space, motivating the search as a genuine investigation: the analysis will determine whether any DM subhalo contribution is present and, if not, translate the null result into constraints on ⟨σv⟩.

### 5.3.1 Expected Gamma-Ray Properties

**Key points:**
- Gamma-ray flux from DM annihilation: Φ_DM ∝ (⟨σv⟩ / 2m²_DM) × J × (dN_γ/dE). Cross-ref Ch. 1 §1.4.4.
- Spectral shape determined by annihilation channel (bb̄ peaked at ~m_DM/20; τ⁺τ⁻ harder). All subhalos with same DM mass share the same spectral template → distinctive population signature.
- Angular extent: brightest subhalos may subtend 0.2°–0.3° (Coronado-Blázquez et al. 2022), marginally resolvable; fainter ones are point-like.
- Spatial distribution: approximately isotropic at |b| > 10°, contrasting Galactic source populations.

### 5.3.2 Detection Predictions and Search Strategy

**Key points:**
- **Wide prediction landscape:** The expected number of detectable subhalos spans orders of magnitude — from zero to several tens — depending on the assumed ⟨σv⟩, J-factor model (V_max vs. M_sub, tidal vs. point-like integration), and subhalo survival assumptions. No single prediction is privileged; these uncertainties are exactly what makes a data-driven search necessary.
- The precise count depends critically on: (1) the true ⟨σv⟩, (2) the J-factor prescription, (3) baryonic survival of low-mass subhalos.
- **Search strategy:** The analysis proceeds in two stages: first, determine whether the data favor a model with a DM subhalo component over a purely astrophysical one; second, if no statistically significant excess is found, translate the result into upper limits on ⟨σv⟩ — further characterizing the sensitivity of the technique.
- **Why both outcomes are informative:** A detection would constitute direct evidence for the ΛCDM subhalo population through particle annihilation. Dark subhalos are uniquely clean targets: unlike the GCE, there is no astrophysical emission to confuse the DM signal — a dark subhalo is a "pure" DM laboratory, making any detection particularly informative. A null result constrains ⟨σv⟩ and benchmarks the reach of current instruments, directly informing forecasts for CTA/SWGO.
- Defer quantitative J-factor distributions and detection threshold calculations to the paper body (Section 3).

> [!NOTE]
> **Action item:** Search the literature further for context on DM subhalo detectability predictions (e.g., Coronado-Blázquez et al. 2022, Calore et al. 2019, Arina et al. 2024 CosmiXs predictions, sensitivity forecasts for CTA/SWGO). Incorporate key quantitative statements about detection horizons.

---

## 5.4 The Unassociated Source Problem (~1.5 pages)

**Purpose:** Introduce unassociated sources and prior DM subhalo search efforts. Provides a brief survey with 2–3 representative works per approach; the detailed comparison with prior results is deferred to the paper body.

### 5.4.1 Unassociated Sources in Fermi-LAT Catalogs

**Key points:**
- 4FGL-DR4: ~7200 sources, 2428 (~33%) unassociated. At |b| > 10°: 1282 unassociated.
- "Association" requires multi-wavelength counterpart; completeness depends on brightness, localization, latitude.
- Majority expected to be astrophysical: faint AGNs, pulsars with unfavorable beaming, confused regions.
- No unassociated source has been confirmed as a DM subhalo.
- Cross-ref Ch. 2 §2.2–2.3.

### 5.4.2 Previous DM Subhalo Searches

**Key points (brief survey):**
- **Hand-crafted approaches:** Coronado-Blázquez et al. (2019) identified 16 candidates in 3FGL using spectral, spatial, and variability criteria.
- **ML classification:** Butter et al. (2023) found 281 candidates in the most conservative scenario using supervised classifiers.
- **Common strategy:** "classify-and-count" — identify N candidates, assume N_DM ≤ N, derive ⟨σv⟩ bounds.
- **Fundamental limitation:** relies on ad hoc probability thresholds, balanced training sets that don't reflect real prevalences, and the assumption that training and target distributions are identical. These failures motivate §5.5.

---

## 5.5 From Classification to Quantification: The Dataset Shift Challenge (~5–6 pages)

**Purpose:** Present the methodological innovation that motivates the paper. Builds on the formal dataset shift framework introduced in Ch. 3 §3.4; this section focuses on *why* these shifts matter for subhalo searches, *how* classify-and-count fails, and *what* quantification learning offers as a solution. Equations are cross-referenced from Ch. 3 §3.4 rather than re-derived.

### 5.5.1 Why Standard Classification Fails for DM Subhalo Searches (~1.5 pages)

**Key points:**
- Recap setup (cross-ref Ch. 3 §3.4): classifiers trained on associated sources, applied to unassociated. The assumption p_train(x,k) = p_target(x,k) is violated.
- **The training set problem:** Zero confirmed DM subhalos → the "DM" class has no real training data. Simulated spectra are surrogates with uncontrolled simulation-to-reality gap.
- **The balanced class fallacy:** Standard ML balances classes (33/33/33 AGN/pulsar/DM), but real prevalences are ~90/10/? at |b| > 10°. Balanced training artificially inflates rare-class predictions.
- **The threshold arbitrariness:** Number of DM candidates depends entirely on chosen probability threshold (p_DM > 0.5 vs. > 0.9). No statistical principle determines the threshold.
- **Concrete example:** Butter et al. (2023) find 281 candidates → extremely weak ⟨σv⟩ bounds. Different threshold → different number → different bounds.

### 5.5.2 Dataset Shift in the Fermi-LAT Context (~1.5 pages)

**Key points:**
- Associated and unassociated source distributions *are* measurably different. Cross-ref Ch. 3 §3.4 for the visual evidence and formal definitions.
- **Prior shift:** Galactic sources (pulsars) constitute ~29% of unassociated vs. ~6% of associated at |b| > 10°. Pulsars with unfavorable beaming remain unassociated; bright blazars are easily associated.
- **Covariate shift:** Within a single class, feature distributions differ. Unassociated sources are systematically fainter and have larger spectral uncertainties.
- **The degeneracy:** The same mismatch can be explained by prior shift, covariate shift, or a genuinely new source class (DM subhalos). This is the central statistical challenge (cross-ref Ch. 3 §3.4, "Combined shift").
- **Why ignoring the shift is dangerous:** A classifier assuming p_train = p_target misattributes the excess of pulsar-like unassociated sources either to pulsars (underestimating DM) or to DM (overestimating DM).

### 5.5.3 Quantification Learning: From p(k|x) to p(x|k) (~1 page)

**Key points:**
- **Classification paradigm:** Standard ML estimates p(k|x). Useful for individual sources but doesn't model the population coherently.
- **Quantification paradigm:** Estimate p(x|k) and fit class prevalences p(k) to the target data. This is *quantification learning* (González et al. 2017, Moreo et al. 2024).
- **Key advantage:** Prevalences (including a potential DM class) are free parameters fit to data, not assumed from training.
- **Astrophysics analogy:** Analogous to template fitting in Fermi-LAT spatial analyses — here the "templates" are spectral parameter distributions of each source class.
- **Generative vs. discriminative:** This is a generative model yielding a well-defined likelihood → essential for statistical hypothesis testing and mock data generation.
- Cross-ref Ch. 3 §3.4 for the formal framework (Eqs. 3.XX–3.XX).

### 5.5.4 The Mixture Model Concept (~1 page)

**Key points:**
- The unassociated source distribution is modeled as a three-component mixture: Galactic + extragalactic astrophysical + (hypothetical) DM subhalos.
- Prior shift: handled by fitting π_k. Covariate shift: handled by sigmoid modulation C̃(x). (Cross-ref Ch. 3 §3.4 for equations.)
- DM component: fully determined by physics parameters (m_DM, ⟨σv⟩, channel) via Monte Carlo simulation with J-factor distributions. Not a free-form template.
- Likelihood: product over unassociated sources → maximize → profile for ⟨σv⟩ upper bounds.
- **Why this is better than classify-and-count:** (i) no threshold, (ii) handles both shifts, (iii) DM contribution by maximum likelihood, (iv) rigorous statistical interpretation via likelihood ratio.
- **Transition:** "The remainder of this chapter presents the full analysis."

---

## Paper Body — §5.6 onward

**Source:** Paper 4 (`dm_halos`, arXiv:2503.14584) — included from Section 2 onward.

| Thesis Section | Paper Section | Content |
|---|---|---|
| §5.6 | Section 2 | Statistical analysis: data selection, covariate/prior shifts, statistical model |
| §5.7 | Section 3 | DM subhalos model: J-factors, gamma-ray emission simulation |
| §5.8 | Section 4 | Mixture model results and DM annihilation limits |
| §5.9 | Section 5 | Discussion and conclusions |

## Appendices (at end of chapter)

Paper appendices included as thesis chapter appendices for self-consistency:

| Appendix | Content |
|---|---|
| 5.A | Simulation of gamma-ray signals from DM subhalos |
| 5.B | Details of model optimization with the EM algorithm |
| 5.C | Consistency checks of the model |
| 5.D | DM signal injection tests |
| 5.E | Performance measures |

## Summary (~0.5 page)

- No significant excess of DM subhalos found among Fermi-LAT unassociated sources.
- 95% CL upper bounds on ⟨σv⟩ for bb̄ across m_DM = 10 GeV – 1 TeV.
- First maximum-likelihood upper bounds from subhalo searches.
- Bounds competitive with but ~1 order of magnitude weaker than dSph limits (subhalo positions/J-factors unknown).
- Outlook: Sommerfeld enhancement, future instruments (CTA, SWGO).
- Connection forward: limitations of individual source ID motivate population-level approaches (Part III).

---

## Structural Notes

- **Figures in introduction:** Only Fig. 5.1 (N-body simulation visualization). Paper figures stay in the paper body where they are.
- **No repeated figures:** Do not duplicate Paper 4's figures in the introduction.
- **Tone:** Scholarly, neutral. The search is a genuine investigation of whether DM subhalos contribute to the unassociated source population; both detection and null outcomes are scientifically valuable. Frame quantification learning as a natural evolution, not a revolution.
- **Length budget:** §5.1 (0.5p) + §5.2 (2p) + §5.3 (1.5p) + §5.4 (1.5p) + §5.5 (5.5p) + transition (0.5p) = **~11.5 pages**.
- **Relationship to Ch. 3 §3.4:** Cross-reference for formal definitions and equations. Ch. 5 is *contextual* and *applied*.

> [!NOTE]
> **Ch. 3 §3.4 action item:** Rethink the α–β distribution figure currently in §3.4. Consider replacing with a different graphic that illustrates the dataset shift concept generically, since the paper-specific figure should remain in the paper body (Ch. 5).
