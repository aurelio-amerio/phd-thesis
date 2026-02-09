# Chapter 7 Outline: Probabilistic Cataloging

## 1. Introduction: The Limitations of "Hard" Thresholding
*Goal: Frame the motivation. Why is the standard way of making catalogs (cutting at $4\sigma$ / TS=25) insufficient for our science goals?*

### 1.1 The Incompleteness Problem
- **Narrative:** Traditional catalogs maximize *purity* (low false positives) at the expense of *completeness*.
- **Key Concepts:**
    - The "Iceberg" effect: The resolved sources (Chapter 5) are just the tip.
    - Information Loss: By discarding everything below TS=25, we throw away a huge amount of physical information about the population.
- **Key References:**
    - *Bhat & Malyshev (2022)* (Instability of thresholds)
    - *Abdo et al. (2010)* (Fermi-LAT spectral bias)

### 1.2 Variability and Threshold Bias
- **Narrative:** Fixed thresholds are particularly bad for variable sources (like Blazars).
- **Key Concepts:**
    - A source fluctuating around the threshold might be "detected" one month and "vanish" the next, merely due to noise or slight variability.
    - Bias: We systematically select sources when they are in a "high state" (Eddington bias equivalent for variability).
    - **Transition:** We need a method that doesn't say "Yes/No" but "Maybe (with probability P)".

## 2. The Solution: Probabilistic Cataloging (Paper 2)
*Goal: Present the solution directly. We use a frequentist probabilistic approach calibrated on simulations.*

### 2.1 The Concept: Catalogs as Models
- **Narrative:** Shift the paradigm. A catalog is not a list of coordinates; it is a hypothesis. We assign a probability of existence to every candidate.
- **Key References:** *Brewer et al. (2013)* (General concept).

### 2.2 Using Population Priors ($dN/dS$)
- **Narrative:** How do we constrain this model? We use the knowledge we already gained in Chapter 6.
- **Key Concepts:**
    - The $dN/dS$ (from Paper 1) tells us *how many* faint sources should exist.
    - We generate "Synthetic Skies" based on this prior to model the sub-threshold population.

### 2.3 The "Quality Factor" Metric
- **Narrative:** The core innovation of Paper 2.
- **Key Concepts:**
    - **Definition:** The "Quality Factor" $Q(TS)$ is the probability that a source is real, calibrated by comparing real data to synthetic skies.
    - **Result:** We reach down to TS=10, assigning a calibrated probability ($P_{real}$) to every seed.

## 3. Results and Impact
*Goal: Show what this new method achieves.*

### 3.1 A Deeper Catalog
- **Narrative:** We doubled the population of known gamma-ray candidates.
- **Key Findings:**
    - Doubling the number of candidates compared to 4FGL.
    - Recovering spectral properties of sources previously discarded as noise.

### 3.2 Validation and Future Work
- **Narrative:** Is it real?
- **Validation:** Consistency check of the catalog statistics.
- **Future Work:** Cross-correlation with other wavelengths (Radio/Optical) is the next logical step (left for future work).

## 4. Conclusion and Outlook
- **Summary:** We moved from "Thresholding" to "Probabilistic Inference".
- **Synthesis:** We have populated the "sub-threshold" regime with candidate sources.
- **Future Directions:**
    - Mention the potential for cross-correlating these probabilistic candidates with galaxy catalogs or radio sources to confirm their nature (as suggested in Section 3.3).
- **Transition to Part IV:** Now that we have squeezed every drop of information out of point sources (resolved and unresolved), we turn to the final frontier: **Large Scale Structure** and the Cosmic Web (Chapter 8).
