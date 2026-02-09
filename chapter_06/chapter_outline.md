# Chapter 6 Outline: From Individual Sources to Populations

## 1. Introduction: The Resolved-Unresolved Continuum
*Goal: Frame the shift from the previous part (searching for individual sources) to this part (analyzing the collective population below the detection threshold).*

### 1.1 The Concept of the Isotropic Diffuse Gamma-Ray Background (IGRB)
- **Narrative:** The "Diffuse Background" is not a static physical object; it is an instrumental definition. It is simply the radiation remaining after we subtract what we can see (resolved sources) and the Galactic foreground.
- **Key Concepts:**
    - Definition of IGRB and its dependence on instrumental sensitivity (e.g., *Fermi*-LAT vs EGRET).
    - As sensitivity improves, the "unresolved" becomes "resolved" (e.g., sources move from background to catalog).
- **Key References:**
    - *Ackermann et al. (2015)* (The *Fermi*-LAT IGRB measurement)
    - *Fornasa & Sánchez-Conde (2015)* (Review of IGRB composition)

### 1.2 The Source-Count Distribution ($dN/dS$)
- **Narrative:** Introduce the $dN/dS$ (number of sources per flux interval) as the fundamental physical observable that unifies the two regimes.
- **Key Concepts:**
    - **Bright End:** Directly measured by counting sources in catalogs (Chapter 5).
    - **Faint End:** Must be inferred statistically.
    - **Physical Connection:** The integral of $S \times dN/dS$ below the threshold gives the total intensity of the unresolved background.
- **Transition:** We cannot count faint sources individually (too few photons, confusion noise). We must detect their collective validity through statistical methods.

## 2. Statistical Inference of Populations (The P(D) Method)
*Goal: Explain the traditional statistical framework used to probe sub-threshold populations, establishing the state-of-the-art before our contribution.*

### 2.1 Photon Count Statistics (1-point PDF)
- **Narrative:** How do we see sources we can't resolve? They distort the "texture" of the gamma-ray sky.
- **Key Concepts:**
    - **Poisson vs. Non-Poisson:** A smooth background creates a Poisson distribution of photon counts in pixels. A population of unresolved point sources creates a "tail" of high-count pixels (clustering of photons).
    - The "Pixel Count Distribution" or $P(D)$ formalism.
- **Key References:**
    - *Malyshev & Hogg (2011)* (Foundational statistical framework)
    - *Zechlin et al. (2016)* (Experimental application to *Fermi*-LAT)

### 2.2 Probability Generating Functions
- **Narrative:** Detail the mathematical engine. We model the sky as a superposition of components.
- **Key Concepts:**
    - Generating functions allow us to analytically convolve the contributions of Galactic foregrounds, isotropic backgrounds, and point source populations.
    - Fitting these models to the observed histogram constrains the $dN/dS$ parameters.

### 2.3 Limitations of Likelihood-Based Methods
- **Narrative:** Why do we need a new method (Paper 1)?
- **Key Challenges:**
    - **Computational Cost:** Exact likelihoods are expensive for complex models or large maps.
    - **Rigidity:** Hard to incorporate complex instrumental effects or spatial correlations beyond the 1-point function.

## 3. Deep Learning for Population Studies (Paper 1)
*Goal: Introduce the specific innovation of the thesis: replacing analytical likelihoods with Simulation-Based Inference (SBI) using Neural Networks.*

### 3.1 Simulation-Based Inference (SBI)
- **Narrative:** Shift from "writing down the likelihood" to "learning the likelihood" from simulations.
- **Key Concepts:**
    - Neural Posterior Estimation (NPE).
    - Training on massive datasets of synthetic gamma-ray maps that include all physical effects (PSF, energy dispersion, backgrounds).
    - **References:** *Amerio et al. (2023) [Paper 1]*

### 3.2 Convolutional Neural Networks on the Sphere
- **Narrative:** The technical challenge of applying CNNs to the full sky.
- **Key Innovation:**
    - **DeepSphere / Graph CNNs vs Projected Maps:** We chose a projection method effectively.
    - **The `map2patch` approach:** Dividing the HEALPix sphere into overlapping flat patches to leverage standard, highly optimized 2D CNN architectures (like ResNet/EfficientNet).
    - Handling boundary conditions and distortions.

### 3.3 Results: Recovering the $dN/dS$
- **Narrative:** Present the results of Paper 1.
- **Key Findings:**
    - We recover the $dN/dS$ down to fluxes of $\sim 5 \times 10^{-12}$ ph cm$^{-2}$ s$^{-1}$ (factor of >10 below the 4FGL threshold).
    - Validation: The Deep Learning results match the traditional P(D) results in the overlap region, proving robustness.
    - The Source Count distribution continues as a power-law ($S^{-2}$) deep into the unresolved regime, explaining a significant fraction of the IGRB.

## 4. Conclusion and Outlook
- **Summary:** We successfully transitioned from counting sources to characterizing populations. The $dN/dS$ is the bridge.
- **Link to Chapter 7:** Now that we have the statistical description of the population ($dN/dS$), can we use this *prior knowledge* to go back and try to find likely candidates that were just below the threshold? This leads to **Probabilistic Cataloging (Paper 2)**.
