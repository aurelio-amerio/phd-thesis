# Chapter 8 — Cross-Correlations and Future Prospects

## Introduction (untitled, ~1 page)

This chapter introduces Part IV of the thesis and bridges from the resolved-source analyses of Parts II–III to a cosmological-scale dark matter search.

### Key points
- Parts II–III searched for DM at increasing levels of statistical sophistication: targeted GCE analysis (Ch. 4), individual subhalo identification (Ch. 5), and population-level characterization of the unresolved sky (Chs. 6–7). No definitive DM signal was identified.
- If DM annihilates or decays, gamma-ray emission occurs in every DM halo and subhalo across all cosmic epochs. This cumulative, unresolved signal contributes to the UGRB.
- Central question: can we isolate this contribution by exploiting its unique spatial signature — the anisotropy pattern imprinted by the large-scale distribution of DM structures?
- Chapter roadmap: Section 8.1 motivates the shift to cosmological scales. Section 8.2 introduces cross-correlations as the technique. Section 8.3 presents CTAO. The paper that follows applies this framework.

### Connections
- **Back**: Parts II–III (Chs. 4–7) establish the landscape of DM searches this chapter extends.
- **Forward**: Paper 5 (Pinetti et al. 2025) applies cross-correlations to forecast CTAO's DM sensitivity.
- **Chapter 3**: Section 3.5 provides the formal APS and cross-correlation machinery referenced throughout.

---

## 8.1 From Resolved Sources to the Cosmic Web (~3–4 pages)

Explains *why* we shift from source-level searches to cosmological-scale cross-correlations.

### 8.1.1 The Thesis So Far: Scales and Strategies (~1.5 pages)

Recaps Parts II–III — brief, no re-derivation — framed by what each approach achieved and its scope.

#### Key points
- **GCE (Ch. 4):** Targeted the strongest expected DM signal. The GeV excess is real, but a decade of analysis has not resolved the DM vs. MSP degeneracy due to systematic uncertainties in diffuse emission modeling.
  - Refs: Daylan et al. (1402.6703), Bartels et al. (1506.05104), Leane & Slatyer (1904.08430), Buschmann et al. (1908.10874)
- **Subhalo searches (Ch. 5):** Searched for individual DM subhalos among Fermi-LAT unassociated sources via ML classification. No significant DM subhalo population was identified, consistent with theoretical expectations at current sensitivity.
  - Refs: Amerio et al. (2503.14584), Coronado-Blázquez et al. (2103.10861)
- **Population statistics (Chs. 6–7):** Shifted scope to characterizing the *aggregate* gamma-ray source population regardless of origin. dN/dS recovery and probabilistic cataloging mapped the unresolved sky down to fluxes ~50× below threshold. This work did not target DM specifically, but it characterized the landscape in which any DM contribution must hide.
  - Refs: Amerio et al. (2302.01947, 2306.16483), Zechlin et al. (1512.07190)
- The conceptual pivot: each approach operated at a specific astrophysical scale. We now ask whether the *cumulative* gamma-ray emission from all unresolved DM structures across cosmological distances leaves a detectable spatial imprint in the UGRB.

#### Transition
"The signal we seek is not a smooth, featureless glow — it is a specific pattern of spatial anisotropies produced by the hierarchical distribution of DM halos and subhalos that form the cosmic web."

### 8.1.2 Dark Matter in the Cosmic Web (~1.5–2 pages)

Introduces hierarchical structure formation and the UGRB as the observable.

#### Key points
- **Hierarchical structure**: DM forms a hierarchical network of halos at all scales (clusters → galaxies → subhalos). DM annihilation/decay produces gamma-rays within each individual structure.
  - Refs: Ullio et al. (astro-ph/0207125), Fornasa & Sánchez-Conde (1502.02866), Peebles textbook
- **The UGRB**: Cumulative emission from unresolved sources. Contains astrophysical components (blazars HSP/LISP, SFGs, misaligned AGN) and potentially DM emission from the full population of halos and subhalos.
  - Refs: Ackermann et al. (1410.3696), Fornasa & Sánchez-Conde (1502.02866)
- **Anisotropy as the discriminating handle**: The UGRB is not perfectly isotropic. Each contributing population imprints spatial fluctuations with different angular signatures, energy spectra, and redshift distributions. The energy spectrum alone cannot distinguish DM from astrophysical backgrounds (spectral degeneracy). Spatial anisotropies provide the additional dimensional handle.
  - Refs: Ando & Komatsu (astro-ph/0512217), Ackermann et al. (1202.2856)
- **From auto-correlation to cross-correlation**: Auto-correlations of the gamma-ray sky are noise-dominated and lack redshift information. Cross-correlating with a gravitational tracer (galaxy catalog, cosmic shear) provides redshift selectivity and breaks degeneracies.
  - Refs: Fornengo & Regis (1312.4835), Camera et al. (1212.5018)
- **Potential figure**: Window functions W_γ(z) for DM annihilation vs. astrophysical sources, from Paper 5 Fig. 4.

#### Transition
"The angular cross-power spectrum between the UGRB and galaxy catalogs, introduced in Section 3.5, provides the mathematical framework to quantify these correlations. We now discuss how this technique exploits the physical differences between DM and astrophysical signals."

---

## 8.2 The Cross-Correlation Technique (~3 pages)

Explains *how* cross-correlations work at a conceptual/physical level, without re-deriving equations.

### 8.2.1 Tomographic Redshift Slicing (~1 page)

#### Key points
- Window functions W_γ(z) and W_g(z) describe the redshift distribution of each observable. The cross-power spectrum is sensitive to the *overlap* of these two distributions.
- DM annihilation peaks at z < 0.1 (ρ² weighting). Correlating with local galaxy catalogs (2MASS, 2MRS at z ≲ 0.1) maximizes this overlap.
- Astrophysical backgrounds at higher redshifts (blazars at z ~ 0.3–0.4 at 50 GeV, z ~ 0.1–0.2 at >1 TeV due to EBL absorption) do not correlate with a z < 0.1 galaxy catalog — they effectively vanish from the cross-correlation signal.
- Cross-ref Section 3.5.1 for the formal definition of window functions and Limber approximation.
  - Refs: Pinetti et al. (2505.20383) Fig. 4 and Fig. 15, Xia et al. (1503.05918)

### 8.2.2 Why Cross-Correlation Outperforms Auto-Correlation (~1 page)

#### Key points
- Auto-correlation: dominated by blazar Poisson shot noise; photon noise C_N adds directly to the signal, requiring accurate noise subtraction.
- Cross-correlation: photon noise in the gamma-ray map and galaxy shot noise are physically independent — their cross-noise vanishes on average. Noise only inflates error bars, not the signal itself.
- The 1-halo / 2-halo decomposition provides the physical power: 1-halo term probes DM + hosted galaxies within the same halo (small scales), 2-halo term probes large-scale clustering of different halos (large scales).
- Result preview: cross-correlation yields ~5× improvement in DM sensitivity over auto-correlation (Paper 5).
- Cross-ref Section 3.5.2 for the variance formula and SNR/Δχ² definitions.
  - Refs: Fornengo & Regis (1312.4835), Camera et al. (1212.5018), Pinetti et al. (2505.20383)

### 8.2.3 The "Golden Channel": Low-Redshift Galaxy Catalogs (~1 page)

#### Key points
- DM annihilation signal peaks at z < 0.3 due to ρ² weighting.
- 2MASS (~1 million galaxies, z ≲ 0.1–0.2) and 2MRS (spectroscopic subsample). Dense, local catalogs minimize galaxy shot noise and maximize overlap with the DM window function.
- Prior Fermi-LAT cross-correlation results: 4.5σ with SDSS quasars, 3.6σ with 2MASS, 10σ with NVSS (contaminated by 1-halo), 3σ with SDSS main galaxies (Xia et al. 2015). Cosmic shear: null detection, used for upper limits (Shirasaki et al. 2014).
- Cross-correlation uniquely bridges an electromagnetic DM signal with a gravitational tracer — a positive detection would demonstrate that DM is indeed a particle, not a modification of gravity.
  - Refs: Cuoco et al. (1506.01030), Xia et al. (1503.05918), Fornasa & Sánchez-Conde (1502.02866) Sec. 5

#### Transition
"The cross-correlation technique requires an instrument with broad sky coverage, good angular resolution at the relevant multipoles, and sensitivity at energies where heavy DM candidates produce their signal. The Cherenkov Telescope Array Observatory meets all three requirements."

---

## 8.3 The Cherenkov Telescope Array Observatory (~2–3 pages)

Introduces CTAO and transitions into the paper.

### 8.3.1 From Fermi-LAT to CTAO (~1 page)

#### Key points
- Fermi-LAT: 15+ years of data, 0.1–300 GeV, full-sky survey, effective area ~1 m².
- CTAO: ground-based IACT, 20 GeV – 300 TeV, ~10× better angular resolution, effective area ~10⁶ m². Three telescope types: LST (low E), MST (mid E), SST (high E, Southern only).
- CTAO probes the TeV mass range where heavy WIMPs (m_χ > 1 TeV) produce their signal, beyond Fermi-LAT's reach.
- At >20 GeV, SFGs and misaligned AGN are negligible; only blazars (HSP, LISP) contribute as astrophysical background.
  - Refs: Acharya et al. (2018, CTA science book), Mazin (1907.08530), Pinetti et al. (2505.20383) Sec. II

### 8.3.2 The Extragalactic Survey (EGAL) (~1–1.5 pages)

#### Key points
- CTAO's Key Science Project: survey of 25% of the extragalactic sky (|b| > 5°, −90° < l < 90°).
- ~1000 hours total: 400 h Southern array, 600 h Northern array.
- Grid of pointings spaced by ~3°, effective exposure ~3 hours per point.
- Off-source scenario: ~50 hours from accumulated pointed observations.
- Uniform sky coverage critical for anisotropy studies: non-uniform coverage introduces spurious angular correlations.
  - Refs: Acharya et al. (2018) Sec. 8, Pinetti et al. (2505.20383) Sec. II.A

### 8.3.3 Transition to the Paper (~0.5 page)

#### Key points
- Connect chapter introduction to the paper: "In the following, we present a sensitivity forecast for detecting DM signals through cross-correlations between the CTAO extragalactic survey and the 2MASS galaxy catalog."
- What the paper shows: SNR for astrophysical source detection, Δχ² sensitivity to DM annihilation (⟨σv⟩ ~ 10⁻²³ cm³/s) and decay (τ ~ 10²⁷ s), comparison with dwarf galaxy and cluster constraints, ~5× improvement of cross-correlation over auto-correlation.
  - Ref: Pinetti et al. (2505.20383)

---

## Cross-Reference Map

| Element | Source | Chapter 8 action |
|---|---|---|
| APS formalism (C_ℓ, Limber, window functions) | Section 3.5.1 | Cross-reference |
| SNR, Δχ² test statistic | Section 3.5.2 | Cross-reference |
| Halo model (1h/2h), beam function, noise terms | Section 3.5 (to be expanded) | Cross-reference |
| UGRB definition and composition | Section 2.2 | Brief recap in 8.1.2 |
| DM halo profiles, J-factor | Section 1.4 | Brief recap in 8.1.2 |
| GCE (Chs. 4) | Part II | Brief recap in 8.1.1 |
| Subhalo searches (Ch. 5) | Part II | Brief recap in 8.1.1 |
| dN/dS and probabilistic catalogs (Chs. 6–7) | Part III | Brief recap in 8.1.1 |
