---
title: "Probabilistic Cataloging and UGRB Composition"
date: 2026-03-30
source_skill: literature_research
chapter: chapter_07
tags: [probabilistic-catalog, ugrb, ks-test, 1ppdf, pcat]
---

## Summary
The Unresolved Gamma-Ray Background (UGRB) contains sub-threshold point source populations like blazars, mAGNs, star-forming galaxies, and MSPs. Standard Fermi-LAT cataloging (e.g., 4FGL) employs a fixed Test Statistic threshold of TS > 25 (~4σ), which struggles to catalog faint or highly variable sources without introducing severe false-positive background fluctuations. To recover information below this limit, probabilistic methods are used. These include 1-point probability distribution functions (1pPDF) for estimating photon-count statistics, Bayesian frameworks like PCAT that sample posterior catalogs, and frequentist simulated-sky comparisons (e.g., gPCS) that use KS tests to probabilistically identify candidate firing pixels against synthetically driven $dN/dS$ skies.

## Source References
- [Fornasa & Sánchez-Conde (2015)] — arXiv: 1502.02866, bib key: `Fornasa:2015qua`
- [Pinetti Thesis (2021)] — arXiv: 2212.00125, bib key: `Pinetti:2022qnj`
- [Abdollahi et al. (2020)] — arXiv: 1902.10045, bib key: `Fermi-LAT:2019yla`
- [Abdollahi et al. (2022)] — arXiv: 2201.11184, bib key: `Fermi-LAT:2022byn`
- [Bhat & Malyshev (2022)] — arXiv: 2102.07642, bib key: `Bhat:2021sog`
- [Daylan et al. (2017)] — arXiv: 1607.04637, bib key: `Daylan:2016twa`
- [Malyshev & Hogg (2011)] — arXiv: 1104.0010, bib key: `Malyshev:2011zi`
- [Zechlin et al. (2016)] — arXiv: 1512.07190, bib key: `Zechlin:2015wdz`
- [Ackermann et al. (2015)] — arXiv: 1410.3696, bib key: `Fermi-LAT:2014ryh`
- [Amerio et al. (2024)] — arXiv: 2306.16483, bib key: `Amerio:2023dky`

## Context
Compiled during literature research for Chapter 7 to contextualize the transition from calculating sub-threshold flux distributions ($dN/dS$, Chapter 6) to assigning spatial information (probabilistic catalogs). This bridges the conceptual gap between a population statistic and a catalog suitable for cross-correlation studies (Chapter 8).
