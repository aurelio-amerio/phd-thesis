# Chapter 2: The Gamma-Ray Sky and Fermi-LAT - Detailed Outline

**Goal:** Establish the "Standard Model" of the gamma-ray sky (Foregrounds/Backgrounds) and the Instrument (Fermi-LAT) that observes it. This chapter provides the **Astrophysical** and **Instrumental** context for the thesis, defining the "noise" contained in the data from which we seek to extract the DM "signal".

**Connection:** Follows the theoretical motivation (Chapter 1) by describing the experimental reality. Sets the stage for the complexity of the data analyzed in Papers 1-5.

---

## 2.1 Gamma-Ray Production Mechanisms
**Narrative:** Before discussing *what* emits gamma-rays, we define *how* they are produced. We categorize them into **Prompt** (Direct/Hadronic) and **Secondary** (Radiative/Leptonic) processes, following the *Cirelli et al. (PPPC 4 DM ID)* and *Dermer & Menon* formalism.

### 2.1.1 Hadronic Emission (The "Prompt" Channel)
*   **Physics:** Inelastic collisions of Cosmic Rays (CR) protons with interstellar gas.
    *   $p + p \to \pi^0 + X \to \gamma\gamma + X$.
*   **Spectral Feature:** The "Pion Bump" at $m_{\pi^0}/2 \approx 67.5$ MeV.
    *   *Significance:* This is the dominant component of the Galactic Diffuse Emission (GDE).
    *   **Parametrization:** *Kafexhiu et al. (2014)* cross-sections.
*   **Relevance to Thesis:** This forms the bulk of the "background" model (IEM) used in the GCE analysis (Paper 3) and subhalo searches (Paper 4).

### 2.1.2 Leptonic Emission (Radiative Processes)
*   **Inverse Compton Scattering (ICS):**
    *   **Physics:** High-energy electrons ($e^\pm$) up-scattering soft photons (CMB, Starlight, IR) to gamma-ray energies. $e + \gamma_{soft} \to e' + \gamma_{high}$.
    *   **Spectra:** Harder spectrum than hadronic (typically).
    *   **Relevance:** The primary component of the "Fermi Bubbles" and a major confused component in the Galactic Center.
*   **Bremsstrahlung:**
    *   **Physics:** Deceleration of $e^\pm$ in the Coulomb field of nuclei/ions.
    *   **Relevance:** Dominates at lower energies (< 1 GeV) in gas-rich regions.
*   **Synchrotron Radiation:**
    *   **Physics:** Electrons accelerating in magnetic fields.
    *   **Relevance:** Primarily radio, but traces the same populations.

---

## 2.2 The Astrophysical Gamma-Ray Sky
**Narrative:** Applying the physics of 2.1 to the Universe. We decompose the sky into the **Resolved** (Catalog) and **Unresolved** (Background) components, following the structure of *Fornasa & Sánchez-Conde (2015)*.

### 2.2.1 The Measurement of the Background
*   **The IGRB Definition:** The Isotropic Diffuse Gamma-Ray Background.
    *   IGRB = Total Extragalactic Sky - Resolved Sources.
    *   **Key Measurement:** *Ackermann et al. (2015)* spectrum.
    *   *Goal:* We aim to resolve this background into populations.

### 2.2.2 The Guaranteed Populations (Extragalactic)
*   **Blazars (FSRQs & BL Lacs):**
    *   **Nature:** AGNs with jets aligned to line-of-sight.
    *   **Contribution:** The dominant class (~50-80% of IGRB).
    *   **Luminosity Functions:** Introduction of the $dN/dL$ concept (precursor to Chapter 6).
*   **Misaligned AGNs (Radio Galaxies):**
    *   Fainter but numerous (Cen A).
*   **Star-Forming Galaxies (SFGs):**
    *   Passive gamma-ray production (CRs interacting with gas). The "floor" of the background.

### 2.2.3 The Galactic Population (The GCE Contenders)
*   **Millisecond Pulsars (MSPs):**
    *   **Recycling Scenario:** *Alpar et al. (1982)*. Old neutron stars spun up by accretion.
    *   **Spectrum:** Cut-off power law ($\sim$ few GeV).
    *   **Relevance:** The spectral similarity to WIMP annihilation makes them the "mimics" (Paper 3).

---

## 2.3 The Fermi Large Area Telescope (LAT)
**Narrative:** The instrument that collected the data. Understanding its limitations (PSF, Energy Dispersion) is crucial for the definitions of "Resolved" vs "Unresolved" used in the thesis.

### 2.3.1 Instrument Overview
*   **Design:** Pair-conversion telescope principle.
    *   **Tracker:** Si strips (direction).
    *   **Calorimeter:** CsI crystals (energy).
    *   **ACD:** Anti-Coincidence Detector (CR background rejection).
*   **Source:** *Atwood et al. (2009)*.

### 2.3.2 Instrument Response Functions (IRFs) & Pass 8
*   **Pass 8 Reconstruction:** *Atwood et al. (2013)*.
    *   Why it matters: "Ghost" signal removal, improved effective area at low/high energies.
*   **Key Performance Metrics:**
    *   **Point Spread Function (PSF):** The "blurring" of the sky. $68\%$ containment radius vs energy.
        *   *Thesis Link:* The size of the PSF determines the "confusion limit" for point sources (Paper 1, 2).
    *   **Energy Dispersion ($E_{disp}$):** The uncertainty in photon energy.
    *   **Effective Area ($A_{eff}$):** The "size" of the aperture.

### 2.3.3 Data Reduction Pipeline
*   **Standard Analysis:** Likelihood analysis, Test Statistic (TS) definition ($TS \approx \sigma^2$).
    *   *Connection:* Defines the "Threshold" discussed in Chapter 6 (Paper 1) and Chapter 7 (Paper 2).

---

## 2.4 Summary & Transition
*   **Summary:** We have the Physics (2.1), the Sky contributions (2.2), and the Instrument (2.3).
*   **Transition:** However, standard analysis (2.3.3) is failing to find DM (Chapter 1) because of the "confusion" from these backgrounds (2.2).
*   **Next:** In Chapter 3, we introduce the **Statistical Methods** (Machine Learning/SBI) required to go beyond the standard Fermi-LAT pipeline and handle these complex backgrounds.
