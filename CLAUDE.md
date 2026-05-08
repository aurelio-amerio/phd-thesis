# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a PhD thesis repository: *Probing the Dark Universe: Machine Learning and Statistical Approaches to Gamma-Ray Dark Matter Searches* by Aurelio Amerio (advisor: Prof. Bryan Zaldivar Montero).

The thesis integrates 6 research papers across 8–9 chapters, following a *decreasing signal strength → increasing methodological sophistication* narrative arc.

## Build

Compiled with `pdflatex` + BibTeX (JHEP style). The main entry point is `main.tex`. Build artifacts (`.aux`, `.bbl`, `.log`, `.synctex.gz`, `main.pdf`) are gitignored. Use `latexmk` or your editor's LaTeX plugin to compile.

## Repository Structure

```
main.tex              # Root document (memoir class + dinostyle.sty)
macros.tex            # Shared macros (\be \ee \dnds \aure{} etc.)
acronyms.tex          # Glossary entries (30+ acronyms)
bibliography.bib      # 542 BibTeX entries, JHEP style
dinostyle.sty         # Custom thesis style package
chapter_0X/           # Chapters 01–08
  chapter_X.tex       # Chapter wrapper (\input{sections/...})
  chapter_outline.md  # Detailed section-by-section outline
  references.md       # Chapter-specific reference notes
  sections/           # Section .tex files
    paper_*/          # Integrated paper subdirectories
    md/               # Markdown drafts (work-in-progress)
  figures/            # Chapter figures
frontmatter/          # Title, copyright, acknowledgements, abstract
introduction/         # Thesis introduction
conclusion/           # Conclusion chapter
papers/               # Standalone paper versions (mirrors chapter-integrated)
```

## Chapter–Paper Mapping

| Chapter | Title | Integrated Paper |
|---------|-------|-----------------|
| 1 | The Dark Matter Problem | — |
| 2 | The Gamma-Ray Sky and Fermi-LAT | — |
| 3 | Statistical Methods for Noise-Dominated Regimes | — |
| 4 | The Galactic Center Excess | Paper 3 (MSP / GCE) |
| 5 | Dark Matter Substructures | Paper 4 (DM subhalos ML) |
| 6 | From Individual Sources to Populations | Paper 1 (dN/dS via SBI) |
| 7 | Probabilistic Cataloging | Paper 2 (gPCS catalog) |
| 8 | Cross-Correlations and Future Prospects | Paper 5 (CTA xcorr) |
| 9 | Generative Models for SBI (optional) | Paper 6 (GenSBI) |

## Agent Workflows (Slash Commands)

These are the primary ways to drive thesis writing. Invoke via Claude Code:

| Command | Effect |
|---------|--------|
| `/chapter N` | Generate detailed chapter outline for chapter N |
| `/draft X.Y` or `/draft X.Y.Z` | Write prose for a section or subsection |
| `/review X.Y` or `/review X` | Critical review of a section or full chapter |

The `/draft` workflow runs a three-layer writing pipeline: `scientific-writing` → `humanizer` → personal style adaptation. It automatically performs a review pass at the end.

Skills live in `.agent/skills/` (antigravity) and `.claude/skills/` (Claude Code), invoked via the Skill tool. Slash commands are defined in `.claude/commands/`.

## Key Macros

- `\aure{...}` — orange highlighted author comment/annotation
- `\be` / `\ee` — begin/end equation (shorthand)
- `\ben` / `\een` — begin/end equation with no number
- `\dnds`, `\dNdS` — source-count distribution notation
- `\Fermi`, `\fermi` — Fermi-LAT references
- `\gsim`, `\lsim` — approximate ≳ ≲ comparisons

## Writing Conventions

- Physics drives the narrative — ML/statistical methods are introduced in the chapter where they first solve a problem, not in a standalone toolbox chapter.
- Each chapter starts from a physics problem and motivates its methodological contribution.
- `chapter_outline.md` per chapter is the authoritative section-level specification.
- `outline.md` is the master thesis-level narrative document.
- The `.revisions/` directory contains revision directives from supervisor feedback.
