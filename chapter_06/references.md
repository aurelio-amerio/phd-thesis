# Chapter 06: From Individual Sources to Populations - References & Sources

## 1. Reviews & Textbooks
*General consensus, theoretical foundations, and state-of-the-art summaries.*

### Fornasa & Sánchez-Conde (2015) - "The nature of the Diffuse Gamma-Ray Background"
*   **Source:** **Priority: arXiv:1502.02866**
    *   **Relevance:** A complete review of the Isotropic Diffuse Gamma-Ray Background (IGRB), detailing its composition from unresolved source populations (blazars, star-forming galaxies, MSPs). It formally connects the source-count distribution ($dN/dS$) to the luminosity function and discusses statistical methods (1-point PDF, anisotropy) for probing below the detection threshold.

### Malyshev & Hogg (2011) - "Statistics of gamma-ray point sources below the Fermi detection limit"
*   **Source:** **Priority: arXiv:1104.0010**
    *   **Relevance:** The seminal paper establishing the statistical framework for analyzing sub-threshold populations. It derives the analytic relationship between the $dN/dS$ and the pixel photon count distribution (P(D)), demonstrating how non-Poissonian fluctuations allow for the characterization of sources too faint to be resolved individually.

### Ackermann et al. (Fermi-LAT) (2015) - "The spectrum of isotropic diffuse gamma-ray emission between 100 MeV and 820 GeV"
*   **Source:** **Priority: arXiv:1410.3696**
    *   **Relevance:** The benchmark Fermi-LAT measurement of the IGRB spectrum. It defines the "unresolved background" experimentally and serves as the primary dataset that population studies (using $dN/dS$ or NPTF) aim to explain by resolving it into constituent populations.

---

## 2. Key Specific Papers
*Primary sources for specific claims, historical limits, and experimental results.*

*   **Zechlin et al. (2016):** *Unveiling the Gamma-ray Source Count Distribution Below the Fermi Detection Limit with Photon Statistics*
    *   **Source:** *arXiv:1512.07190*
    *   **Relevance:** Key experimental result using 1-point statistics to measure the extragalactic $dN/dS$ down to a factor of ~10 below the catalog threshold. It provides the observational ground truth for the transition from resolved sources to the diffuse background.

*   **Lee et al. (2016):** *Evidence for Unresolved Gamma-Ray Point Sources in the Inner Galaxy*
    *   **Source:** *arXiv:1506.05124*
    *   **Relevance:** The primary application of Non-Poissonian Template Fitting (NPTF). While focused on the Galactic Center, it validates the method for characterizing unresolved populations and attributes the bulk of the excess to point sources (MSPs) rather than Dark Matter.

*   **Amerio et al. (2023):** *Extracting the gamma-ray source-count distribution below the Fermi-LAT detection limit with deep learning*
    *   **Source:** *arXiv:2302.01947*
    *   **Relevance:** **(Paper 1)** Introduces a Machine Learning approach (CNNs) to measure the $dN/dS$, overcoming limitations of traditional histogram-based P(D) methods. It reconstructs the source counts significantly deeper than previous statistical methods.

*   **Feldman & Cousins (1998):** *Unified approach to the classical statistical analysis of small signals*
    *   **Source:** *physics/9711021*
    *   **Relevance:** Foundational statistical text for setting limits near physical boundaries (flux > 0). Crucial for discussing the rigorous definition of detection thresholds and Upper Limits in the low-count regime.

*   **Bertoni et al. (2015):** *Dark Matter Subhalos from Unassociated Fermi-LAT Sources*
    *   **Source:** *arXiv:1504.02087*
    *   **Relevance:** Explicitly handles the "look-elsewhere" effect (trials factor) when searching for extended subhalos across the sky. Demonstrates how high local significance ($4.2\sigma$) is penalized ($3.6\sigma$) by the size of the search space.

---

## 3. References Breakdown by Section
*Detailed mapping of which sections to read for each thesis part.*

### 6.1 The Limits of Detection
**Topics:** Point source sensitivity, Check-elsewhere effect (Trials), Transition to statistical regimes.

*   **Malyshev & Hogg (2011):**
    *   **Chapter/Section:** Read **Introduction & Sec 2**. Explains the "confusion limit" and where individual point source detection fails, necessitating statistical descriptions.
*   **Feldman & Cousins (1998):**
    *   **Chapter/Section:** Classical reference for the definition of detection significance.
*   **Bertoni et al. (2015):**
    *   **Chapter/Section:** Read **Sec IV**. Provides a concrete example of calculating global significance from local significance (Look-Elsewhere Effect) in DM searches.
*   **Leane & Slatyer (2020) [arXiv:2002.12371]:**
    *   **Chapter/Section:** Read **Sec 2**. Discusses how systematic errors (mismodeling) can fake high-significance signals, adding a "systematic" trials factor dimension to the detection problem.

#### Additional Sources (Statistics)
*   **Lyons (2008)** *[arXiv:0811.1663]* - "Open statistical issues in Particle Physics" - overview of p-values/look-elsewhere.
*   **Gross & Vitells (2010)** *[arXiv:1005.1891]* - "Trial factors for the look elsewhere effect in high energy physics".
*   **Vianello et al. (2017)** *[arXiv:1706.01481]* - "Point source detection in the Fermi-LAT tracking data" - technical details on Fermi detection pipelines.

### 6.2 The Source Count Distribution ($dN/dS$)
**Topics:** $dN/dS$ definition, relation to Luminosity Function, Contribution to Backgrounds, P(D)/NPTF methods.

*   **Fornasa & Sánchez-Conde (2015):**
    *   **Chapter/Section:** Read **Sec 2 & 3**. Defines the $dN/dS$, its connection to the Luminosity Function ($dN/dL$), and how integrating $S \times dN/dS$ gives the diffuse intensity.
*   **Zechlin et al. (2016) [arXiv:1512.07190]:**
    *   **Chapter/Section:** Read **Sec 3 & 4**. Shows the actual measurement of $dN/dS$ using photon statistics (1-point function).
*   **Manconi et al. (2020) [arXiv:1912.01622]:**
    *   **Chapter/Section:** Read **Sec 2**. links the physical Blazar Luminosity Function (LDDE) to the observed $dN/dS$ and anisotropy.
*   **Amerio et al. (2023) [arXiv:2302.01947]:**
    *   **Chapter/Section:** **(Paper 1)** Read **Introduction**. Summarizes the history of $dN/dS$ measurements and the gap filled by ML.

#### Additional Sources (dN/dS & NPTF)
*   **Di Mauro et al. (2018)** *[arXiv:1711.03111]* - Constrains blazar $dN/dS$ and EGB contribution.
*   **Mishra-Sharma et al. (2017)** *[arXiv:1612.03173]* - "NPTFit" code paper, standard reference for NPTF method.
*   **Collin et al. (2021)** *[arXiv:2104.04529]* - "Compound Poisson Generator" - critical review of NPTF biases.
*   **Portillo et al. (2017)** *[arXiv:1703.01303]* - "Probabilistic Cataloging" - Bayesian approach to sub-threshold sources (precursor to Paper 2).
