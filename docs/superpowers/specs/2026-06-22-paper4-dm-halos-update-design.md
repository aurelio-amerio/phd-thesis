# Updating Chapter 5 (Paper 4, DM subhalos) to the revised paper version

**Date:** 2026-06-22
**Status:** Approved for planning

## Problem

The integrated Chapter 5 paper lives at `chapter_05/sections/paper_dm_halos/`, split into a
`paper_4.tex` wrapper plus eight `sections/*.tex` files, using thesis conventions
(`\chapter`, abstract-as-intro paragraph, `\input` list, `subappendices`, `\Fermi` macro,
central `bibliography.bib`).

A revised version of the same paper (currently under referee review) has arrived as a single
standalone document at `chapter_05/sections/paper_dm_halos_new/main.tex`, with its own
`DM_halos.bib`, `JHEP.bst`, `jcappub.sty`, and `img/`.

We must propagate the revisions into the integrated thesis version.

## Approach

**Reshape the new paper into the existing thesis file layout**, rather than surgically porting
diffs into the old files. The new content is authoritative; the old structure (file split,
wrapper, thesis dialect) is preserved. For each of the eight section files, replace the body
with the corresponding `main.tex` section, then adapt dialect. The `\input` structure and
`paper_4.tex` shell are unchanged, so the build cannot break structurally.

### Section ↔ main.tex line mapping

| Old file | main.tex range | Change magnitude (word-tokens) |
|---|---|---|
| `introduction.tex` | 131–224 | minor (~35) |
| `statistical_analysis.tex` | 225–431 | moderate (~270) |
| `dm_subhalos_model.tex` | 432–571 | moderate (~229) |
| `mixture_model_and_limits.tex` | 572–1007 | **major rewrite (~2994, content ~doubled)** |
| `conclusions.tex` | 1008–1056 | moderate (~181) |
| `appendix_simulation.tex` | 1057–1168 | minor (~64) |
| `appendix_em_algorithm.tex` | 1169–1233 | moderate (~124) |
| `appendix_consistency_checks.tex` | 1236–1456 | moderate (~152) |

(Line ranges are from the current `main.tex`; re-verify section boundaries during implementation.)

## Integration surface to preserve

- **No `\aure{}` notes** exist in the old section files — nothing WIP to protect.
- The paper is self-contained: no cross-chapter `\ref`s out. **Exactly one** external reference
  *into* it: `chapter_06/sections/6.1_limits_individual.tex` cites `\ref{sec:halos:results}`.
  **That label must survive** the reshape.
- Old files use thesis-style labels (`sec:halos:*`); preserve these names where new sections map
  to old ones. New labels introduced by the mixture-model rewrite get thesis-consistent
  `sec:halos:*` names.
- Old files use the `\Fermi`/`\fermi` macros (27× `\Fermi`); convert the new paper's plain
  `Fermi`/`{\it Fermi}` text to these macros.
- Spelling: keep whatever the new paper uses; do not normalize (thesis convention for
  paper-integrated sections).

## Bibliography — remap only, no new entries

Verified by cross-checking arXiv numbers / DOIs / titles against `bibliography.bib`. Of the 86
distinct cite keys in the new paper: **72 already match verbatim**; **14 exist under a different
key** and are pure remaps; **0 are genuinely new**. `bibliography.bib` is **never modified**.

Remap table (rewrite these keys in the ported text):

| New paper key | → Thesis key | matched by |
|---|---|---|
| `2008Natur.454..735D` | `Diemand:2008in` | arXiv 0805.1244 |
| `2009PhRvD..79a5014A` | `ArkaniHamed:2008qn` | arXiv 0810.0713 |
| `2012ApJ...753...83A` | `Fermi-LAT:2011sla` | arXiv 1108.1202 |
| `2016PhR...636....1C` | `Charles:2016pgz` | arXiv 1605.02016 |
| `2019Galax...7...81Z` | `Zavala:2019gpq` | arXiv 1907.11775 |
| `2020ApJS..247...33A` | `Fermi-LAT:2019yla` | arXiv 1902.10045 |
| `2022A&A...660A..87B` | `Bhat:2022` | arXiv 2102.07642 |
| `2022ApJS..260...53A` | `Fermi-LAT:2022byn` | arXiv 2201.11184 |
| `2023arXiv230712546B` | `Ballet:2023qzs` | arXiv 2307.12546 |
| `2024JCAP...03..035A` | `Arina:2023eic` | arXiv 2312.01153 |
| `Fornasa:2015qua` | `DGRB-review` | arXiv 1502.02866 |
| `Hooper:2024avz` | `Hooper:2024` | title |
| `Steigman_2012` | `Steigman:2012nb` | DOI |
| `hastie2009elements` | `Hastie:2009` | title |

## Figures

Top-level `img/` filenames match between old and new. Byte-compare actual files; copy over any
whose content changed (the mixture-model rewrite likely updated/added limit plots). Report any
new figure files referenced by the new text that are absent from the old `img/`.

## Abstract / wrapper

Refresh the abstract-as-intro paragraph in `paper_4.tex` from the new `main.tex` abstract **iff
it changed**. Keep `\chapter`, `\label{ch:dm_halos}`, the `\input` list, and `subappendices`.

## Verification

1. Every cite key in the reshaped sections resolves in `bibliography.bib` (no remap key remains).
2. Every `\ref`/`\label` resolves; `sec:halos:results` still exists.
3. `latexmk` build of `main.tex` compiles the chapter without new errors.

## Out of scope

- Modifying `bibliography.bib`.
- Refactoring unrelated chapters.
- Deleting `paper_dm_halos_new/` (kept until the update is verified).
