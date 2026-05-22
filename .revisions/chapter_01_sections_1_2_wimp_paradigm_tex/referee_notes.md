# Review Report: §1.2 (The WIMP Paradigm)

## Summary
Section 1.2 is a well-structured, scientifically sound treatment of the WIMP paradigm that successfully implements the funnel-structured roadmap (landscape → freeze-out → mass bounds → refinements). The prose is mature, the physics is accurate in its substance, and the section largely conforms to the thesis voice. Its main weaknesses are: (i) two cross-references to §1.1 that point to material §1.1 does not in fact contain (Tremaine–Gunn bound, small-scale tensions); (ii) one missing-citation placeholder (`AxionLimits` Zenodo); (iii) several internal numerical/quantitative inconsistencies (Lee–Weinberg quoted as both 2 and 3 GeV in adjacent sentences; the "GeV–TeV WIMP window" advertised in the roadmap is delivered later as "3 GeV–100 TeV"); and (iv) a handful of stylistic blemishes (residual "crucially", em-dash density, a couple of vague attributions).

## Verdict
Needs revision — the cross-reference inaccuracies and a couple of quantitative inconsistencies are correctness-level issues; everything else is polish.

## Issue counts
- 🔴 Critical: 4
- 🟡 Important: 8
- 🟢 Minor: 9

## Strengths
- The intro funnel is exemplary: it explicitly disavows ideological WIMP-centrism, names the candidate classes the section will *not* focus on, and gives an operational justification for the WIMP focus (lines 7–13). This is a substantial improvement over the typical "WIMP is the default" framing and matches the thesis style guide ("the author takes positions").
- §1.2.2 is the standout: the qualitative warm-up paragraph (lines 88–93) before any formula appears realises the "physical picture before formulas" instruction in the user's memory exactly. The "weakest particle wins" framing is concise and correct.
- The cross-section disambiguation paragraph (lines 121–126), distinguishing $\langle\sigma v\rangle$ (cm³/s, thermally averaged annihilation) from direct-detection $\sigma_{\chi N}$ (cm², elastic), is a genuinely useful pedagogical move that few textbooks bother with.
- §1.2.3 cleanly separates "theory-quality" (perturbativity) from "physics-quality" (unitarity) bounds (lines 173–178) — exactly the kind of conceptual hierarchy the style guide rewards.
- The BBN floor (lines 179–181) is a nice independent lower bound that complements Lee–Weinberg and is often omitted from competing textbooks.
- The Daylan-et-al numerical anchor in §1.2.4 (line 216) provides forward-pointing scaffolding to Chapter 4 with concrete numbers, not just a chapter cross-reference.
- §1.2.4 correctly distinguishes the Sommerfeld regimes (Coulomb $\propto 1/v$ vs Yukawa saturation vs resonances) and connects them to specific WIMP masses (wino 3 TeV, higgsino 1.1 TeV), with a realistic statement that wino DM is currently disfavoured by gamma-ray constraints for cuspy profiles.
- Bibliography keys are all present in `bibliography.bib`; no broken cite keys were found.

## Critical Issues (🔴)

### Issue 1: Cross-reference to §1.1 for the Tremaine–Gunn bound is unsupported
- **Location**: §1.2.1, paragraph 1 (line 37)
- **Quote**: "the Tremaine--Gunn phase-space bound discussed in Section~\ref{sec:1.1.1} forbids any fermionic candidate lighter than about $1$~keV~\cite{Tremaine:1979we}"
- **Problem**: §1.1.1 does not in fact discuss the Tremaine–Gunn bound. `grep -ni tremaine` on `1.1_evidence_for_dark_matter.tex` returns zero hits. The Tremaine–Gunn citation appears only here in §1.2. The cross-reference is therefore false to the reader.
- **Suggested fix**: Either (a) drop the `Section~\ref{sec:1.1.1}` pointer and present the bound as a stand-alone fact citing only `Tremaine:1979we`; or (b) add a one-sentence treatment of the phase-space bound to §1.1.1 (most natural in the dwarf-spheroidal subsection where stellar dynamics are already in play); or (c) move the bound to the SM-exclusion paragraph in §1.2.1 with the citation alone. Option (a) is the lowest-friction fix.

### Issue 2: Cross-reference to §1.1.2 for "small-scale tensions" is also unsupported
- **Location**: §1.2.1, paragraph 6 (line 67)
- **Quote**: "The persistent small-scale tensions reviewed in Section~\ref{sec:1.1.2} --- the cusp/core problem in dwarf galaxies, the diversity of rotation curves at fixed maximum circular velocity, and the too-big-to-fail puzzle of the Milky Way satellites --- all point to fewer dense, cuspy halos on sub-galactic scales..."
- **Problem**: §1.1.2 covers the *cluster* scale (Zwicky, virial theorem, X-rays, SZ, Bullet Cluster). It does not contain a small-scale-tension discussion; `grep -ni "cusp\|small.scale\|diversity\|too.big"` returns no matches in §1.1. The reference is incorrect both in section number and in content (these are galactic-scale tensions, not cluster-scale).
- **Suggested fix**: Either (a) drop the `Section~\ref{sec:1.1.2}` pointer and cite `Bullock:2017xww` directly for a brief stand-alone summary; or (b) add a paragraph on small-scale tensions to §1.1.1 (galactic scale, where they belong) and update the pointer to `sec:1.1.1`. Given §1.1.1 already covers dwarf-spheroidal dynamics, option (b) is the more thesis-coherent fix and produces a cleaner backward reference from §1.2.4 / §5.

### Issue 3: Internal inconsistency in the Lee–Weinberg numerical bound
- **Location**: §1.2.3 (lines 149–153)
- **Quote**: "The original Lee--Weinberg analysis~\cite{Lee:1977ua} ... obtained $M_\chi \gtrsim 2$~GeV for a heavy Dirac neutrino; modern evaluations with updated effective-degree-of-freedom counts give ... $M_\chi \gtrsim 3$~GeV"
- **Problem**: The historical "2 GeV" and the modern "3 GeV" are then conflated downstream: the WIMP window in Eq.~\eqref{eq:wimp_window} uses 3 GeV (line 185), which is fine, but the intro roadmap (line 18) advertises the lower edge "near the GeV scale", and §1.2.4 inherits the 3-GeV anchor implicitly. The bigger issue is the BBN bound stated in line 181 — "$M_\chi \gtrsim 3$~MeV" — which is a *thousand* times below the 3 GeV figure quoted next door. The text claims the BBN bound "extends the lower edge into the MeV regime once one allows for non-Standard-Model mediators" (line 188), which is correct phenomenologically, but the order-of-magnitude gap between 3 GeV and 3 MeV is large enough to confuse a reader on first pass.
- **Suggested fix**: Add one clarifying sentence after Eq.~\eqref{eq:lee_weinberg} explicitly noting that the Lee–Weinberg bound *assumes* SM-mediation and is replaced by the much weaker BBN floor when that assumption is dropped — the reverse logical ordering of what is currently written. This restores the conceptual hierarchy (SM-mediation: ~3 GeV; any thermal relic: ~3 MeV) without introducing new physics.

### Issue 4: Missing citation placeholder for AxionLimits
- **Location**: §1.2.1 (line 49)
- **Quote**: "the open-source \texttt{AxionLimits} compilation maintained by O'Hare and collaborators \aure{cite cajohare/AxionLimits Zenodo} is the standard reference for the current global picture"
- **Problem**: This is a hanging `\aure{}` placeholder. CLAUDE.md says "Never create BibTeX entries manually. Only add bib entries fetched from InspireHEP or arXiv. For papers not found on these platforms, list them in an MD artifact". AxionLimits has a Zenodo DOI (10.5281/zenodo.3932430). The right move is to either (a) add a Zenodo bib entry by hand if the project allows it, since Zenodo is a recognised archival source even if not InspireHEP/arXiv, or (b) drop the AxionLimits sentence — it is not load-bearing for the argument. The current state, an unresolved `\aure`, must not survive a final draft per the style guide ("resolve before final submission").
- **Suggested fix**: Drop the sentence (lowest-friction) or commit to adding the Zenodo entry to `bibliography.bib`. Either way, the `\aure{}` should not survive review.

## Important Issues (🟡)

### Issue 5: "GeV–TeV WIMP window" in the roadmap is not what §1.2.3 actually delivers
- **Location**: §1.2 intro, line 18; §1.2.3, line 185
- **Quote**: roadmap: "jointly defining the GeV--TeV WIMP window targeted by gamma-ray experiments"; payoff: "$3~\mathrm{GeV} \lesssim M_\chi \lesssim 100~\mathrm{TeV}$"
- **Problem**: 100 TeV is not "the TeV scale" in any natural reading; it is two orders of magnitude above the electroweak scale. The roadmap suggests a window narrower than what §1.2.3 derives. This is not wrong, just under-promising.
- **Suggested fix**: Change "GeV–TeV WIMP window" to "GeV–100 TeV thermal window" in the roadmap (line 18), or note that the unitarity ceiling sits *above* the electroweak scale by two orders of magnitude.

### Issue 6: The Lee–Weinberg derivation skips a physical-picture step that the rest of §1.2.2 sets up
- **Location**: §1.2.3 (lines 146–148)
- **Quote**: "At freeze-out energies the annihilation cross section for such a particle, dominated by exchange of $W$ and $Z$ bosons, scales as $\sigma_0 \approx G_F^2 M_\chi^2 / 2\pi$ ... Because the relic density goes inversely as the cross section through Eq.~\eqref{eq:relic_abundance}, and because $\sigma_0$ shrinks with the candidate mass, a sufficiently light particle annihilates too weakly to thin itself out and ends up overproducing dark matter."
- **Problem**: The phrase "$\sigma_0$ shrinks with the candidate mass" is the *opposite* of what the formula above says ($\sigma_0 \propto M_\chi^2$ grows with mass). The author actually means: as you *lower* $M_\chi$, $\sigma_0$ falls — so the cross section is smaller at smaller masses — but the current phrasing is genuinely confusing on a first read because the cross section is being described as "shrinking" while its formula clearly grows.
- **Suggested fix**: Rephrase as "Because $\sigma_0$ scales as $M_\chi^2$, *lowering* the candidate mass *reduces* the annihilation cross section quadratically; combined with the inverse scaling of the relic density in Eq.~\eqref{eq:relic_abundance}, this means a sufficiently light particle annihilates too weakly to thin itself out, and ends up overproducing dark matter." The point is to make the direction of the scaling explicit.

### Issue 7: The "FIMP abundance grows with the coupling" claim needs unpacking
- **Location**: §1.2.1, FIMP paragraph (lines 62–64)
- **Quote**: "their abundance is built up gradually through rare decays and $2 \to 2$ scatterings, and crucially it grows with the coupling rather than shrinking, opposite to the freeze-out logic of Section~\ref{sec:1.2.2}~\cite{Cirelli:2024ssz}."
- **Problem**: The claim "abundance grows with the coupling" is correct but the freeze-out analogy is mis-stated. In freeze-out, the *relic* abundance shrinks with coupling, while the *production* rate grows. Both regimes have abundance built up by interactions; the difference is whether you sit on the equilibrium curve (freeze-out) or asymptote to a frozen-in coupling-controlled value (freeze-in). The current phrasing — "opposite to the freeze-out logic" — is true for the *final relic*, not for the *production rate*, and a careful reader will notice the slip.
- **Suggested fix**: Replace "and crucially it grows with the coupling rather than shrinking" with "and the *final relic abundance* therefore grows with the coupling rather than shrinking, the inverse of the freeze-out logic of Section~\ref{sec:1.2.2}" — italicising "final relic" makes the distinction explicit. Also: this is one of the residual "crucially" tokens — drop it (see Issue 12).

### Issue 8: Sterile-neutrino mass range claim needs a citation or hedge
- **Location**: §1.2.1, sterile-neutrino paragraph (lines 53–55)
- **Quote**: "Resonant production is the more flexible option because it evades the most stringent free-streaming bounds from Lyman-$\alpha$ and Milky Way satellite counts, which otherwise push the allowed mass above $20$--$30$~keV."
- **Problem**: The "20–30 keV" lower edge on the allowed mass is a specific quantitative claim that should carry a citation. The Boyarsky 2018 and Drewes 2016 references appear in the *next* sentence but for different content (model-space reviews, not the Lyman-α floor). The reader has to infer the citation.
- **Suggested fix**: Append `~\cite{Boyarsky:2018tvu}` to the Lyman-α sentence; the 20–30 keV figure is consistent with that review.

### Issue 9: Sommerfeld factor magnitude claim should be sourced
- **Location**: §1.2.4, Sommerfeld paragraph (lines 211–213)
- **Quote**: "Halo velocities $v_\mathrm{rel}\sim 10^{-3}\,c$ therefore probe a regime in which $S$ can reach $\mathcal{O}(10^2\text{--}10^3)$"
- **Problem**: The $10^2$–$10^3$ enhancement is a specific phenomenological claim. The Hisano:2004ds + ArkaniHamed:2008qn citations appear earlier in the paragraph but the quantitative range deserves a more specific anchor (e.g., the wino phenomenology papers, or `Hisano:2003ec` for the wino tree-level calculation).
- **Suggested fix**: Add a citation to a Sommerfeld phenomenology paper directly at the "$10^2$–$10^3$" claim. The closest existing entry is already `Hisano:2004ds`; restating it inline would be sufficient.

### Issue 10: The "Cirelli et al. 2024" citation is overused
- **Location**: 9 occurrences of `Cirelli:2024ssz` across §1.2 (lines 9, 30, 37, 47, 59, 63, 146, 149, 157, 204, 207, 211, 219, 226)
- **Problem**: A single review paper carries roughly half the section's factual load. The style guide warns: "specificity (right paper, not just a 'review')". For axions, sterile neutrinos, PBHs, and FIMPs there are dedicated reviews (`Adams:2022pbo`, `Boyarsky:2018tvu`, `Drewes:2016upu`, `Hall:2009bx`) that should bear the primary citation, with `Cirelli:2024ssz` as a secondary/synthesis pointer.
- **Suggested fix**: For each factual claim, swap one `Cirelli:2024ssz` for the most-specific available citation. E.g., line 37 (the SM-exclusion paragraph) should cite the relevant `Aghanim:2018eyx` for the CMB baryon budget and `Tremaine:1979we` for the phase-space bound (it already does the latter); line 47 for the misalignment mechanism should cite the original `Preskill:1982cy`, `Abbott:1982af`, `Dine:1982ah` triplet (the standard misalignment-mechanism papers) instead of leaning on the Cirelli review.

### Issue 11: Co-annihilation claim "annihilation cross section ... typically smaller" needs hedging
- **Location**: §1.2.4, co-annihilation paragraph (lines 219–220)
- **Quote**: "After freeze-out the heavier states decay into $\chi$, so that only the lightest species remains in the present-day halo; its annihilation cross section is then typically smaller than the effective freeze-out value, and the link between $\Omega_\chi h^2$ and the indirect-detection signal is weakened."
- **Problem**: "Typically smaller" is qualitatively correct but somewhat softer than the literature warrants. The standard statement is that co-annihilation *reduces* the present-day signal because the effective cross section at freeze-out is enhanced by the co-annihilating partners which are absent today. Either commit to "is smaller" (with a caveat that it depends on the coupling structure) or quote a reference number range.
- **Suggested fix**: Replace "typically smaller" with "smaller, often by orders of magnitude when the co-annihilation partners dominate the freeze-out rate". This sharpens the claim without overcommitting.

### Issue 12: Residual "crucially / crucial" tokens against the style guide
- **Location**: Multiple — lines 63 ("crucially it grows"), implicit elsewhere
- **Problem**: The humanizer skill flags "crucial / crucially / pivotal / key" as AI-writing markers. Line 63 is the one explicit hit.
- **Suggested fix**: Replace "crucially it grows" with "and the final relic abundance grows" (this also fixes Issue 7 in one sweep).

## Minor Issues (🟢)

### Issue 13: Two TODO/`\aure{}` markers in figure captions
- **Location**: lines 30, 101
- **Quote**: "\aure{TODO: recreate from arXiv:2406.01705v3 figs/MDMscale.pdf}" and "\aure{TODO: produce Y vs x freeze-out figure}"
- **Suggested fix**: These are explicitly allowed by the style guide ("Keep them in drafts; resolve before final submission"). No action needed at the section-review stage, but flag them in the chapter-level TODO list.

### Issue 14: Em-dash density
- **Location**: §1.2.1 paragraphs 1–2 (lines 7–13)
- **Problem**: The opening paragraph has three em-dashes in close succession ("--- the so-called WIMP miracle --- and"; "--- the main classes (WIMPs, axions, ...) ---"; etc.). The style guide tolerates em-dashes but the humanizer flags overuse.
- **Suggested fix**: Convert one of the parenthetical inserts to a comma-bounded clause. E.g., line 11: "Their dominance of the indirect-detection literature over the past two decades is a historical fact, driven by the so-called WIMP miracle (the observation that ...), and not a statement that..." — the parentheses do the same job.

### Issue 15: Rule-of-three pattern in the introduction
- **Location**: line 7
- **Quote**: "dark matter exists, contributes roughly five times the cosmological energy density of baryons, and cannot be accommodated within the Standard Model."
- **Problem**: Triplet. This is a clean rule-of-three. The humanizer skill considers them an AI marker only when stacked; a single triplet at the section opening is unobjectionable but worth noting.
- **Suggested fix**: Optional — could be left as is. If trimming for style, drop the middle clause and let the first and last carry the weight.

### Issue 16: "perhaps surprising punchline" is a slightly informal idiom
- **Location**: §1.2.2, line 86
- **Quote**: "with the perhaps surprising punchline already visible in advance"
- **Suggested fix**: "with a counterintuitive result already visible in advance" — keeps the meaning, drops the journalistic register.

### Issue 17: "we crank the candidate mass upward" is colloquial
- **Location**: §1.2.3, line 164
- **Quote**: "As we crank the candidate mass upward, the unitarity ceiling drops"
- **Suggested fix**: "As the candidate mass increases, the unitarity ceiling drops" — same meaning, neutral register.

### Issue 18: "$x_f \approx 20$–$25$" vs "$T_\mathrm{fo} \sim M_\chi/25$"
- **Location**: §1.2.2, line 109 vs chapter outline §1.2.2 line 97 ("$x_f \approx 20$–$25$")
- **Problem**: The text quotes only the upper end ($x_\mathrm{fo}\sim 25$) without acknowledging the customary 20–25 range. Minor pedagogical loss.
- **Suggested fix**: "$T_\mathrm{fo} \sim M_\chi/(20\text{–}25)$" matches the outline and the literature consensus.

### Issue 19: Vague attribution "a community of hydrodynamical simulators"
- **Location**: §1.2.1, line 72
- **Quote**: "a community of hydrodynamical simulators (the ETHOS framework and the works of Vogelsberger, Rocha, Peter, Fischer, and collaborators) now routinely compares SIDM and WDM predictions to dwarf-galaxy data."
- **Problem**: The style guide explicitly flags "vague attributions" as an anti-pattern. "A community of simulators" with five surnames in parentheses and no citation is a soft attribution; either commit to a citation (the ETHOS paper, `Vogelsberger:2015gpr`) or remove the name-cloud.
- **Suggested fix**: Replace the parenthetical with a single citation to the ETHOS framework paper.

### Issue 20: Figure 1.X labelling consistency
- **Location**: lines 25–32, 95–103
- **Problem**: Figures use the placeholder `chapter_01/figures/dm_mass_landscape.pdf` and `freezeout_yx.pdf`. Verify these files actually exist or are placeholders.
- **Suggested fix**: Confirm at compile time. No action at review level.

### Issue 21: The "perturbativity" subsection title is missing
- **Location**: §1.2.3, lines 173–178
- **Problem**: The perturbativity paragraph is structurally a sub-claim of "upper bounds on $M_\chi$" but is not given a bold lead-in (the style guide endorses `\textbf{Perturbativity.}` lead-ins for scannable structure). The Sommerfeld-related paragraphs in §1.2.4 likewise lack lead-ins ("Velocity dependence.", "Sommerfeld enhancement.", "Co-annihilation.", "Resonant annihilation.").
- **Suggested fix**: Add bold paragraph lead-ins to the four refinement paragraphs in §1.2.4 to match the style guide ("bold/italic lead-ins for scannable structure").

## Dimension scores

| Dimension | Score (1-5) | Notes |
|---|---|---|
| Scientific Rigor | 4 | Physics is correct; the Lee–Weinberg vs BBN bound interplay and the "$\sigma_0$ shrinks with mass" wording need tightening, but no actual scientific errors. |
| Citation Quality | 3 | All cite keys resolve; however, `Cirelli:2024ssz` is overused as a catch-all, `AxionLimits` is unresolved, and a couple of specific factual claims (sterile-neutrino mass floor, Sommerfeld $S \sim 10^2$–$10^3$) lack a direct anchor. |
| Writing Quality | 4 | The prose is mature and conforms to the thesis voice. A handful of "crucially"/colloquial/em-dash issues remain. |
| Structure & Transitions | 4 | The four-subsection structure and the funnel-shaped intro work well; the missing bold lead-ins in §1.2.4 are a minor structural opportunity. |
| Thesis Integration | 2 | The two §1.1 cross-references (Tremaine–Gunn, small-scale tensions) point to material that §1.1 does not contain. This is the only major integration problem; once fixed, the score would be 4+. |

## Recommendations
Address in this order:

1. **Fix the two false cross-references to §1.1** (Issues 1, 2). Either drop the section pointers or add the missing content to §1.1.1. This is the only correctness-level fix; everything else is polish.
2. **Resolve the AxionLimits `\aure{}` placeholder** (Issue 4) — either add a Zenodo bib entry, replace with a more standard reference, or drop the sentence.
3. **Reconcile the Lee–Weinberg / BBN bound hierarchy** (Issues 3, 5) — one clarifying sentence and one roadmap rewording.
4. **Fix the "$\sigma_0$ shrinks with mass" wording** (Issue 6) and the FIMP-coupling wording (Issue 7). Both are physically correct but easily misread.
5. Sharpen citations on the sterile-neutrino floor and the Sommerfeld factor (Issues 8, 9). Reduce reliance on `Cirelli:2024ssz` for paragraph-level anchors (Issue 10).
6. Style polish: drop the residual "crucially" (Issue 12), trim a couple of em-dashes (Issue 14), neutralise "crank" and "punchline" (Issues 16, 17), add bold lead-ins to §1.2.4 paragraphs (Issue 21).
7. Cosmetic: figure-file existence check (Issue 20), $x_f$ range (Issue 18), ETHOS attribution (Issue 19).

Once Issues 1–4 are addressed the section is publication-ready as a thesis chapter. The remaining items are polish that can be batched into the chapter-level revision sweep.
