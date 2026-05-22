# §1.2 (WIMP Paradigm) — Revision Plan

Structural plan for addressing the 36 review-mode annotations on `chapter_01/sections/1.2_wimp_paradigm.tex`. **This document holds structural decisions and content notes only — no verbatim prose.** Drafting, sentence-level rewording, and stylistic choices (including the specific replacement for flagged phrases like "anchored") are the implementation agent's job.

Status: brainstorming complete. Ready to hand off to writing-plans + implementation.

---

## Guiding philosophy (locked, applies throughout)

- **Clarity, not structure.** Open every paragraph/subsection with the *what and why* (qualitative narrative + physical intuition); equations follow only when the reader has a reason to care. The chapter outline (`chapter_01/chapter_outline.md`) was a first-pass indication, not a prescriptive plan.
- **Describe / present / review, not derive.** This thesis derives in the paper chapters (4–8), not in introductory chapters. Apply globally.
- **Soften the WIMP framing.** WIMPs are not the best or only candidate; their prominence over the past 10–20 years stems from the WIMP miracle, and they are the class this thesis probes with gamma-rays. That is the honest framing.
- **Drop heavy connectives.** Avoid "With the SM excluded, the search turns to new physics" (l.35) and "This testability, combined with the quantitative success..." (l.77).
- **Address all 36 comments.** Coverage audit at the end of this document.

---

## §1.2 intro (lines 4–16)

**Structure:** two paragraphs (setup + roadmap).

**¶1 — setup + softened WIMP framing.** Bullets:
- One-sentence recall of §1.1 conclusion (DM exists, ~5× baryons, non-baryonic) — bridge only, not a re-litigation.
- Note the breadth of the viable parameter space (~90 orders of magnitude in mass; interactions from purely gravitational to just below current sensitivity).
- Introduce WIMPs as one prominent candidate class among many — *not* the best or only one. Their prominence over the past two decades stems from the WIMP miracle. Mention explicitly that axions, sterile neutrinos, and other candidates remain alive.
- State the operational reason for the WIMP focus: this is the class the thesis probes via gamma-ray indirect detection.
- Delete the orphan WIP marker on line 6 (`\aure{stopped here...}`) — no longer relevant.

**¶2 — roadmap.** Bullets:
- §1.2.1: surveys the candidate landscape — main classes (WIMPs, axions, sterile-ν, PBHs, FIMPs) and modifications of the cold collisionless paradigm (warm + self-interacting DM).
- §1.2.2: describes the thermal freeze-out mechanism, the Boltzmann equation, and the thermally-averaged $\langle\sigma v_\mathrm{rel}\rangle$ as the central DM observable. Names $\langle\sigma v\rangle_\mathrm{cosmo} \approx 2.2 \times 10^{-26}$ cm³/s as the canonical benchmark.
- §1.2.3: reviews the theoretical bounds — perturbativity and unitarity from above, Lee-Weinberg from below — defining the GeV–TeV WIMP mass window.
- §1.2.4: surveys the refinements that complicate the mapping from freeze-out cross-section to present-day signal.
- One closing sentence on the thermal-relic cross-section as the primary indirect-detection benchmark throughout the thesis. Implementation note: replace "anchored" (l.16) with a more neutral term.

---

## §1.2.1 — Candidate Landscape

**Structure:** opening figure + ~8 paragraphs (SM-exclusion bridge, WIMPs, Axions, Sterile-ν, PBHs, FIMPs, "Beyond CC paradigm" — SIDM/WDM, closing transition).

**Opening figure.** New: DM mass-landscape schematic recreated from Cirelli's `MDMscale.pdf`. Marker: `\aure{TODO: recreate from arXiv:2406.01705v3 figs/MDMscale.pdf}`.

**¶ on SM exclusion (replaces current ll.27–33).** Bullets:
- Short paragraph. Do NOT re-prove SM exclusion — point to §1.1.
- Bullet refs to make: §1.1.3 (CMB/BBN baryon-density argument); §1.1.1 (Tremaine-Gunn bound for fermionic DM); §1.1 generally (hot DM ruled out by structure formation).
- Conclude: DM must be a new, non-baryonic, cold-or-warm form of matter.
- Add a non-Cirelli citation alongside Cirelli for the hot-DM structure-formation argument (e.g. Bullock & Boylan-Kolchin 2017).

**¶ on WIMPs (cleaned).** Bullets:
- First candidate paragraph but not framed as the implicit winner.
- Keep mention of WIMP miracle; cross-ref §1.2.2 for the quantitative version.
- Remove the broad-statement Cirelli citation (l.41 — "dominant paradigm for over three decades" doesn't need a citation).
- Note operationally: WIMPs are what this thesis probes via gamma-ray indirect detection.

**¶ on Axions (expanded).** Bullets:
- Frame axions as a currently leading DM candidate alongside WIMPs — community attention has grown as the WIMP parameter space gets squeezed by dSph and direct-detection limits.
- Keep: Peccei-Quinn origin, misalignment mechanism, classical-field behavior at large occupation numbers.
- Drop the specific "~26 µeV" misalignment value (l.48 — too narrow).
- Mention the broad axion search range ($10^{-12}$ to $10^7$ eV) as visualized in modern compilations.
- Add Cajohare AxionLimits citation (Zenodo software, manual bib add needed).
- Possibly add a recent axion review (Adams et al. 2023 Snowmass — TBD).

**¶ on Sterile-ν (cleaned).** Bullets:
- Keep the content (keV mass, Dodelson-Widrow + Shi-Fuller mechanisms, X-ray decay line searches).
- Add a non-Cirelli citation (Boyarsky et al. 2019 or Drewes et al. 2017).

**¶ on Sub-GeV / dark photons — DROP.** The dark-photon mention survives only in §1.2.3 (Lee-Weinberg loophole).

**¶ on PBHs (kept ~as-is).** Bullets:
- Keep paragraph approximately verbatim — the asteroid-mass window content is fine.

**¶ on FIMPs (kept ~as-is).** Bullets:
- Keep paragraph — short, makes the freeze-in vs freeze-out distinction.

**NEW ¶ on "Beyond cold collisionless DM — warm and self-interacting DM."** Bullets:
- Open with the small-scale tensions motivating these modifications: cusp/core, diversity of rotation curves, too-big-to-fail.
- WDM = kinematic classification (intermediate free-streaming length); sterile-ν (above) is one realization but the classification is broader.
- SIDM = property of the DM, orthogonal to particle identity. Quote the canonical $\sigma/M$ scales.
- Mention cluster/lensing bounds ($\sigma/M \lesssim 1$ cm²/g from Bullet; $\lesssim 0.1$ cm²/g at cluster scales motivating velocity-dependent SIDM).
- One sentence acknowledging the active hydrodynamical-simulation community (Vogelsberger, Rocha, Peter, Fischer, ETHOS framework).
- Citations: Spergel-Steinhardt 2000, Tulin-Yu 2018, Bullock-Boylan-Kolchin 2017, Adhikari et al. 2022, Kaplinghat-Tulin-Yu 2016.

**Closing transition.** Bullets:
- Drop the connective at ll.75–77.
- Replace with a one-sentence transition into §1.2.2.

---

## §1.2.2 — Thermodynamics / Freeze-out (clarity-first rewrite)

**Structure:** 6 paragraphs, ordered to deliver physical picture before equations.

**¶1 — The story, no equations.** Bullets:
- DM particle in thermal equilibrium with SM plasma in the early universe via $\chi\chi \leftrightarrow$ SM SM reactions.
- Expansion + cooling eventually breaks equilibrium; leftover comoving abundance = the relic.
- Job of the subsection: make this quantitative enough to pin down what kind of particle gives $\Omega_\chi h^2 \approx 0.12$.

**¶2 — The intuition, no equations.** Bullets:
- Stronger annihilation → tracks falling equilibrium longer → decouples later → less abundant today.
- Weaker annihilation → decouples earlier → more abundant today.
- "Weakest particle wins."
- Mass enters only logarithmically. → $\langle\sigma v_\mathrm{rel}\rangle$ is the central observable, not the mass.

**¶3 — Freeze-out picture, with new figure.** Bullets:
- Insert classic $Y(x)$ plot here. Marker: `\aure{TODO: produce Y vs x freeze-out figure with multiple ⟨σv⟩ curves}`.
- Text describes what the figure shows: $Y$ tracks $Y_\mathrm{eq}$ at high $T$; Boltzmann suppression once $T \lesssim M_\chi$; $Y$ peels off when $\Gamma$ falls below $H$ and plateaus.
- State $T_\mathrm{fo} \sim M_\chi/25$ as the operative number for weak-scale DM. No iterative log formula.

**¶4 — Boltzmann equation, as quantification of the picture.** Bullets:
- Write the Boltzmann equation once: $\dot n_\chi + 3 H n_\chi = -\langle\sigma v_\mathrm{rel}\rangle(n_\chi^2 - n_\mathrm{eq}^2)$.
- One sentence per term (Hubble dilution, annihilation depletion, inverse-process creation).
- One sentence on the change of variable $Y \equiv n_\chi/s$ and *why* (entropy conservation).
- **Drop:** the explicit closed-form $n_\mathrm{eq} = g_\chi (M_\chi T/2\pi)^{3/2} e^{-M_\chi/T}$ (Boltzmann suppression mentioned in prose suffices); the rewritten $dY/dx$ equation; the $g_*$ vs $g_{*S}$ digression (or relegate to footnote); the iterative $x_f \approx 25 + \ln(\ldots)$ expansion.

**¶5 — What $\langle\sigma v_\mathrm{rel}\rangle$ actually is — cross-section disambiguation.** Bullets:
- Define $\langle\sigma v_\mathrm{rel}\rangle$ as the thermal average of $\sigma v_\mathrm{rel}$ over the Maxwell-Boltzmann velocity distribution at temperature $T$. Units cm³/s.
- Contrast with direct-detection convention: $\sigma_{\chi N}$ in cm² (or barns), nucleon-recoil scattering, no thermal averaging, different process ($\chi$+SM → $\chi$+SM, not $\chi\chi$ → SM SM).
- Both are called "cross-section" — common stumbling block. Thesis works in cm³/s throughout.
- Note: relevant velocity averaging is cosmological MB at $T \sim M/25$ for freeze-out vs. present-day halo distribution ($v \sim 10^{-3} c$) for ID. Naturally sets up §1.2.4 ($p$-wave, Sommerfeld).

**¶6 — Relic-abundance formula and WIMP miracle, fully elaborated.** Bullets:
- State $\Omega_\chi h^2 / 0.12 \approx (2.2\times 10^{-26}\,\mathrm{cm^3/s}) / \langle\sigma v_\mathrm{rel}\rangle$.
- Inverse relation; mass enters only logarithmically; canonical $\langle\sigma v\rangle_\mathrm{cosmo}$ benchmark. Cite Steigman-Dasgupta-Beacom 2012.
- WIMP miracle, properly explained (fixes l.156):
  - Dimensional analysis: $\langle\sigma v\rangle \sim \alpha^2 / M_\chi^2$ for generic $2\to 2$ annihilation, where $\alpha = g^2/4\pi$.
  - Plug in $\alpha \sim \alpha_\mathrm{weak} \sim 0.03$, demand match to $\langle\sigma v\rangle_\mathrm{cosmo}$, solve for $M_\chi$ → a few hundred GeV to a few TeV.
  - Punchline: the electroweak scale falls out of dimensional analysis at weak-strength coupling, *not* by hand. That's the miracle.

---

## §1.2.3 — Theoretical Bounds

**Structure:** 6 paragraphs.

**¶1 — Lee-Weinberg lower bound.** Bullets:
- Open with the physical statement: SM-weak-mediated annihilation has $\sigma_0 \approx G_F^2 M_\chi^2 / 2\pi$, $s$-wave (velocity-independent — fixes l.168).
- Combined with the relic formula → lighter particles annihilate less efficiently and overclose.
- Lee-Weinberg 1977 got ≳ 2 GeV; modern $g_*$ values give ≳ 3 GeV.
- Add a non-Cirelli companion citation: Bertone-Hooper-Silk 2005, or original Hut 1977 / Vysotsky-Dolgov-Zeldovich 1977 (fixes l.170).

**¶2 — Dark-photon loophole (only surviving dark-photon mention).** Bullets:
- Lee-Weinberg applies specifically to $W$/$Z$ mediation.
- Models with alternative mediators (dark photons, new scalars, hidden-sector states) sit outside this constraint and can be much lighter — sub-GeV to keV.
- Motivates parallel program (SENSEI, DAMIC, etc.).
- Addresses l.176.

**¶3 — Unitarity bound, expanded.** Bullets:
- Frame as fundamental, not technical: unitarity = probability conservation, must hold in any physical theory.
- Briefly explain partial waves: amplitude expanded in orbital-angular-momentum eigenstates; partial-wave cross-section bounded by $\sigma_\ell \leq 4\pi(2\ell+1)/k^2$.
- For nonrelativistic DM annihilation: $k = M_\chi v/2$; $s$-wave bound gives max $\langle\sigma v\rangle \propto 1/M_\chi^2$ — decreases with mass.
- Why this gives an upper mass bound for thermal relics: as $M_\chi$ grows, unitarity ceiling drops below $\langle\sigma v\rangle_\mathrm{cosmo}$ → over-abundance.
- Griest-Kamionkowski 1990: $M_\chi \lesssim 100$ TeV. Above: requires bound states, multi-step processes, or non-thermal production.

**¶4 — Perturbativity (related but weaker).** Bullets:
- Different constraint: dimensionless couplings can't exceed $\mathcal{O}(4\pi)$ before perturbation theory breaks down.
- Caps interaction strength; gives a slightly looser upper mass bound.
- Distinction: perturbativity is a theory-quality constraint (calculability); unitarity is a physics-quality constraint (must hold).
- Addresses l.181.

**¶5 — BBN floor (existing, cleaned).** Bullets:
- Independent lower bound: $M_\chi \gtrsim 3$ MeV from DM freeze-out before BBN.
- Cite Nollett-Steigman 2014.

**¶6 — Closing (bridge-to-§1.2.4, factual CTAO fix).** Bullets:
- State the mass window: $3$ GeV $\lesssim M_\chi \lesssim 100$ TeV for WIMPs annihilating through SM weak interactions.
- $\langle\sigma v\rangle_\mathrm{cosmo}$ as natural indirect-detection benchmark.
- Forward refs: Fermi-LAT reaches benchmark in dSphs up to several tens of GeV in $b\bar b$ (Chapter 4); CTAO projections extend sensitivity into the TeV domain (Chapter 8). **No claim of reaching thermal-σ at 100 TeV.** Addresses l.196, l.198.
- Bridge: bounds assume simplest freeze-out scenario; several effects modify the picture — pivot to §1.2.4.
- Do NOT smuggle in the thesis-wide methodological motivation here — that belongs in §1.4.7.

---

## §1.2.4 — Beyond Standard Freeze-out

**Structure:** 4 paragraphs.

**Sommerfeld + GCE context** (NotebookLM-verified, 2026-05-22): GCE does NOT require Sommerfeld — Daylan et al. 2014 explicit. Standard ~30–50 GeV WIMP at $\langle\sigma v\rangle \approx (1$–$3)\times 10^{-26}$ cm³/s fits cleanly. But Sommerfeld IS essential for heavy electroweak WIMPs (wino ~3 TeV, higgsino ~1.1 TeV, MDM more generally): difference between thermal-relic mass at hundreds of GeV vs. multi-TeV. At halo velocities, Sommerfeld can boost present-day rate by ~200× over freeze-out → rules out pure wino for cuspy halos. Asymmetry must be reflected in the cross-ref.

**¶1 — Velocity-dependent cross-sections (less technical for l.218).** Bullets:
- Open with non-relativistic partial-wave expansion: $\sigma v_\mathrm{rel} \simeq \sigma_0 + \sigma_1 v_\mathrm{rel}^2 + \mathcal{O}(v^4)$.
- $s$-wave: cross-section ~constant from freeze-out ($v\sim 0.3c$) to halo ($v\sim 10^{-3}c$). $\langle\sigma v\rangle_\mathrm{cosmo}$ is meaningful ID benchmark.
- $p$-wave: present-day rate suppressed by $v_\mathrm{rel}^2 \sim 10^{-6}$ → invisible to ID.
- Reword the helicity-suppression sentence: drop "Majorana fermion annihilation into light fermions" jargon; just say selection rules / initial-state structure can cause $s$-wave to vanish in specific models, leaving $p$-wave as the leading term.
- Thesis focuses on $s$-wave channels.

**¶2 — Sommerfeld enhancement (length-preserving, cross-refs richer and honest).** Bullets:
- Physical picture: light mediator ($M_V \ll M_\chi$) → long-range attractive force distorts incoming wave function → annihilation enhanced at low velocity.
- $S \propto 1/v_\mathrm{rel}$ for $v_\mathrm{rel} \ll \pi\alpha_g$ (Coulomb), saturates at $v_\mathrm{rel} \sim M_V/M_\chi$ (Yukawa), can show resonant peaks.
- Halo velocity $v\sim 10^{-3}c$: $S$ can reach $\mathcal{O}(10^2$–$10^3)$; freeze-out velocity $v\sim 0.2c$: $S$ moderate.
- **Asymmetric cross-ref (fixes l.229):**
  - Sommerfeld is essential for heavy electroweak WIMPs — wino, higgsino, MDM — where it shifts the thermal-relic mass from hundreds of GeV to multi-TeV and dominates ID phenomenology. Cross-ref §1.4 (J-factor formalism + MDM loop-suppression discussion).
  - For the GeV-scale candidates relevant to the GCE in Chapter 4, the standard thermal cross-section fits the observed signal *without* Sommerfeld enhancement (cite Daylan 2014).
  - Implementation note: prose must make the asymmetric framing clear — *not* a blanket claim that Sommerfeld "impacts GCE interpretation."

**¶3 — Additional refinements: co-annihilation + resonance (condensed, no equation).** Bullets:
- Single paragraph. Drop the $\langle\sigma_\mathrm{eff} v\rangle$ formula (l.232 — flagged as unclear).
- Co-annihilation: nearly degenerate states (mass splitting $\lesssim T_\mathrm{fo}$) contribute to freeze-out depletion via their own annihilations and $\chi$-partner co-annihilations. After freeze-out, partners decay; only $\chi$ annihilates today, typically with smaller cross-section than effective freeze-out value. Weakens $\Omega_\chi h^2$ ↔ ID signal connection.
- Resonant annihilation: $s$-channel mediator near $m_\mathrm{med} \approx 2 M_\chi$ → Breit-Wigner resonance with sharp velocity dependence. Enhancement or suppression of present-day rate depends on whether resonance is approached at thermal or halo velocities.
- Both introduce model dependence into the $\langle\sigma v\rangle_\mathrm{cosmo}$ ↔ present-day signal mapping.

**¶4 — Closing.** Bullets:
- $s$-wave + no Sommerfeld + no co-annihilation + no resonance → cosmological cross-section also fixes galactic-halo rate. Least model-dependent assumption, cleanest ID target. **Answers l.249 affirmatively.**
- In richer scenarios, mapping remains calculable but model-dependent. Sommerfeld can enhance by orders of magnitude; $p$-wave or resonance can suppress or shift.
- Thesis adopts standard thermal-relic $\langle\sigma v\rangle$ as primary benchmark; notes explicitly where refinements would alter the interpretation.
- One-sentence bridge to §1.3 (three complementary experimental strategies).

---

## Citations to add (BibTeX cross-check via InspireHEP / arXiv)

Do NOT create entries manually. Use InspireHEP / arXiv lookup. For papers not on either platform, list in an MD artifact for manual entry by the author.

- Bullock & Boylan-Kolchin 2017 — arXiv:1707.04256 — small-scale challenges review
- Tulin & Yu 2018 — arXiv:1705.02358 — SIDM canonical review
- Adhikari et al. 2022 — arXiv:2207.10638 — astrophysical tests of DM self-interactions
- Spergel & Steinhardt 2000 — arXiv:astro-ph/9909386 — original SIDM proposal
- Kaplinghat, Tulin & Yu 2016 — arXiv:1508.03339 — velocity-dependent SIDM
- Boyarsky et al. 2019 — arXiv:1807.07938 — sterile-ν review
- Drewes et al. 2017 — arXiv:1602.04816 — keV sterile-ν white paper
- Adams et al. 2023 (Snowmass) — arXiv:2203.14923 — axion white paper (TBD)
- Bertone, Hooper & Silk 2005 — arXiv:hep-ph/0404175 — Lee-Weinberg companion
- Hut 1977 / Vysotsky-Dolgov-Zeldovich 1977 — Lee-Weinberg historical companions (check InspireHEP)
- Daylan et al. 2014 — already in bib (`Daylan:2014rsa`) — used for §1.2.4 GCE non-need-for-Sommerfeld
- Steigman, Dasgupta & Beacom 2012 — already in bib (`Steigman:2012nb`) — used for $\langle\sigma v\rangle_\mathrm{cosmo}$
- Nollett-Steigman 2014 — already in bib (`Nollett:2014lwa`) — used for BBN floor
- Cajohare AxionLimits — Zenodo software citation, **manual addition required** (DOI: 10.5281/zenodo.3932430). List in MD artifact.

## Figures to add

- **DM mass-landscape schematic** at the start of §1.2.1 — recreate from `cirelli-paper/arXiv-2406.01705v3/figs/MDMscale.pdf`. Marker: `\aure{TODO: recreate from Cirelli figs/MDMscale.pdf}`.
- **Freeze-out $Y(x)$ plot** in §1.2.2 ¶3 — generate or adapt from Steigman 2012 / Kolb-Turner / Cirelli style, showing $Y_\mathrm{eq}$ + several $Y$ curves for different $\langle\sigma v\rangle$. Marker: `\aure{TODO: produce Y vs x freeze-out figure}`.

## Cross-references to verify before implementation

- **§1.4 Sommerfeld mentions** — confirmed (2 occurrences: l.94 Minimal DM, l.298 velocity-dependent J-factor). Cross-ref language must match these specific uses.
- **Ch.4 Sommerfeld mention** — confirmed (l.110 of `4.1_discovery_and_characterization.tex`: "No Sommerfeld enhancement... required" — i.e. the *opposite* of what the original §1.2.4 claimed). Cross-ref must reflect that GCE fits do NOT require Sommerfeld.
- **Ch.8 CTAO sensitivity projections** — confirm they do NOT reach thermal-σ at 100 TeV before locking the §1.2.3 closing prose. Honest claim is "extend sensitivity into the TeV domain."

---

## Coverage audit: all 36 annotations addressed

| # | ID | Line | Comment summary | Addressed in |
|---|----|------|-----------------|--------------|
| 1 | u2v9jgr | 10 | Soften WIMP framing | §1.2 intro ¶1 |
| 2 | 6uit90r | 12 | Don't repeat §1.1 in §1.2.1 roadmap | §1.2 intro ¶2 + §1.2.1 SM-exclusion paragraph |
| 3 | m3iipxc | 13 | "Derive" → "describe" (§1.2.2) | §1.2 intro ¶2 |
| 4 | vxa8lpk | 14 | "Derive" → "describe" (§1.2.3) | §1.2 intro ¶2 |
| 5 | e1m2hq2 | 15 | "Check" refinements list | §1.2 intro ¶2 (verified vs §1.2.4 content) |
| 6 | a2b2r1g | 16 | "Anchored" is not rigorous | §1.2 intro ¶2 closing — implementation reword |
| 7 | p5ygs4p | 24 | Add DM mass-landscape figure | §1.2.1 opening figure |
| 8 | hc1zid8 | 28 | Point to §1.1, don't re-litigate BBN/CMB | §1.2.1 SM-exclusion paragraph |
| 9 | 1dm0van | 31 | Need non-Cirelli citation for hot-DM argument | §1.2.1 SM-exclusion paragraph (Bullock & Boylan-Kolchin) |
| 10 | s83r7pf | 35 | Dislike "With SM excluded..." connective | §1.2.1 — drop, restructure transition |
| 11 | cy2je3d | 40 | "Derive" → "describe" (WIMP paragraph) | §1.2.1 WIMP paragraph |
| 12 | e1tid42 | 41 | Remove Cirelli citation on broad statement | §1.2.1 WIMP paragraph |
| 13 | 41pely5 | 45 | Expand axions, frame as leading candidate today | §1.2.1 Axion paragraph |
| 14 | gf05p3a | 48 | Drop 26 µeV specific, broader range, AxionLimits | §1.2.1 Axion paragraph |
| 15 | jx5yoij | 58–60 | Sub-GeV / dark photon paragraph fate | §1.2.1 — DROP; survives in §1.2.3 ¶2 |
| 16 | sepc5l1 | 61 | Add SIDM / WDM | §1.2.1 new "Beyond CC paradigm" paragraph |
| 17 | pczapxa | 77 | Drop connective "This testability..." | §1.2.1 closing transition |
| 18 | mjf5909 | 79 | §1.2.2 too heavy, rethink | §1.2.2 full restructure (clarity-first) |
| 19 | ebbejik | 83 | "Derive" → "describe" | §1.2.2 ¶1 |
| 20 | 3pf5st9 | 117 | Add freeze-out diagram | §1.2.2 ¶3 figure |
| 21 | 0wevvhz | 142 | $\langle\sigma v\rangle$ definition + DD comparison | §1.2.2 ¶5 |
| 22 | p2upgmv | 156 | Elaborate "electroweak scale" handwave | §1.2.2 ¶6 |
| 23 | 687cn7m | 168 | Note $s$-wave = velocity-independent | §1.2.3 ¶1 |
| 24 | wk6031c | 170 | Cite besides Cirelli for Lee-Weinberg modern value | §1.2.3 ¶1 (Bertone-Hooper-Silk 2005) |
| 25 | 1915dkh | 176 | Keep dark-photon part | §1.2.3 ¶2 |
| 26 | 5y34ho1 | 178 | Expand unitarity bound | §1.2.3 ¶3 |
| 27 | 9xt1hso | 179 | Explain "partial-wave unitarity" | §1.2.3 ¶3 |
| 28 | 4k09e6e | 181 | Explain "perturbativity" | §1.2.3 ¶4 |
| 29 | 97iwmph | 196 | Cite Ch. 8 CTAO + correct "far from 100 TeV" | §1.2.3 ¶6 |
| 30 | xv5xsvc | 198 | Don't claim thermal-σ reach with CTAO | §1.2.3 ¶6 |
| 31 | baae25x | 218 | Helicity suppression too technical | §1.2.4 ¶1 — reword |
| 32 | 97w6pqg | 229 | Verify §1.4 and Ch.4 actually discuss Sommerfeld | §1.2.4 ¶2 — asymmetric cross-ref (verified) |
| 33 | usq5m5q | 231–246 | Condense co-annihilation + resonance | §1.2.4 ¶3 — single paragraph |
| 34 | cxkn3ch | 232 | Co-annihilation equation unclear | §1.2.4 ¶3 — drop equation |
| 35 | 4csvq4m | 249 | Update closing; affirm $s$-wave less model-dependent | §1.2.4 ¶4 |
| 36 | (l.6) | 6 | Orphan `\aure{stopped here}` WIP marker | §1.2 intro ¶1 — delete |

All 36 review-mode annotations are addressed by an explicit structural change. Implementation agent will handle wording-level rephrasing for items 6, 10, 11, 12, 17, 18 (small stylistic rewrites) and produce the actual prose for everything else.

---

## Next step (implementation handoff)

Brainstorming complete. Hand off to writing-plans to produce an implementation plan that sequences the rewrite into reviewable chunks (suggested order: §1.2.1 → §1.2.2 → §1.2.3 → §1.2.4 → §1.2 intro, with figure-generation tasks parallel and citation-fetching front-loaded).
