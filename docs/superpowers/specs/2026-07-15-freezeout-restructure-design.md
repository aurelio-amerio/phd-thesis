# Freeze-Out Section Restructure — Design

**Date:** 2026-07-15
**Target:** `chapter_01/sections/freezout.tex` (§1.2.2, "The Freeze-Out Mechanism")
**Status:** approved design, pending implementation plan

## Problem

The current section introduces concepts out of order:

- The comoving abundance $Y \equiv n_\chi/s$ and the entropy density $s$ are introduced twice — first on the fly inside the figure discussion (before any formalism), then again after the Boltzmann equation ("It is convenient to factor out...").
- The equilibrium number density $n_\mathrm{eq}$ appears in the Boltzmann equation without ever being defined explicitly, so the origin of the $e^{-x}$ falloff in the figure is asserted, not shown.
- The strong-vs-weak annihilator comparison references figure curves before the axes ($x$, $Y$) are defined.
- The old figure (Steigman et al.) plots $M_\chi\, n(x)/n_\mathrm{eq}(x{=}1)$, which relates to $Y$ only up to $g_{*s}(T)$ factors — forcing a hedged "up to a constant proportional to $M_\chi Y$" caption.

## Goal

Reorder the existing content into a linear logical flow, adding only one paragraph and one displayed equation. Replace the Steigman figure with the author's own $Y(x)$ figure so the plot matches the text's notation exactly.

## New paragraph order

1. **Qualitative opening** — unchanged (current opening: chemical equilibrium, expansion vs. annihilation competition, purpose statement).
2. **NEW — equilibrium density.** Short paragraph: as long as chemical equilibrium holds, $n_\chi$ tracks the equilibrium density $n_\mathrm{eq}(T)$ obtained by integrating the thermal (Maxwell–Boltzmann) phase-space distribution. Define $x \equiv M_\chi/T$ here. Displayed equation with the two limits:
   - relativistic ($x \ll 1$): $n_\mathrm{eq} \propto T^3$,
   - non-relativistic ($x \gg 1$): $n_\mathrm{eq} = g_\chi\,(M_\chi T/2\pi)^{3/2}\, e^{-M_\chi/T}$.

   This makes the exponential Boltzmann suppression explicit before the figure uses it.
3. **Boltzmann equation** — current Eq. `eq:boltzmann` paragraph moved up essentially unchanged: term-by-term reading, assumptions footnote, Friedmann/$H \sim T^2/M_\mathrm{Pl}$ remark. $n_\mathrm{eq}$ is now already defined when it appears.
4. **Entropy and comoving abundance — single merged introduction.** Define $s = (2\pi^2/45)\, g_{*s}\, T^3$, comoving entropy conservation, then $Y \equiv n_\chi/s$ and $Y_\mathrm{eq} \equiv n_\mathrm{eq}/s$ as the change of variable that factors out expansion dilution. Merges the two currently duplicated introductions.
5. **Figure + solution behaviour.** Present the figure and merge the two currently split discussions: $Y$ tracks $Y_\mathrm{eq}$ at $x \ll 1$; exponential fall at $x \gtrsim 1$; departure when $\Gamma = n_\chi \langle\sigma v_\mathrm{rel}\rangle$ drops below $H$; plateau at $Y_\infty$; freeze-out completes at $x_\mathrm{fo} \sim 20$–$25$; strong-vs-weak comparison ("the weakest particle wins", $Y_\infty \propto 1/\langle\sigma v\rangle$).
6. **Everything from Eq. `eq:omega_Y` onward — unchanged order:** relic abundance from $Y_\infty$; the $\langle\sigma v\rangle$ terminology subtlety; partial-wave expansion; solution → `eq:relic_general` → `eq:relic_abundance` → thermal cross section → WIMP miracle; `fig:thermal_relic` untouched.

## Figure replacement

- **New figure:** `chapter_01/figures/freezeout.pdf` (author-made in Affinity, source `freezeout.af`, preview `freezeout.png`). Plots comoving abundance vs $x = m/T$: solid "Equilibrium" curve, three dashed freeze-out curves labelled $\langle\sigma v\rangle_\mathrm{weak}$ (top) / unlabelled middle / $\langle\sigma v\rangle_\mathrm{strong}$ (bottom), plateaus spanning $\sim 10^{-9}$–$10^{-15}$.
- **Caption:** rewritten in the text's own $Y(x)$ notation (no conversion caveats). Full descriptive sentences per thesis style. Ends with: `Credit: adapted from Hooper~\cite{Hooper:2009zm}.`
- **Bibliography:** add `Hooper:2009zm` (Dan Hooper, *Particle Dark Matter*, TASI lectures, arXiv:0901.4090) fetched from InspireHEP — entry already retrieved, not yet in `bibliography.bib`.
- **Removal:** the old `\includegraphics{chapter_01/figures/Steigman2012nb_fig1_v2.pdf}` figure block and its conversion-caveat caption go away. The `fig:freezeout_yx` label moves to the new figure so existing cross-references keep working (verify no other file references the label with Steigman-specific wording).
- The no-longer-used Steigman PDF stays on disk (not deleted) unless the author says otherwise.

## Editing conventions

- Moved-but-unchanged text keeps its existing `\blue{}` markers.
- The new $n_\mathrm{eq}$ paragraph, stitching/transition sentences, and the new caption are wrapped in `\blue{}` per revision convention.
- Existing `\aure{}` annotations are preserved.
- No new material beyond: the $n_\mathrm{eq}$ paragraph + displayed equation, stitching sentences, and the new caption.

## Out of scope

- No numerical Boltzmann-solver script (earlier idea, dropped — author supplied the figure).
- No changes to other subsections of Chapter 1.
- No $dY/dx$ form of the Boltzmann equation in the text (considered, not selected).

## Verification

- Section compiles (`pdflatex` via latexmk or a targeted build).
- `fig:freezeout_yx` referenced correctly; no dangling `\ref`/`\cite`.
- Read-through confirms each symbol ($x$, $n_\mathrm{eq}$, $s$, $Y$, $Y_\mathrm{eq}$, $\Gamma$, $H$) is defined before first use.
- Review pass (humanizer / referee) dispatched in a fresh subagent per repo convention.
