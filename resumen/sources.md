# Resumen source dossier

Verified facts for the English summary (`resumen_en.tex`). Every fact carries its source `file:line`. Bib keys listed per section are verified against `bibliography.bib` (grep line noted). Facts not listed here must NOT appear in the resumen.

## Thesis papers (verified bib keys)

- Paper 1 (dN/dS via deep learning/SBI, ch. 6): `Amerio:2023uet` — bibliography.bib:6787
- Paper 2 (gPCS sub-threshold catalog, ch. 7): `Amerio:2023rjn` — bibliography.bib:5902
- Paper 3 (MSPs in globular clusters / GCE, ch. 4): `Amerio:2024qor` — bibliography.bib:6800
- Paper 4 (DM subhalos among unassociated sources, ch. 5): `Amerio:2025fhz` — bibliography.bib:5932
- Paper 5 (CTAO cross-correlations, ch. 8): `Pinetti:2025hgd` — bibliography.bib:5944

## Preface

### Evidence and unknown nature
- "The evidence for dark matter comes from many independent probes at different scales. Galactic rotation curves, the motions of galaxies within clusters, gravitational lensing, and the anisotropies of the cosmic microwave background all require a form of matter that outweighs ordinary baryons by roughly a factor of five and interacts with light only through gravity." — frontmatter/abstract_en.tex:4
- "These probes, however, are all gravitational in nature, and they say little about what dark matter actually is." — frontmatter/abstract_en.tex:4
- "Proposed candidates span nearly ninety orders of magnitude in mass, from ultralight axions to primordial black holes, and none is singled out by the data alone." — chapter_01/sections/1.0_introduction.tex:10-11
- ΛCDM: "approximately 85% of the matter density is composed of cold, non-baryonic dark matter" — chapter_01/sections/1.0_introduction.tex:7 [cite: Aghanim:2018eyx]

### WIMPs and gamma rays as messengers
- "If it is made of weakly interacting massive particles, it can annihilate or decay into Standard Model states, and gamma rays are especially attractive messengers: undeflected by magnetic fields, they carry the spectral signature of the interaction that produced them." — frontmatter/abstract_en.tex:4
- WIMP miracle: stable particle with electroweak-scale mass and coupling, produced thermally, naturally yields observed relic abundance — chapter_01/sections/1.0_introduction.tex:12 [cite: Cirelli:2024ssz, Steigman:2012nb]
- "The same annihilation process that sets the relic abundance also predicts that WIMPs should annihilate today in regions of high dark matter density, producing Standard Model particles — gamma rays, neutrinos, positrons, and antiprotons" — chapter_01/sections/1.0_introduction.tex:13 [cite: Cirelli:2024ssz, Bergstrom:1997fj]

### Fermi-LAT and the maturity problem
- "For more than fifteen years the Large Area Telescope on board the Fermi Gamma-ray Space Telescope (Fermi-LAT) has surveyed the GeV sky where these signatures are expected, and its measurements are at the core of this thesis." — frontmatter/abstract_en.tex:4
- (COMMENTED OUT in source, usable as closely-paraphrased framing:) "The brightest targets have already been studied at length, and the signals that remain are faint, blended with astrophysical foregrounds, or hidden below the detection threshold. Setting a detection threshold and counting what rises above it leaves most of the information untouched." — frontmatter/abstract_en.tex:6 (line is `%`-commented)
- "Standard methodologies successfully classify the brightest objects and map the prominent diffuse components, but they struggle with overlapping populations and instrumental constraints such as finite spatial resolution and detection thresholds." — chapter_02/sections/2.0_introduction.tex:8-9
- "instrumental effects—finite angular resolution, energy-dependent sensitivity, detection thresholds—leave a large fraction of the emitting population unresolved or unclassified." — chapter_03/sections/3.0_introduction.tex:5

### Thesis claim and arc
- "In this thesis, we argue that progress in indirect dark matter searches now depends on statistical and machine-learning methods capable of recovering signals in noise-dominated environments." — frontmatter/abstract_en.tex:8
- "The work follows an arc from the Galactic Center outward to the cosmic web, tracking the expected signal into regimes of progressively lower signal-to-noise." — frontmatter/abstract_en.tex:8
- "we draw on traditional statistical methods, generative modeling, implicit likelihood methods, and deep learning, applied to Fermi-LAT data and to forecasts for future instruments." — frontmatter/abstract_en.tex:8
- "Taken together, these results trace a coherent path through the gamma-ray sky, from the brightest anticipated signal to the faint imprint of the cosmic web." — frontmatter/abstract_en.tex:16
- "None of these searches returns a confirmed detection, and the particle identity of dark matter remains an open problem." — frontmatter/abstract_en.tex:16
- Closing: "The next steps in indirect detection, we argue, will require better instruments, more data, and sharper statistical tools to read them, all advancing together." — frontmatter/abstract_en.tex:16
- Actual final sentence: "The hope is that this groundwork will help extend these searches as current gamma-ray surveys continue to grow and next-generation observatories come online." — frontmatter/abstract_en.tex:16

### The five works and deliverables (for naming in the preface close)
- Work 1: MSP luminosity function in globular clusters → GCE (ch. 4) [Amerio:2024qor]
- Work 2: DM subhalos among unassociated sources with quantification learning (ch. 5) [Amerio:2025fhz]
- Work 3: dN/dS below threshold with CNN + SBI (ch. 6) [Amerio:2023uet]
- Work 4: probabilistic sub-threshold catalog, public gPCS deliverable (ch. 7) [Amerio:2023rjn]
- Work 5: CTAO cross-correlation forecast (ch. 8) [Pinetti:2025hgd]
- "This framework is then applied to fourteen years of Fermi-LAT data, delivering a publicly available probabilistic catalog." — chapter_07/sections/7.0_introduction.tex:17
- NOTE: introduction/introduction.tex is an empty stub (3 words); rely on abstract + chapter intros.

### Allowed cite keys for Preface
- Normally none (per plan, citations only if a fact carries a mandatory key). The five paper keys above are available if the writer names the works with citations.

## Objectives

- Ch. 4 goal: "constraining the MSP luminosity function through observations of the Milky Way's globular cluster system, a measurement that further sharpens the tension with the MSP interpretation as it has been formulated so far." — chapter_04/sections/4.0_introduction.tex:23
- Ch. 5 goal: "this chapter asks whether any of the point sources detected by the Fermi Large Area Telescope could be dark matter subhalos." — chapter_05/sections/5.1_introduction.tex:11 (NOTE: ch. 5 intro file is 5.1_introduction.tex)
- Ch. 5 method link: "the dataset shift between associated and unassociated source populations necessitates the quantification learning framework" — chapter_05/sections/5.1_introduction.tex:19
- Ch. 6 goal: "This chapter introduces the framework required to probe the unresolved sky and presents a deep learning approach to measuring the gamma-ray source count distribution dN/dS." — chapter_06/sections/6.0_introduction.tex:15
- Ch. 6 validation: "we validate our methodology by recovering the extragalactic dN/dS down to a factor of 50 below the Fermi-LAT threshold." — chapter_06/sections/6.0_introduction.tex:16
- Ch. 7 goal: "whether this population-level statistical knowledge can be turned into spatial information... complementing the source-count distribution with positional identifications." — chapter_07/sections/7.0_introduction.tex:9,11
- Ch. 7 method: "a frequentist comparison of the real sky against ensembles of synthetic skies generated from the recovered dN/dS, flagging candidate source directions below the detection threshold." — chapter_07/sections/7.0_introduction.tex:13
- Ch. 8 goal: "In this chapter we focus on how to isolate a signal from dark matter hidden in the UGRB... forecasting its reach for dark matter annihilation and decay." — chapter_08/sections/8.0_introduction.tex:11,24
- Cross-cutting: "progress in indirect dark matter searches now depends on statistical and machine-learning methods capable of recovering signals in noise-dominated environments" — frontmatter/abstract_en.tex:8
- Transferability: "population models that make sub-threshold sources statistically accessible and inference frameworks robust to the mismatch between simulations and real data, together with probabilistic catalogs and cross-correlation analyses" — frontmatter/abstract_en.tex:16
- No citations needed in Objectives.

## DM problem

### Evidence pillars
- Rotation curves: Rubin and Ford 1970, first high-precision optical rotation curve of M31, no Keplerian decline — chapter_01/sections/1.1_evidence_for_dark_matter.tex:19 [cite: Rubin:1970zza]
- 21-cm curves flat "out to the largest measurable radii in hundreds of systems"; implies M(r) ∝ r, halo with ρ ∝ r⁻² — chapter_01/sections/1.1_evidence_for_dark_matter.tex:21-22
- Zwicky 1933, Coma Cluster virial analysis, mass-to-light ratio ~400, "dunkle Materie" — chapter_01/sections/1.1_evidence_for_dark_matter.tex:60-62 [cite: Zwicky:1933]
- Bullet Cluster (1E 0657-558): weak-lensing mass offset from X-ray gas, coincides with collisionless galaxies — chapter_01/sections/1.1_evidence_for_dark_matter.tex:79-82 [cite: Clowe:2006eq]
- CMB: "a universe without cold dark matter would produce a strongly suppressed third peak" — chapter_01/sections/1.1_evidence_for_dark_matter.tex:113

### Measured abundance
- "The Planck 2018 analysis yields Ω_c h² = 0.1200 ± 0.0012 for the cold dark matter density and Ω_b h² = 0.02237 ± 0.00015 for the baryon density" — chapter_01/sections/1.1_evidence_for_dark_matter.tex:114 [cite: Aghanim:2018eyx]
- "dark matter is roughly five times more abundant than ordinary matter" — chapter_01/sections/1.1_evidence_for_dark_matter.tex:114

### WIMP hypothesis and relic punchline
- WIMPs: "masses in the GeV–TeV range and interact with Standard Model particles through weak-scale couplings" — chapter_01/sections/1.2_wimp_paradigm.tex:46
- s-wave relic abundance (KEY equation, exact LaTeX): `\frac{\Omega_\chi h^2}{0.12} \approx \frac{2.2 \times 10^{-26}~\mathrm{cm^3/s}}{\langle \sigma v_\mathrm{rel}\rangle}` — chapter_01/sections/1.2_wimp_paradigm.tex:185 (eq:relic_abundance) [cite: Steigman:2012nb, Cirelli:2024ssz]
- "The numerator is the canonical thermal cross section, ⟨σv⟩_cosmo ≈ 2.2 × 10⁻²⁶ cm³/s" — chapter_01/sections/1.2_wimp_paradigm.tex:189 (NOTE: thesis uses 2.2, not 3, ×10⁻²⁶)
- WIMP miracle: ⟨σv⟩ ~ α²/M_χ² with α_weak ~ 0.03 returns M_χ of order a few hundred GeV to a few TeV — chapter_01/sections/1.2_wimp_paradigm.tex:190-191
- WIMP window: 3 GeV ≲ M_χ ≲ 100 TeV — chapter_01/sections/1.2_wimp_paradigm.tex:254

### Detection strategies
- "We therefore explore three complementary strategies for detecting dark matter: direct detection, collider searches, and indirect detection" — chapter_01/sections/1.3_searching_for_dark_matter.tex:12
- "The same coupling that governs dark matter annihilation in the early universe also mediates scattering off nuclei in underground detectors and pair-production at particle colliders." — chapter_01/sections/1.3_searching_for_dark_matter.tex:11
- Direct: nuclear recoil in deep-underground detectors, σ_SI ≲ 10⁻⁴⁷ cm² at M_χ ~ 30 GeV — chapter_01/sections/1.3_searching_for_dark_matter.tex:39-45
- Collider: missing transverse energy at the LHC — chapter_01/sections/1.3_searching_for_dark_matter.tex:54-64

### Master flux equation (exact LaTeX)
- Annihilation flux: `\frac{d\Phi_\gamma}{dE\, d\Omega} = \underbrace{\frac{1}{4\pi} \frac{\langle \sigma v_\text{rel} \rangle}{2 m_\chi^2} \frac{dN_\gamma}{dE}}_{\text{Particle Physics}} \quad \times \underbrace{J(\psi)}_{\text{Astrophysics}}` — chapter_01/sections/1.4_indirect_detection.tex:245 (eq:flux_ann) [cite: Cirelli:2024ssz, Hooper:2024]
- J-factor: `J(\psi) = \int_\text{l.o.s.} \rho^2\bigl(r(s, \psi)\bigr) \, ds` — chapter_01/sections/1.4_indirect_detection.tex:253 (eq:jfactor); units GeV² cm⁻⁵ — :258
- Decay version: dΦ/dEdΩ = (1/4π)(Γ/m_χ)(dN/dE) × D(ψ), D(ψ) = ∫ ρ ds — chapter_01/sections/1.4_indirect_detection.tex:264,273
- Factorization: "The particle physics factor — containing m_χ, ⟨σv_rel⟩ (or τ), and the spectral shape dN_γ/dE — encodes the dark matter model we wish to test. The astrophysical factor — J or D — encodes the distribution of dark matter along the line of sight" — chapter_01/sections/1.4_indirect_detection.tex:283-284
- "A non-detection translates directly into an upper limit on ⟨σv_rel⟩" — chapter_01/sections/1.4_indirect_detection.tex:285
- J-factor is quadratic in density profile → dominant systematic — chapter_01/sections/1.4_indirect_detection.tex:305-307

### Target hierarchy
- Galactic Center: "largest J-factor of any astronomical source, owing to its proximity (~8 kpc) and the expected steep rise of the dark matter density at small radii"; but "severe astrophysical contamination" — chapter_01/sections/1.4_indirect_detection.tex:317,322-325 [cite: Hooper:2024]
- GC flux from inner 10° exceeds any individual dwarf by more than three orders of magnitude (NFW γ=1, ρ_⊙ = 0.4 GeV/cm³) — chapter_01/sections/1.4_indirect_detection.tex:318
- Dwarf spheroidals: "among the most dark matter–dominated objects known... the absence of competing emission makes them the cleanest targets available"; J ~ 10¹⁶–10¹⁹·⁵ GeV² cm⁻⁵ — chapter_01/sections/1.4_indirect_detection.tex:335-340,295
- Subhalos: ΛCDM predicts far more bound subhalos than the ~50 known satellites; most entirely dark; "would appear in the Fermi-LAT data as unassociated point sources with no counterpart at other wavelengths" — chapter_01/sections/1.4_indirect_detection.tex:356-358 [cite: Springel:2008cc]
- UGRB / cosmic web: unresolved gamma-ray background after subtracting resolved sources and Galactic diffuse; DM component "expected to be subdominant in the total intensity spectrum"; extraction via anisotropy cross-correlation with LSS tracers — chapter_01/sections/1.4_indirect_detection.tex:363-373 [cite: DGRB-review]
- GCE preview: excess at ~0.5–5 GeV "consistent with the predictions for a ~40–70 GeV dark matter particle annihilating into b b̄ quarks at a rate close to the thermal relic value" — chapter_01/sections/1.4_indirect_detection.tex:327-328 [cite: Goodenough:2009gk, Hooper:2010mq, Daylan:2014rsa]

### Allowed cite keys for DM problem
`Aghanim:2018eyx` (bib:51), `Cirelli:2024ssz` (bib:4969), `Steigman:2012nb` (bib:6346), `Rubin:1970zza` (bib:4995), `Zwicky:1933` (bib:7330), `Clowe:2006eq` (bib:5086), `Hooper:2024` (bib:6777), `Goodenough:2009gk` (bib:3822), `Hooper:2010mq` (bib:3808), `Daylan:2014rsa` (bib:3737), `Bergstrom:1997fj` (bib:5549)

## Methodology

### Bayesian inference / intractable likelihoods
- Pixel Poisson likelihood: `\mathcal{L}(\boldsymbol{\theta}) = \prod_{a=1}^{N_{\mathrm{pix}}} \frac{\lambda_a(\boldsymbol{\theta})^{k_a} \, e^{-\lambda_a(\boldsymbol{\theta})}}{k_a!}` — chapter_03/sections/3.1_inference.tex:46 [cite: Mattox:1996zz]
- Intractable likelihood (exact LaTeX): `p(\mathbf{x}|\boldsymbol{\theta}) = \int p(\mathbf{x}, \mathbf{z}|\boldsymbol{\theta}) \, d\mathbf{z}` — chapter_03/sections/3.2_sbi.tex:25 (eq:intractable_likelihood) [cite: Cranmer:2020]
- "it breaks down when the data-generating process involves a complex simulator whose internal stochastic structure prevents the likelihood from being written in closed form." — chapter_03/sections/3.2_sbi.tex:5
- Concrete case: "Writing a closed-form likelihood for this full sky map would require integrating over every possible spatial configuration, flux, and number of the unresolved sources." — chapter_03/sections/3.2_sbi.tex:35-37

### SBI / NPE
- "Neural Posterior Estimation (NPE) trains a conditional density estimator—typically a discrete or continuous normalizing flow—to directly approximate the posterior distribution p(θ|x)" — chapter_03/sections/3.2_sbi.tex:53 [cite: Papamakarios:2021, Greenberg:2019]
- NOTE: ch. 3 defines NPE in prose; no boxed q_φ(θ|x) equation exists. If an equation is wanted, use eq:intractable_likelihood instead.
- Amortization: "Once trained, the inference is amortized: the network can be applied to the real Fermi-LAT sky map" — chapter_03/sections/3.2_sbi.tex:76-80
- Ch. 6 implementation: "the network directly maps an observed sky map to posterior summaries (the mean and variance for each flux bin)." — chapter_03/sections/3.2_sbi.tex:78

### Quantification learning / dataset shift
- Definition: "fitting the mixture weights π_k of a generative model directly to the target data, rather than relying on the class fractions of the training set" — chapter_03/sections/3.4_domain_shift.tex:93 [cite: 10.1145/3117807_Gonzalez_quantification]
- Covariate shift: p_train(k|x) = p_target(k|x) while p_train(x) ≠ p_target(x) — chapter_03/sections/3.4_domain_shift.tex:58-61 (eq:covariate_shift) [cite: MorenoTorres2012AUV]
- Prior shift: p_train(x|k) = p_target(x|k) but p_train(k) ≠ p_target(k) — chapter_03/sections/3.4_domain_shift.tex:86-89 (eq:prior_shift)
- Why it matters: "Machine learning classifiers are typically trained on associated sources... and then applied to unassociated sources to infer their nature. However, several observational biases break the equal-distribution assumption." — chapter_03/sections/3.4_domain_shift.tex:23-24
- "Any analysis that ignores this mismatch risks producing biased class prevalence estimates and, in the context of dark matter searches, unreliable upper bounds on the annihilation cross-section." — chapter_03/sections/3.4_domain_shift.tex:28
- Ch. 5 preview: mixture p(x) = Σ_k π_k p(x|k); prior shift handled by fitting π_k, covariate shift by sigmoid modulation functions — chapter_03/sections/3.4_domain_shift.tex:106-109

### Deep learning on sky maps
- "convolutional neural networks (CNNs) exploit this spatial structure directly" (input: pixel grid or HEALPix sky map) — chapter_03/sections/3.3_ml_astrophysics.tex:76
- "Stacking convolutional layers builds progressively larger receptive fields: shallow layers detect local features such as edges and peaks, while deeper layers combine these into more abstract representations." — chapter_03/sections/3.3_ml_astrophysics.tex:88
- "Chapter 6 works at the field level, feeding gamma-ray sky maps into a convolutional network to reconstruct the source-count distribution" — chapter_03/sections/3.3_ml_astrophysics.tex:9

### Probabilistic cataloging
- NOT in ch. 3 — concept lives in ch. 7: "a frequentist comparison of the real sky against ensembles of synthetic skies generated from the recovered dN/dS, flagging candidate source directions below the detection threshold" — chapter_07/sections/7.0_introduction.tex:13

### Cross-correlations
- APS definition (exact LaTeX): `C_\ell^{ij} = \frac{1}{2\ell+1} \left\langle \sum_{m=-\ell}^{\ell} a_{\ell m}^{(i)}\, a_{\ell m}^{(j)*} \right\rangle` — chapter_03/sections/3.5_cross_correlations.tex:42 (eq:aps_definition) [cite: Fornengo:2013rga, Camera:2012cj]
- "When i ≠ j, we obtain the cross-correlation APS" — chapter_03/sections/3.5_cross_correlations.tex:46
- Limber form: `C_\ell^{ij} = \int \frac{d\chi}{\chi^2}\, W_i(\chi)\, W_j(\chi)\, P_{ij}\!\left(k = \frac{\ell}{\chi},\, \chi\right)` — chapter_03/sections/3.5_cross_correlations.tex:53-54 (eq:limber_aps)
- Ch. 8 preview: "this formalism is applied to forecast the sensitivity of the Cherenkov Telescope Array Observatory (CTAO) to dark matter annihilation and decay, by cross-correlating the predicted gamma-ray emission with the 2MASS galaxy catalog." — chapter_03/sections/3.5_cross_correlations.tex:158

### Allowed cite keys for Methodology
`Cranmer:2020` (bib:6068), `Greenberg:2019` (bib:6152), `Papamakarios:2021` (bib:6082), `MorenoTorres2012AUV` (bib:972), `10.1145/3117807_Gonzalez_quantification` (bib:1016), `Fornengo:2013rga` (bib:6830), `Camera:2012cj` (bib:6880), `Mattox:1996zz` (bib:6767)

## Gamma sky

### Fermi-LAT instrument
- "Launched in 2008, the Fermi Large Area Telescope (LAT) has provided the most sensitive all-sky survey in the GeV domain to date, operating continuously for over fifteen years." — chapter_02/sections/2.3_fermi_lat.tex:8
- "a pair-conversion telescope designed to measure cosmic gamma rays" — chapter_02/sections/2.3_fermi_lat.tex:16
- Four subsystems: convert photons to charged particles, track trajectories, measure energy, reject cosmic-ray background — chapter_02/sections/2.3_fermi_lat.tex:18 [cite: Atwood:2009ez]
- Energy range: "from 20 MeV to over 300 GeV" — chapter_02/sections/2.3_fermi_lat.tex:48
- Field of view ~2.4 sr at 1 GeV — chapter_02/sections/2.3_fermi_lat.tex:49
- Survey cadence: "nearly uniform exposure of the entire sky every two orbits — approximately three hours" — chapter_02/sections/2.3_fermi_lat.tex:50
- PSF: 68% containment ~3.5°–5° at 100 MeV, ~0.6° at 1 GeV, <0.15° above 10 GeV — chapter_02/sections/2.3_fermi_lat.tex:62 [cite: Atwood:2009ez]
- Source confusion at low energies limits catalog depth and "motivates the use of statistical population methods" — chapter_02/sections/2.3_fermi_lat.tex:64-65

### Sky decomposition
- Galactic sky dominated by diffuse foreground of cosmic-ray interactions + Galactic sources (pulsars most prominent); extragalactic sky characterized by isotropic background from unresolved AGN and star-forming galaxies — chapter_02/sections/2.2_astrophysical_sky.tex:9-10
- Galactic Diffuse Emission dominates the observed sky; template modeling is the largest systematic in Fermi-LAT analyses — chapter_02/sections/2.2_astrophysical_sky.tex:17
- Dominant extragalactic contributors are blazars — chapter_02/sections/2.2_astrophysical_sky.tex:59
- UGRB: "residual, almost isotropic emission that remains after subtracting the Galactic Diffuse Emission and all cataloged point sources", composed of cumulative emission of unresolved sources plus residual truly diffuse background — chapter_02/sections/2.2_astrophysical_sky.tex:56 [cite: Fermi-LAT:2014ryh, DGRB-review]
- UGRB measured from 100 MeV to 820 GeV — chapter_02/sections/2.2_astrophysical_sky.tex:57
- Blazars account for approximately 50^{+12}_{-11}% of total EGB photons — chapter_02/sections/2.2_astrophysical_sky.tex:66 [cite: Ajello:2015mfa]

### 4FGL catalog and threshold
- Catalog progression: 1FGL (11 months) → 3FGL (4 yr, 3,033 sources) → 4FGL (8 yr, 5,064 sources) — chapter_02/sections/2.3_fermi_lat.tex:132 [cite: Fermi-LAT:2015bhf, Fermi-LAT:2019yla]
- "The most recent published incremental release, 4FGL-DR4, extends the dataset to 14 years and contains 7,194 sources" — chapter_02/sections/2.3_fermi_lat.tex:133 [cite: Ballet:2023qzs]
- Detection threshold TS > 25 ≈ just over 4σ (four free parameters); threshold unchanged across catalog history — chapter_02/sections/2.3_fermi_lat.tex:127,134
- TS = 2 ln(L1/L0) — chapter_02/sections/2.3_fermi_lat.tex:125 [cite: Mattox:1996zz]
- "This threshold defines the boundary between what is considered a 'resolved' source entering the catalog and what remains part of the unresolved diffuse background." — chapter_02/sections/2.3_fermi_lat.tex:129
- 4FGL-DR4 associations: 4021 extragalactic, 593 Galactic, 2577 unassociated — chapter_02/sections/2.3_fermi_lat.tex:142-143 [cite: Ballet:2023qzs]

### The two blind spots
- Unassociated sources: concentrated along the Galactic plane and at high latitudes where average spectral properties resemble blazars of unknown type — chapter_02/sections/2.3_fermi_lat.tex:143-144 [cite: Ballet:2023qzs]
- "Beyond its likely composition of faint blazars and pulsars below the sensitivity of current multi-wavelength surveys, it also constitutes the primary search pool for exotic gamma-ray emitters such as dark matter subhalos." — chapter_02/sections/2.3_fermi_lat.tex:146-147
- ΛCDM predicts low-mass Galactic subhalos invisible at all wavelengths except gamma rays, where WIMP annihilation could resemble an unassociated point source — chapter_02/sections/2.3_fermi_lat.tex:148
- Sub-threshold population: "Integrating the dN/dS distribution from zero flux up to the telescope's point-source detection threshold yields the intensity of the UGRB... probing the distribution below the detection threshold requires statistical techniques that extract population-level information from the collective imprint of unresolved sources on the photon-count map." — chapter_02/sections/2.2_astrophysical_sky.tex:78-79
- NOTE: the chapter does not use the literal phrase "two blind spots"; treat as a framing device, not a quote.

### Allowed cite keys for Gamma sky section
- `Atwood:2009ez` (LAT instrument) — bib:6519
- `Ballet:2023qzs` (4FGL-DR4) — bib:6897
- `Fermi-LAT:2019yla` (4FGL) — bib:6963
- `Fermi-LAT:2014ryh` (UGRB measurement; used for the UGRB definition sentence) — bib:7063

## Results-MSP

### Problem
- "The leading astrophysical interpretation of the Galactic Center Gamma-Ray Excess has long been that this signal could be generated by large population of centrally-located millisecond pulsars." — chapter_04/sections/paper_msp/sections/summary_conclusions.tex:7
- GCE consistent with annihilation of a ~50 GeV thermal relic (framing; commented block) — chapter_04/sections/paper_msp/sections/introduction.tex:4 [cite: Goodenough:2009gk, Hooper:2010mq, Daylan:2014rsa, Calore:2014xka]

### Method
- "we have analyzed the gamma-ray emission from the Milky Way's globular clusters, using 15.8 years of publicly available data collected by the Fermi Gamma-Ray Space Telescope. We report the robust detection of 56 globular clusters with a statistically significant test statistic of TS > 25" — chapter_04/sections/paper_msp/sections/summary_conclusions.tex:3
- 157 globular clusters analyzed; 56 detected, "8 of which are not contained in previous gamma-ray source catalogs" — chapter_04/sections/paper_msp/sections/introduction.tex:52
- Luminosity-function fit: 87 globular clusters with high stellar encounter rates and/or visible luminosities — chapter_04/sections/paper_msp/sections/summary_conclusions.tex:5
- Log-normal luminosity function, marginalized joint likelihood over clusters (distances, Poisson MSP counts) — chapter_04/sections/paper_msp/sections/luminosity_function.tex:49-58
- Photons 100 MeV–100 GeV — chapter_04/sections/paper_msp/sections/fermi_data_analysis.tex:7

### Luminosity function values
- "favor a mean pulsar luminosity of ⟨L_γ⟩ ~ (1–8)×10³³ erg/s (integrated between 0.1 and 100 GeV), and a width of σ_L ~ 1.4–2.7" — chapter_04/sections/paper_msp/sections/summary_conclusions.tex:5
- NOTE: abstract_en.tex:10 says σ_L ~ 1.4–2.8; chapter text says 1.4–2.7. USE 1.4–2.7 (chapter is source of truth) or hedge; do not silently mix.
- "these 87 globular clusters contain a total of ~400–1500 gamma-ray emitting MSPs" — chapter_04/sections/paper_msp/sections/luminosity_function.tex:93

### Prediction and strain
- "If the GCE is generated by MSPs with the same luminosity function and other characteristics as those found in globular clusters, Fermi's source catalogs would have contained N_MSP ~ 17–37 individual members of this population. Given that only three millisecond pulsars have been detected with a direction and distance that does not preclude it from being part of an Inner Galaxy population..." — chapter_04/sections/paper_msp/sections/implications_gce.tex:20 [cite: Holst:2024fvb, Fermi-LAT:2023zzt]
- Conservative cluster-to-cluster variation model: "lowers the number of expected detections to the range of N_MSP ≈ 3–30... the results nonetheless remain in tension at a level of at least 2σ with the three identified pulsar candidates." — chapter_04/sections/paper_msp/sections/implications_gce.tex:29
- Conclusion (calibrated language, verbatim): "the luminosity function derived here is incompatible with pulsar interpretations of the GCE, unless a large number of unassociated Fermi sources are, in fact, unidentified MSPs. Given systematic efforts that have been conducted to search for radio pulsations from unassociated Fermi sources, this possibility seems unlikely." — chapter_04/sections/paper_msp/sections/implications_gce.tex:20
- "This result poses a challenge to pulsar interpretations of the Galactic Center Gamma-Ray Excess and, by extension, potentially bolsters dark matter interpretations of this long-standing signal." — chapter_04/sections/paper_msp/sections/summary_conclusions.tex:9

### Allowed cite keys for Results-MSP
`Amerio:2024qor` (bib:6800), `Goodenough:2009gk` (bib:3822), `Hooper:2010mq` (bib:3808), `Daylan:2014rsa` (bib:3737), `Calore:2014xka` (bib:3684), `Holst:2024fvb` (bib:3136), `Fermi-LAT:2023zzt` (bib:2943)

## Results-Subhalos

### Problem
- "these unassociated sources have long been recognized as the natural testing ground for DM subhalo searches." — chapter_05/sections/5.4_unassociated_sources.tex:9
- "To date, no unassociated Fermi-LAT source has been unambiguously confirmed as a dark matter subhalo" — chapter_05/sections/5.4_unassociated_sources.tex:23

### Method
- Catalog: 4FGL-DR4 — chapter_05/sections/paper_dm_halos/sections/statistical_analysis.tex:8 [cite: Fermi-LAT:2022byn, Ballet:2023qzs]
- "The latest incremental release, the 4FGL-DR4 catalog, contains 7,195 sources detected above a significance threshold of 4σ. Of these, 2563 sources — roughly one third — remain unassociated" — chapter_05/sections/5.4_unassociated_sources.tex:14-15 (NOTE: ch2 quotes 7,194 / 2577; per-chapter numbers differ — use each within its own section)
- "Among the unassociated population, 1,283 sources lie at Galactic latitudes |b| > 10°" — chapter_05/sections/5.4_unassociated_sources.tex:16
- Mixture model: "a probabilistic model p(x) for the unassociated sources as a weighted mixture of three source classes: Galactic and extragalactic astrophysical sources plus the hypothetical DM subhalos." — chapter_05/sections/paper_dm_halos/sections/conclusions.tex:8
- Features: log-parabola spectral parameters {log10 φ, α, β} — chapter_05/sections/paper_dm_halos/sections/statistical_analysis.tex:44-54
- "We analyze data shifts between associated and unassociated sources within a general framework of quantification learning, considering two effects: (1) a covariate shift affecting all source classes in the same way, and (2) a prior probability shift, which allows for changes in class prevalence, including the possible presence of a new source class" — chapter_05/sections/paper_dm_halos/sections/conclusions.tex:8
- Prior shift preferred at 7σ; covariate shift at 4.5σ; both at 6.7σ — chapter_05/sections/paper_dm_halos/sections/mixture_model_and_limits.tex:47
- Optimization via Expectation-Maximization, semi-supervised — chapter_05/sections/paper_dm_halos/sections/mixture_model_and_limits.tex:13-14

### Outcome
- "No significant excess corresponding to DM subhalos is observed beyond Galactic and extragalactic sources. Consequently, we derive 95% upper bounds on the DM annihilation cross section." — chapter_05/sections/paper_dm_halos/sections/conclusions.tex:14-15
- "For all tested models, the significance is less than 2 sigma." — chapter_05/sections/paper_dm_halos/sections/mixture_model_and_limits.tex:161
- Channel and CL: "Upper bounds with 95% confidence on the DM annihilation cross section ⟨σv⟩ in the b b̄ channel." — chapter_05/sections/paper_dm_halos/sections/mixture_model_and_limits.tex:283
- Masses tested: 10, 30, 100, 300, 1000 GeV (i.e. 10 GeV–1 TeV) — chapter_05/sections/paper_dm_halos/sections/mixture_model_and_limits.tex:20
- Limits "an order of magnitude less stringent than the limits derived using dwarf spheroidal galaxies" — chapter_05/sections/paper_dm_halos/sections/mixture_model_and_limits.tex:332
- "Our constraints are competitive with previous limits derived from DM subhalo searches using classify-and-count methods." — chapter_05/sections/paper_dm_halos/sections/conclusions.tex:16

### Allowed cite keys for Results-Subhalos
`Amerio:2025fhz` (bib:5932), `Fermi-LAT:2022byn` (bib:6312), `Ballet:2023qzs` (bib:6897), `Springel:2008cc` (bib:5522)

## Results-dNdS

### Problem
- "Even though individual sources below the detector flux-threshold cannot be individually seen... it is possible to infer their source-count distribution even in this regime, looking at the collective effects of these unresolved sources." — chapter_06/sections/paper_dnds/sections/introduction.tex:8

### Method
- CNN trained on synthetic maps: "We have generated in total 1 million maps, 90% of which have been used for training and 10% for validation." — chapter_06/sections/paper_dnds/sections/synthetic_map_generation.tex:195 ("trained on 900k synthetic maps and validated on 100k additional maps" — conclusions.tex:4)
- Data: "the first 14 years of data collected by the Fermi-LAT" — chapter_06/sections/paper_dnds/sections/data_selection.tex:24; energy range 1–10 GeV — data_selection.tex:11-12,22
- Sky region: baseline |b| > 30° (latitude cut excluding |b|<30°) — chapter_06/sections/paper_dnds/sections/synthetic_map_generation.tex:140
- Output: dN/dS in 20 flux bins in [5×10⁻¹², 1×10⁻⁷] cm⁻² s⁻¹ plus F_iso — chapter_06/sections/paper_dnds/sections/nn_architecture_training.tex:6

### Outcome
- "extends it to the unresolved regime with a behaviour compatible with dN/dS ~ S⁻² down to the smallest flux considered of S = 5×10⁻¹² cm⁻² s⁻¹" — chapter_06/sections/paper_dnds/sections/results.tex:4
- Threshold S_th ~ 2×10⁻¹⁰ cm⁻² s⁻¹; "the lower limit is set at about 1.6 orders of magnitude below the Fermi threshold for resolving sources" — chapter_06/sections/paper_dnds/sections/synthetic_map_generation.tex:103
- Thesis phrasing: "roughly 50 times below the detection threshold" — chapter_08/sections/8.0_introduction.tex:8; "down to a factor of 50 below the Fermi-LAT threshold" — chapter_06/sections/6.0_introduction.tex:16
- "in the resolved limit, the CNN reconstructs a dN/dS fully compatible with the one derived from the [4FGL-DR3] catalog" — chapter_06/sections/paper_dnds/sections/results.tex:4
- "dN/dS ~ S⁻² behaviour over almost four orders of magnitude in flux in the range [5×10⁻¹², 1×10⁻⁸] cm⁻² s⁻¹" — chapter_06/sections/paper_dnds/sections/conclusions.tex:6-7
- dN/dS ~ S⁻³ for S > 10⁻⁸ cm⁻² s⁻¹ (bright end) — chapter_06/sections/paper_dnds/sections/results.tex:7

### Allowed cite keys for Results-dNdS
`Amerio:2023uet` (bib:6787), `Ballet:2023qzs` (bib:6897)

## Results-Catalog

### Problem
- "statistically push the Fermi-LAT sensitivity to point-like sources at high latitudes below the current threshold for detection, leveraging on the fact that the underlying source count distribution function is constrained even for lower test statistics (TS)" — chapter_07/paper_dnds_catalog/sections/conclusions.tex:6

### Method
- "a catalogue of directions (i.e. firing pixels) in the sky likely to be associated to sources, albeit only in a probabilistic sense, that we assessed via a Kolmogorov-Smirnov (KS) test." — chapter_07/paper_dnds_catalog/sections/conclusions.tex:6
- Frequentist comparison of real sky vs ensembles of synthetic skies generated from the recovered dN/dS — chapter_07/sections/7.0_introduction.tex:13

### Outcome
- "we found a number of 'firing pixels' ~50% higher than what one would infer from a catalogue only including sources listed in the latest incarnation of the Fermi-LAT catalogue." — chapter_07/paper_dnds_catalog/sections/conclusions.tex:6
- Public deliverable: "a Python package called gPCS (for gamma-ray Photon Count Statistics), as well as a summary FITS, both available on Zenodo" — chapter_07/paper_dnds_catalog/sections/results.tex:114
- Applied to fourteen years of Fermi-LAT data — chapter_07/sections/7.0_introduction.tex:17
- Cross-correlation suitability: "The most obvious [application] we can think of consists of cross-correlation studies, either multi-wavelength or multi-messenger, where the statistical advantage of a significantly larger sample more than compensates having a (sub-leading) fraction of spurious directions." — chapter_07/paper_dnds_catalog/sections/conclusions.tex:8

### Allowed cite keys for Results-Catalog
`Amerio:2023rjn` (bib:5902)

## Results-Xcorr

### Problem
- "Dark matter emission is mainly local (highest at z < 0.1), while the blazar background is not, so cross-correlating the gamma-ray sky with a catalog of nearby galaxies selects the redshift window where the dark matter contribution is largest relative to the astrophysical background, while suppressing the bulk of the blazar population." — chapter_08/sections/8.1_from_resolved_to_cosmic_web.tex:87
- "Cross-correlating the gamma-ray map with an external gravitational tracer resolves both limitations at once." — chapter_08/sections/8.1_from_resolved_to_cosmic_web.tex:70

### Method / forecast
- "a sensitivity forecast for detecting dark matter signals through cross-correlations between the CTAO extragalactic survey and the 2MASS galaxy catalog" — chapter_08/paper_xcorr/sections/introduction.tex:28
- 2MASS: "approximately one million galaxies... redshift distribution peaking at z ≈ 0.072" — chapter_08/sections/8.2_cross_correlation_technique.tex:83 [cite: 2MASS:2006qir]
- EGAL survey: quarter of the sky; total ~1000 h, effective exposure ≈ 3 h per point — chapter_08/paper_xcorr/sections/cherenkov_telescope_array.tex:17-19
- Deeper scenario: "assuming an effective observation time of ~50 hours per point and the same sky coverage as in the EGAL survey" — chapter_08/paper_xcorr/sections/cherenkov_telescope_array.tex:59
- Energies 30 GeV–30 TeV — chapter_08/paper_xcorr/sections/cherenkov_telescope_array.tex:55

### Outcome
- "reaching values around 10⁻²³ cm³ s⁻¹ for annihilation cross-section ⟨σv⟩ and 10²⁷ s for decay" (NOTE source LaTeX writes annihilation units as cm^{-3} s^{-1}; standard is cm³/s — quote carefully or omit units discussion) — chapter_08/paper_xcorr/sections/conclusions.tex:7
- Competitiveness (verbatim): "These sensitivities are comparable to and complementary with those obtained from existing strategies, such as observations of dwarf spheroidal galaxies or galaxy clusters." — chapter_08/paper_xcorr/sections/conclusions.tex:8
- "Our results show that the cross-correlation technique is competitive, yielding constraints comparable to those from other methodologies." — chapter_08/paper_xcorr/sections/sensitivity_forecast.tex:116
- "the cross-correlation outperforms the auto-correlation by approximately a factor of 5" — chapter_08/paper_xcorr/sections/sensitivity_forecast.tex:112 (upstream "5 hrs"/"50 hrs" typo flagged at chapter_08/sections/8.3_ctao.tex:56 — avoid quoting the hours in this sentence)
- CTAO capability: "extends the accessible energy range an order of magnitude above the Fermi-LAT ceiling and brings effective collecting areas six orders of magnitude larger, opening the TeV mass window to cross-correlation searches for the first time." — chapter_08/sections/8.0_introduction.tex:22

### Allowed cite keys for Results-Xcorr
`Pinetti:2025hgd` (bib:5944), `2MASS:2006qir` (bib:1572), `CTAConsortium:2017dvg` (bib:6949)

## Conclusions

### Synthesis material (abstract)
- "Taken together, these results trace a coherent path through the gamma-ray sky, from the brightest anticipated signal to the faint imprint of the cosmic web. None of these searches returns a confirmed detection, and the particle identity of dark matter remains an open problem." — frontmatter/abstract_en.tex:16
- "The next steps in indirect detection, we argue, will require better instruments, more data, and sharper statistical tools to read them, all advancing together." — frontmatter/abstract_en.tex:16
- "This thesis contributes to the third of these fronts, working toward new statistical tools for the field: population models that make sub-threshold sources statistically accessible and inference frameworks robust to the mismatch between simulations and real data, together with probabilistic catalogs and cross-correlation analyses." — frontmatter/abstract_en.tex:16
- "The hope is that this groundwork will help extend these searches as current gamma-ray surveys continue to grow and next-generation observatories come online." — frontmatter/abstract_en.tex:16

### Future directions actually written in the chapters (ONLY these may appear)
- Ch. 4 (MSP): measuring the globular-cluster MSP luminosity function bears on GCE pulsar viability; remaining loophole is a large population of unidentified MSPs among unassociated sources, "this possibility seems unlikely" given radio-pulsation searches — chapter_04/sections/paper_msp/sections/implications_gce.tex:18,20
- Ch. 5 (subhalos): "Our approach is broadly applicable to searches of anomalies in distributions for datasets exhibiting both covariate and prior shifts, where the target data is unlabeled." — chapter_05/sections/paper_dm_halos/sections/conclusions.tex:28
- Ch. 5 (subhalos): velocity-dependent (Sommerfeld-enhanced) annihilation analysis "deferred to a future work" — chapter_05/sections/paper_dm_halos/sections/mixture_model_and_limits.tex:419-425
- Ch. 6 (dN/dS): "Possible future applications includes the extension to multiple energy ranges and energy correlations, and the investigation of features in the dN/dS which might indicate the presence of exotic components like dark matter." — chapter_06/sections/paper_dnds/sections/conclusions.tex:15
- Ch. 6 (dN/dS): graph convolutional networks preserving spatial relations and rotational invariance; truncated marginal neural ratio estimation possibly matching performance with simpler architecture and fewer training samples — chapter_06/sections/paper_dnds/sections/conclusions.tex:16-17
- Ch. 7 (catalog): cross-correlation studies (multi-wavelength or multi-messenger); guided source search and identification programs to turn candidate directions into bona fide sources — chapter_07/paper_dnds_catalog/sections/conclusions.tex:8-9
- Ch. 7 (catalog): method applies to any other determination of the high-latitude dN/dS; extension to energy-resolved analysis and to low Galactic latitudes; more realistic probability scale for the TS maps — chapter_07/paper_dnds_catalog/sections/conclusions.tex:11,13,15
- Ch. 8 (xcorr): "these results can be further improved with upcoming, deeper, and more densely sampled galaxy catalogs, such as those from the European Space Agency's Euclid satellite mission, as well as by incorporating cross-correlations with other large-scale-structure tracers, such as weak lensing." — chapter_08/paper_xcorr/sections/conclusions.tex:11
- NOTE: conclusion/conclusion.tex is empty (7 words) — do not use.

### Allowed cite keys for Conclusions
The five paper keys only (if needed): `Amerio:2024qor`, `Amerio:2025fhz`, `Amerio:2023uet`, `Amerio:2023rjn`, `Pinetti:2025hgd`

## Cross-section consistency notes (for the writer briefs)

1. Thermal cross section: thesis value is 2.2×10⁻²⁶ cm³/s (chapter_01/sections/1.2_wimp_paradigm.tex:189), NOT the older 3×10⁻²⁶.
2. σ_L range: chapter text 1.4–2.7 (use this); abstract says 1.4–2.8.
3. 4FGL-DR4 counts: ch2 says 7,194 sources / 2577 unassociated; ch5 says 7,195 / 2563 / 1,283 at |b|>10°. Use ch2 numbers in the Gamma-sky section and ch5 numbers in the Subhalos block.
4. dN/dS reach: "factor of ~50 below threshold" (thesis phrasing) = 1.6 orders of magnitude (paper phrasing). Either is verified.
5. "gPCS" = gamma-ray Photon Count Statistics (public Python package + FITS on Zenodo).
