# Chapter 2: The Gamma-Ray Sky and Fermi-LAT - References & Sources

## 1. Reviews & Textbooks
*General consensus, theoretical foundations, and state-of-the-art summaries. **Prioritizing reviews included in the research corpus.***

### Fornasa & Sánchez-Conde (2015) - "The nature of the Unresolved Gamma-Ray Background"
*   **Source:** *arXiv:1502.02866* (Physics Reports)
*   **Relevance:** The definitive "core review" for the **Astrophysical Gamma-Ray Sky** (Sec 2.2). It systematically reviews every population contributing to the background: **Blazars**, **Star-Forming Galaxies**, **Misaligned AGNs**, and **Millisecond Pulsars**. It discusses their spectral properties, luminosity functions, and their contribution to the Isotropic Diffuse Gamma-Ray Background (IGRB), tying directly into the thesis's population studies.

### Cirelli et al. (2011) - "PPPC 4 DM ID: A Poor Particle Physicist Cookbook for Dark Matter Indirect Detection"
*   **Source:** *arXiv:1012.4515*
*   **Relevance:** The standard reference for **Gamma-Ray Production Mechanisms** (Sec 2.1). Instead of generic textbook derivations, it provides the "industry standard" spectra and parametrizations for **Generalized Yields** from WIMP annihilation ($\pi^0$, ICS, Bremsstrahlung). It essentially replaces a textbook for the practical purpose of calculating signals.

### Ackermann et al. (The Fermi-LAT Collaboration) (2015) - "The spectrum of isotropic diffuse gamma-ray emission between 100 MeV and 820 GeV"
*   **Source:** *arXiv:1410.3696*
*   **Relevance:** The baseline measurement of the **IGRB**. It defines the experimental reality that all population models must fit. It separates the "Galactic Foreground" (diffuse emission) from the extragalactic signal, critical for defining the "Unresolved Sky" problem.

### Dermer & Menon (2009) - "High Energy Radiation from Black Holes"
*   **Source:** Textbook (Princeton University Press)
*   **Relevance:** The standard pedagogical reference for derivation of **leptonic and hadronic radiation processes**. It provides step-by-step derivations for Inverse Compton Scattering (ICS), Bremsstrahlung, and pion decay kinematics, essential for writing the "Theory" section of Chapter 2.

### Atwood et al. (2009) - "The Large Area Telescope on the Fermi Gamma-ray Space Telescope Mission"
*   **Source:** *arXiv:0902.1089*
*   **Relevance:** The foundational reference for the **Fermi-LAT Instrument** (Sec 2.3). It details the detector physics (pair conversion), subsystems (Tracker, Calorimeter), and key performance metrics (PSF, Effective Area), providing the primary citation for the instrument description.

---

## 2. Key Specific Papers
*Primary sources for specific claims, historical limits, and experimental results.*

*   **Kafexhiu et al. (2014):** *Parametrization of gamma-ray production cross-sections...*
    *   **Source:** *arXiv:1406.6373*
    *   **Relevance:** The precise modern calculation for **pp -> $\pi^0$ -> $\gamma\gamma$** cross-sections. This is the specific "module" needed to calculate the Hadronic emission component of the Galactic Diffuse Emission.

*   **Atwood et al. (2013):** *Pass 8: Toward the Full Realization of the Fermi-LAT Scientific Potential*
    *   **Source:** *arXiv:1303.3514*
    *   **Relevance:** Describes the specific event reconstruction version (**Pass 8**) used in this thesis. It details the improvements in "Ghost Signal" rejection and the extension of effective area to lower/higher energies compared to the original Pass 7.

*   **Alpar et al. (1982):** *A new class of radio pulsars*
    *   **Source:** *Nature 300*
    *   **Relevance:** Establishes the **"Recycling Scenario"** for Millisecond Pulsars—key for identifying them as the potential source of the Galactic Center Excess and as a major contaminant in subhalo searches in high-stellar-density regions.

*   **Blumenthal & Gould (1970):** *Bremsstrahlung, Synchrotron Radiation, and Compton Scattering...*
    *   **Source:** *Rev. Mod. Phys. 42*
    *   **Relevance:** The classic physics reference for **Leptonic interactions**. While Cirelli (PPPC) gives the yields, Blumenthal & Gould provide the fundamental cross-sections for Inverse Compton Scattering (ICS) on the CMB.

*   **Ackermann et al. (2012):** *The Fermi Large Area Telescope On Orbit: Event Classification...*
    *   **Source:** *arXiv:1206.1896*
    *   **Relevance:** The definitive reference for **Instrument Response Functions (IRFs)** and on-orbit calibration. It explains the "P7" era basics which underpin the later "P8" upgrades, crucial for understanding systematics in exposure maps.

---

## 3. References Breakdown by Section
*Detailed mapping of which sections to read for each thesis part.*

### 2.1 Gamma-Ray Production Mechanisms
**Topics:** Hadronic ($\pi^0$), Leptonic (ICS), Spectra.

*   **Cirelli et al. (PPPC 4 DM ID):**
    *   **Main Text:** Read the sections on **"Production of distributions at the source"** and **"Electroweak corrections"** for standard spectra.
*   **Fornasa & Sánchez-Conde (2015):**
    *   **Sec 3:** Read the discussion on **Galactic Diffuse Emission models**, which applies these production mechanisms to the interstellar medium.
*   **Dermer & Menon (Textbook):**
    *   **Chapter 4/5:** Use *only* for the foundational derivations if the reviews are too phenomenological.

#### Additional Sources (2.1)
*   **Kelner, Aharonian & Bugayov (2006)** *[astro-ph/0606058]* - Analytical parametrization of p-p interaction cross-sections.
*   **Kamae et al. (2006)** *[astro-ph/0605581]* - Parametrization of gamma-ray resulting from p-p collisions.
*   **Stecker (1971)** *[NASA SP-249]* - Cosmic Gamma Rays (Classic text on fundamental production physics).
*   **Strong, Moskalenko & Ptuskin (2007)** *[astro-ph/0701517]* - GALPROP model for Cosmic Ray propagation.

### 2.2 The Astrophysical Gamma-Ray Sky
**Topics:** Blazars, Pulsars, Populations, Backgrounds.

*   **Fornasa & Sánchez-Conde (2015):**
    *   **Sec 2:** Point Source Populations (Blazars, Radio Galaxies, Star-Forming Galaxies).
    *   **Sec 3:** The Diffuse Backgrounds (Galactic vs Isotropic).
    *   **Sec 4:** Measuring the UGRB (Anisotropies, 1-point statistics).
*   **Ackermann et al. (2015):**
    *   **Discussion:** The decomposition of the IGRB.

#### Additional Sources (2.2)
*   **Ajello et al. (2014)** *[arXiv:1310.0006]* - The geometric luminosity function of gamma-ray blazars.
*   **Abdo et al. (2010)** *[arXiv:1002.0152]* - The First Fermi-LAT Catalog of Gamma-ray Pulsars (1PC).
*   **Linden et al. (2011)** *[arXiv:1101.2619]* - Star-forming galaxies as substantial contributors to the IGRB.
*   **Di Mauro et al. (2014)** *[arXiv:1311.6621]* - Diffuse gamma-ray emission from unresolved BL Lac objects.
*   **Ajello et al. (2012)** *[arXiv:1110.2943]* - Measurement of the EGB using 2 years of Pass 7 data.

### 2.3 The Fermi Large Area Telescope
**Topics:** Detector Physics, PSF, Pass 8.

*   **Atwood et al. (2009) (Instrument):**
    *   **Sec 2:** Description of the LAT subsystems (Tracker, Calorimeter, ACD).
*   **Ackermann et al. (2012) (Calibration):**
    *   **Results:** Read for **Instrument Response Functions (IRFs)** and on-orbit calibration realities.
*   **Atwood et al. (2013) (Pass 8):**
    *   **Sec 2 & 3:** Improvements in reconstruction (Ghost Signals, event types).

#### Additional Sources (2.3)
*   **Abdollahi et al. (2020)** *[arXiv:1902.10045]* - 4FGL Catalog: Details extraction pipeline and Energy Dispersion usage.
*   **Bruel et al. (2018)** *[arXiv:1810.11394]* - P8R3 event selection improving background rejection.
*   **Acero et al. (2015)** *[arXiv:1501.02003]* - Fermi-LAT Third Source Catalog (3FGL).
