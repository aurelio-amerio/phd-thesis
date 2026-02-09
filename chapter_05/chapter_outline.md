# Chapter 5 Outline: Searching for Dark Matter Substructures

## 1. Theoretical Motivation: The Small-Scale Crisis
*Goal: Establish why we are looking for dark matter subhalos in the first place, grounding the search in the "Small-Scale Crisis" of $\Lambda$CDM.*

### 1.1 The Success and Failure of $\Lambda$CDM
- **Narrative:** Start by acknowledging the incredible success of $\Lambda$CDM on large scales (CMB, large scale structure). Contrast this with the tension on galactic scales.
- **Key Concepts:**
    - Hierarchical clustering: theories predict substructures within halos.
    - The "Missing Satellites" Problem: $\Lambda$CDM predicts orders of magnitude more satellites than observed.
    - The "Too Big to Fail" Problem: The massive subhalos predicted should form stars, but we don't see them.
- **Key References:**
    - *Bullock & Boylan-Kolchin (2017)* (Review of small-scale challenges)
    - *Press & Schechter (1974)* / *Springel et al. (2008)* (Aquarius/Millennium simulations context)

### 1.2 Unassociated Gamma-ray Sources as Candidates
- **Narrative:** Propose the solution: these "missing" satellites might be "dark" (no stars) but visible in gamma-rays via DM annihilation. This leads us to the *Fermi*-LAT "Unassociated Sources".
- **Key Concepts:**
    - The "Dark" Subhalo hypothesis.
    - *Fermi*-LAT Catalogs (3FGL/4FGL) and the population of unassociated sources (unIDs).
- **Transition:** If dark subhalos exist, they are likely hiding among the unassociated sources. How do we find them?

## 2. The "Classify-and-Count" Approach (Traditional Method)
*Goal: Describe the standard methodology used in the field to date, setting the stage for the critique and improvement methodology presented in Paper 4.*

### 2.1 Criteria for Association and Filtering
- **Narrative:** How have researchers traditionally searched for subhalos? By filtering out everything that looks like a normal astrophysical source.
- **Key Concepts:**
    - **Galactic Latitude Cuts:** avoiding the plane ($|b| > 10^\circ$).
    - **Variability:** Rejection of variable sources (likely AGN/Blazars).
    - **Multiwavelength Vetoes:** Rejection of sources with Radio/Optical/X-ray counterparts.
- **Key References:**
    - *Coronado-Blázquez et al. (2019)* (Defining specific filtering criteria)
    - *Bertoni et al. (2015)* (Early subhalo searches)

### 2.2 The Limitations of Thresholding
- **Narrative:** Critically analyze this approach. It relies on hard cuts and "thresholding."
- **Key Concepts:**
    - The "Look-Elsewhere" Effect.
    - Sensitivity limits: what if subhalos are inextricably mixed with faint background sources?
    - **Transition to Paper 4:** The biggest issue is that the training data (associated sources) looks different from the target data (unassociated sources).

## 3. Investigating Unassociated Sources with Machine Learning (Paper 4)
*Goal: Introduce the specific contribution of this thesis (Paper 4), which addresses the "Dataset Shift" problem in ML classifications.*

### 3.1 The Problem of Domain Shift
- **Narrative:** Introduce the concept of "Dataset Shift" or "Domain Shift." Standard supervised learning fails when the training set (bright, associated sources) differs from the test set (faint, unassociated sources).
- **Key Concepts:**
    - **Covariate Shift:** The distribution of features (flux, spectral index) changes.
    - **Prior Shift:** The ratio of classes (AGN vs Pulsar vs DM) is unknown in the unassociated sample.
- **Key References:**
    - *Amerio et al. (2025) [Paper 4]*
    - *Mishra-Sharma et al. (2021)* (Context of SBI/Shift)

### 3.2 From Classification to Quantification (Mixture Models)
- **Narrative:** Detail the methodological breakthrough. Instead of classifying *individual* sources (discriminative), we model the *collective* population (generative/quantification).
- **Key Concepts:**
    - **Quantification Learning:** Estimating class prevalence rather than individual labels.
    - **Mixture Models:** Modeling the unassociated population as a linear combination of source classes + DM.
    - **Forward Modeling:** Folding in the instrument response (PSF, thresholds).

### 3.3 Results: Constraining the Subhalo Population
- **Narrative:** Present the results of Paper 4.
- **Key Points:**
    - Upper limits on the number of dark subhalos among unassociated sources.
    - Constraints on the DM annihilation cross-section derived from these population limits.
    - Comparison with "Classify-and-Count" limits—demonstrating robustness against systematics.
- **Key References:**
    - *Amerio et al. (2025) [Paper 4]*

## 4. Conclusion and Transition
*Goal: Summarize the findings and bridge to the next part of the thesis (The Unresolved Sky).*

### 4.1 Summary
- We investigated the "missing satellites" problem by searching for dark subhalos among unassociated gamma-ray sources.
- We developed a robust ML framework (Mixture Models/Quantification) to handle the dataset shift inherent in this search.
- We placed stringent limits on the existence of these objects.

### 4.2 Transition to Part III
- **Narrative:** We have pushed the search for *individual* (point-like) subhalos to its statistical limit. However, many subhalos might be too faint to be detected even as unassociated sources.
- **Link:** This motivates **Part III**, where we move from studying *resolved* point sources to analyzing the *unresolved* background and the source-count distribution ($dN/dS$) to find the cumulative signal of sub-threshold populations (Paper 1 & 2).
