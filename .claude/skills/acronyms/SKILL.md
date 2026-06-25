---
name: acronyms
description: Use when the user runs /acronyms, or asks to find, define, or mark up acronyms in a LaTeX thesis .tex file — e.g. converting literal acronyms like CMB, WIMP, dSph, NFW into glossaries macros and adding any missing definitions to acronyms.tex.
---

# Acronyms — detect, define, mark up

## Overview

The thesis uses the `glossaries` package. Every acronym is defined once in
`acronyms.tex`; in the prose it is written as a macro that auto-expands on first
use and abbreviates thereafter. This skill scans one `.tex` file, proposes
definitions for any missing acronyms, and replaces literal occurrences with the
correct macro — **presenting a plan and waiting for approval before editing**.

## How the machinery works (already set up in `acronyms.tex`)

```latex
\RequirePackage{xspace}
\setacronymstyle{long-short}                       % first use "long (SHORT)", later "SHORT"
\newcommand{\newacro}[4][]{%                        % like \newacronym, plus a \SHORT command
  \newacronym[#1]{#2}{#3}{#4}%
  \expandafter\newcommand\csname #3\endcsname{\gls{#2}\xspace}%
}
```

- `\newacro[opts]{KEY_}{SHORT}{long form}` defines the acronym **and** a `\SHORT`
  command equal to `\gls{KEY_}\xspace`. Keys carry a trailing underscore (`CMB_`).
- **Convention: every entry in `acronyms.tex` uses `\newacro`**, so *every* acronym
  has a working `\SHORT` command (`\CMB`, `\WIMP`, `\UV`, `\ICS`, `\AGN`, …) in
  addition to the `\gls{KEY_}` forms. Always define new acronyms with `\newacro`,
  never raw `\newacronym` — a raw `\newacronym` entry has **no** `\SHORT` macro, so
  `\UV` would throw "Undefined control sequence". If you ever find a stray
  `\newacronym`, upgrade its line to `\newacro` (a one-word edit).

### Which markup form to use

| Situation | Write | Renders (first use / later) |
|---|---|---|
| mid-sentence, singular | `\SHORT` (≡ `\gls{KEY_}`) | cosmic microwave background (CMB) / CMB |
| **sentence start** | `\Gls{KEY_}` | Cosmic microwave background (CMB) / CMB |
| **plural** | `\glspl{KEY_}` | dwarf spheroidal galaxies (dSphs) / dSphs |
| sentence start + plural | `\Glspl{KEY_}` | Dwarf spheroidal galaxies (dSphs) / dSphs |

`\xspace` (in `\SHORT`) preserves a following space **and** correctly suppresses
it before `. , : ; ! ? ) ' - /` — so `\CMB.`, `\WIMP--nucleon`, `\UGRB's`,
`\WIMP/c` all render correctly. Never write `\CMB{}` or hand-add spacing.
The `\gls/\Gls/\glspl/\Glspl{KEY_}` forms take a braced argument, so the space
after `}` is always safe.

## Determining the first-use (expansion) site — do this carefully

The "long (SHORT)" expansion fires at the **document-first** `\gls` for a key, in
source order. Getting this right is the step most likely to go wrong:

1. **Already used in an earlier chapter?** Grep the other section/chapter files
   (e.g. `grep -rn '\\gls{KEY_}\|\\SHORT\b' chapter_0*/`) for an existing use. If
   the key is already used earlier in the document, **no** occurrence in this file
   expands — just convert every occurrence to the short form; force no expansion.
2. **New to the document?** Find the **earliest occurrence in source order within
   scope** — this is often *not* the line with the human-written `Long Form (ABBR)`
   parenthetical. That earliest occurrence carries the expansion form; then strip
   the now-redundant manual "(SHORT)" at the later introduction. **Also grep
   outside the current file:** a new acronym's true first mention may live in an
   earlier-source-order file (e.g. defining GCE here when "Galactic Center excess"
   first appears in §1.2). If so, the expansion belongs in that earlier file —
   convert (or at least flag) that occurrence in the plan and force short forms
   here; never let the expansion silently land on a later file because the earlier
   one was left literal.
3. **Prefer running prose for the expansion.** If the earliest occurrence sits in
   a bold lead-in label (`\textbf{...}`) or a float caption, expand at the first
   **running-prose** occurrence instead — an expansion firing inside a heading or
   caption reads badly.

## Procedure

1. **Target file.** Use the path argument; otherwise the file the user has open in
   the IDE. State which file. Read it and read `acronyms.tex` (the registry).

2. **Detect occurrences.**
   - *Already-defined:* for each registry SHORT, find literal occurrences of that
     SHORT and of its long form in the prose. Every entry is `\newacro`, so the
     `\SHORT` macro is available for all of them.
   - *New candidates:* find `Long Form (ABBR)` introductions and repeated
     ALL-CAPS / mixed-case tokens (`NFW`, `dSph`, `mAGN`, `ResNet`) not in the
     registry.
   - *Exclude:* math (`$...$`, `\[...\]`, `equation`/`align`), `\text{}`/`\textit{}`
     wrappers, and the arguments of `\cite`, `\ref`/`\cref`, `\label`,
     `\includegraphics`, `\input`; units (GeV, TeV, K, Mpc, kpc); `$\Lambda$CDM`;
     roman numerals; surnames (Einasto, Burkert); one-off object/survey/instrument
     names (M31, 1E 0657-558, SDSS, SPARC, Planck) unless the user asks.

3. **Judgment — do not over-convert.**
   - Leave terms the thesis deliberately spells out everywhere, above all **"dark
     matter"/DM** — macro-izing it would print "dark matter (DM)" against house
     style. Flag such terms instead of converting.
   - **Earn the abbreviation:** define a *new* acronym only when its short form is
     genuinely reused — it must occur ≥2× in scope (a written-out `Long Form (ABBR)`
     intro counts as just *one* occurrence, so it needs at least one further use).
     A single mention, even with an explicit `(ABBR)`, stays spelled out (e.g. ISRF,
     gNFW, UV each used once).
   - **Overlapping entries:** if more than one registry key could match (e.g.
     `IC_` "inverse Compton" vs `ICS_` "inverse Compton scattering"), pick the
     longest / most-specific long-form match; if unsure, flag it.
   - **Case/format mismatch:** if the registry long form's casing or formatting
     differs from the prose (e.g. a title-cased registry entry vs lowercase prose,
     or a dropped `\textit{}`), flag for the author — `glossaries` renders the
     registry's casing — rather than silently retitling. Resolution:
     if it is a common noun, prefer lowercasing the registry entry (it then renders
     correctly everywhere); if genuinely title-case, keep the prose consistent or
     skip that conversion. Use **one markup form per key consistently** within a
     file — never mix `\gls{KEY_}` and a bare `\SHORT` for the same key.

4. **Propose new entries.** For each new acronym draft
   `\newacro{KEY_}{SHORT}{long form}` (key = SHORT + `_`; long form lowercase
   unless a proper noun; add `[longplural={...}]` for plural long forms). Always
   use `\newacro`, never raw `\newacronym`. Group new entries under a chapter
   comment, matching the file's style.

5. **Build the plan**, listing: (a) new `\newacro` lines for `acronyms.tex`;
   (b) every replacement as `line — "before" → after`, with the chosen markup form,
   and marking the single first-use expansion per key (per the first-use rules
   above).

6. **Present the plan and STOP.** Ask the user to approve before any edit.

7. **On approval, apply.** Edit `acronyms.tex` (new entries + upgrades), then the
   target file, respecting source order. Never hand-edit `.bbl` or invent bib
   entries.

8. **Verify.** Compile — an isolated test doc with the new entries, or
   `latexmk -pdf -interaction=nonstopmode main.tex`. Spot-check: no gobbled-space
   artifacts ("CMBphotons"), no macro inside math/labels, expansion fires once at
   the right place. Report changes.

## Common mistakes (seen in real use)

| Symptom | Cause / fix |
|---|---|
| `Undefined control sequence \UV` | Entry was added with raw `\newacronym` (no `\SHORT`). All entries must use `\newacro`; upgrade the line, or use `\gls{UV_}`. |
| `CMBphotons`, `(SZ)effect` | Space gobbled after a bare command lacking `\xspace`. Fix the wrapper; never use `\CMB{}`. |
| Sentence starts lowercase "cosmic microwave…" | Used `\SHORT`/`\gls` at a sentence start. Use `\Gls{KEY_}`. |
| `\CMBs` undefined | Plurals use `\glspl{KEY_}` / `\Glspl{KEY_}`. |
| Expansion fires at the wrong line, or twice | First-use site wrong. It's the earliest source-order occurrence (not the `(ABBR)` intro), and only if not already used in an earlier chapter. |
| Expansion appears inside a `\textbf{}` heading or caption | Site the expansion in the first running-prose occurrence instead. |
| "dark matter (DM)" appears | Over-conversion. Leave deliberately-spelled-out terms in full. |
| Acronym retitled / `\textit` dropped | Registry casing differs from prose. Flag, don't silently change. |
| Macro injected into an equation or `\ref{}` | Detection ignored math/label exclusions. Re-check step 2. |
