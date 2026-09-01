# Acronym Consistency Pass — Design

**Date:** 2026-09-01
**Status:** Approved design, pending implementation plan

## Goal

Make acronym usage consistent across all English thesis prose using the
existing glossaries infrastructure (`acronyms.tex`, `\newacro`, long-short
style), produce a complete inventory of every acronym used, and ensure the
already-wired List of Acronyms in the back matter renders complete and
correct.

## Current state

- `acronyms.tex` defines ~40 acronyms via `\newacro{KEY_}{SHORT}{long form}`,
  each also exposing a `\SHORT` shorthand (e.g. `\CMB` → `\gls{CMB_}`).
- `main.tex` already calls `\makeglossaries` and prints a
  `List of Acronyms` (`\printglossary[type=\acronymtype]`) in the back
  matter. Glossaries prints only entries actually referenced via `\gls`.
- Macro usage is uneven: Chapter 1 (plus `6.3_sbi_cnn.tex` and
  `8.3_ctao.tex`) uses the macros; ~35 other prose files use literal
  acronyms throughout.
- The `/acronyms` skill already implements per-file conversion
  (literal acronym → glossary macro, extending `acronyms.tex` with missing
  definitions).

## Scope

**In scope (English thesis prose):**
- `chapter_01/` … `chapter_08/` section files (`sections/*.tex`)
- `introduction/introduction.tex` (currently not imported by `main.tex`;
  convert it anyway so it is consistent if re-included)
- `conclusion/conclusion.tex`

**Out of scope (never modified):**
- Integrated paper content: all `paper_*` directories and everything
  reached through the paper wrapper files (`4.5_paper.tex` includes,
  `5.6`, `6.5`, `7.4`, `8.4` includes). Wrapper files themselves may be
  touched only for `\glsresetall` placement if needed.
- `frontmatter/abstract_en.tex` (explicitly untouched), `abstract_es.tex`,
  `abstract_vlc.tex`, `resumen/` (non-English).
- Backup/scratch files: `*.bak*`, `*.bk`, `*.old`, `* copy*`.
- `papers/` (standalone paper mirrors).

## Decisions

- **First-use reset: per chapter.** Add `\glsresetall` at the start of each
  chapter wrapper (`chapter_X.tex`) and of the conclusion, so every chapter
  re-expands acronyms on first local use. Papers use literal text, so they
  do not interact with glossaries' first-use tracking.
- **No `\blue{}` marking.** This is a mechanical normalization pass;
  review happens via git diff. One commit per chapter for reviewability.
- **Headings stay literal.** No `\gls` inside `\chapter/\section/\subsection`
  titles (breaks PDF bookmarks, can trigger first use in the TOC). Plain
  short form in headings; running prose uses the macros.
- **Skip zones within files:** comments, `\aure{}` annotations, math mode,
  `\cite`/`\label`/`\ref` keys, verbatim, file paths/URLs.
- **Plural / sentence-start forms:** `\glspl{KEY_}`, `\Gls{KEY_}`,
  `\Glspl{KEY_}` directly, per the convention documented in `acronyms.tex`.
- **New definitions follow existing conventions:** key = `SHORT_`,
  long form lowercase except proper nouns, `longplural` where the plural
  long form is irregular. Definitions added to `acronyms.tex` in one pass
  (Phase 2), grouped by chapter of first appearance.

## Phases

**Phase 1 — Inventory (read-only, parallelizable).**
Scan every in-scope file for acronym usage. Deliverable: an inventory
report (markdown, e.g. `docs/superpowers/specs/2026-09-01-acronym-inventory.md`)
listing every acronym found, per chapter, each flagged as:
- defined in `acronyms.tex` and used via macro,
- defined but used literally (needs conversion),
- undefined (needs a new `\newacro` entry),
- deliberate non-acronym (e.g. experiment proper names that should stay
  literal — flagged for author decision).

**Phase 2 — Extend `acronyms.tex` once.**
Add all missing `\newacro` entries from the inventory. `acronyms.tex` is
frozen after this phase.

**Phase 3 — Per-file conversion (mechanical, parallelizable).**
Run the `/acronyms` skill workflow on each in-scope file. Since
`acronyms.tex` is frozen, files are independent. Mechanical task —
cheaper models permitted per prose-model policy.
One commit per chapter.

**Phase 4 — Reset + verify.**
- Add `\glsresetall` per chapter wrapper and conclusion.
- Full `latexmk` build; confirm zero new warnings/errors from glossaries.
- Visually check the List of Acronyms: complete, correctly sorted,
  long forms correct.
- Spot-check first-use expansions at the start of 2–3 middle chapters.

## Error handling / edge cases

- An acronym whose expansion differs between contexts (e.g. IC vs ICS,
  SNR already defined as supernova remnant vs signal-to-noise ratio):
  flag in the inventory for author decision rather than auto-converting.
- Acronyms appearing only inside skip zones: record in inventory, no edit.
- If a conversion changes rendered text beyond the expected first-use
  expansion, that file's diff is called out explicitly in the phase report.

## Verification

- `latexmk` build succeeds; `.glsdefs`/glossary warnings clean.
- `grep` audit after Phase 3: no remaining literal occurrences of defined
  acronyms in in-scope prose (outside skip zones and headings).
- Git diff per chapter reviewed by author before merge to `main` history
  is considered accepted.
