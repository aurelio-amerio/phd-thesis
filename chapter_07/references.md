# Chapter 07: Probabilistic Cataloging - References & Sources

## 1. Reviews & Textbooks
*General consensus, theoretical foundations, and state-of-the-art summaries.*

### Brewer, Foreman-Mackey & Hogg (2013) - "Probabilistic Catalogs for Crowded Stellar Fields"
*   **Source:** **Priority: arXiv:1211.5805**
    *   **Relevance:** The seminal paper introducing the concept of "Probabilistic Cataloging" (PCAT) in astronomy. It establishes the Bayesian framework for inferring catalogs in crowded fields where the number of sources is unknown (trans-dimensional inference), replacing deterministic lists with posterior samples.

### Daylan, Portillo & Finkbeiner (2017) - "Inference of Unresolved Point Sources... Using Probabilistic Catalogs"
*   **Source:** **Priority: arXiv:1607.04637**
    *   **Relevance:** The primary application of PCAT to high-energy gamma-ray data (Fermi-LAT). It explicitly deals with the transition from resolved to unresolved regimes and demonstrates how population priors (hyperparameters on the source count distribution) allow for the recovery of sub-threshold information.

---

## 2. Key Specific Papers
*Primary sources for specific claims, historical limits, and experimental results.*

*   **Amerio et al. (2024):** *Deepening gamma-ray point-source catalogues with sub-threshold information*
    *   **Source:** *arXiv:2306.16483*
    *   **Relevance:** **(Paper 2)** The core contribution of this chapter. It introduces the "Quality Factor" as a probabilistic metric to assess the reliability of sources below the standard Test Statistic (TS) threshold, effectively creating a probabilistic catalog using the $dN/dS$ as a prior.

*   **Portillo et al. (2017):** *Improved point-source detection in crowded fields using probabilistic cataloging*
    *   **Source:** *arXiv:1703.01303*
    *   **Relevance:** Demonstrates the practical gain of PCAT over traditional thresholding (e.g., DAOPHOT) in crowded fields. It quantifies the "completeness" and "false discovery rate" in a Bayesian sense, providing the rigorous statistical justification for the method used in Paper 2.

*   **Bhat & Malyshev (2022):** *Dependence of source variability on the flux threshold...*
    *   **Source:** *arXiv:2102.07642*
    *   **Relevance:** Critically analyzes the instability of fixed TS thresholds. It shows that near the threshold, source variability can cause sources to "disappear" from catalogs (leading, e.g., to false "transient" classifications), arguing for a probabilistic treatment of threshold-level sources.

---

## 3. References Breakdown by Section
*Detailed mapping of which sections to read for each thesis part.*

### 7.1 The Problem with Thresholding
**Topics:** Bias in fixed TS cuts, Variability selection effects, Dependence on Background.

*   **Abdo et al. (Fermi-LAT) (2010):**
    *   **Chapter/Section:** Read **Sec 4**. Discusses "spectral bias" (hard sources detected at lower flux) and the non-uniformity of detection thresholds across the sky due to background.
*   **Bhat & Malyshev (2022):**
    *   **Chapter/Section:** Read **Sec 2 & 3**. Detailed discussion on how fixed thresholds interact with source variability.
*   **Amerio et al. (2024) [arXiv:2306.16483]:**
    *   **Chapter/Section:** **(Paper 2)** Read **Introduction**. Summarizes why standard cataloging discards useful information in the "sub-threshold" regime (pixels with $TS < 25$).

#### Additional Sources (Thresholding)
*   **Aeillo et al. (2017)** *[arXiv:1702.00664]* - 3FHL Catalog paper, discussing efficiency maps $\omega(S)$ and detection bias.
*   **Mattox et al. (1996)** *[ApJ 461, 396]* - The definition of Test Statistic (TS) for high-energy astronomy (**Classical Reference**).

### 7.2 Priors from Populations
**Topics:** Probabilistic Cataloging (PCAT), Using dN/dS as a prior, Recovering sub-threshold sources.

*   **Brewer et al. (2013):**
    *   **Chapter/Section:** Read **Introduction**. The philosophy of "Cataloging as Inference" rather than "Cataloging as Detection".
*   **Daylan et al. (2017):**
    *   **Chapter/Section:** Read **Sec 2**. The mathematical formulation of the Hierarchical Bayesian model connecting individual sources to the population ($dN/dS$).
*   **Portillo et al. (2017):**
    *   **Chapter/Section:** Read **Sec 3**. Comparison of PCAT vs. Traditional methods in crowded fields.
*   **List et al. (2020) [arXiv:2006.12504]:**
    *   **Chapter/Section:** Read **Sec 4**. Use of Bayesian Graph CNNs to separate point sources from diffuse emission, representing a modern deep-learning analog to PCAT.

#### Additional Sources (Bayesian Inference)
*   **Mishra-Sharma et al. (2017)** *[arXiv:1612.03173]* - NPTFit context: another way of using population priors (via templates) rather than catalogs.
*   **Leane & Slatyer (2019)** *[arXiv:1904.08430]* - Discusses robustness of these priors against systematic errors.
