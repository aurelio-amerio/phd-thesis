# Chapter 3 Review Fixes — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Address all issues identified in `chapter_03/chapter_review.md` — replace self-citations with cross-references, replace "Paper~N" jargon with chapter references, trim application previews to conceptual level, fix broken cross-references, and deduplicate bibliography entries.

**Architecture:** Six LaTeX section files are edited file-by-file. Each task addresses all review issues relevant to that file in a single pass. A final task handles bibliography deduplication.

**Tech Stack:** LaTeX (pdflatex + BibTeX, JHEP style)

**Reference:** The full issue list is in `chapter_03/chapter_review.md`. The chapter-paper mapping is:

| Internal label | Thesis chapter | `\ref` label |
|---|---|---|
| Paper 1 (dN/dS via SBI) | Chapter 6 | `ch:6` |
| Paper 2 (probabilistic catalog) | Chapter 7 | `ch:7` |
| Paper 3 (MSP/GCE) | Chapter 4 | `ch:4` |
| Paper 4 (subhalo search) | Chapter 5 | `ch:5` |
| Paper 5 (CTA cross-correlations) | Chapter 8 | `ch:8` |

---

### Task 1: Fix `3.1_inference.tex`

**File:** `chapter_03/sections/3.1_inference.tex`

**Issues addressed:** 5 (self-citations → cross-refs), 6 (Paper~N → chapter refs), 7 (trim previews), 8 (hardcoded chapter numbers)

- [ ] **Step 1: Line 7 — Replace "Papers~1--5" with thesis-level language**

```
old: "which connect the general formalism to its specific use in Papers~1--5."
new: "which connect the general formalism to its specific use in the research chapters of this thesis."
```

- [ ] **Step 2: Line 51 — Remove self-citation on Poisson likelihood**

The Poisson likelihood is standard and already attributed to Mattox:1996 on line 52.

```
old: "the model prediction in pixel $a$ \cite{Amerio:2023dns}."
new: "the model prediction in pixel $a$."
```

- [ ] **Step 3: Lines 83–92 — Rewrite Sec 3.1.2 application preview**

Replace the entire application preview paragraph with a trimmed version that uses chapter cross-references, removes implementation details, and drops self-citations:

```latex
old:
\paragraph{Application preview.}

The frequentist framework developed above is used extensively in this thesis:
\begin{itemize}
	\item In Paper~3 \cite{Amerio:2024msp}, the MSP luminosity function parameters $(\langle L_\gamma \rangle, \sigma_L)$ are constrained via MLE applied to an integrated likelihood.
	      The observational likelihood profile of each globular cluster's gamma-ray flux is combined with the theoretical luminosity function and marginalized over the true flux, yielding a joint integrated likelihood across all clusters.
	      Model comparison among five scaling hypotheses is performed through $-2\Delta\ln\mathcal{L}$ values.
	\item In Paper~4 \cite{Amerio:2025sub}, a profile likelihood $\mathrm{TS}(\langle\sigma v\rangle) = -2\ln[\mathcal{L}(\langle\sigma v\rangle)/\mathcal{L}_{\mathrm{max}}]$ is used to set 95\% CL upper bounds on the dark matter annihilation cross-section, relying on Wilks' theorem with one degree of freedom ($\mathrm{TS} = 3.84$).
	\item In Paper~5 \cite{Pinetti:2025}, a $\Delta\chi^2$ test statistic compares the astrophysical-only and astrophysical-plus-DM hypotheses for the cross-correlation angular power spectrum, with $2\sigma$ sensitivity bounds drawn at $\Delta\chi^2 = 4$.
\end{itemize}

new:
\paragraph{Application preview.}

The frequentist framework developed above is used extensively in this thesis:
\begin{itemize}
	\item In Chapter~\ref{ch:4}, the MSP luminosity function is constrained via MLE applied to an integrated likelihood, and model comparison is performed through $-2\Delta\ln\mathcal{L}$ values.
	\item In Chapter~\ref{ch:5}, a profile likelihood test statistic is used with Wilks' theorem to set 95\% CL upper bounds on the dark matter annihilation cross-section.
	\item In Chapter~\ref{ch:8}, a $\Delta\chi^2$ test statistic compares astrophysical-only and astrophysical-plus-DM hypotheses for the cross-correlation angular power spectrum.
\end{itemize}
```

- [ ] **Step 4: Lines 149–154 — Rewrite Sec 3.1.3 application preview**

```latex
old:
\paragraph{Application preview.}

In Paper~1 \cite{Amerio:2023dns}, a CNN trained on $\sim$900k synthetic gamma-ray sky maps uses this framework to reconstruct the source-count distribution $dN/dS$ and its uncertainty.
The network employs the heteroscedastic Gaussian NLL to learn the aleatoric error as a function of flux, while concrete dropout \cite{Gal:2017}---a variant that self-learns the optimal dropout probability during training---provides the epistemic uncertainty.
The resulting Bayesian error estimates are independently validated against a frequentist cross-check (see Section~\ref{sec:3.1.4}), with the two approaches yielding compatible error bands on the reconstructed $dN/dS$.
Full architectural and training details are deferred to Chapter~6.

new:
\paragraph{Application preview.}

In Chapter~\ref{ch:6}, this framework is applied to reconstruct the source-count distribution $dN/dS$ and its uncertainty from gamma-ray sky maps.
A neural network trained with the heteroscedastic loss learns the aleatoric uncertainty as a function of flux, while concrete dropout \cite{Gal:2017} provides the epistemic component.
The resulting Bayesian error estimates are validated against an independent frequentist cross-check (Section~\ref{sec:3.1.4}).
```

- [ ] **Step 5: Lines 165 — Replace self-citations in Sec 3.1.4**

```
old: "new physics contributions \cite{Amerio:2025sub, Amerio:2024msp}."
new: "new physics contributions (see Chapters~\ref{ch:4} and~\ref{ch:5})."
```

- [ ] **Step 6: Lines 177–181 — Rewrite Sec 3.1.4 cross-check discussion**

```latex
old:
In practice, both paradigms are used throughout this thesis, and in some cases they are applied to the same problem as independent cross-checks.
In Paper~1 \cite{Amerio:2023dns}, the CNN provides Bayesian error estimates on the reconstructed $dN/dS$ through dropout and the heteroscedastic loss.
These are validated against a frequentist analysis of the same validation dataset, where the $1\sigma$ and $2\sigma$ confidence intervals are extracted from the empirical distribution of residuals across 100\,000 synthetic maps.
The frequentist cross-check also provides a formal estimate of the model's bias---the systematic deviation between the median prediction and the true value---which is found to be negligible across the flux range of interest.
The compatibility of the two independent error estimates provides confidence that the uncertainty quantification is robust \cite{Amerio:2023dns}.

new:
In practice, both paradigms are used throughout this thesis, and in some cases they are applied to the same problem as independent cross-checks.
In Chapter~\ref{ch:6}, the neural network provides Bayesian error estimates on the reconstructed $dN/dS$ through dropout and the heteroscedastic loss.
These are validated against a frequentist analysis of the same data, where confidence intervals are extracted from the empirical distribution of residuals across the validation set.
The frequentist cross-check also provides a formal estimate of the model's bias, which is found to be negligible across the flux range of interest.
The compatibility of the two independent error estimates provides confidence that the uncertainty quantification is robust.
```

- [ ] **Step 7: Verify no remaining self-citations or "Paper~N" in this file**

Search for `Amerio:`, `Pinetti:`, and `Paper~` in `3.1_inference.tex`. Should find zero matches.

---

### Task 2: Fix `3.2_sbi.tex`

**File:** `chapter_03/sections/3.2_sbi.tex`

**Issues addressed:** 5 (self-citations), 6 (Paper~N), 7 (trim previews)

- [ ] **Step 1: Lines 35–38 — Replace self-citations in the worked example (Sec 3.2.1)**

```latex
old:
As we will discuss in detail in Chapter~6, the observed photon-count map results from the superposition of thousands of unresolved point sources, each convolved with the instrument point spread function, added to a diffuse Galactic foreground and an isotropic background, and finally subjected to Poisson counting noise~\cite{Amerio:2023dns}.
Writing a closed-form likelihood for this full sky map would require integrating over every possible spatial configuration, flux, and number of the unresolved sources.
Generating a synthetic map from a given set of $dN/dS$ parameters, by contrast, amounts to a sequence of well-defined sampling steps: draw source fluxes from the $dN/dS$, scatter them on the sky, convolve with the PSF, add backgrounds, multiply by the exposure, and apply Poisson noise~\cite{Amerio:2023dns}.

new:
As discussed in detail in Chapter~\ref{ch:6}, the observed photon-count map results from the superposition of thousands of unresolved point sources, each convolved with the instrument point spread function, added to a diffuse Galactic foreground and an isotropic background, and finally subjected to Poisson counting noise.
Writing a closed-form likelihood for this full sky map would require integrating over every possible spatial configuration, flux, and number of the unresolved sources.
Generating a synthetic map from a given set of $dN/dS$ parameters, by contrast, amounts to a sequence of well-defined sampling steps: draw source fluxes from the $dN/dS$, scatter them on the sky, convolve with the PSF, add backgrounds, multiply by the exposure, and apply Poisson noise.
```

- [ ] **Step 2: Lines 73–77 — Rewrite Sec 3.2.2 application preview**

```latex
old:
In this thesis, NPE is the SBI strategy most directly relevant to our work.
In Paper~1~\cite{Amerio:2023dns}, a convolutional neural network is trained on $9 \times 10^5$ synthetic gamma-ray sky maps to estimate the $dN/dS$ and its uncertainty for any input map, without ever evaluating an explicit likelihood.
The approach operates in the spirit of NPE: the CNN directly maps an observed sky map to posterior summaries (the mean and variance for each flux bin), bypassing any explicit likelihood evaluation, though it uses a heteroscedastic Gaussian loss (Section~\ref{sec:3.1.3}) rather than a normalizing flow to parameterize the output distribution.
Once trained, the network can be applied to the real 14-year Fermi-LAT sky map to immediately obtain the source-count distribution.
The full details of the architecture and training procedure are deferred to Chapter~6.

new:
In this thesis, NPE is the SBI strategy most directly relevant to our work.
In Chapter~\ref{ch:6}, a convolutional neural network trained on synthetic gamma-ray sky maps estimates the source-count distribution $dN/dS$ and its uncertainty for any input map, without evaluating an explicit likelihood.
The approach operates in the spirit of NPE: the network directly maps an observed sky map to posterior summaries (the mean and variance for each flux bin), though it uses a heteroscedastic Gaussian loss (Section~\ref{sec:3.1.3}) rather than a normalizing flow to parameterize the output distribution.
Once trained, the inference is amortized: the network can be applied to the real Fermi-LAT sky map to immediately obtain the source-count distribution.
```

- [ ] **Step 3: Lines 101–104 — Rewrite Sec 3.2.3 validation paragraph**

```latex
old:
In Paper~1~\cite{Amerio:2023dns}, the internally estimated Bayesian uncertainties from the CNN are cross-checked against frequentist error bars derived from the distribution of residuals over the validation set.
The close agreement between the two error estimates provides confidence in the reliability of the uncertainty quantification without requiring access to the true posterior, which, for the $dN/dS$ problem, is unknown.
The details of this validation strategy are presented in Chapter~6.

new:
In Chapter~\ref{ch:6}, the internally estimated Bayesian uncertainties are cross-checked against frequentist error bars derived from the distribution of residuals over the validation set (see also Section~\ref{sec:3.1.4}).
The close agreement between the two independent error estimates provides confidence in the reliability of the uncertainty quantification.
```

- [ ] **Step 4: Verify no remaining self-citations or "Paper~N" in this file**

---

### Task 3: Fix `3.3_ml_astrophysics.tex`

**File:** `chapter_03/sections/3.3_ml_astrophysics.tex`

**Issues addressed:** 1 (broken ref), 2 (wrong chapter), 5 (self-citations), 6 (Paper~N), 7 (trim previews), 11 (z_{ik} notation)

- [ ] **Step 1: Lines 4–5 — Uncomment the subsection heading (Issue 1/12)**

```latex
old:
% \subsection{Learning Tasks}
% \label{sec:3.3.1}

new:
\subsection{Learning Tasks}
\label{sec:3.3.1}
```

- [ ] **Step 2: Line 14 — Replace Paper~4 + self-citation**

```latex
old: "In Paper~4, we extend this paradigm beyond standard source classes by introducing a generative mixture model that can accommodate an entirely new population---dark matter subhalos---among the unassociated sources \cite{Amerio:2025sub}."
new: "In Chapter~\ref{ch:5}, this paradigm is extended beyond standard source classes through a generative mixture model that accommodates an entirely new population---dark matter subhalos---among the unassociated sources."
```

- [ ] **Step 3: Lines 17–19 — Replace Paper~1 + self-citation, remove implementation details**

```latex
old:
Paper~1 employs a convolutional neural network to estimate the source-count distribution $dN/dS$ directly from gamma-ray sky maps \cite{Amerio:2023dns}.
The network ingests a two-dimensional flux map and outputs a 21-element vector: the reconstructed $dN/dS$ discretized across 20 flux bins, together with the predicted isotropic diffuse background level $F_\mathrm{iso}$.
By adopting a heteroscedastic loss function (described in Section~\ref{sec:3.3.2}), the same network simultaneously performs regression on the associated uncertainties, predicting the variance of each output alongside its mean \cite{Kendall:2017}.

new:
In Chapter~\ref{ch:6}, a convolutional neural network estimates the source-count distribution $dN/dS$ directly from gamma-ray sky maps.
By adopting a heteroscedastic loss function (described in Section~\ref{sec:3.3.2}), the network simultaneously performs regression on both the $dN/dS$ values and their associated uncertainties, predicting the variance of each output alongside its mean \cite{Kendall:2017}.
```

- [ ] **Step 4: Lines 22–25 — Replace Paper~4 + self-citation, trim implementation details**

```latex
old:
This shift from individual classification to population-level inference is central to the quantification learning framework adopted in Paper~4 \cite{Amerio:2025sub}, where Kernel Density Estimation is used to model the distributions of spectral parameters ($\log_{10}\phi$, $\alpha$, $\beta$) for known Galactic and extragalactic source classes.
The resulting class-conditional densities $p(\mathbf{x}|k)$ are then combined into a generative mixture model whose parameters---including the prevalence of a potential dark matter component---are determined by maximizing the likelihood over the unassociated source data.

new:
This shift from individual classification to population-level inference is central to the quantification learning framework developed in Chapter~\ref{ch:5}, where Kernel Density Estimation is used to model the spectral parameter distributions of known source classes.
The resulting class-conditional densities $p(\mathbf{x}|k)$ are then combined into a generative mixture model whose parameters---including the prevalence of a potential dark matter component---are determined by maximizing the likelihood over the unassociated source data.
```

- [ ] **Step 5: Line 39 — Remove self-citation**

```
old: "convolved with the instrument's point spread function \cite{Amerio:2023dns}."
new: "convolved with the instrument's point spread function."
```

- [ ] **Step 6: Lines 45–47 — Replace self-citations with cross-references**

```latex
old:
The second approach, \texttt{map2patch} \cite{Amerio:2023dns}, subdivides the sphere into the 12 equal-area base pixels of the HEALPix scheme, treating each as an independent flat image processed through standard 2D convolutions.
This subdivision preserves the exact area and photon content of every pixel without resampling, at the cost of discarding spatial information at patch boundaries.
For statistically isotropic, small-scale signals such as the point-source population studied in Paper~1, the two methods produce compatible results, but \texttt{map2patch} provides more than an order of magnitude improvement in execution speed \cite{Amerio:2023dns}.

new:
The second approach, \texttt{map2patch} (Chapter~\ref{ch:6}), subdivides the sphere into the 12 equal-area base pixels of the HEALPix scheme, treating each as an independent flat image processed through standard 2D convolutions.
This subdivision preserves the exact area and photon content of every pixel without resampling, at the cost of discarding spatial information at patch boundaries.
For statistically isotropic, small-scale signals such as the point-source population studied in Chapter~\ref{ch:6}, the two methods produce compatible results, but \texttt{map2patch} provides more than an order of magnitude improvement in execution speed.
```

- [ ] **Step 7: Lines 73–79 — Rewrite Sec 3.3.2 application preview**

```latex
old:
\paragraph{Application preview.}

In Paper~1, the $dN/dS$ reconstruction employs an EfficientNet V2M architecture \cite{Tan:2021} applied to Fermi-LAT sky maps via the \texttt{map2patch} algorithm.
The network is trained on $9 \times 10^5$ synthetic maps with a heteroscedastic Gaussian NLL cost function, so that it outputs both the reconstructed source-count distribution and its associated aleatoric uncertainties.
Concrete dropout is applied before each convolutional layer, providing self-learned regularization and enabling the estimation of epistemic uncertainties through Monte Carlo dropout at inference time.
As discussed in Section~\ref{sec:3.1.4}, the Bayesian uncertainties produced by this architecture are cross-validated against an independent frequentist bias estimation, with both approaches yielding compatible results.
The full architectural details and training procedure are deferred to Chapter~6.

new:
\paragraph{Application preview.}

In Chapter~\ref{ch:6}, a CNN is applied to gamma-ray sky maps using the heteroscedastic loss and Monte Carlo dropout framework described above, producing both the reconstructed source-count distribution and its associated aleatoric and epistemic uncertainties.
The uncertainty estimates are cross-validated against an independent frequentist analysis (Section~\ref{sec:3.1.4}).
```

- [ ] **Step 8: Lines 97–99 — Remove Paper~N + self-citation from KDE paragraph**

```latex
old:
In Paper~4, we determine the optimal bandwidth through 5-fold cross-validation repeated 20 times, selecting the value that maximizes the model likelihood on held-out data \cite{Amerio:2025sub}.
Separate KDE models are computed independently for each source class (Galactic and extragalactic), yielding the class-conditional densities $p_\mathrm{assoc}(\mathbf{x}|k)$ that form the building blocks of the mixture model described below.

new:
The optimal bandwidth is determined through cross-validation, selecting the value that maximizes the model likelihood on held-out data.
Separate KDE models are computed independently for each source class (Galactic and extragalactic), yielding the class-conditional densities $p_\mathrm{assoc}(\mathbf{x}|k)$ that form the building blocks of the mixture model described below.
```

- [ ] **Step 9: Line 109–110 — Fix z_{ik} notation (Issue 11)**

```latex
old: "computing the posterior class responsibilities $\gamma(z_{ik}) = p(k | \mathbf{x}_i)$ for each data point (the E-step), and updating the model parameters to maximize the expected log-likelihood under those responsibilities (the M-step).
For the mixing weights, the M-step admits a closed-form solution: $\pi_k^\mathrm{new} = N^{-1}\sum_i \gamma(z_{ik})$"

new: "computing the posterior class responsibilities $\gamma_{ik} = p(k | \mathbf{x}_i)$ for each data point (the E-step), and updating the model parameters to maximize the expected log-likelihood under those responsibilities (the M-step).
For the mixing weights, the M-step admits a closed-form solution: $\pi_k^\mathrm{new} = N^{-1}\sum_i \gamma_{ik}$"
```

- [ ] **Step 10: Lines 112–122 — Rewrite Sec 3.3.3 application preview, remove paper-specific equation, fix Chapter~9 → Chapter~\ref{ch:5}**

```latex
old:
\paragraph{Application preview.}

In Paper~4, we construct a generative mixture model that extends this framework to search for dark matter subhalos among the unassociated Fermi-LAT sources \cite{Amerio:2025sub}.
The model of the unassociated source distribution takes the form
\begin{equation}
	\tilde{p}_\mathrm{unas}(\mathbf{x}) = \left(\sum_{k=1}^{K} \pi_k\, p_\mathrm{assoc}(\mathbf{x}|k)\right) \tilde{C}(\mathbf{x};\boldsymbol{\theta}_\mathrm{cov}) + \pi_\mathrm{DM}(\boldsymbol{\theta}_\mathrm{DM})\, p_\mathrm{DM}(\mathbf{x};\boldsymbol{\theta}_\mathrm{DM}),
	\label{eq:mixture_unas}
\end{equation}
where the first term describes the astrophysical background (with a covariate shift modulation $\tilde{C}$ that accounts for observational biases between associated and unassociated sources; see Section~\ref{sec:3.4}), and the second term represents the dark matter contribution derived from $N$-body simulations.
The class prevalences $\pi_k$ and covariate shift parameters are determined by maximizing the product likelihood over all unassociated sources via the EM algorithm, following the approach of Saerens et al.~\cite{10.1162/089976602753284446_Saerens} for correcting prior probability shifts.
This quantification learning framework---which infers population-level properties rather than individual source labels---is developed in full detail in Chapter~9.

new:
\paragraph{Application preview.}

In Chapter~\ref{ch:5}, this framework is extended to search for dark matter subhalos among the unassociated Fermi-LAT sources.
The mixture model combines astrophysical class-conditional densities with a covariate shift correction (Section~\ref{sec:3.4}) and a possible dark matter component, with class prevalences determined via the EM algorithm following the approach of Saerens et al.~\cite{10.1162/089976602753284446_Saerens}.
```

- [ ] **Step 11: Verify no remaining self-citations or "Paper~N" in this file**

---

### Task 4: Fix `3.4_domain_shift.tex`

**File:** `chapter_03/sections/3.4_domain_shift.tex`

**Issues addressed:** 5 (self-citations), 6 (Paper~N)

- [ ] **Step 1: Line 34 — Replace self-citation**

```
old: "differ measurably between associated and unassociated sources \cite{Amerio:2025fhz}."
new: "differ measurably between associated and unassociated sources (see Chapter~\ref{ch:5})."
```

- [ ] **Step 2: Line 36 — Replace self-citation**

```
old: "unreliable upper bounds on the annihilation cross-section \cite{Amerio:2025fhz}."
new: "unreliable upper bounds on the annihilation cross-section."
```

- [ ] **Step 3: Lines 41–42 — Fix figure caption**

```latex
old:
\caption{Distributions of the spectral index $\alpha$ and spectral curvature $\beta$ for associated (blue) and unassociated (orange) Fermi-LAT sources, from \cite{Amerio:2025fhz}, Figure~1.
		The visible mismatch between the two populations illustrates the dataset shift discussed in the text.
	}

new:
\caption{Distributions of the spectral index $\alpha$ and spectral curvature $\beta$ for associated (blue) and unassociated (orange) Fermi-LAT sources from the 4FGL-DR4 catalog.
		The visible mismatch between the two populations illustrates the dataset shift discussed in the text.
		See Chapter~\ref{ch:5} for the full analysis.
	}
```

- [ ] **Step 4: Line 64 — Replace self-citation with general reference**

```
old: "characterizes the covariate shift \cite{Amerio:2025fhz}."
new: "characterizes the covariate shift \cite{MorenoTorres2012AUV}."
```

- [ ] **Step 5: Line 73 — Replace self-citation**

The sigmoid modulation equation is introduced here as general methodology. Attribute to the thesis chapter where it was developed:

```
old: "the midpoint of the modulation along feature dimension $d$ \cite{Amerio:2025fhz}."
new: "the midpoint of the modulation along feature dimension $d$ (see Chapter~\ref{ch:5} for the derivation and application)."
```

- [ ] **Step 6: Line 86 — Replace self-citation**

```
old: "lie near the Galactic plane \cite{Amerio:2025fhz}."
new: "lie near the Galactic plane \cite{2023RASTI...2..735M}."
```

(This fact is already supported by the Malyshev 2023 reference cited earlier in the section.)

- [ ] **Step 7: Line 101 — Replace Paper~4 + self-citation**

```
old: "In Paper~4, we construct the first such statistical model for Fermi-LAT sources \cite{Amerio:2025fhz}."
new: "In Chapter~\ref{ch:5}, we construct the first such statistical model for Fermi-LAT sources."
```

- [ ] **Step 8: Verify no remaining self-citations or "Paper~N" in this file**

---

### Task 5: Fix `3.5_cross_correlations.tex`

**File:** `chapter_03/sections/3.5_cross_correlations.tex`

**Issues addressed:** 3 (Chapter~10 → Chapter~8), 5 (self-citations), 8 (TODO removal)

- [ ] **Step 1: Line 8 — Remove TODO comment (Issue 8)**

```
old: "% TODO: review in light of the xcorr chapter. are there some overlaps? maybe we can bring or bridge the xcorr formalism appendix here, and remove that appendix. "
new: (delete line entirely)
```

- [ ] **Step 2: Line 20 — Fix Chapter~10 → Chapter~\ref{ch:8} (Issue 3)**

```
old: "is deferred to Chapter~10."
new: "is deferred to Chapter~\ref{ch:8}."
```

- [ ] **Step 3: Lines 67–68 — Remove Pinetti self-citation from multi-cites**

The formalism here comes from Fornengo:2013rga. Remove the Pinetti key where it co-occurs with the original source:

```
old: "\cite{Pinetti:2025hgd, Fornengo:2013rga}"  (3 occurrences: lines 67, 68, 78)
new: "\cite{Fornengo:2013rga}"
```

- [ ] **Step 4: Line 90 — Fix Chapter~10 → Chapter~\ref{ch:8} (Issue 3)**

```
old: "is deferred to Chapter~10, where the full cross-correlation analysis is presented."
new: "is deferred to Chapter~\ref{ch:8}, where the full cross-correlation analysis is presented."
```

- [ ] **Step 5: Lines 98, 103, 112 — Replace Pinetti self-citations with original sources**

The SNR and variance formulas are standard. Replace `\cite{Pinetti:2025hgd}` with the original sources:

```
Line 98: old: "\cite{Pinetti:2025hgd}" → new: "\cite{Fornengo:2013rga}"
Line 103: old: "\cite{Pinetti:2025hgd}" → new: "\cite{Fornengo:2013rga}"
Line 112: old: "\cite{Pinetti:2025hgd}" → new: "\cite{Fornengo:2013rga}"
```

- [ ] **Step 6: Line 109 — Replace Pinetti self-citation**

```
old: "\cite{Pinetti:2025hgd}."
new: "(Chapter~\ref{ch:8})."
```

- [ ] **Step 7: Line 121 — Replace Pinetti in multi-cite**

```
old: "\cite{Pinetti:2025hgd, Camera:2012cj}."
new: "\cite{Fornengo:2013rga, Camera:2012cj}."
```

- [ ] **Step 8: Line 123 — Replace Pinetti self-citation**

```
old: "\cite{Pinetti:2025hgd}:"
new: "\cite{Fornengo:2013rga}:"
```

- [ ] **Step 9: Line 130 — Replace Pinetti self-citation in application preview**

```
old: "by cross-correlating the predicted gamma-ray emission with the 2MASS galaxy catalog \cite{Pinetti:2025hgd}."
new: "by cross-correlating the predicted gamma-ray emission with the 2MASS galaxy catalog."
```

- [ ] **Step 10: Verify no remaining self-citations or "Paper~N" in this file**

---

### Task 6: Fix `3.6_summary.tex`

**File:** `chapter_03/sections/3.6_summary.tex`

**Issues addressed:** 5 (self-citations), 6 (Paper~N)

- [ ] **Step 1: Line 10 — Replace "Papers~3, 4, and~5"**

```
old: "tools that underpin the analyses in Papers~3, 4, and~5."
new: "tools that underpin the analyses in Chapters~\ref{ch:4}, \ref{ch:5}, and~\ref{ch:8}."
```

- [ ] **Step 2: Line 11 — Replace "Paper~1"**

```
old: "as exploited in Paper~1."
new: "as applied in Chapter~\ref{ch:6}."
```

- [ ] **Step 3: Line 19 — Replace "Paper~4"**

```
old: "that forms the basis of the subhalo search in Paper~4."
new: "that forms the basis of the subhalo search in Chapter~\ref{ch:5}."
```

- [ ] **Step 4: Verify no remaining self-citations or "Paper~N" in this file**

---

### Task 7: Bibliography deduplication (Issue 4)

**File:** `bibliography.bib`

**Note:** This task removes duplicate bib entries for the same papers. After Tasks 1–6, Chapter 3 no longer cites any of these keys, but other chapters may still reference them. A thesis-wide search is needed.

- [ ] **Step 1: Check thesis-wide usage of duplicate keys**

Search the entire repo for `\cite{Amerio:2025sub}` and `\cite{Pinetti:2025}` (the duplicates). If they appear in other chapters, those citations need updating too.

- [ ] **Step 2: Standardize on canonical keys**

The canonical InspireHEP keys are `Amerio:2025fhz` and `Pinetti:2025hgd`. Replace all `Amerio:2025sub` → `Amerio:2025fhz` and `Pinetti:2025` → `Pinetti:2025hgd` throughout the thesis.

- [ ] **Step 3: Remove duplicate bib entries**

Delete the `@article{Amerio:2025sub,...}` block (lines ~7660–7668) and the `@article{Pinetti:2025,...}` block (lines ~7670–7679) from `bibliography.bib`.

- [ ] **Step 4: Compile and verify no "undefined citation" warnings**

---

### Task 8: Final verification

- [ ] **Step 1: Search Chapter 3 for any remaining issues**

Run these searches across `chapter_03/sections/*.tex`:
- `Paper~` — should return zero matches
- `Amerio:` — should return zero matches
- `Pinetti:` — should return zero matches
- `Chapter~[0-9]` (hardcoded chapter numbers) — should return zero matches (all should use `\ref`)

- [ ] **Step 2: Compile the thesis**

Run `pdflatex main && bibtex main && pdflatex main && pdflatex main` and check for:
- No "undefined reference" warnings from Chapter 3
- No "undefined citation" warnings
- No duplicate bibliography entries for the same paper

- [ ] **Step 3: Commit**

```
git add chapter_03/sections/*.tex bibliography.bib
git commit -m "refactor(ch3): replace self-citations with cross-references, trim application previews

- Replace all Paper~N labels with chapter cross-references
- Replace ~30 self-citations (Amerio, Pinetti) with \ref{} to thesis chapters
- Trim application previews to conceptual level, defer implementation details
- Fix broken \ref{sec:3.3.1}, wrong chapter numbers (Ch 9→5, Ch 10→8)
- Deduplicate bibliography entries for Papers 4 and 5
- Simplify EM notation (z_{ik} → gamma_{ik})
- Remove TODO comment in Sec 3.5

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```
