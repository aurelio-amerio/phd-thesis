# Chapter 1: The Dark Matter Problem - Detailed Outline

**Goal:** Establish the theoretical and observational foundation for the thesis. The chapter follows a robust "Evidence $\to$ Theory $\to$ Phenomenology" structure, drawing inspiration from the hierarchical evidence classification of *Cirelli et al.* and the thermodynamic derivation style of *Pinetti*.

---

## 1.1 Evidence for Dark Matter (The "Why")
**Narrative:** We establish DM not as a hypothesis, but as an observational necessity across all astrophysical scales. We adopt the "Mini-Midi-Maxi" classification structure.

### 1.1.1 Galactic Scale ("Mini")
*   **Rotation Curves:**
    *   **Historical Context:** Freeman (1970) and Rubin & Ford (1970). The flatness of $v_c(r)$ at large radii violates Keplerian prediction ($v \propto r^{-1/2}$).
    *   **The Halo Hypothesis:** Implies $M(r) \propto r$, necessitating an extended Dark Matter halo.
    *   **Standard Reference:** Persic, Salucci & Stel (1996) (Universal Rotation Curve).

### 1.1.2 Cluster Scale ("Midi")
*   **Dynamical Evidence:**
    *   **Zwicky (1933):** The Coma Cluster. Application of the **Virial Theorem** ($2K + U = 0$) showed mass-to-light ratios $\sim 400$ times what was expected from stars.
*   **Hydrostatic Equilibrium (X-rays):**
    *   Hot intracluster gas (ICM) traced by X-rays requires deep potential wells to remain bound.
*   **Gravitational Lensing:**
    *   **Strong/Weak Lensing:** Direct mapping of the potential well independent of baryon luminosity.
    *   **The Bullet Cluster (Direct Proof):** *Clowe et al. (2006)*. The separation of the lensing potential (collisionless DM) from the X-ray gas (collisional baryons) during a merger. This is the "smoking gun" that disfavors Modified Gravity (MOND).

### 1.1.3 Cosmological Scale ("Maxi")
*   **The Cosmic Microwave Background (CMB):**
    *   **Planck Results (2018):** The power spectrum of temperature anisotropies.
    *   **Acoustic Peaks:** The relative height of the 1st (flatness), 2nd (baryons), and 3rd (DM) peaks determines the matter content.
    *   **Result:** $\Omega_c h^2 \approx 0.120$, $\Omega_b h^2 \approx 0.022$. DM is $\sim 5\times$ more abundant than baryons.
*   **Large Scale Structure (LSS):**
    *   **Structure Formation:** Baryons were coupled to photons (Silk Damping) and could not collapse early. DM implies potential wells grew before recombination, matching the observed power spectrum $P(k)$.

---

## 1.2 The WIMP Paradigm (The "What" and "When")
**Narrative:** Having established DM exists, we narrow the search. We briefly mention the landscape of candidates but focus on the WIMP due to the "WIMP Miracle," deriving it from first principles (Thermodynamics).

### 1.2.1 The Landscape of Candidates
*   **Standard Model Exclusions:** Baryons (BBN constraints), Neutrinos (Hot DM/Structure formation problems - *Tremaine & Gunn 1979*).
*   **Brief Mention of Alternatives:**
    *   **Primordial Black Holes (PBHs):** "Macroscopic" candidate.
    *   **Axions:** Solving the Strong CP problem.
    *   **Focus:** This thesis focuses on **Weakly Interacting Massive Particles (WIMPs)** due to their connection to Electroweak physics.

### 1.2.2 Thermodynamics of the Early Universe
*   **The Boltzmann Equation:**
    *   Formal derivation of the number density evolution $n(t)$ in an expanding Universe.
    *   $\frac{dn}{dt} + 3Hn = -\langle \sigma v \rangle (n^2 - n_{eq}^2)$.
*   **The Freeze-out Mechanism:**
    *   **Equilibrium:** At high $T$, $\Gamma \gg H$. Matches Maxwell-Boltzmann distribution.
    *   **Decoupling:** As $T$ drops below $m_\chi$, production suppresses ($e^{-m/T}$). Eventually $\Gamma < H$ and the comoving density "freezes out."
*   **The "WIMP Miracle":**
    *   Approximate solution: $\Omega_\chi h^2 \propto \frac{1}{\langle \sigma v \rangle}$.
    *   Plugging in a weak-scale cross-section ($\sigma \sim G_F^2 m_\chi^2 \approx 10^{-36}$ cm$^2$) naturally yields $\Omega \sim 0.1$.
    *   **Canonical Target:** $\langle \sigma v \rangle_{th} \approx 3 \times 10^{-26} \text{ cm}^3/\text{s}$.

### 1.2.3 Theoretical Bounds
*   **The Lee-Weinberg Bound (Lower):** $m_\chi > 2$ GeV (for standard fermions) to avoid overclosing the Universe.
*   **The Unitarity Bound (Upper):** *Griest & Kamionkowski (1990)*. $\sigma_{ann} \le 4\pi/m^2v$. Implies $m_\chi \lesssim 100$ TeV.
*   *Conclusion:* This sets the search window: GeV to TeV scale particles.

---

## 1.3 Indirect Detection Principles (The "How")
**Narrative:** We know *why* it's there, *what* it might be, and *when* it was made. Now, *how* do we see it? This section builds the mathematical formalism used in Papers 1-5.

### 1.3.1 Annihilation Physics
*   **The Process:** $\chi\chi \to SM\bar{SM} \to \text{stable particles } (\gamma, \nu, e^\pm, p)$.
*   **Spectra ($dN/dE$):**
    *   **Soft Channels ($b\bar{b}$):** Hadronization cascades, broad peaks.
    *   **Hard Channels ($\tau^+\tau^-$):** Final state radiation, sharp cutoffs.
    *   **Phenomenology:** The choice of channel determines the spectral shape we search for in the Fermi-LAT data.

### 1.3.2 Gamma-Ray Production
*   **Prompt Emission:**
    *   $\pi^0 \to \gamma\gamma$ dominates.
*   **Secondary Emission (Radiative Processes):**
    *   **Inverse Compton Scattering (ICS):** $e^\pm$ on ISRF/CMB.
    *   **Bremsstrahlung:** $e^\pm$ on gas.
    *   *Significance:* Crucial for the Galactic Center Excess interpretation (Chapter 4).

### 1.3.3 The Flux Factorization ($J$-factor)
*   The master equation for Indirect Detection:
    $$ \frac{d\Phi}{dE} = \underbrace{\frac{1}{4\pi} \frac{\langle \sigma v \rangle}{2m_\chi^2} \frac{dN}{dE}}_{\text{Particle Physics}} \times \underbrace{\int_{\Delta\Omega} \int_{los} \rho^2(r) dl d\Omega}_{\text{Astrophysics (J-factor)}} $$
*   **The J-factor:** Encodes all astrophysical uncertainty.
*   **Density Profiles:**
    *   **NFW (Cusp):** $\rho \propto r^{-1}$. Derived from CDM simulations.
    *   **Burkert/Core:** $\rho \propto const$. Empirical fits to rotation curves.
    *   *Systematic Uncertainty:* The choice of profile fundamentally changes the J-factor and resulting limits (discussed in Chapter 4).

### 1.3.4 Status of the Field (The Motivation)
*   **The "WIMP Crisis":**
    *   Fermi-LAT dSphs limits (*Ackermann et al. 2015*) exclude the canonical thermal cross-section for $m_\chi \lesssim 100$ GeV ($b\bar{b}$).
    *   Direct Detection (LZ/XENON) limits are pushing towards the "Neutrino Floor".
*   **The Thesis Argument:**
    *   The "low-hanging fruit" (bright peaks, canonical WIMPs) have not been found.
    *   **We must move from "Thresholding" to "Statistics":**
        1.  Deep Learning for sub-threshold populations (Part III).
        2.  Probabilistic catalogs (Part III).
        3.  Cross-correlations/Anisotropies (Part IV).
        4.  Complex backgrounds analysis (Part II).
