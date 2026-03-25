# Chapter 3: Statistical Methods for Noise-Dominated Regimes — References & Sources

## 1. Textbooks

### Bishop (2006) — "Pattern Recognition and Machine Learning"
- **Source**: Springer
- **Bib Key**: `Bishop:2006`
- **Relevance**: Foundational textbook for Bayesian inference, KDE, mixture models, and the EM algorithm. Referenced across Secs. 3.1, 3.3.

### Hastie, Tibshirani & Friedman (2009) — "The Elements of Statistical Learning"
- **Source**: Springer
- **Bib Key**: `Hastie:2009`
- **Relevance**: Covers both frequentist and Bayesian inference, the EM algorithm, and regularization. Referenced in Secs. 3.1, 3.3.

---

## 2. Key Specific Papers

### Sec. 3.1: Frequentist vs. Bayesian Inference

- **Mattox et al. (1996)** — "The Likelihood Analysis of EGRET Data"
  - **Source**: ApJ 461, 396
  - **Bib Key**: *needs checking*
  - **Relevance**: Foundational definition of the Test Statistic $TS = 2\ln(L/L_0)$ for gamma-ray likelihood analysis.

- **Wilks (1938)** — "The Large-Sample Distribution of the Likelihood Ratio"
  - **Source**: Annals of Mathematical Statistics 9, 60
  - **Bib Key**: *needs adding*
  - **Relevance**: Proves that $-2\ln\Lambda$ follows $\chi^2$ under the null hypothesis. Used in Papers 3, 4, 5.

- **Kendall & Gal (2017)** — "What Uncertainties Do We Need in Bayesian Deep Learning?"
  - **Source**: arXiv:1703.04977
  - **Bib Key**: `Kendall:2017`
  - **Relevance**: Estimating aleatoric and epistemic uncertainty via heteroscedastic Gaussian NLL. Key for Paper 1's Bayesian error estimation.

- **Gal & Ghahramani (2016)** — "Dropout as a Bayesian Approximation"
  - **Source**: arXiv:1506.02142
  - **Bib Key**: `Gal:2016`
  - **Relevance**: Mathematical equivalence between dropout and approximate Bayesian inference. Used in Paper 1.

- **Hüllermeier & Waegeman (2021)** — "Aleatoric and Epistemic Uncertainty in Machine Learning"
  - **Source**: arXiv:1910.09457
  - **Bib Key**: `Hullermeier:2021`
  - **Relevance**: Conceptual review comparing uncertainty estimation across statistical paradigms.

### Author Papers (Frequentist/Bayesian examples)

- **Amerio, Hooper & Linden (2025)** — Paper 3 (MSP luminosity function)
  - **Source**: arXiv:2412.05220
  - **Bib Key**: `Amerio:2024msp`
  - **Relevance**: Worked example of MLE + profile likelihood + integrated likelihood. Purely frequentist.

- **Amerio, Cuoco & Fornengo (2023)** — Paper 1 (dN/dS via SBI)
  - **Source**: arXiv:2302.01947
  - **Bib Key**: `Amerio:2023dns`
  - **Relevance**: Directly compares Bayesian and frequentist error estimation on the same CNN output.

- **Amerio et al. (2025)** — Paper 4 (subhalo search)
  - **Source**: arXiv:2503.14584
  - **Bib Key**: `Amerio:2025sub`
  - **Relevance**: Profile likelihood TS with Wilks' theorem for 95% CL upper bounds.

---

### Sec. 3.2: Simulation-Based Inference

- **Cranmer, Brehmer & Louppe (2020)** — "The frontier of simulation-based inference"
  - **Source**: PNAS 117(48), arXiv:1911.01429
  - **Bib Key**: `Cranmer:2020`
  - **Relevance**: Core foundational review of the SBI landscape. Defines NPE, NLE, NRE.

- **Greenberg, Nonnenmacher & Macke (2019)** — "Automatic Posterior Transformation for Likelihood-Free Inference"
  - **Source**: ICML 2019
  - **Bib Key**: `Greenberg:2019`
  - **Relevance**: Seminal paper introducing direct NPE with normalizing flows.

- **Papamakarios et al. (2021)** — "Normalizing Flows for Probabilistic Modeling and Inference"
  - **Source**: JMLR 22, arXiv:1912.02762
  - **Bib Key**: `Papamakarios:2021`
  - **Relevance**: Foundational text for the architectures underpinning NPE.

- **Diggle & Gratton (1984)** — "Monte Carlo Methods of Inference for Implicit Statistical Models"
  - **Source**: JRSS-B 46(2)
  - **Bib Key**: `Diggle:1984`
  - **Relevance**: Historical foundation for likelihood-free inference.

- **Lueckmann et al. (2021)** — "Benchmarking Simulation-Based Inference"
  - **Source**: PMLR, AISTATS 2021
  - **Bib Key**: `Lueckmann:2021`
  - **Relevance**: Standardized SBI benchmark suite.

- **Talts et al. (2018)** — "Validating Bayesian Inference Algorithms with Simulation-Based Calibration"
  - **Source**: arXiv:1804.06788
  - **Bib Key**: `Talts:2018`
  - **Relevance**: Definitive SBC framework for posterior consistency validation.

---

### Sec. 3.3: Machine Learning in Astrophysics

- **Tan & Le (2021)** — "EfficientNetV2: Smaller Models and Faster Training"
  - **Source**: arXiv:2104.00298
  - **Bib Key**: `Tan:2021`
  - **Relevance**: Architecture used in Paper 1. Fast training, low memory footprint.

- **Krachmalnicoff & Tomasi (2019)** — "CNNs on the HEALPix sphere"
  - **Source**: arXiv:1902.04083
  - **Bib Key**: `Krachmalnicoff:2019`
  - **Relevance**: Pixel-based spherical CNN (NNHealpix). Alternative to map2patch.

- **Gal, Hron & Kendall (2017)** — "Concrete Dropout"
  - **Source**: arXiv:1705.07832
  - **Bib Key**: `Gal:2017`
  - **Relevance**: Self-learning optimal dropout probability. Used in Paper 1.

- **Dempster, Laird & Rubin (1977)** — "Maximum Likelihood from Incomplete Data via the EM Algorithm"
  - **Source**: JRSS-B 39(1), 1
  - **Bib Key**: `Dempster:1977`
  - **Relevance**: Seminal paper defining the EM algorithm. Used in Paper 4.

- **Saerens, Latinne & Decaestecker (2002)** — "Adjusting the Outputs of a Classifier to New A Priori Probabilities"
  - **Source**: Neural Computation 14(1), 21
  - **Bib Key**: `Saerens:2002`
  - **Relevance**: EM-based prior adjustment. Foundational for Paper 4's mixture model.

- **Bhat & Malyshev (2022)** — "ML methods for constructing probabilistic Fermi-LAT catalogs"
  - **Source**: arXiv:2102.07642
  - **Bib Key**: `Bhat:2022`
  - **Relevance**: Probabilistic catalogs with hierarchical mixture models.

---

### Sec. 3.4: Domain Shift

- **Moreno-Torres et al. (2012)** — "A unifying view on dataset shift in classification"
  - **Source**: Pattern Recognition 45, 521
  - **Bib Key**: `MorenoTorres:2012`
  - **Relevance**: Definitive review of covariate, prior, and concept shift. Foundational reference.

- **Malyshev (2023)** — "Effect of covariate shift on multi-class classification of Fermi-LAT sources"
  - **Source**: arXiv:2307.09584
  - **Bib Key**: `Malyshev:2023`
  - **Relevance**: Concrete astrophysical application of covariate shift to Fermi-LAT classification.

- **Moreo, González & del Coz (2024)** — "Kernel Density Estimation for Multiclass Quantification"
  - **Source**: arXiv:2401.00490
  - **Bib Key**: `Moreo:2024`
  - **Relevance**: KDE-based quantification learning for resolving prior shift.

- **González, Castaño, Chawla & del Coz (2017)** — "A review on quantification learning"
  - **Source**: ACM Computing Surveys 50
  - **Bib Key**: `Gonzalez:2017`
  - **Relevance**: Comprehensive review of quantification learning methods.

---

### Sec. 3.5: Cross-Correlations

- **Limber (1953)** — Limber approximation
  - **Source**: ApJ 117, 134L
  - **Bib Key**: *needs checking*
  - **Relevance**: Foundation of 2D angular projection from 3D power spectra.

- **Cooray & Sheth (2002)** — "Halo Models of Large Scale Structure"
  - **Source**: arXiv:astro-ph/0206508
  - **Bib Key**: `Cooray:2002`
  - **Relevance**: Definitive reference for halo model (1-halo + 2-halo terms).

- **Fornengo & Regis (2014)** — "Particle dark matter searches in the anisotropic sky"
  - **Source**: arXiv:1312.4835
  - **Bib Key**: `Fornengo:2014`
  - **Relevance**: Derives $C_\ell$ formalism with window functions for DM cross-correlations.

- **Camera, Fornasa, Fornengo & Regis (2013)** — "Cross-correlation of Gamma-Ray Anisotropies and Cosmic Shear"
  - **Source**: arXiv:1212.5018
  - **Bib Key**: `Camera:2013`
  - **Relevance**: Pioneered DM gamma-ray × gravitational tracer cross-correlation technique.

- **Ando & Komatsu (2006)** — "Anisotropy of the cosmic gamma-ray background from DM annihilation"
  - **Source**: arXiv:astro-ph/0512217
  - **Bib Key**: `Ando:2006`
  - **Relevance**: Window function formalism and APS for annihilating DM.

- **Pinetti et al. (2025)** — Paper 5 (CTA cross-correlations)
  - **Source**: arXiv:2505.20383
  - **Bib Key**: `Pinetti:2025`
  - **Relevance**: SNR forecasting for gamma-ray × galaxy cross-correlations with CTAO.

---

## 3. Reference Data Table

| Paper | Bib Key | In Bib | Section |
|---|---|---|---|
| **Sec 3.1: Frequentist vs. Bayesian Inference** | | | |
| Mattox et al. (1996) — TS definition | *needs checking* | ❌ | 3.1.2 |
| Wilks (1938) — Likelihood ratio distribution | *needs adding* | ❌ | 3.1.2 |
| Bishop (2006) — Pattern Recognition and ML | `Bishop:2006` | ❌ | 3.1.3, 3.3 |
| Hastie et al. (2009) — Elements of Statistical Learning | `Hastie:2009` | ❌ | 3.1, 3.3 |
| Kendall & Gal (2017) — Bayesian Deep Learning | `Kendall:2017` | ❌ | 3.1.3 |
| Gal & Ghahramani (2016) — Dropout ≈ Bayesian | `Gal:2016` | ❌ | 3.1.3 |
| Hüllermeier & Waegeman (2021) — Uncertainty types | `Hullermeier:2021` | ❌ | 3.1.4 |
| Amerio et al. (2025) — Paper 3 | `Amerio:2024msp` | ✅ | 3.1.2 |
| Amerio et al. (2023) — Paper 1 | `Amerio:2023dns` | ✅ | 3.1.4 |
| Amerio et al. (2025) — Paper 4 | `Amerio:2025sub` | ✅ | 3.1.2 |
| **Sec 3.2: Simulation-Based Inference** | | | |
| Cranmer et al. (2020) — SBI Frontier | `Cranmer:2020` | ❌ | 3.2.1 |
| Greenberg et al. (2019) — NPE | `Greenberg:2019` | ❌ | 3.2.2 |
| Papamakarios et al. (2021) — Normalizing Flows | `Papamakarios:2021` | ❌ | 3.2.2 |
| Diggle & Gratton (1984) — Implicit models | `Diggle:1984` | ❌ | 3.2.1 |
| Lueckmann et al. (2021) — Benchmarking SBI | `Lueckmann:2021` | ❌ | 3.2.2 |
| Talts et al. (2018) — SBC | `Talts:2018` | ❌ | 3.2.3 |
| **Sec 3.3: Machine Learning in Astrophysics** | | | |
| Tan & Le (2021) — EfficientNetV2 | `Tan:2021` | ❌ | 3.3.2 |
| Krachmalnicoff & Tomasi (2019) — NNHealpix | `Krachmalnicoff:2019` | ❌ | 3.3.2 |
| Gal et al. (2017) — Concrete Dropout | `Gal:2017` | ❌ | 3.3.2 |
| Saerens et al. (2002) — EM prior adjustment | `Saerens:2002` | ❌ | 3.3.3 |
| Bhat & Malyshev (2022) — Probabilistic catalogs | `Bhat:2022` | ❌ | 3.3.3 |
| **Sec 3.4: Domain Shift** | | | |
| Moreno-Torres et al. (2012) — Dataset shift | `MorenoTorres:2012` | ❌ | 3.4.1 |
| Malyshev (2023) — Covariate shift Fermi | `Malyshev:2023` | ❌ | 3.4.1 |
| Moreo et al. (2024) — KDE quantification | `Moreo:2024` | ❌ | 3.4.2 |
| González et al. (2017) — Quantification review | `Gonzalez:2017` | ❌ | 3.4.2 |
| **Sec 3.5: Cross-Correlations** | | | |
| Limber (1953) — Limber approximation | *needs checking* | ❌ | 3.5.1 |
| Cooray & Sheth (2002) — Halo model | `Cooray:2002` | ❌ | 3.5.1 |
| Fornengo & Regis (2014) — APS formalism | `Fornengo:2014` | ❌ | 3.5.1 |
| Camera et al. (2013) — γ × shear | `Camera:2013` | ❌ | 3.5.1 |
| Ando & Komatsu (2006) — DM APS | `Ando:2006` | ❌ | 3.5.1 |
| Pinetti et al. (2025) — Paper 5 | `Pinetti:2025` | ✅ | 3.5.2 |
