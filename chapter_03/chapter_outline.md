# Chapter 3: Statistical Methods for Noise-Dominated Regimes

> **Scope**: ~15 pages. Foundational methods chapter establishing the mathematical framework referenced throughout the thesis. Uses standard statistical examples (Poisson counts, Gaussian distributions) with explicit "Application Preview" paragraphs connecting each method to Papers 1–5. Treatment is conceptual: definitions and key equations, not full derivations. Technical deep dives are deferred to the individual paper chapters.

## Connections
- **Previous**: Chapter 2 established the gamma-ray sky, its complexity, and the instrumental limitations that make standard approaches insufficient.
- **Next**: Chapter 4 introduces the Galactic Center Excess and applies the methods of Sec. 3.1 (Paper 1/MSPs).
- **Inserted Paper**: None. This chapter is purely foundational.

## Paper Dependencies

| Paper | What Chapter 3 Must Set Up |
|-------|---------------------------|
| **Paper 1** (dN/dS via SBI) | SBI/NPE paradigm, Bayesian error estimation, frequentist cross-checks, CNN concept |
| **Paper 2** (sub-threshold catalogs) | Poisson likelihood, TS definition, KS test |
| **Paper 3** (MSPs/GCE) | MLE, profile likelihood, integrated likelihood, $-2\Delta\ln\mathcal{L}$ model comparison |
| **Paper 4** (subhalo search) | Mixture models, EM algorithm, KDE, covariate + prior shift, profile likelihood |
| **Paper 5** (CTA cross-correlations) | Angular power spectrum $C_\ell$, Limber approximation, SNR, $\Delta\chi^2$ |

---

## [3.0] Chapter Introduction (~0.5 page)
**Goal**: Untitled opening paragraphs. Motivate the need for a unified statistical framework.
- The gamma-ray sky described in Chapter 2 is dominated by noise: faint signals embedded in bright backgrounds, overlapping source populations, and instrumental limitations.
- Extracting physics requires a toolbox spanning classical statistics, modern machine learning, and domain-specific techniques.
- This chapter provides the mathematical vocabulary used throughout the thesis. Each method is introduced with standard examples, followed by a preview of where it appears in the research papers.
- Chapter roadmap: Sec. 3.1 (Frequentist/Bayesian foundations), Sec. 3.2 (SBI), Sec. 3.3 (ML), Sec. 3.4 (Domain shift), Sec. 3.5 (Cross-correlations).

---

## [3.1] Frequentist and Bayesian Inference (~4 pages)
**Goal**: Build the full statistical vocabulary from scratch. Both paradigms treated as complementary tools.
**Narrative**: From the inference problem → frequentist approach → Bayesian approach → when to use which.

### [3.1.1] The Inference Problem (~0.5 page)
- Generic setup: observed data $\mathbf{d}$, model parameters $\boldsymbol{\theta}$, model $\mathcal{M}$
- The central question: what can we learn about $\boldsymbol{\theta}$ from $\mathbf{d}$?
- Two philosophies for answering this question — both valid and complementary
- **Key refs**: Bishop (2006), Hastie et al. (2009)

### [3.1.2] Frequentist Inference (~1.5 pages)
- **The likelihood function** $\mathcal{L}(\boldsymbol{\theta}) = p(\mathbf{d}|\boldsymbol{\theta})$ as a function of parameters for fixed data
- **MLE**: $\hat{\boldsymbol{\theta}} = \arg\max_{\boldsymbol{\theta}} \mathcal{L}(\boldsymbol{\theta})$
- **Integrated (marginal) likelihood**: integrating out nuisance parameters within the likelihood framework — this is *not* Bayesian posterior computation
- **Profile likelihood**: maximizing the likelihood over nuisance parameters
- **Confidence intervals**: from the likelihood ratio
- **Test Statistics**: $TS = -2\ln(L_0/L_1)$ and Wilks' theorem ($TS \sim \chi^2$)
- **Standard example**: Counting photons from a gamma-ray source — Poisson likelihood $\mathcal{L}(\mu) = e^{-\mu}\mu^N / N!$
- **Application Preview**:
  - *Paper 3*: MLE of the MSP luminosity function parameters $(\langle L_\gamma \rangle, \sigma_L)$ via 3D likelihood scans, integrated likelihood over flux, and $-2\Delta\ln\mathcal{L}$ model comparison across 5 hypotheses — purely frequentist throughout
  - *Paper 4*: Profile likelihood $TS(\langle\sigma v\rangle)$ with Wilks' theorem to set 95% CL upper bounds on the DM annihilation cross-section
  - *Paper 5*: $\Delta\chi^2$ test statistic comparing astrophysical-only vs astrophysical+DM hypotheses
- **Key refs**: Mattox et al. (1996), Wilks (1938), Hastie et al. (2009)

### [3.1.3] Bayesian Inference (~1.5 pages)
- **Bayes' Theorem**: $p(\boldsymbol{\theta}|\mathbf{d}) \propto p(\mathbf{d}|\boldsymbol{\theta}) \, p(\boldsymbol{\theta})$
- Prior $p(\boldsymbol{\theta})$: encoding prior knowledge
- Posterior $p(\boldsymbol{\theta}|\mathbf{d})$: the full answer to the inference problem
- Evidence $p(\mathbf{d})$: normalization, used for model comparison
- **Credible intervals** vs. confidence intervals
- **Marginalization**: integrating out nuisance parameters from the posterior (contrast with frequentist integrated likelihood)
- **Standard example**: Updating a belief about source flux given $N$ photon counts, starting from an uninformative prior
- **Application Preview**:
  - *Paper 1*: Bayesian error estimation via heteroscedastic Gaussian NLL — the CNN learns both the mean and variance of the posterior for the $dN/dS$
- **Key refs**: Bishop (2006), Kendall & Gal (2017), Gal & Ghahramani (2016)

### [3.1.4] When to Use Which (~0.5 page)
- Frequentist strengths: hypothesis testing, upper limits, minimal assumptions (no priors)
- Bayesian strengths: natural uncertainty quantification, incorporation of prior knowledge, marginalization over nuisance parameters
- In practice, both are used throughout this thesis — sometimes on the same problem
- **Application Preview**:
  - *Paper 1*: The CNN provides Bayesian errors via dropout approximation, cross-checked against a frequentist bias estimation — both yield compatible results
- **Key refs**: Hüllermeier & Waegeman (2021)

---

## [3.2] The Simulation-Based Inference Paradigm (~3 pages)
**Goal**: Introduce the SBI concept for readers unfamiliar with it. Motivate why traditional likelihood evaluation fails for complex models.
**Narrative**: From the intractable likelihood problem → the SBI solution → validation.

### [3.2.1] The Intractable Likelihood Problem (~0.5 page)
- When the forward model involves complex simulations (many latent variables, stochastic elements), the likelihood $p(\mathbf{d}|\boldsymbol{\theta})$ cannot be written in closed form
- Forward simulation is easy; inverting it analytically is not
- **Standard example**: Generating a synthetic gamma-ray sky map from a parameterized $dN/dS$ — easy to simulate, impossible to write a closed-form likelihood for the full map
- **Key refs**: Cranmer et al. (2020), Diggle & Gratton (1984)

### [3.2.2] Likelihood-Free Approaches (~1.5 pages)
- The SBI concept: replace explicit likelihood evaluation with learned surrogates trained on simulated data
- **Three main strategies** (brief characterization):
  - **NPE** (Neural Posterior Estimation): directly approximate $p(\boldsymbol{\theta}|\mathbf{d})$
  - **NLE** (Neural Likelihood Estimation): approximate the likelihood, then use MCMC for the posterior
  - **NRE** (Neural Ratio Estimation): learn the likelihood-to-evidence ratio
- **Amortized inference**: upfront training cost → instant posterior estimation for any new observation
- Keep focus on NPE as the approach most directly relevant to the thesis
- **Application Preview**:
  - *Paper 1*: The CNN performs NPE — trained on 900k synthetic sky maps, it directly estimates the $dN/dS$ and its uncertainty for any input map, without evaluating any explicit likelihood
- **Key refs**: Greenberg et al. (2019), Papamakarios et al. (2021), Lueckmann et al. (2021)

### [3.2.3] Validation of SBI (~1 page)
- The challenge: how do you verify a learned posterior when no ground truth posterior exists?
- **Simulation-Based Calibration (SBC)**: Generate synthetic observations from known parameters → run the estimator → check that the recovered posteriors are statistically consistent
- **Coverage diagnostics**: Do the $X$% credible intervals contain the true value $X$% of the time?
- **Application Preview**:
  - *Paper 1*: The frequentist cross-check (Sec. 3.1.4) serves as an independent validation of the Bayesian CNN errors — the compatibility of both approaches provides confidence in the SBI output
- **Key refs**: Talts et al. (2018), Cranmer et al. (2020)

---

## [3.3] Machine Learning in Astrophysics (~3 pages)
**Goal**: Provide the ML background needed to understand Papers 1 and 4. Not a general ML textbook — focused on the specific techniques used.
**Narrative**: From learning tasks → architectures → density estimation.

### [3.3.1] Learning Tasks (~0.5 page)
- **Classification**: Assigning sources to categories (Galactic, extragalactic, DM)
- **Regression**: Estimating continuous quantities (flux, $dN/dS$ values)
- **Density estimation**: Modeling the distribution of source features
- **Standard example**: Classifying gamma-ray sources by their spectral parameters $(\alpha, \beta)$
- **Key refs**: Bishop (2006)

### [3.3.2] Neural Networks and Deep Learning (~1.5 pages)
- Basic architecture: layers, activations, training via backpropagation
- **CNNs**: weight sharing, translation equivariance, convolutional filters → natural for spatial data (images, sky maps)
- **Cost functions**: MSE for regression, cross-entropy for classification, heteroscedastic Gaussian NLL for learning the variance
- **Regularization**: Dropout (+ concrete dropout for self-tuning), batch normalization — preventing overfitting on large models
- **Application Preview**:
  - *Paper 1*: EfficientNet V2M architecture applied to gamma-ray sky maps via the map2patch algorithm (HEALPix sphere → 12 flat patches). Concrete dropout provides self-learned regularization. Details of the architecture and training deferred to Chapter 6
- **Key refs**: Tan & Le (2021), Gal et al. (2017), Krachmalnicoff & Tomasi (2019)

### [3.3.3] Density Estimation (~1 page)
- **Kernel Density Estimation (KDE)**: Non-parametric estimation of probability densities from data. Gaussian kernels, bandwidth selection via cross-validation
- **Mixture models**: $p(\mathbf{x}) = \sum_k \pi_k \, p_k(\mathbf{x}|\boldsymbol{\theta}_k)$ — parametric density estimation as a weighted sum of component distributions
- **The EM algorithm**: Iterative optimization for mixture model parameters when class labels are latent variables. E-step (evaluate posterior class probabilities) → M-step (update parameters and weights)
- **Application Preview**:
  - *Paper 4*: KDE approximates the empirical distributions of Fermi-LAT source spectral features. A 3-component generative mixture model (Galactic + extragalactic + DM subhalos) is optimized via EM to determine class prevalences and set upper bounds on $\langle\sigma v\rangle$. Full details deferred to Chapter 5
- **Key refs**: Bishop (2006), Saerens et al. (2002), Bhat & Malyshev (2022)

---

## [3.4] The Domain Shift Challenge (~2 pages)
**Goal**: Introduce the formalism of dataset shift as applied to astrophysical classification problems. This is a key conceptual advance of Paper 4.
**Narrative**: From the problem statement → types of shift → the combined solution.

### [3.4.1] Problem Statement (~0.5 page)
- In standard classification, $p_\text{train}(\mathbf{x}, k) = p_\text{target}(\mathbf{x}, k)$
- In practice, this assumption often fails: training on associated sources, but classifying unassociated ones
- The joint distribution can be factored two ways: $p(\mathbf{x}, k) = p(k|\mathbf{x})p(\mathbf{x}) = p(\mathbf{x}|k)p(k)$, giving rise to two types of shift
- **Standard example**: A catalog where faint sources are systematically under-represented, so the feature distributions differ from the true population
- **Key refs**: Moreno-Torres et al. (2012)

### [3.4.2] Types of Dataset Shift (~1.5 pages)
- **Covariate shift**: $p_\text{train}(k|\mathbf{x}) = p_\text{target}(k|\mathbf{x})$ but $p_\text{train}(\mathbf{x}) \neq p_\text{target}(\mathbf{x})$
  - The class-conditional relationship is preserved, but the feature distributions change
  - Can be modeled by a monotonic modulation function (e.g., sigmoid)
- **Prior shift** (label shift): $p_\text{train}(\mathbf{x}|k) = p_\text{target}(\mathbf{x}|k)$ but $p_\text{train}(k) \neq p_\text{target}(k)$
  - The per-class distributions are unchanged, but class prevalences shift
  - Solved by fitting the mixture weights $\pi_k$
- In general, both effects act simultaneously
- **Application Preview**:
  - *Paper 4*: Constructs the first model simultaneously accounting for both shifts among Fermi-LAT sources. Prior shift (Galactic/extragalactic class fractions change from associated to unassociated sources: 6% → 29% Galactic) + covariate shift (sigmoid modulation functions $f(x_d; b_d, c_d)$). This combined framework enables statistically rigorous upper bounds on a new source class (DM subhalos). Full formalism deferred to Chapter 5
- **Key refs**: Moreno-Torres et al. (2012), Malyshev (2023), Moreo et al. (2024), González et al. (2017)

---

## [3.5] Cross-Correlations as a Complementary Probe (~2 pages)
**Goal**: Introduce the cross-correlation formalism that underpins Paper 5. Establish the $C_\ell$ language.
**Narrative**: From the angular power spectrum definition → sensitivity metrics.

### [3.5.1] The Angular Power Spectrum (~1.5 pages)
- **Intensity fluctuations**: Expanding a sky map into spherical harmonics → the angular power spectrum $C_\ell$
- **Auto-correlation** ($C_\ell^{\gamma\gamma}$) and **cross-correlation** ($C_\ell^{\gamma g}$) between gamma-ray intensity and galaxy counts
- **The Limber approximation**: Projecting the 3D cross-correlation power spectrum $P_{\gamma g}(k)$ into 2D angular space:
  $C_\ell^{\gamma g} = \int \frac{d\chi}{\chi^2} W_\gamma(\chi) W_g(\chi) P_{\gamma g}(k = \ell/\chi, \chi)$
- **Window functions** $W(\chi)$: describe the redshift distribution of each observable
- **The halo model**: Decomposing $P(k) = P_\text{1h}(k) + P_\text{2h}(k)$ into intra-halo and inter-halo contributions
- Brief conceptual introduction — full derivation deferred to Chapter 10
- **Key refs**: Limber (1953), Cooray & Sheth (2002), Fornengo & Regis (2014), Camera et al. (2013), Ando & Komatsu (2006)

### [3.5.2] Statistical Sensitivity (~0.5 page)
- **Signal-to-noise ratio**: $\text{SNR} = \sqrt{\sum_{\ell,i} (C_{\ell,i}^{\gamma g} / \Delta C_{\ell,i}^{\gamma g})^2}$
- **Variance** $\Delta C_\ell$: depends on auto-correlation spectra, noise terms $C_N$, beam function $B_\ell$, and sky fraction $f_\text{sky}$
- **$\Delta\chi^2$ test statistic**: Comparing null (astrophysical-only) vs alternative (astrophysical + DM) hypotheses
- **Application Preview**:
  - *Paper 5*: Forecasts the CTAO sensitivity to DM annihilation/decay by cross-correlating gamma-ray maps with the 2MASS galaxy catalog. The cross-correlation outperforms auto-correlation by ~5× due to reduced astrophysical contamination. Full analysis deferred to Chapter 10
- **Key refs**: Pinetti et al. (2025)

---

## [3.6] Summary and Transition (~0.5 page)
- This chapter has established the statistical toolkit: frequentist and Bayesian inference (Sec. 3.1), simulation-based inference (Sec. 3.2), machine learning (Sec. 3.3), domain adaptation (Sec. 3.4), and cross-correlations (Sec. 3.5).
- Each method has been introduced conceptually and connected to its application in the thesis papers.
- The following chapters present the physics results, referencing this chapter's definitions rather than re-deriving them.
- **Bridge**: Chapter 4 introduces the Galactic Center Excess and the first application of these methods — the MSP luminosity function measurement (Paper 3) using the frequentist framework of Sec. 3.1.

---

## Page Budget

| Section | Pages | Key Design Choice |
|---------|-------|-------------------|
| 3.0 Introduction | ~0.5 | Motivate the need for a statistical toolbox |
| 3.1 Frequentist vs. Bayesian | ~4 | Both paradigms valued; standard examples + previews |
| 3.2 SBI Paradigm | ~3 | Conceptual; NPE focus; defer architectures to Ch. 6 |
| 3.3 ML in Astrophysics | ~3 | CNN + density estimation; two tracks for Papers 1 & 4 |
| 3.4 Domain Shift | ~2 | Formalism from Paper 4; standard example then preview |
| 3.5 Cross-Correlations | ~2 | $C_\ell$ language; defer halo model details to Ch. 10 |
| 3.6 Summary | ~0.5 | Bridge to Chapter 4 |
| **Total** | **~15** | |

## No-Repetition Principle

Chapter 3 introduces concepts at a general level. The papers (included verbatim) contain the detailed specifics:

| Concept | Chapter 3 introduces | Paper(s) detail |
|---------|----------------------|-----------------|
| MLE / Profile likelihood | Definitions, standard examples | Paper 3: applied to MSP luminosity function |
| Bayesian error estimation | Heteroscedastic NLL, dropout ≈ BNN | Paper 1: full architecture and training |
| SBI / NPE | Paradigm, amortization, validation | Paper 1: CNN design, map2patch, training on 900k maps |
| KDE / Mixture models / EM | Definitions, standard example | Paper 4: 3-component generative model, KDE bandwidth |
| Covariate + prior shift | Formal definitions, types | Paper 4: sigmoid modulation, full optimization |
| $C_\ell$ / Limber approximation | Equations, window functions | Paper 5: full halo model, blazar and DM window functions |
| $\Delta\chi^2$ / SNR | Definitions | Paper 5: energy-binned CTAO sensitivity forecasts |
