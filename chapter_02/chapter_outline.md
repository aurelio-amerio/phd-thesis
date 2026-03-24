# Chapter 2: The Gamma-Ray Sky and Fermi-LAT

> **Scope**: 20–23 pages. This is an astroparticle physics thesis on DM indirect detection. Chapter 2 provides the astrophysical and instrumental context — the backgrounds, the source populations, and the instrument — that all five thesis papers build upon. Treatment is phenomenological: spectral signatures and energy regimes, not derivations. The papers themselves (included verbatim in the thesis) contain detailed pipeline and analysis specifics; this chapter introduces concepts at a general level without duplicating that material.

## Connections
- **Previous**: Chapter 1 established the DM problem and the indirect detection formalism ($J$-factor, annihilation spectra, observational targets).
- **Next**: Chapter 3 introduces the statistical methods (SBI, ML) motivated by the complexity and instrumental limitations described here.
- **Inserted Paper**: None. This chapter is purely contextual.

## Paper Dependencies

| Paper | What Chapter 2 Must Set Up |
|-------|---------------------------|
| **Paper 1** (MSPs/GCE) | MSP physics, spectral shape vs WIMP, GDE as background, 4FGL catalog |
| **Paper 2** (dN/dS via SBI) | EGB/IGRB decomposition, blazar populations, dN/dS formalism, PSF, Fermi maps |
| **Paper 3** (sub-threshold catalogs) | dN/dS formalism, TS definition, Fermi pipeline |
| **Paper 4** (subhalo search) | Pulsars vs DM spectral degeneracy, 4FGL catalog features, unassociated sources |
| **Paper 5** (CTA cross-correlations) | AGN populations, angular power spectra (mostly self-contained) |

---

## [2.0] Chapter Introduction (~1 page)
**Goal**: Untitled opening paragraphs. Funnel structure.
- The gamma-ray sky is rich and complex — dominated by Galactic diffuse emission, punctuated by thousands of point sources, underlaid by a faint isotropic extragalactic glow.
- For DM indirect detection, astrophysical gamma rays are backgrounds. We must understand where they come from and how the instrument observes them.
- Chapter roadmap: Sec. 2.1 (production mechanisms), Sec. 2.2 (source populations, Galactic and extragalactic), Sec. 2.3 (the Fermi-LAT and its data products).
- Bridge: the backgrounds and instrumental limitations defined here are the systematics addressed by ML/SBI in later chapters.

---

## [2.1] Gamma-Ray Production Mechanisms (~4–5 pages)
**Goal**: Define *how* astrophysical gamma rays are produced. Phenomenological: state the processes, describe spectral signatures and energy regimes, include key formulae (e.g. pion bump energy), but defer cross-section derivations to textbooks.
**Narrative**: From fundamental processes to the Galactic foreground model.

### [2.1.1] Hadronic Emission (~1.5–2 pages)
- **Physics**: CR protons + interstellar gas → $\pi^0 \to \gamma\gamma$. Threshold $E_p \gtrsim 1.2$ GeV
- **The pion bump**: Each photon carries $m_\pi/2 \approx 67.5$ MeV in the $\pi^0$ rest frame — the spectral "smoking gun" of hadronic acceleration
- **Why it matters**: Dominant component of the Galactic Diffuse Emission. Primary foreground for the GCE (Paper 1) and subhalo searches (Paper 4)
- **Figure**: Pion-bump spectrum or pp cross-section → Hooper textbook
- **Key refs**: Hooper (Ch. 5), Dermer & Menon (Ch. 8), Kafexhiu et al. (2014)
- Transition: leptonic processes produce the complementary diffuse components

### [2.1.2] Leptonic Emission (~1.5–2 pages)
- **Inverse Compton Scattering**: Relativistic $e^\pm$ up-scatter CMB/starlight/IR. Thomson regime (soft spectrum) vs Klein-Nishina (peaked at $E_\gamma \approx E_e$). Dominates at high Galactic latitudes
- **Bremsstrahlung**: $e^\pm$ in Coulomb fields. Mirrors electron spectrum. Subdominant, relevant at $\lesssim 1$ GeV in gas-rich regions
- **Synchrotron**: $e^\pm$ in magnetic fields → primarily radio; traces the same populations
- Keep compact: spectral shapes and regimes of importance, no cross-section derivations
- **Key refs**: Blumenthal & Gould (1970), Hooper (Ch. 5)
- Transition: these processes combine into the Galactic foreground

### [2.1.3] The Galactic Diffuse Emission Model (~1 page)
- **GALPROP**: Numerical CR propagation → combines hadronic + leptonic components spatially and spectrally
- **Spatial structure** (qualitative): $\pi^0$ dominates along Plane (traces gas); ICS dominates at high latitudes (extended halo); bremsstrahlung subdominant at low energies
- **Template decomposition**: Fermi-LAT models sky as linear combination of GALPROP templates
- **Relevance**: GDE model uncertainties are the primary systematic for Papers 1 and 4. "Dataset shift" in Paper 4 arises directly from IEM mismodeling
- **Figure**: Energy loss coefficients at two Galactic locations → Pinetti thesis
- **Key refs**: Strong et al. (2007), Ackermann et al. (2015) [`Ackermann:2014usa`]
- Transition: with the physics established, we survey the sources that populate the sky

---

## [2.2] The Astrophysical Gamma-Ray Sky (~8–10 pages)
**Goal**: Survey the main source populations and backgrounds. Organized as Galactic → Extragalactic (~3:2 balance). Emphasis on *what each population means for the thesis*.
**Narrative**: From the Galactic foreground through resolved populations to the unresolved extragalactic glow.

### [2.2.1] Galactic Sources (~5 pages)

#### The Galactic Diffuse Foreground (~1.5 pages)
- The GDE as the dominant observed component (~80% of detected gamma rays)
- Recap the decomposition from Sec. 2.1.3 — how Fermi-LAT separates it from point sources and the isotropic background
- Systematic uncertainties: IEM model dependence, alternative templates
- **Thesis link**: GDE mismodeling → dataset shift (Paper 4), GCE extraction systematics (Paper 1)

#### Pulsars and Millisecond Pulsars (~3 pages)
- **Young pulsars**: Rapidly spinning neutron stars, large $B$-fields ($\sim 10^{11}$–$10^{13}$ G), spin-down timescale $\tau = P/2\dot{P}$. GeV emission from curvature radiation in magnetospheric gaps
- **MSP recycling**: Old neutron stars spun up by accretion in binaries → $P \sim 2$–10 ms, $B \sim 10^8$–$10^9$ G, lifetimes $\sim 0.1$–100 Gyr
- **Gamma-ray spectrum**: Power law with exponential cutoff at a few GeV — spectrally similar to WIMP annihilation ($b\bar{b}$ channel, $m_\chi \sim 50$ GeV). This spectral degeneracy is the core of the GCE debate
- **MSP luminosity function**: The key observable that determines whether MSPs can explain the GCE. Mean $\langle L_\gamma \rangle \sim 10^{33}$–$10^{34}$ erg/s from Galactic Plane population
- **Spatial distribution**: MSPs in globular clusters, in the Galactic Bulge, and in the Plane. Natal kicks broaden the distribution relative to the stellar population
- **Thesis link**: Paper 1 measures the MSP luminosity function in globular clusters to test GCE interpretations. Paper 4 must distinguish MSP-like from DM-like unassociated sources
- **Key refs**: Alpar et al. (1982), Calore et al. (2014) [`Calore:2014oga`], Hooper et al. (2016)

#### Other Galactic Sources (~0.5 page)
- Brief mention of SNRs, PWNe, and other resolved Galactic populations for completeness. Not central to the thesis.

### [2.2.2] Extragalactic Sources (~3–4 pages)

#### Active Galactic Nuclei (~1.5–2 pages)
- **Blazars (FSRQs and BL Lacs)**: AGNs with jets toward observer. Bimodal SED (synchrotron + IC). FSRQs (broad lines, LSP) vs BL Lacs (weak/absent lines, HSP). Classification by synchrotron peak frequency
- **Contribution to EGB**: Blazars account for $50^{+12}_{-11}$% of total extragalactic emission above 100 MeV. HSP BL Lacs dominate above ~100 GeV
- **Luminosity functions**: LDDE models. Brief mention of how the GLF connects to $dN/dS$
- **Misaligned AGNs (radio galaxies)**: Jets at large angles. ~25% of DGRB. Compact treatment
- **Star-forming galaxies**: Hadronic emission from CR–gas interactions, luminosity tracks SFR. ~50% of DGRB at 0.3–30 GeV. Compact treatment (~1 paragraph)
- **Thesis link**: Blazars and SFGs define the bright and faint ends of the $dN/dS$ (Papers 2, 3). AGN vs pulsar classification is central to Paper 4
- **Key refs**: Ajello et al. (2015) [`Ajello:2015mfa`], Fornasa & Sánchez-Conde (2015) [`DGRB-review`], Di Mauro et al. (2014)

#### The Isotropic Background and the Source-Count Distribution (~1.5–2 pages)
- **IGRB**: The isotropic residual after subtracting GDE + resolved sources. Measured 100 MeV–820 GeV, featureless spectrum
- **EGB = IGRB + resolved sources**: The total extragalactic budget
- **The dN/dS**: Source-count distribution connects the resolved catalog to the unresolved background. $\int_0^{S_\text{thr}} (dN/dS) \, S \, dS$ = UGRB intensity
- **Below-threshold methods**: Photon-count PDF / 1-point PDF can probe $dN/dS$ below detection threshold by exploiting the non-Poissonian spatial clustering of unresolved point sources. Brief mention — not a full derivation (Papers 2, 3 do that)
- **Figure**: IGRB and EGB spectrum → Fornasa & Sánchez-Conde, Fig. 1
- **Thesis link**: The $dN/dS$ is the direct subject of Papers 2 and 3. Chapter 2 *defines* it; the papers *reconstruct* it
- **Key refs**: Ackermann et al. (2015) [`Ackermann:2014usa`], Malyshev & Hogg (2011), Fornasa & Sánchez-Conde (2015) [`DGRB-review`]

Transition: the complexity of this sky — overlapping populations, diffuse foregrounds, unresolved sources — places stringent demands on the instrument

---

## [2.3] The Fermi Large Area Telescope (~5–6 pages)
**Goal**: Compact instrument description, then focus on the performance metrics and data products that directly matter for the thesis. Avoid repeating pipeline specifics already covered in the papers.
**Narrative**: From detector principle to data products.

### [2.3.1] Instrument Overview (~1 page)
- **Pair-conversion principle**: Incoming $\gamma \to e^+e^-$ in tungsten foils, tracked by Si microstrips, energy measured by CsI calorimeter, charged particles vetoed by ACD
- **Key numbers**: 20 MeV–500 GeV; FoV ~2.4 sr; survey mode → full-sky every ~3 hours; ~30× EGRET sensitivity
- **Figure**: LAT schematic diagram → Atwood et al. (2009)
- **Key refs**: Atwood et al. (2009) [`Atwood:2009ez`]

### [2.3.2] Instrument Response Functions (~2 pages)
- **Point Spread Function**: 68% containment ~5° at 100 MeV, ~0.8° at 1 GeV, < 0.15° above 10 GeV. Energy dependence defines the source confusion limit
  - **Thesis link**: PSF determines what "resolved" means → directly impacts Papers 2, 3, 4
  - **Figure**: PSF containment angle vs energy
- **Energy Dispersion**: 10–15% at 1 GeV. Brief mention.
- **Effective Area**: ~8000 cm² on-axis at 1 GeV. Energy-dependent. Brief mention.
- **Pass 8 and P8R3**: Comprehensive rewrite of event reconstruction. Ghost signal removal, expanded effective area, PSF/EDISP event types. Keep to ~1 paragraph — papers provide specifics when needed
- **Key refs**: Atwood et al. (2013) [`Fermi-LAT:2013jgq`], Bruel et al. (2018) [`Bruel:2018lac`]

### [2.3.3] Data Products and Catalogs (~2–3 pages)
- **Likelihood framework**: Binned/unbinned ML fits of parametric sky models. Sky model = GDE templates + point sources + isotropic component. Mention Fermi Science Tools without going into operational detail (papers do that)
- **Test Statistic**: $TS = -2\ln(L_0/L_1)$, significance $\approx \sqrt{TS}$. Threshold TS > 25 (~5σ). *Define it here; Papers 2, 3 apply it*
- **The Fermi-LAT catalogs**:
  - Evolution: 1FGL → 3FGL (3,033 sources) → 4FGL (~5,000+) → 4FGL-DR4 (6,659 sources)
  - Catalog content: fluxes, spectra, associations, variability indices
  - **Unassociated sources**: ~1/3 of 4FGL sources lack multi-wavelength counterparts. These are the search pool for Paper 4
- **Thesis link**: The TS threshold defines "resolved" vs "unresolved" — the fundamental divide that Papers 2 and 3 address. The catalog features are the input space for Paper 4's classification
- **Key refs**: Acero et al. (2015) [`Fermi-LAT:2015bhf`], Abdollahi et al. (2020) [`Fermi-LAT:2019yla`]

---

## [2.4] Summary and Transition (~0.5 page)
- The gamma-ray sky is a superposition of hadronic/leptonic diffuse emission and multiple point-source populations — both Galactic and extragalactic.
- The Fermi-LAT has catalogued thousands of sources, but instrumental limitations (PSF, detection threshold) and foreground complexity prevent standard methods from fully exploiting the data.
- **Bridge**: These challenges — complex backgrounds, spectral degeneracies between MSPs and DM, and a large population of unresolved/unassociated sources — motivate the ML and SBI methods introduced in Chapter 3.

---

## Page Budget

| Section | Pages | Key Design Choice |
|---------|-------|-------------------|
| 2.0 Introduction | ~1 | Funnel structure |
| 2.1 Production Mechanisms | ~4–5 | Phenomenological, no derivations |
| 2.2 Astrophysical Sky | ~8–10 | Galactic/Extragalactic ~3:2 |
| 2.3 Fermi-LAT | ~5–6 | Compact hardware, focus on PSF + pipeline + catalogs |
| 2.4 Summary | ~0.5 | Bridge to Ch. 3 |
| **Total** | **~20–23** | |

## No-Repetition Principle

Chapter 2 introduces concepts at a general level. The papers (included verbatim) contain the detailed specifics:

| Concept | Chapter 2 introduces | Paper(s) detail |
|---------|----------------------|-----------------|
| TS definition | What it is, threshold | Papers 2, 3: how it's used for sub-threshold detection |
| $dN/dS$ | Definition, relationship to IGRB | Paper 2: SBI reconstruction; Paper 3: as prior for cataloging |
| MSP spectrum | Shape, WIMP degeneracy | Paper 1: luminosity function measurement in GCs |
| PSF | Energy dependence, confusion limit | Paper 2: effect on map-level inference |
| Unassociated sources | Fraction, origin | Paper 4: full statistical model for classification |
| GDE model | Template decomposition | Paper 4: dataset shift from IEM uncertainties |
