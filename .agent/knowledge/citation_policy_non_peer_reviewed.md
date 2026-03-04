---
title: "Citation Policy for Non-Peer-Reviewed Sources"
date: 2026-03-04
source_skill: manual
chapter: all
tags: [citation-policy, pinetti, thesis, peer-review, references]
---

## Summary

Non-peer-reviewed sources (PhD theses, lecture notes, preprints) can be used as references but must NOT be the sole citation for a claim. Always pair with peer-reviewed original papers.

## Policy

1. **Published books (e.g., Hooper 2024, Dodelson):** Fully reliable standalone sources — they undergo editorial peer review. Can be cited as sole reference for standard results and derivations.
2. **PhD theses (e.g., Pinetti 2021):** Reliable for structural guidance, derivation style, and identifying relevant papers. Cite for context, but always also cite the original peer-reviewed paper for the specific result. Must NOT be the sole citation for a claim.
3. **Large preprints (e.g., Cirelli et al. 2024):** Comprehensive reviews are generally acceptable even if not formally published, especially when widely cited. Still prefer adding the original paper citation for specific results.

## Citation Pattern

**Correct:**
```latex
The J-factor formalism follows the standard derivation~\cite{Bergstrom:1997fj}
(see also~\cite{Pinetti:2021jjs} for a detailed pedagogical treatment).
```

**Incorrect (sole non-peer-reviewed citation):**
```latex
The J-factor is defined as~\cite{Pinetti:2021jjs}.
```

## Context

This policy applies to all chapters. The Pinetti thesis is a ✅ Direct Source in NotebookLM and provides excellent structural guidance, but its content should always be backed by peer-reviewed references when making specific claims. Published textbooks (Hooper, Dodelson) do not have this limitation.
