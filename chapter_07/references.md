# Chapter 7 References

## 1. Reviews & Textbooks

*   **Fornasa & Sánchez-Conde (2015)** — *The nature of the Diffuse Gamma-Ray Background* (arXiv:1502.02866). Comprehensive review of the UGRB composition, dedicating sections to guaranteed sub-threshold astrophysical populations like blazars, mAGNs, star-forming galaxies, and MSPs. Also discusses photon-count statistics.
*   **Pinetti (2021)** — *From gamma rays to radio waves: Dark Matter searches across the spectrum* (PhD Thesis, arXiv:2212.00125). Extensive review contextualizing sub-threshold source populations and cross-correlation techniques used to disentangle them from the unresolved gamma-ray background. 

## 2. Key Specific Papers

*   **Abdollahi et al. (2020)** — *Fermi Large Area Telescope Fourth Source Catalog* (arXiv:1902.10045). Details the 4FGL construction, formalizing the standard TS > 25 (roughly 4σ) threshold for point source detection.
*   **Abdollahi et al. (2022)** — *Incremental Fermi Large Area Telescope Fourth Source Catalog* (arXiv:2201.11184). The 4FGL-DR3 update. Highlights the limitations of sharp TS thresholds over long integration times, noting that many DR1 sources formally dropped below TS > 25 but were retained for continuity.
*   **Bhat & Malyshev (2022)** — *Machine learning methods for constructing probabilistic Fermi-LAT catalogs* (arXiv:2102.07642). Explicitly discusses the limitations of hard TS=25 detection thresholds, especially for variable sources that drop below the threshold when time-averaged, and proposes machine learning probabilistic solutions.
*   **Daylan et al. (2017)** — *Inference of Unresolved Point Sources At High Galactic Latitudes Using Probabilistic Catalogs* (arXiv:1607.04637). Introduces PCAT (Probabilistic Cataloger), a Bayesian framework that samples posterior probability distributions of sub-threshold catalogs instead of relying on fixed thresholds.
*   **Malyshev & Hogg (2011)** — *Statistics of gamma-ray point sources below the Fermi detection limit* (arXiv:1104.0010). Pioneering work establishing the use of 1-point probability distribution functions (1pPDF) for analyzing sub-threshold photon-count statistics.
*   **Ackermann et al. (2015)** — *The spectrum of isotropic diffuse gamma-ray emission between 100 MeV and 820 GeV* (arXiv:1410.3696). Fundamental measurement of the isotropic diffuse background, critical for defining the sub-threshold population space.

## 3. References Breakdown by Section

*   **7.1.1 The Standard Catalog-Construction Paradigm**
    *   *4FGL and TS > 25 limits:* `Fermi-LAT:2019yla` (4FGL), `Fermi-LAT:2022byn` (4FGL-DR3), `Fermi-LAT:2015hja` (3FGL).
*   **7.1.2 The Information Below Threshold**
    *   *UGRB composition and sub-threshold populations:* `Fornasa:2015qua` (UGRB review), `Pinetti:2022qnj` (Thesis review), `Fermi-LAT:2014ryh` (IGRB measurement).
    *   *Limitations of fixed thresholds:* `Bhat:2021sog`.
*   **7.2.1 The Core Idea: Simulated-Sky Comparison**
    *   *Alternative probabilistic cataloging:* `Daylan:2016twa` (PCAT).
    *   *Photon count statistics context:* `Malyshev:2011zi` (1pPDF), `Zechlin:2015wdz`.
    *   *Link to dN/dS extraction:* `Amerio:2023aqc` (GenSBI dN/dS).
*   **7.2.2 A Frequentist Framework: TS, KS Test, and Quality Factor**
    *   *Methodology directly extending from:* `Amerio:2023dky` (gPCS probabilistic cataloging).

## 4. Reference Data Table

| Paper Name | Bib Key | In NB | Cited In |
|---|---|---|---|
| **Fermi Catalogs & Thresholds** | | | |
| 4FGL Catalog | `Fermi-LAT:2019yla` | ✅ | — |
| 4FGL-DR3 Catalog | `Fermi-LAT:2022byn` | ✅ | — |
| 3FGL Catalog (Acero et al. 2015) | `Fermi-LAT:2015hja` | ✅ | — |
| ML Probabilistic Catalogs (Bhat & Malyshev 2022) | `Bhat:2021sog` | ✅ | — |
| **UGRB & Sub-threshold Populations** | | | |
| UGRB Review (Fornasa & Sánchez-Conde 2015) | `Fornasa:2015qua` | ✅ | — |
| Dark Matter Searches Review (Pinetti Thesis 2021) | `Pinetti:2022qnj` | ✅ | — |
| IGRB Spectrum (Ackermann et al. 2015) | `Fermi-LAT:2014ryh` | ✅ | — |
| **Probabilistic Cataloging & Statistics** | | | |
| PCAT (Daylan et al. 2017) | `Daylan:2016twa` | ✅ | — |
| 1pPDF below Fermi limits (Malyshev & Hogg 2011) | `Malyshev:2011zi` | ✅ | — |
| 1pPDF dN/dS (Zechlin et al. 2016) | `Zechlin:2015wdz` | ✅ | — |
| **Author Papers** | | | |
| Paper 1: dN/dS SBI (Amerio et al. 2023) | `Amerio:2023aqc` | ✅ | — |
| Paper 2: Probabilistic Cataloging (Amerio et al. 2024) | `Amerio:2023dky` | ✅ | — |
