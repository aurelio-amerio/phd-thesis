# PhD Thesis Structure: Probing the Dark Universe

**Tentative Title:** Probing the Dark Universe: Machine Learning and Statistical Approaches to Gamma-Ray Dark Matter Searches

**Format:** Cumulative Dissertation (Compendium)

## **Introduction**

### **0.1 Scope of the Thesis**
TBD
<!-- - **The Quest for Dark Matter:** Briefly introduce the current status of Dark Matter (DM) searches, highlighting the transition from "golden gun" signals (bright, smoking-gun spectral lines) to the need for advanced statistical extraction from noise-dominated regimes.
- **The Data Landscape:** The role of the *Fermi* Large Area Telescope (LAT) after more than a decade of operations. The challenge of extracting new physics from an instrument where the "low-hanging fruit" has arguably been harvested.
- **The Methodological Shift:** Introduce the central thesis argument: that progress requires moving beyond standard frequentist "thresholding" (detecting individual bright sources) toward **statistical learning** and **population studies** (analyzing the collective properties of faint/unresolved sources) using Machine Learning and Simulation-Based Inference. -->

### **0.2 Outline and Summary of Contributions**

- **Part I: Theoretical Foundations:** A guide to the introductory chapters (1-3) which establish the physical framework ($\Lambda$CDM, WIMPs) and the methodological toolkit (SBI, Bayesian Inference).
- **Part II: The Galactic Center and Resolved Structures:** Summarize the investigation into specific targets.
  - *Paper 3:* Investigating the Millisecond Pulsar hypothesis for the Galactic Center Excess.
  - *Paper 4:* The search for individual DM subhalos among unassociated sources using ML techniques.
- **Part III: The Unresolved Sky:** Summarize the shift to population studies.
  - *Paper 1:* Recovering the source-count distribution ($dN/dS$) of faint sources below the detection threshold.
  - *Paper 2:* Constructing probabilistic catalogs to utilize sub-threshold information.
- **Part IV: Large Scale Anisotropies:** Summarize the study of the cosmic web.
  - *Paper 5:* Forecasting the sensitivity of future observatories (CTA) to DM via cross-correlations with galaxy catalogs.

## **Part I: Theoretical and Methodological Foundations**

### **Chapter 1: The Dark Matter Problem**

- **1.1 The Cosmological Context:**
  - Evidence for Dark Matter (Rotation curves, CMB, Large Scale Structure).
  - The $\Lambda$CDM paradigm.
- **1.2 The Particle Nature of Dark Matter:**
  - Limitations of the Standard Model.
  - The WIMP Miracle and thermal freeze-out.
- **1.3 Indirect Detection:**
  - Annihilation and Decay channels.
  - Gamma-ray production mechanisms (prompt emission, secondary radiation).

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

### **Chapter 3: Statistical Methods and Machine Learning in Astrophysics**

- **3.1 Frequentist vs. Bayesian Inference:**
  - Profile Likelihoods (Standard Fermi analysis).
  - Bayesian Priors and Posteriors.
- **3.2 Simulation-Based Inference (SBI):**
  - The concept of "Likelihood-Free" inference.
  - Neural Posterior Estimation (NPE).
  - *Grounding:* Mathematical foundation for **Paper 1**.
- **3.3 Machine Learning on the Sphere:**
  - Convolutional Neural Networks (CNNs).
  - Handling spherical data: Custom implementation (`map2patches`) featuring mapped convolutions on the sphere.
- **3.4 The Domain Shift Challenge:**
  - Training on simulations vs. testing on real data.
  - Domain adaptation techniques.
  - *Grounding:* Critical context for **Paper 4**.

## **Part II: The Galactic Center and Resolved Sources**

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

- **5.1 Halo Substructure in** $\Lambda$**CDM:**
  - Hierarchical clustering and the subhalo mass function.
  - Dark satellites vs. Dwarf Spheroidal Galaxies (dSphs).
- **5.2 The Unassociated Source Problem:**
  - Criteria for associating gamma-ray sources.
  - Classifying unassociated sources as potential dark subhalos.
- **5.3 Machine Learning Classification:**
  - Application of the methods from Chapter 3 to source classification and population studies.
  - Addressing the domain shift between associated and unassociated sources.

### **[INSERT PAPER 4]**

- **Title:** Search for dark matter subhalos among unassociated Fermi-LAT sources in presence of dataset shift
- **File:** `001) paper 4 - 2503.14584v1.pdf`
- **Key Contribution:** Constraints on the subhalo population using ML classification.

## **Part III: The Unresolved Sky**

### **Chapter 6: From Individual Sources to Populations**

- **6.1 The Limits of Detection:**
  - *Transitional Argument:* As shown in Part II, individual identification of subhalos is limited by the instrument's sensitivity and the "look-elsewhere" effect. If DM subhalos exist below the detection threshold, they must be searched for statistically.
- **6.2 The Source Count Distribution (**$dN/dS$**):**
  - Definition and relationship to the Luminosity Function.
  - How $dN/dS$ connects the resolved (catalogs) to the unresolved (background).
  - Using the $dN/dS$ to probe non-Poissonian populations.

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

## **Part IV: Large Scale Anisotropies**

### **Chapter 8: Cross-Correlations and Future Prospects**

- **8.1 The Cosmic Web:**
  - Dark Matter traces Large Scale Structure (LSS).
- **8.2 Cross-Correlation Formalism:**
  - Angular Power Spectra ($C_\ell$).
  - Correlating Gamma-rays (Fermi/CTA) with Galaxy Catalogs/Lensing.
  - *Theoretical Basis:* Drawing on the formalism from Camera et al. (2013) `'1212.5018'` and Fornengo et al. (2014) `'1312.4835'`, and the comprehensive framework detailed in the thesis of Pinetti (2022) `'2212.00125'`.
- **8.3 Looking Forward (CTA):**
  - Moving from Fermi-LAT to the Cherenkov Telescope Array Observatory (CTAO).
  - Sensitivity forecasts for cross-correlation studies.

### **[INSERT PAPER 5]**

- **Title:** Cherenkov Telescope Array Observatory sensitivity to dark matter and galaxy cross-correlations
- **File:** `001) paper 5 - 2505.20383.pdf`
- **Key Contribution:** Forecasting the power of cross-correlations with next-gen instruments.

## **Part V: Conclusions**

### **Chapter 9: Summary and Outlook**

- **9.1 Synthesis:**
  - Combining individual source classification (Paper 3, 4) with population statistics (Paper 1, 2) and large-scale correlations (Paper 5) provides the most robust constraints.
- **9.2 Final Remarks:**
  - The role of ML in the future of astroparticle physics.