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
| `/referee X.Y` or `/referee X` | Critical review of a section or full chapter |

The `/draft` workflow runs a three-layer writing pipeline: `scientific-writing` → `humanizer` → personal style adaptation. It automatically performs a review pass at the end.

**Review in fresh context.** Always dispatch review workflows (humanizer, scientific-writing, `/referee`) in independent subagents with fresh context — never inline in the drafting conversation. A fresh agent reads the prose cold, avoiding the familiarity bias that makes the drafter blind to issues.

Skills live in `.agent/skills/` (antigravity) and `.claude/skills/` (Claude Code), invoked via the Skill tool. Slash commands are defined in `.claude/commands/`.

## Key Macros

- `\aure{...}` — orange highlighted author comment/annotation
- `\be` / `\ee` — begin/end equation (shorthand)
- `\ben` / `\een` — begin/end enumerate (paper 4 macro; NOT an equation environment — use `\[...\]` for unnumbered displays)
- `\dnds`, `\dNdS` — source-count distribution notation
- `\Fermi`, `\fermi` — Fermi-LAT references
- `\gsim`, `\lsim` — approximate ≳ ≲ comparisons

## Writing Conventions

- Physics drives the narrative — ML/statistical methods are introduced in the chapter where they first solve a problem, not in a standalone toolbox chapter.
- Each chapter starts from a physics problem and motivates its methodological contribution.
- `chapter_outline.md` per chapter is the authoritative section-level specification.
- `outline.md` is the master thesis-level narrative document.
- The `.revisions/` directory contains revision directives from supervisor feedback.
- **Never create BibTeX entries manually.** Only add bib entries fetched from InspireHEP or arXiv. For papers not found on these platforms, list them in an MD artifact (authors, year, title, journal) so the author can add them via Google Scholar. Use `\aure{}` placeholders in the LaTeX for the missing cite keys.
- **Figures from external papers.** Always download figures from the original arXiv TeX source using `python arxiv_downloader.py <arxiv_id>` to extract publication-quality vector PDFs. InspireHEP figure API images are low-resolution rasters — acceptable as temporary placeholders during drafting, but must be replaced with originals from the arXiv source before the final version. When adding a figure placeholder, mark it with `\aure{replace with original PDF from arXiv source: <arxiv_id>}`.

## Style and Tone

The voice is consistent across hand-written and paper-integrated chapters. Match it when drafting new prose. (Inferred from the compiled `main.pdf` as of May 2026 — sample Ch. 2, 3, 4, 6.)

**Voice and person.** First-person plural ("we", "our analysis"). The author takes positions: names competing camps, summarizes community consensus, calls open questions open. Avoid effacing constructs ("the present author") and false neutrality on contested issues.

**Sentence and paragraph rhythm.**
- Long, multi-clause sentences. Em dashes for parenthetical inserts; colons and semicolons to chain related ideas.
- Paragraphs are **long** (typically 6–12 sentences) and self-contained: topic sentence → development → implication/transition.
- **No bullet points in narrative prose.** Numbered enumerations only when comparing alternatives or stating discrete hypotheses (cf. the five MSP-scaling hypotheses in §4.5.2).

**Section openings.** Each chapter and major section opens with (1) a broad-scene paragraph ("The gamma-ray sky is rich and complex..."), (2) why standard methods fall short, and (3) what this chapter contributes — with an explicit roadmap: *"Section 2.1 reviews..., Section 2.2 surveys..., Finally, Section 2.3 describes..."*

**Bold/italic lead-ins.** Subsections use bold or italic paragraph lead-ins for scannable structure: `\textbf{Application preview.}`, `\textbf{Credible intervals versus confidence intervals.}`, `\emph{Neglect of spatial correlations.}` Italicize *technical terms on first appearance* (e.g. *simulation-based inference*, *pion bump*, *aleatoric*/*epistemic*).

**Application-preview pattern.** Methodological subsections close with a bolded `\textbf{Application preview.}` paragraph naming the chapter where the abstract method is concretely used. This is the main device that ties Chapter 3 to Chapters 5–9.

**Cross-references as connective tissue.** Heavy forward and backward referencing — "as developed in Section 3.2", "(cf. Section 2.2.2)", "we defer the details to Chapter 6". Use these liberally; they make the integrated papers read as one thesis rather than a stapled collection.

**Citations.** JHEP numbered style: `[22]`, `[76, 77]`. In running prose, refer to authors as "Leane and Slatyer", "Buschmann et al."

**Calibrated hedging.** Quantitative when possible ("roughly 17 ± 2%", "of order 10⁵", "approximately"). Avoid vague hedges ("perhaps", "might possibly", "somewhat"). When a question is unsettled, say so plainly: *"remains an open problem"*, *"should be regarded as provisional"*.

**Tense.** Past for results obtained ("we measured", "we detected"). Present for general scientific facts and methodological description ("hadronic emission dominates", "we adopt").

**Recurring connectives.** *Rather than X, ...*; *In practice, ...*; *In the limit of ...*; *Crucially*, *Specifically*, *Notably*; *Taken together, ...* (closes synthesis paragraphs).

**Figures and tables.** Captions are full descriptive sentences, not labels. End with `Credit: ...` when reusing external figures. Reference inline as `Fig. X.Y` / `Table X.Y`.

**Spelling.** US/UK spelling is inconsistent across paper-integrated sections (each paper carried its own convention). Do not normalize globally — follow the surrounding section.

**WIP markers.** `\aure{...}` orange annotations mark in-progress notes, missing citations, "double-check this" reminders. Keep them in drafts; resolve before final submission. Do not silently delete them.
