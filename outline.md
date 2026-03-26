# PhD Thesis Structure: Probing the Dark Universe

**Tentative Title:** Probing the Dark Universe: Machine Learning and Statistical Approaches to Gamma-Ray Dark Matter Searches

**Format:** Traditional thesis (chapters + papers included verbatim)

**Narrative Arc:** The thesis follows a *decreasing signal strength → increasing methodological sophistication* progression. We start from the strongest expected DM signal (Galactic Center), move to fainter resolved targets (subhalos), then probe below the detection threshold with population methods, advance the inference tools themselves, and finally connect to the cosmic web at the largest scales. Each chapter's limitations naturally motivate the next chapter's innovations.

**Design Principles:**
- *Physics drives the narrative* — each chapter starts from a physics problem, then introduces the ML/statistical tool that solves it.
- *Methods in context* — ML techniques appear where they are first used, not in a standalone toolbox chapter.
- *Modularity* — Parts II, III, IV, and V can be read largely independently after Part I. A reader interested only in the GCE need not read Part III.

---

## **Introduction/Abstract**

### **0.1 Scope of the Thesis**

- **The Quest for Dark Matter:** The current status of DM searches and the transition from bright, smoking-gun signals to advanced statistical extraction from noise-dominated regimes.
- **The Data Landscape:** The role of the *Fermi* LAT after more than a decade of operations. The challenge of extracting new physics from an instrument where the low-hanging fruit has been harvested.
- **The Methodological Shift:** The central thesis argument: progress requires moving beyond standard frequentist thresholding toward **statistical learning** and **population studies** using Machine Learning and Simulation-Based Inference.

### **0.2 Outline and Summary of Contributions**

- **Part I: Theoretical Foundations** — introductory chapters (1–3) establishing the physical framework (ΛCDM, WIMPs) and the shared methodological vocabulary (SBI, Bayesian Inference).
- **Part II: The Galactic Center and Resolved Structures** — investigating DM in specific, resolved targets.
  - *Paper 3:* Investigating the Millisecond Pulsar hypothesis for the Galactic Center Excess.
  - *Paper 4:* The search for individual DM subhalos among unassociated sources using ML techniques.
- **Part III: The Unresolved Sky** — the shift to population studies below the detection threshold.
  - *Paper 1:* Recovering the source-count distribution ($dN/dS$) of faint sources using SBI.
  - *Paper 2:* Constructing probabilistic catalogs to utilize sub-threshold information.
- **Part IV: Advancing Simulation-Based Inference** *(provisional)* — improving the inference tools themselves.
  - *Paper 6:* GenSBI — a library for SBI using flow matching and diffusion models.
- **Part V: Large Scale Anisotropies** — studying DM at cosmological scales.
  - *Paper 5:* Forecasting the sensitivity of CTA to DM via cross-correlations with galaxy catalogs.

---

## **Part I: Theoretical and Methodological Foundations**

### **Chapter 1: The Dark Matter Problem**

- **1.1 Evidence for Dark Matter:**
  - Multi-scale evidence (Rotation curves, galaxy clusters, CMB, Large Scale Structure).
  - The $\Lambda$CDM paradigm.
- **1.2 The WIMP Paradigm:**
  - Limitations of the Standard Model, landscape of candidates.
  - Thermal freeze-out and the WIMP Miracle.
- **1.3 Searching for Dark Matter:**
  - The detection triangle: direct, collider, and indirect searches as complementary probes.
  - Direct detection (~1 page): nuclear recoil, noble liquid TPCs (LZ, XENONnT), neutrino fog.
  - Collider searches (~1 page): missing-$E_T$, mono-X, simplified models, LHC status.
  - Why indirect detection: unique sensitivity to the thermal annihilation cross-section.
- **1.4 Indirect Detection via Gamma-Rays:**
  - Annihilation and Decay channels, spectral features.
  - Density profiles, J/D-factor formalism.
  - Observational targets (Galactic Center, dSphs, extragalactic).
  - Multi-messenger context, status of the field.

### **Chapter 2: The Gamma-Ray Sky and Fermi-LAT**

- **2.1 Gamma-Ray Production Mechanisms:**
  - **Hadronic Emission:** Cosmic Ray interactions with interstellar gas (neutral pion decay $\pi^0 \to \gamma\gamma$). The dominant component of the Galactic Diffuse Emission.
  - **Leptonic Emission:** Inverse Compton Scattering (electrons up-scattering CMB/starlight) and Bremsstrahlung (interaction with ionized gas).
  - *Relevance:* These processes form the "Galactic Foreground" model, the primary systematic uncertainty discussed in **Paper 4** (dataset shift) and **Paper 3** (GCE background).
- **2.2 The Astrophysical Gamma-Ray Sky:**
  - **Blazars (FSRQs & BL Lacs):** The dominant extragalactic population. Their luminosity function determines the bright end of the $dN/dS$ (relevant for **Paper 1**).
  - **Pulsars and Millisecond Pulsars (MSPs):** The dominant Galactic point-source population. Crucial for the GCE debate (**Paper 3**) and the main contaminant in subhalo searches (**Paper 4**).
  - **Star-Forming Galaxies & Misaligned AGNs:** Faint populations contributing to the unresolved background and the low-flux end of the $dN/dS$ (**Paper 1**).
  - **The Diffuse Backgrounds:** Distinguishing between the Galactic Diffuse Emission (GDE) and the Isotropic Diffuse Gamma-Ray Background (IGRB).
- **2.3 The Fermi Large Area Telescope:**
  - Instrument overview.
  - Point Spread Function (PSF) and Energy Dispersion.
  - Standard data reduction pipelines (Fermi Science Tools).

### **Chapter 3: Statistical Methods for Noise-Dominated Regimes**

> *Compact conceptual overview (~15 pages). Technique-specific details are introduced in the chapters where they are first applied, keeping each Part modular and self-contained.*

- **3.1 Frequentist vs. Bayesian Inference:**
  - Profile Likelihoods (standard Fermi analysis).
  - Bayesian Priors and Posteriors.
- **3.2 The Simulation-Based Inference Paradigm:**
  - The concept of "Likelihood-Free" inference.
  - Why SBI matters for complex forward models with intractable likelihoods.
- **3.3 Machine Learning in Astrophysics:**
  - ML approaches (classification, regression, density estimation).
  - Why ML is suited to noise-dominated gamma-ray data.
  - *(Technical details of NPE → Chapter 6; flow matching/diffusion → Chapter 9)*
- **3.4 The Domain Shift Challenge:**
  - Problem statement: training on simulations vs. testing on real data.
  - *(Domain adaptation techniques → Chapter 5)*
- **3.5 Cross-Correlations as a Complementary Probe:**
  - At cosmological scales, the angular cross-power spectrum ($C_\ell$) between gamma-ray maps and galaxy/lensing catalogs provides sensitivity to the collective DM signal from unresolved structure.
  - *More details on the formalism in Chapter 10; introduced here to complete the methodological landscape.*


---

## **Part II: The Galactic Center and Resolved Sources**

> *Modular: can be read after Part I without requiring Parts III–V. Deals with DM searches in specific, resolved targets. The GCE provides the strongest expected signal but remains inconclusive, motivating the search for DM in other galactic targets.*

### **Chapter 4: The Galactic Center Excess (GCE)**

- **4.1 The Signal:**
  - Morphology and Spectrum of the GCE.
- **4.2 Interpretations:**
  - Dark Matter Annihilation vs. Millisecond Pulsars (MSPs).
  - The "Cusp vs. Core" debate (NFW, Burkert profiles).
- **4.3 Stellar Clusters as Laboratories:**
  - Using Globular Clusters to constrain the MSP luminosity function.
  - *Context:* Setting the stage for the following paper.

### **[INSERT PAPER 3]**

- **Title:** Millisecond Pulsars in Globular Clusters and Implications for the Galactic Center Gamma-Ray Excess
- **File:** `001) paper 3 - 2412.05220.pdf`
- **Key Contribution:** Constraining the MSP contribution to the GCE.

### **Chapter 5: Searching for Dark Matter Substructures**

- **5.1 Introduction:**
  - Frame subhalo searches as the second prong of Part II; complementary to the GCE (Ch. 4).
- **5.2 Dark Matter Substructure in** $\Lambda$**CDM:**
  - Hierarchical structure formation and the subhalo mass function ($dN/dM \propto M^{-1.9}$).
  - Luminous satellites (dSphs) vs. truly dark subhalos ($M \lesssim 10^8\,M_\odot$).
- **5.3 DM Subhalos as Gamma-Ray Targets:**
  - Expected gamma-ray properties (spectral shape, angular extent, isotropic distribution).
  - Detection prospects: J-factor distributions, expected counts as $f(m_\mathrm{DM}, \langle\sigma v\rangle)$.
- **5.4 The Unassociated Source Problem:**
  - The 4FGL-DR4 catalog: 2428 unassociated sources ($\sim$33%), 1282 at $|b|>10°$.
  - Previous DM subhalo searches: hand-crafted and ML classify-and-count approaches.
- **5.5 From Classification to Quantification: The Dataset Shift Challenge ($\sim$5–6 pp.):**
  - Why standard classification fails for DM subhalo searches (balanced class fallacy, threshold arbitrariness).
  - Dataset shift in the Fermi-LAT context: prior shift (class prevalence), covariate shift (selection bias). Cross-ref Ch. 3 §3.4.
  - Quantification learning: from $p(k|\mathbf{x})$ to $p(\mathbf{x}|k)$ — generative mixture models.
  - The mixture model concept: astrophysical components + DM subhalo component with simultaneous prior and covariate shift correction.

### **[INSERT PAPER 4]**

- **Title:** Search for dark matter subhalos among unassociated Fermi-LAT sources in presence of dataset shift
- **File:** `papers/dm_halos/main.tex`
- **Key Contribution:** First maximum-likelihood generative model for Fermi-LAT unassociated sources; constraints on the subhalo population using quantification learning with dataset shift correction.

---

## **Part III: The Unresolved Sky**

> *Modular: can be read after Part I without requiring Part II. Shifts from individual source identification to population-level statistics. Motivated by the fact that individual identification of subhalos hits sensitivity limits — if DM subhalos exist below the detection threshold, they must be searched for statistically.*

### **Chapter 6: From Individual Sources to Populations**

- **6.1 The Limits of Detection:**
  - *Transitional Argument:* Individual identification is limited by sensitivity and the look-elsewhere effect (decide if I wanna talk about LEE or not). Population methods are needed to probe below threshold.
- **6.2 The Source Count Distribution (**$dN/dS$**):**
  - Definition and relationship to the Luminosity Function.
  - How $dN/dS$ connects the resolved (catalogs) to the unresolved (background).
  - Using the $dN/dS$ to probe non-Poissonian populations.
- **6.3 Simulation-Based Inference for** $dN/dS$**:**
  - Neural Posterior Estimation (NPE): architecture, training, validation.
  - Machine Learning on the sphere: `map2patches`, mapped convolutions.

### **[INSERT PAPER 1]**

- **Title:** Extracting the gamma-ray source-count distribution below the Fermi-LAT detection limit with deep learning
- **File:** `001) paper 1 - 2302.01947.pdf`
- **Key Contribution:** Deriving the $dN/dS$ using SBI and Deep Learning.

### **Chapter 7: Probabilistic Cataloging**

- **7.1 The Problem with Thresholding:**
  - Inconsistencies in standard Test Statistic (TS) cuts due to varying background levels.
  - The "Quality Factor" alternative.
- **7.2 Priors from Populations:**
  - Using the $dN/dS$ (derived in Chapter 6) as a prior for source detection.
  - Recovering sub-threshold information.

### **[INSERT PAPER 2]**

- **Title:** Deepening gamma-ray point-source catalogues with sub-threshold information
- **File:** `001) paper 2 - 2306.16483.pdf`
- **Key Contribution:** Creating probabilistic catalogs to dig into the noise.

---

## **Part IV: Advancing Simulation-Based Inference** *(maybe)*

> *Modular and self-contained. This Part may be included depending on the completion of the associated paper. It is motivated by the SBI methodology introduced in Chapter 6: the NPE approach works, but modern generative models (flow matching, diffusion) can improve flexibility and performance.*

### **Chapter 9: Generative Models for Simulation-Based Inference**
*(the structure of this section may change)*
- **9.1 Beyond Normalizing Flows:**
  - Limitations of standard NPE with normalizing flows.
  - The shift toward flow matching and diffusion models for density estimation.
- **9.2 Optimal Transport Flow Matching:**
  - Conditional flow matching formulation.
  - Advantages over normalizing flows (training stability, expressivity).
- **9.3 Diffusion Models for SBI:**
  - Score-based generative models for posterior estimation.
  - Connections to flow matching.
- **9.4 GenSBI: A Library for Generative SBI:**
  - Architecture and design (JAX/Flax NNX, Flux1/Simformer models).
  - High-level recipes API for common SBI workflows.
  - Benchmark results.
  - *Looking back:* How GenSBI could be applied to improve the dN/dS inference from Paper 1.

### **[INSERT PAPER 6]** *(maybe)*

- **Title:** TBD (GenSBI paper)
- **Repository:** [`github.com/aurelio-amerio/GenSBI`](https://github.com/aurelio-amerio/GenSBI)
- **Key Contribution:** A modern SBI library using flow matching and diffusion models.

---

## **Part V: Large Scale Anisotropies**

> *Modular: can be read after Part I without requiring Parts II–IV. Connects gamma-ray observations to the cosmic web at cosmological scales, providing a complementary approach to DM searches.*

### **Chapter 10: Cross-Correlations and Future Prospects**

- **10.1 The Cosmic Web:**
  - Dark Matter traces Large Scale Structure (LSS).
- **10.2 Cross-Correlation Formalism:**
  - Angular Power Spectra ($C_\ell$).
  - Correlating Gamma-rays (Fermi/CTA) with Galaxy Catalogs/Lensing.
  - *Theoretical Basis:* Drawing on the formalism from Camera et al. (2013) `'1212.5018'` and Fornengo et al. (2014) `'1312.4835'`, and the framework detailed in the thesis of Pinetti (2022) `'2212.00125'`.
- **10.3 Looking Forward (CTA):**
  - Moving from Fermi-LAT to the Cherenkov Telescope Array Observatory (CTAO).
  - Sensitivity forecasts for cross-correlation studies.

### **[INSERT PAPER 5]**

- **Title:** Cherenkov Telescope Array Observatory sensitivity to dark matter and galaxy cross-correlations
- **File:** `001) paper 5 - 2505.20383.pdf`
- **Key Contribution:** Forecasting the power of cross-correlations with next-gen instruments.

---

## **Part VI: Conclusions**

### **Chapter 11: Summary and Outlook**

- **11.1 Synthesis:**
  - Combining individual source classification (Papers 3, 4) with population statistics (Papers 1, 2), advanced inference tools (Paper 6), and large-scale correlations (Paper 5) provides the most robust constraints on DM.
- **11.2 Final Remarks:**
  - The role of ML in the future of astroparticle physics.