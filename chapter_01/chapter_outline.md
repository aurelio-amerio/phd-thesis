# Chapter 1: The Dark Matter Problem — Detailed Outline

**Goal:** Establish the theoretical and observational foundation for the thesis. The chapter follows a robust "Evidence → Theory → Phenomenology" structure, drawing inspiration from the hierarchical evidence classification of *Cirelli et al.* and the thermodynamic derivation style of *Pinetti*.

## Connections
- **Previous Chapter**: Introduction (Ch. 0) — sets up the thesis scope, the data landscape, and the methodological shift argument.
- **Next Chapter**: Chapter 2 (The Gamma-Ray Sky and Fermi-LAT) — transitions from the general DM framework established here to the specific instrument and astrophysical backgrounds that form the observational basis for Part II–V.
- **Inserted Paper**: None — this is a purely introductory chapter.

---

## 1.1 Evidence for Dark Matter (The "Why")
**Goal**: Establish DM not as a hypothesis, but as an observational necessity across all astrophysical scales.
**Narrative:** We adopt the "Mini-Midi-Maxi" classification structure from Cirelli et al. (2024), building the case from galactic to cosmological scales. Each scale provides independent evidence, creating an overwhelming multi-scale argument.

### 1.1.1 Galactic Scale ("Mini")
*   **Rotation Curves:**
    *   **Historical Context:** Early hints from Babcock (1939), Mayall (1951); foundational work by Freeman (1970) and Rubin & Ford (1970). The flatness of $v_c(r)$ at large radii violates Keplerian prediction ($v \propto r^{-1/2}$).
    *   **The Halo Hypothesis:** Implies $M(r) \propto r$, necessitating an extended Dark Matter halo.
    *   **Standard Reference:** Persic, Salucci & Stel (1996) (Universal Rotation Curve).
    *   **Modern Data:** The SPARC compilation (Lelli, McGaugh & Schombert 2016, arXiv:1606.09251) confirms ubiquitous flat rotation curves across 175 disk galaxies.
    *   **Milky Way:** Recent *Gaia* DR3 analyses hint at Keplerian decline in the MW's far outskirts, constraining the halo profile (Jiao et al. 2023, arXiv:2309.00048; Ou et al. 2024, arXiv:2303.12838).
*   **Velocity Dispersions (Dwarf Spheroidals):**
    *   Dispersion-supported systems like Draco, Sculptor, and Segue 1 have extreme mass-to-light ratios ($M/L \sim 10$–$1000$), indicating DM domination.
    *   Masses derived from line-of-sight velocity dispersions of constituent stars (Walker et al. 2009; Wolf et al. 2010).
    *   → Transition: dSphs reappear in Ch. 5 (substructure searches) and in the Fermi-LAT constraints (Sec. 1.3.4).

### 1.1.2 Cluster Scale ("Midi")
*   **Dynamical Evidence:**
    *   **Zwicky (1933):** The Coma Cluster. Application of the **Virial Theorem** ($2K + U = 0$) showed mass-to-light ratios $\sim 400$ times what was expected from stars.
*   **Hydrostatic Equilibrium (X-rays):**
    *   Hot intracluster gas (ICM) at $\sim 10^8$ K traced by X-ray bremsstrahlung emissions requires deep potential wells to remain bound.
    *   Studies confirm visible galaxies + X-ray gas account for only $\sim 15\%$ of the total mass (Rosati et al. 2002).
*   **Sunyaev-Zel'dovich (SZ) Effect:**
    *   Hot ICM electrons inverse-Compton scatter CMB photons (thermal SZ). Amplitude $\propto$ integrated electron pressure.
    *   Does not dim with redshift → excellent probe for distant clusters and the baryon fraction $f_b \approx \Omega_b / \Omega_m$.
    *   Combined with BBN/CMB baryon density → $\Omega_m \approx 0.3$ (Bleem et al. 2015; Mantz et al. 2014).
*   **Gravitational Lensing:**
    *   **Strong/Weak Lensing:** Direct mapping of the potential well independent of baryon luminosity.
    *   **The Bullet Cluster (Direct Proof):** *Clowe et al. (2006)*. The separation of the lensing potential (collisionless DM) from the X-ray gas (collisional baryons) during a merger. This is the "smoking gun" that disfavors Modified Gravity (MOND).
    *   **Statistical Confirmation:** Harvey et al. (2015, arXiv:1503.07675) analyzed 72 colliding clusters, confirming collisionless DM at $>7\sigma$ significance and setting upper limits on the DM self-interaction cross-section.

### 1.1.3 Cosmological Scale ("Maxi")
*   **The Cosmic Microwave Background (CMB):**
    *   **Planck Results (2018):** The power spectrum of temperature anisotropies.
    *   **Acoustic Peaks:** The relative height of the 1st (flatness), 2nd (baryons), and 3rd (DM) peaks determines the matter content.
    *   **Result:** $\Omega_c h^2 \approx 0.120$, $\Omega_b h^2 \approx 0.022$. DM is $\sim 5\times$ more abundant than baryons.
    *   **CMB Lensing:** Intervening DM structures smooth high-$\ell$ acoustic peaks and convert E-mode to B-mode polarization (Planck Collaboration 2020, arXiv:1807.06210).
*   **Large Scale Structure (LSS):**
    *   **Structure Formation:** Baryons were coupled to photons (Silk Damping) and could not collapse early. DM potential wells grew before recombination, matching the observed power spectrum $P(k)$.
*   **Baryon Acoustic Oscillations (BAO):**
    *   Acoustic waves in the pre-recombination plasma freeze into the matter distribution, leaving a preferred distance scale ($\sim 150$ Mpc) between galaxies — a "standard ruler."
    *   Detected in SDSS, BOSS, and DESI surveys → independently constrains $\Omega_m$ (Eisenstein et al. 2005).
*   **Type Ia Supernovae:**
    *   Standardizable candles measuring the luminosity distance–redshift relation.
    *   Combined with CMB + BAO → $\Omega_\Lambda \approx 0.7$, $\Omega_m \approx 0.3$ (Riess et al. 1998; Perlmutter et al. 1999; Scolnic et al. 2018 Pantheon sample).
*   **Integrated Sachs-Wolfe (ISW) Effect:**
    *   Evolving gravitational potentials in a dark-energy dominated universe impart net energy changes to CMB photons traversing them.
    *   Detected via cross-correlation of CMB anisotropies with galaxy surveys → independent confirmation of DM scaffolding.
*   *Transition:* The confluence of all evidence at different scales strongly supports the $\Lambda$CDM paradigm — but *what* is DM?

---

## 1.2 The WIMP Paradigm (The "What" and "When")
**Goal**: Narrow the search space for DM candidates and build the thermal freeze-out formalism underlying the thesis's indirect detection searches.
**Narrative:** Having established DM exists, we narrow the search. We briefly survey the landscape of candidates (following Cirelli et al.'s "What" structure), then focus on the WIMP due to the "WIMP Miracle," deriving it from first principles.

### 1.2.1 The Landscape of Candidates
*   **Standard Model Exclusions:** Baryons (BBN constraints), Neutrinos (Hot DM/Structure formation problems — *Tremaine & Gunn 1979*; Cowsik & McClelland 1972).
*   **Particle Candidates (overview):**
    *   **WIMPs:** Weakly Interacting Massive Particles — connection to Electroweak physics. *Focus of this thesis.*
    *   **Axions:** Solving the Strong CP problem. Ultra-light bosons forming BEC condensates.
    *   **Sterile Neutrinos (keV-scale):** Warm DM produced via Dodelson-Widrow or Shi-Fuller mechanisms.
    *   **Dark Photon / Sub-GeV DM:** Interacts via new "dark" forces, evades the Lee-Weinberg bound.
*   **Non-Particle Candidates:**
    *   **Primordial Black Holes (PBHs):** "Macroscopic" candidate.
*   **Alternative Production Mechanisms (brief mention):**
    *   **Freeze-in (FIMPs):** Feebly interacting particles with zero initial abundance, slowly populated by bath particles (Hall et al., arXiv:0911.1120).
    *   *Note:* This section follows Cirelli et al.'s strategy of organizing by mass scale and interaction type.

### 1.2.2 Thermodynamics of the Early Universe
*   **The Boltzmann Equation:**
    *   Formal derivation of the number density evolution $n(t)$ in an expanding Universe.
    *   $\frac{dn}{dt} + 3Hn = -\langle \sigma v \rangle (n^2 - n_{eq}^2)$
    *   **Variable transformation:** Track the *yield* $Y \equiv n/s$ (normalizing to entropy density to factor out expansion) and the dimensionless temperature $x \equiv m_\chi / T$.
    *   **Role of $g_*$:** Distinguish $g_*$ (energy density degrees of freedom, entering via $H$) from $g_{*,s}$ (entropy degrees of freedom, entering via $s$). They diverge after $e^\pm$ annihilation.
*   **The Freeze-out Mechanism:**
    *   **Equilibrium:** At high $T$, $\Gamma \gg H$. Matches Maxwell-Boltzmann distribution (non-relativistic approximation: $n_{eq} \propto (mT)^{3/2} e^{-m/T}$).
    *   **Decoupling:** As $T$ drops below $m_\chi$, production suppresses ($e^{-m/T}$). Eventually $\Gamma < H$ and the comoving density "freezes out" (typically at $x_f \approx 20$–$25$).
    *   **Analytical tricks:** Evaluate in two regimes — (1) near equilibrium ($Y \approx Y_{eq}$), (2) post-freeze-out ($Y_{eq}^2$ negligible).
*   **The "WIMP Miracle":**
    *   Approximate solution: $\Omega_\chi h^2 \propto \frac{1}{\langle \sigma v \rangle}$.
    *   Plugging in a weak-scale cross-section ($\sigma \sim G_F^2 m_\chi^2 \approx 10^{-36}$ cm$^2$) naturally yields $\Omega \sim 0.1$.
    *   **Canonical Target:** $\langle \sigma v \rangle_{th} \approx 2.2 \times 10^{-26} \text{ cm}^3/\text{s}$ (Steigman, Dasgupta & Beacom 2012).

### 1.2.3 Theoretical Bounds
*   **The Lee-Weinberg Bound (Lower):** $m_\chi > 2$ GeV (for standard fermions) to avoid overclosing the Universe.
*   **The Unitarity Bound (Upper):** *Griest & Kamionkowski (1990)*. $\sigma_{ann} \le 4\pi/m^2v$. Implies $m_\chi \lesssim 100$ TeV.
*   *Conclusion:* This sets the search window: GeV to TeV scale particles.

### 1.2.4 Beyond Standard Freeze-out (Refinements)
*   **Velocity-Dependent Cross-Sections:**
    *   **$s$-wave:** $\sigma v = a$ (velocity-independent). Standard assumption.
    *   **$p$-wave:** $\sigma v = a + bv^2$, with $a$ suppressed. Freeze-out occurs earlier. Present-day indirect detection signals essentially invisible ($v_{today}^2 \sim 10^{-6}$).
*   **Sommerfeld Enhancement (brief introduction):**
    *   Non-perturbative correction: long-range attractive force from light mediator ($m_{med} \ll m_{DM}$) boosts low-velocity cross-sections ($S \propto 1/v_{rel}$).
    *   Since $v_{\text{freeze-out}} \sim 0.3c \gg v_{\text{today}} \sim 10^{-3}c$, the present-day annihilation rate can be orders of magnitude larger than at freeze-out.
    *   → Detailed treatment deferred to Sec. 1.3 and Chapter 4 where it impacts GCE interpretation.
    *   *Reference:* Hisano et al. (arXiv:hep-ph/0610249); Arkani-Hamed et al. (arXiv:0810.0713).
*   **Co-annihilation:** If other dark-sector states have mass splitting $\Delta m \lesssim T_{\text{f.o.}}$, the effective annihilation cross-section is modified (e.g., Ellis et al. 1984).
*   **Resonances:** $s$-channel mediator with $m_{med} \approx 2 m_\chi$ causes sharp temperature-dependent cross-section enhancement (Griest & Seckel).
*   *Transition:* The WIMP miracle motivates focused experimental searches — how do we detect DM indirectly?

---

## 1.3 Indirect Detection Principles (The "How")
**Goal**: Build the mathematical formalism used in Papers 1–5 and establish the detection strategy.
**Narrative:** We know *why* it's there, *what* it might be, and *when* it was made. Now, *how* do we see it? This section follows Cirelli et al.'s "Particle-to-Astrophysics Pipeline" structure: start at the interaction level, move to unattenuated messengers, then address propagation and secondary signals.

### 1.3.1 Annihilation and Decay Physics
*   **Annihilation:** $\chi\chi \to SM\bar{SM} \to \text{stable particles } (\gamma, \nu, e^\pm, p)$.
    *   Maximum energy: $E = m_{DM}$.
    *   Signal $\propto \rho^2$ → J-factor (line-of-sight integral of $\rho^2$).
*   **Decay:** $\chi \to SM \to \text{stable particles}$.
    *   Maximum energy: $E = m_{DM}/2$.
    *   Signal $\propto \rho$ → D-factor (line-of-sight integral of $\rho$).
    *   More robust than annihilation: less sensitive to substructure uncertainties.
    *   *Reference:* Ibarra et al. (arXiv:1307.6434) for comprehensive review on decaying DM.
*   **Spectra ($dN/dE$):**
    *   **Soft Channels ($b\bar{b}$):** Hadronization cascades, broad peaks.
    *   **Hard Channels ($\tau^+\tau^-$):** Final state radiation, sharp cutoffs.
    *   **Phenomenology:** The choice of channel determines the spectral shape we search for in the Fermi-LAT data.

### 1.3.2 Spectral Features and Signatures
*   **Prompt Gamma-Ray Emission:**
    *   Continuum: $\pi^0 \to \gamma\gamma$ dominates.
    *   **Monochromatic Lines:** $\chi\chi \to \gamma\gamma$, $\gamma Z$, $\gamma h$ — sharp lines at $E_\gamma = m_{DM}$. Loop-level processes. "Smoking gun" signature.
    *   **Virtual Internal Bremsstrahlung (VIB):** Photon emission from virtual charged mediators → sharp feature near kinematic endpoint (Bringmann et al., arXiv:0710.3169).
*   **Electroweak Corrections:** For TeV-scale WIMPs, electroweak bremsstrahlung ($W/Z$ emission) dramatically alters primary spectra (Ciafaloni et al., arXiv:1009.0224).
*   **Secondary Emission (Radiative Processes):**
    *   **Inverse Compton Scattering (ICS):** $e^\pm$ on ISRF/CMB.
    *   **Bremsstrahlung:** $e^\pm$ on gas.
    *   *Significance:* Crucial for the Galactic Center Excess interpretation (Chapter 4).

### 1.3.3 The Flux Factorization ($J$-factor and $D$-factor)
*   **Annihilation — the master equation:**
    $$ \frac{d\Phi}{dE} = \underbrace{\frac{1}{4\pi} \frac{\langle \sigma v \rangle}{2m_\chi^2} \frac{dN}{dE}}_{\text{Particle Physics}} \times \underbrace{\int_{\Delta\Omega} \int_{los} \rho^2(r) \, dl \, d\Omega}_{\text{Astrophysics (J-factor)}} $$
*   **Decay — the analogous equation:**
    $$ \frac{d\Phi}{dE} = \frac{1}{4\pi} \frac{1}{\tau m_\chi} \frac{dN}{dE} \times \int_{\Delta\Omega} \int_{los} \rho(r) \, dl \, d\Omega $$
    where $\tau$ is the DM lifetime.
*   **Density Profiles:**
    *   **NFW (Cusp):** $\rho \propto r^{-1}(1+r/r_s)^{-2}$. Derived from CDM simulations.
    *   **Burkert/Core:** $\rho \propto \text{const}$ at $r \to 0$. Empirical fits to rotation curves.
    *   *Systematic Uncertainty:* The choice of profile fundamentally changes the J-factor and resulting limits (discussed in Chapter 4).
*   **The Boost Factor from Substructure:**
    *   DM halos contain dense substructures (subhalos). Since annihilation $\propto \rho^2$, clumps exponentially increase the rate: replace $\rho^2$ with $(1+B)\rho^2$.
    *   Major uncertainty: the minimum subhalo mass $M_{min}$ — physically motivated by DM kinetic decoupling temperature ($\sim 10^{-6} M_\odot$), far below simulation resolution.
    *   *Reference:* Springel et al. (arXiv:0809.0898).

### 1.3.4 Multi-Messenger Signals (Brief Overview)
*   **Neutrinos:** Travel unattenuated; probe DM captured in Sun/Earth cores (IceCube, arXiv:1612.05949).
*   **Electrons and Positrons ($e^\pm$):** Diffuse through Galactic B-fields, lose energy rapidly → probe local DM sources ($\lesssim 1$ kpc) (PAMELA, arXiv:0810.4995).
*   **Antiprotons ($\bar{p}$):** Negligible energy losses → preserve spectral shape, sample larger Galactic volume (Cuoco et al., arXiv:1610.03071).
*   **Anti-nuclei:** Extremely low astrophysical background → essentially background-free detection window (Donato et al., arXiv:0803.2640).
*   *Note:* This thesis focuses on **gamma-rays** — the motivation for the Fermi-LAT instrument detailed in Chapter 2.

### 1.3.5 Status of the Field (The Motivation)
*   **The "WIMP Crisis":**
    *   Fermi-LAT dSphs limits (*Ackermann et al. 2015*) exclude the canonical thermal cross-section for $m_\chi \lesssim 100$ GeV ($b\bar{b}$).
    *   Direct Detection (LZ/XENON) limits are pushing towards the "Neutrino Floor."
*   **The Thesis Argument:**
    *   The "low-hanging fruit" (bright peaks, canonical WIMPs) have not been found.
    *   **We must move from "Thresholding" to "Statistics":**
        1.  Complex backgrounds analysis (Part II).
        2.  Deep Learning for sub-threshold populations (Part III).
        3.  Probabilistic catalogs (Part III).
        4.  Cross-correlations/Anisotropies (Part V).
    *   *Transition:* To pursue this program, we first need to understand our instrument → Chapter 2.

## Chapter Summary
- The DM problem is established by converging evidence across galactic, cluster, and cosmological scales.
- The WIMP paradigm provides a natural mass and cross-section window (GeV–TeV) through the thermal freeze-out mechanism.
- Indirect detection via gamma-rays offers a clean, model-independent probe of DM annihilation and decay.
- The null results of simple WIMP searches motivate the advanced statistical and ML approaches developed in this thesis.
- **Bridge to Chapter 2:** Having established the physics targets, the next chapter introduces the Fermi-LAT instrument and the astrophysical gamma-ray sky that constitutes the observational setting.
