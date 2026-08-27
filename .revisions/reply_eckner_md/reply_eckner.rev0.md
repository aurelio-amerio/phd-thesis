# Reply to Eckner's comments

Parsed from `Eckner_comments_for_aurelio.txt` (received Aug 2026). Each comment has an ID
(`E-<chapter>.<n>`), a type tag, a faithful summary of the point, and empty **Response** /
**Action** fields to fill during the brainstorming pass.

**Type legend:**
- `[science]` — substantive scientific objection or correction; needs a considered reply and likely a prose change
- `[structure]` — narrative/motivation/ordering issue
- `[clarify]` — request to explain, define, or be more precise
- `[ref]` — missing or additional reference requested
- `[mechanical]` — typo, numbering, acronym, formatting
- `[style]` — wording / AI-register remark (no action strictly required)

**Status legend:** ⬜ open · 🟡 proposed (replacement text drafted below, awaiting author
approval) · ⏳ deferred to the substantive pass (strategy sketched below) · ✅ applied to
the thesis · ❌ rebutted (with justification)

The summary table at the bottom is the authoritative status tracker.

**Verification note:** Eckner's factual claims were cross-checked against the primary
literature (arXiv sources fetched and read where needed). Every checkable claim was
confirmed, with nuances recorded per item; no claim was found wrong.

---

## Chapter 4 — Galactic Center Excess (main comments)

### E-4.1 · §4.1.4 — "Morphology is a prediction" claim is wrong `[science]` ⬜

> You state "the same mass and channel that fit the spectrum also predict the correct
> spatial distribution, and the same halo profile that matches the morphology yields the
> observed flux level."

**Eckner's point:** This is not correct for cold, non-self-interacting DM. Particle
physics properties (mass, channel, cross section) are entirely decoupled from the spatial
profile. Any WIMP model can be paired with whatever spatial profile the GCE has; how that
profile arises is an astrophysics question. The profile is *measured and fitted*, not
*predicted* — it is an observation.

**Response:** He is technically right and the objection lands: mass/channel fix the
*spectrum*; the halo profile fixes the *morphology*; they are independent inputs, so
"the same mass and channel predict the spatial distribution" is wrong as written. What
the passage legitimately wants to say is weaker but still meaningful: (a) the *shape* of
the required profile (steep, approximately spherical, γ ≈ 1.1–1.3 contracted NFW) was
not invented for the GCE — it lies within the range simulations and rotation-curve fits
independently considered plausible; (b) *given* that profile, a single normalization
⟨σv⟩ simultaneously accounts for the flux, and lands near the thermal value. That is a
consistency, not a prediction, and the text should say so. This is the core of the
chapter-rebalancing the author asked Eckner about — treat carefully.

**Action:** ⏳ DEFERRED — substantive pass. Strategy for §4.1.4
(`4.1_discovery_and_characterization.tex:129-141`):
- Delete/replace the "No tuning of separate parameters is required" sentence (line 131).
- Restructure the consistency argument as: spectrum → fixes (m, channel); morphology →
  *measured*, fitted by a contracted NFW whose parameters fall in the independently
  plausible range; normalization → single ⟨σv⟩ near thermal. Three observables, three
  parameters — internally consistent, economical, but not a prediction.
- Reword line 138 "three independent observables… could be described" accordingly
  ("described by" is fine; drop any "predict" language).
- Keep the existing "interpreted with care" paragraph as the pivot into E-4.2's updated
  density discussion.

---

### E-4.2 · §4.1.4 — Local DM density degeneracy may be underestimated `[science]` ⬜

> "The inferred cross section is degenerate with the assumed local dark matter density..."

**Eckner's point:** Recent measurements of the local DM density favour even *larger*
values (> 0.4 GeV/cm³), so the shift in the inferred cross section may be larger than
stated.

**Response:** ✔ Verified, with nuance. The de Salas & Widmark review (arXiv:2012.11477)
finds *local* Gaia-era determinations clustering at 0.4–0.6 GeV/cm³, while *global*
rotation-curve analyses prefer 0.3–0.5; a recent Gaia DR3 K-dwarf analysis (Söding et
al., arXiv:2506.02956) finds 0.44 ± 0.13. So "recent local measurements favour ≥ 0.4" is
accurate, though the community has not converged on it — our quoted range 0.3–0.4 is
outdated on the upper end. Note: a *larger* ρ⊙ shifts the inferred ⟨σv⟩ *down* (flux ∝
ρ²⟨σv⟩), which actually moves the GCE cross section further from the thermal value —
worth stating, since it slightly weakens the "thermal coincidence" argument the section
is qualifying anyway.

**Action:** In `chapter_04/sections/4.1_discovery_and_characterization.tex:140`, update:
> Current: "…varying $\rho_\odot$ within its observationally allowed range
> ($0.3$--$0.4$~GeV/cm$^3$) shifts $\langle \sigma v \rangle$ by a factor of $\sim
> 1.8$~\cite{Abazajian:2014fta,Daylan:2014rsa}."
>
> Proposed: "…varying $\rho_\odot$ within its observationally allowed range shifts
> $\langle \sigma v \rangle$ by a factor of $\sim
> 1.8$~\cite{Abazajian:2014fta,Daylan:2014rsa}\blue{; recent local determinations based
> on \textit{Gaia} data moreover favour values at or above $0.4$~GeV/cm$^3$~\cite{<deSalas-Widmark>},
> which would push the inferred cross section correspondingly further below the thermal
> benchmark}."
>
> Bib to fetch from InspireHEP: arXiv:2012.11477 (review; sufficient on its own).

---

### E-4.3 · §4.2.1 — Bartels et al. (skyFACT) is not like the other analyses `[science]` ⬜

> "By the late 2010s, the NPTF photon statistics, wavelet power, and stellar bulge
> morphology appeared to have settled the question... subsequent studies exposed
> weaknesses in each of these analyses..."

**Eckner's point:** The preceding paragraph cites Bartels et al. 2017 [215], which is
methodologically very different: NPTF and Macias et al. use templates with *fixed* spatial
morphology, whereas Bartels et al. use skyFACT, which performs a data-driven optimisation
of the spatial morphologies. The caveats raised in §4.3 do not necessarily apply to
skyFACT.

**Response:** ✔ Verified. Bartels et al. (arXiv:1711.04778, Nature Astronomy 2018) use
skyFACT (Storm, Weniger & Calore, arXiv:1705.04065): penalized Poisson likelihood with
~10⁵ pixel-level nuisance parameters that re-modulate the templates — data-driven
adaptive morphologies, structurally different from rigid-template NPTF fits. Eckner's
distinction is well founded, and he grants that skyFACT has *other* issues one could
name (regularization choices decide how much freedom templates get; the fit remains
anchored to the input templates it modulates). Handle together with E-4.6 — one
methodological clarification serving both §4.2.1 and §4.3.

**Action:** ⏳ DEFERRED — substantive pass (joint with E-4.6). Strategy:
- In §4.2.1 (`4.2_msp_hypothesis.tex:40-44`): when introducing Bartels et al., add a
  clause distinguishing skyFACT's adaptive-template approach from the fixed-template
  NPTF/Macias analyses just discussed.
- In the §4.3 opener (`4.3_systematics_stalemate.tex:7`): qualify "share a common
  vulnerability" to scope it to *rigid-template* analyses; note explicitly that
  skyFACT-type approaches mitigate morphology mis-specification by construction, while
  remaining subject to their own choices (regularization strength, input template
  anchoring).
- Check §4.3's later text for other blanket "all template-based analyses" statements.
- Bib: arXiv:1705.04065 (skyFACT method paper) to fetch if not present.

---

### E-4.4 · §4.2.2 — Globular clusters "continuously replenished"? `[clarify]` ⬜

> "unlike the disk and globular cluster populations, which are continuously replenished
> with freshly recycled pulsars"

**Eckner's point:** True for the disk, but globular clusters are old objects — the only
replenishment channel is dynamical formation, which should equally apply to the Milky Way
bulge or nuclear stellar cluster. The statement needs a better explanation or a fix.

**Response:** Our conclusions chapter already states the argument correctly
(`conclusion/conclusion.tex`: "surviving clusters through dynamical formation in their
dense cores… the plane through ongoing star formation"); the Chapter 4 sentence
(`4.2_msp_hypothesis.tex:71`) just compresses it into "continuously replenished" without
naming the distinct channels. On Eckner's objection that dynamical formation should also
operate in the bulge/NSC: the standard counter is that dynamical MSP formation requires
the *extreme stellar densities* of cluster cores — the bulge at large is orders of
magnitude too diffuse (the NSC is a possible exception but is spatially tiny compared to
the GCE). A deposited bulge population formed in clusters that have since dissolved has
lost that channel. Spell this out.

**Action:** In `chapter_04/sections/4.2_msp_hypothesis.tex:71`, rework:
> Current: "Such dimming is not implausible: unlike the disk and globular cluster
> populations, which are continuously replenished with freshly recycled pulsars, a
> bulge population that stopped forming new MSPs long ago would have faded through
> spin-down."
>
> Proposed: "Such dimming is not implausible: \blue{the disk and globular cluster
> populations are each replenished with freshly recycled pulsars through a distinct
> channel --- the disk through ongoing star formation, globular clusters through
> dynamical binary formation in their dense cores, at stellar densities the diffuse
> bulge field cannot match. A bulge population deposited long ago, having access to
> neither channel, would have faded through spin-down ever since.}"
>
> Citations: keep `\cite{Fragione:2017rsp,Ploeg:2020jeh,Ye:2022yxt}` on the following
> sentence; `Ye:2022yxt` supports the dynamical-formation clause if one is wanted
> inline.

---

### E-4.5 · §4.2.2 — Motivate the globular-cluster storyline earlier `[structure]` ⬜

**Eckner's point:** Chapter 4 never explains *why* globular clusters matter for the GCE
until the conclusions, where the deposition mechanism (disrupted GCs depositing MSPs in
the bulge) is finally named. This mechanism should be stated in Section 4 itself to
motivate the whole GC storyline.

**Response:** Agreed, and the material already exists: the thesis conclusion names the
mechanism with citations (`conclusion/conclusion.tex:59-61`: clusters spiraling into the
Inner Galaxy and dissolving under tidal forces, `Gnedin:2013cda, Brandt:2015ula,
Fragione:2017rsp`). What is missing is a motivating paragraph *early in Chapter 4* —
naturally in §4.2.2 where the bulge-MSP-origin question first arises, or in the §4.4/§4.5
bridge where globular clusters enter as calibration targets. This is a structural
addition (placement affects the chapter roadmap), so it belongs in the substantive pass.

**Action:** ⏳ DEFERRED — substantive pass. Strategy:
- Add a paragraph when GCs first enter the chapter narrative: bulge MSPs cannot have
  formed in situ through the cluster channel (density argument, cf. E-4.4 fix); the
  leading delivery scenario is tidal disruption of infalling globular clusters
  depositing their MSPs in the bulge (Gnedin:2013cda, Brandt:2015ula,
  Fragione:2017rsp); *therefore* surviving globular clusters are the natural
  calibration sample for the luminosity function of the deposited population — which is
  precisely the chapter's strategy.
- Verify the chapter intro roadmap (`4.0_introduction.tex`) then previews this logic in
  one sentence.
- Coordinate with the E-4.4 rewording (shared density/channel argument — avoid saying
  it twice with different words).

---

### E-4.6 · §4.3 — "Common vulnerability" claim excludes skyFACT `[science]` ⬜

> "both for and against the MSP hypothesis, was obtained through template-based analyses
> that share a common vulnerability"

**Eckner's point:** Same objection as E-4.3 — this is not really true for Bartels et al.
[215], which mitigates the named issues by construction (though other issues could be
raised against it).

**Response:** See E-4.3 — one joint fix.

**Action:** ⏳ DEFERRED — handled jointly with E-4.3 in the substantive pass.

---

### E-4.7 · §4.3.2 — High-energy tail is compatible with MSPs `[science]` ⬜

> "The presence of a power-law tail at higher energies is difficult to reconcile with a
> purely MSP origin"

**Eckner's point:** Disagrees. Manconi et al. [239] state that such a tail arises
naturally in MSP populations embedded in reasonably strong photon fields, via inverse
Compton emission.

**Response:** ✔ Verified. Manconi, Calore & Donato (arXiv:2402.04733 = [239], already in
the bibliography) state the high-energy photons "could be naturally explained by the
inverse Compton scattering of electrons and positrons emitted by a population of MSPs in
the Galactic bulge", with the underlying IC modeling from Song, Macias & Horiuchi
(arXiv:1901.07025). Our sentence at `4.3_systematics_stalemate.tex:71` overstates the
tension: prompt (magnetospheric) MSP emission indeed cuts off at a few GeV, but the same
pulsars' e⁺e⁻ winds up-scattering the intense GC radiation field extend the *population*
spectrum to higher energies. The honest statement: the tail challenges *prompt-only* MSP
emission, and discriminating IC-from-MSPs from a second component (or DM) is an open
question. This fits the user's stated goal of a balanced chapter.

**Action:** In `chapter_04/sections/4.3_systematics_stalemate.tex:71-72`, rework:
> Current: "The presence of a power-law tail at higher energies is difficult to
> reconcile with a purely MSP origin and suggests that either a second emission
> component contributes at high energies or that the GCE is not entirely astrophysical.
> This spectral argument operates independently of the morphological debate and was
> initially cited as evidence against a complete MSP explanation."
>
> Proposed: "\blue{The presence of a power-law tail at higher energies is difficult to
> reconcile with prompt magnetospheric emission alone. It does not, however, rule out an
> MSP origin: the electrons and positrons injected by a bulge MSP population would
> up-scatter the intense interstellar radiation fields of the inner Galaxy, and this
> inverse Compton component can naturally account for both the GeV peak and the
> high-energy tail~\cite{<Song2019>,manconi2024galacticcenterhighest}. The tail
> therefore constrains the composition of the MSP emission rather than excluding it,
> although it was initially cited as evidence against a complete MSP explanation.}"
>
> (Use the actual [239] bib key from `bibliography.bib`; fetch arXiv:1901.07025 from
> InspireHEP for the Song et al. IC modeling.) Check the surrounding §4.3.2 flow and
> §4.4's summary sentences for consistency with the softened claim.

---

### E-4.8 · §4.3.3 — Emphasis on List et al. [221] too strong `[science]` ⬜

**Eckner's point:** The weight given to List et al. is not supported by their results.
Three concerns about robustness:
1. Their astrophysics still relies on the same templates repeatedly shown to have
   mis-modelled features.
2. Their appendix Fig. S12 (PRL manuscript) shows that with a different Galactic diffuse
   model, the whole dN/dF shifts to larger fluxes — compatible with previous results —
   indicating strong sensitivity to background mis-modelling.
3. Their simulator gives *all* point sources the same shared intrinsic spectrum, which is
   unnatural for the Galactic centre's many source classes — forceful mis-modelling that
   will impact the outcome.

*Note:* Eckner explicitly says: "For the thesis, you can build up the claim like this to
make the point for dark matter. Up to you." — so this is a caveat to acknowledge, not a
demand to restructure.

**Response:** ✔ Verified in detail against the arXiv source of List et al. 2025
(arXiv:2507.17804 = `List:2025qbx` = [221]):
1. *Template dependence* — correct: the astrophysical components still come from
   standard diffuse models.
2. *Fig. S12* — confirmed: retraining with diffuse Model A shifts the recovered dN/dF
   almost an order of magnitude brighter, centered near the one-photon line, "roughly
   consistent with the energy independent Model O findings"; the paper itself concedes
   the result "is not independent of the background diffuse model". **Counterweight**
   List et al. would raise: Model A fits the data far worse than their baseline
   (2Δln L ≈ 648), so they frame S12 as a mismodeling stress test, not an equally
   valid alternative. Also, in the *2020* PRL (arXiv:2006.12504) the smooth-emission
   preference survived diffuse-model swaps — Eckner's robustness critique is specific
   to the 2025 energy-dependent result.
3. *Shared intrinsic spectrum* — confirmed verbatim in their simulator description:
   "we assume a common spectrum for all sources".

So all three concerns are factually grounded, with a real counterweight on #2. Given the
author's goal (balanced chapter), the right move is not to drop List et al. but to
present it with its systematic caveats stated as clearly as the NPTF's were — symmetry
of skepticism is exactly what "balanced" means here.

**Action:** ⏳ DEFERRED — substantive pass (core of the chapter rebalance). Strategy for
§4.3.3 (`4.3_systematics_stalemate.tex:85-123`):
- Keep the presentation of the method and result, but add a caveats paragraph
  mirroring the structure used against NPTF earlier in §4.3: (i) same diffuse
  templates → inherited mis-modeling; (ii) diffuse-model sensitivity (S12; state the
  worse-fit counterweight honestly); (iii) shared-spectrum simulator assumption vs the
  GC's mixed source classes.
- Downgrade language that currently reads as settled ("dramatic effect", "This
  consistency reopens…" is already careful — keep that register throughout).
- Re-examine §4.4:41-46 ("connects directly", "converge from independent lines") and
  the thesis conclusion's citation of List:2025qbx so the convergence claim carries the
  same caveats.
- The existing hedge at line 122 ("If the results of this work are confirmed by
  independent studies…") is good — consider moving it earlier so the caveats frame the
  result rather than trail it.

---

### E-4.9 · §4.5.2 — MSP acronym re-introduced `[mechanical]` ⬜

**Eckner's point:** MSP is introduced again in §4.5.2 (see also E-G.1 on global acronym
harmonisation).

**Response:** Confirmed: §4.5.2 = the paper section
`chapter_04/sections/paper_msp/sections/msps_in_globular_clusters.tex:4` re-expands
"millisecond pulsars (MSPs)"; the paper's own introduction
(`paper_msp/sections/introduction.tex:6`) and `4.0_introduction.tex:10` do too.

**Action:** Handle within the E-G.1 acronym sweep (glossary macros make this automatic).

---

### E-4.10 · §4.5.4 — Common (L₀, σ_L) assumption across GCs `[science]` ⬜

**Eckner's point:** At the end of the section, also discuss the assumption that all GCs
and their MSP populations share a common L₀ and σ_L. This needs to be verified, or at
least corrected by average age: MSPs suffer energy losses over time, so populations formed
at different times in different clusters should differ.

**Response:** Legitimate caveat, and §4.5.4
(`chapter_04/sections/paper_msp/sections/comparisons.tex`, closing paragraphs) is indeed
the natural place: the section already discusses whether GC pulsars could differ from
Plane pulsars via the age/spin-down argument, so extending it cluster-to-cluster is one
added paragraph, not new analysis. Two honest replies coexist: (a) the assumption is a
modeling choice the common-LF fit cannot itself verify; (b) the paper's
cluster-to-cluster variation model (§4.5.5, Fig. 3PC-c2c-var) already relaxes the
*number* normalization per cluster — but not (L₀, σ_L) themselves. State both, and note
that age-dependent luminosity corrections would be the next refinement.

**Action:** Add a closing paragraph to `comparisons.tex` (after the Hooper & Linden
comparison), draft:
> \blue{A further assumption implicit in our analysis is that all globular clusters
> share a single luminosity function, with common $L_0$ and $\sigma_L$. This is a
> modeling choice rather than an established fact: clusters formed their pulsars at
> different epochs, and since millisecond pulsars spin down and dim over gigayear
> timescales, populations of different average age should exhibit systematically
> different luminosities. The cluster-to-cluster variation model introduced in
> Section~\ref{<sec-4.5.5-label>} relaxes the normalization of the expected pulsar
> number per cluster, but not the shape parameters of the luminosity function
> themselves. An age-corrected luminosity function, calibrated on cluster formation
> histories, would be the natural refinement of this analysis.}
>
> Note: this modifies integrated-paper text — flag prominently as a thesis-only
> addition (it is an honest extension, not a rewrite of published claims). Ties into
> E-4.12.

---

### E-4.11 · §4.5.5 — Reference for "systematic" radio searches? `[ref]` ⬜

> "Given systematic efforts that have been conducted to search for radio pulsations from
> unassociated Fermi sources, this possibility seems unlikely."

**Eckner's point:** Asks for a reference. To their knowledge there have been a few
*targeted* radio observations towards the bulge (with some detections), but no *systematic*
radio scan. Either cite one or soften the claim.

**Response:** ✔ Verified — Eckner is right and our claim needs softening. The existing
efforts are *targeted*: TRAPUM/MeerKAT observed 79 ML-selected 4FGL unassociated
candidates (2×10 min each, 9 MSPs found; Clark et al., arXiv:2212.08528); Berteaud et al.
(arXiv:2512.16699) deeply observed just 9 bulge candidates, finding 2 MSPs — doubling the
known MSPs within 2° of the GC to ~4. No blind systematic radio survey of the bulge
exists; that is deferred to the SKA. Moreover the targeted searches carry selection
effects that *disfavour* distant, high-dispersion bulge MSPs, so "this possibility seems
unlikely" is stronger than the radio data support. Softening this is a genuine
balance-improving change (the conclusion-chapter mirror of this argument should be
checked too).

**Action:** In `chapter_04/sections/paper_msp/sections/implications_gce.tex:20`, rework:
> Current: "Given systematic efforts that have been conducted to search for radio
> pulsations from unassociated Fermi sources, this possibility seems unlikely."
>
> Proposed: "\blue{Radio follow-up campaigns of Fermi unassociated sources --- most
> recently the targeted TRAPUM searches with MeerKAT~\cite{<Clark2023>,<Berteaud2026>}
> --- have discovered several new MSPs, but they remain pointed observations of selected
> candidates rather than a systematic survey of the bulge, and their selection effects
> disfavour precisely the distant, highly dispersed pulsars an Inner Galaxy population
> would contain. The possibility that many unassociated sources are bulge MSPs is
> therefore constrained but not excluded; a definitive census awaits deeper systematic
> surveys, ultimately with the SKA.}"
>
> Bib to fetch from InspireHEP: arXiv:2212.08528, arXiv:2512.16699. This is
> integrated-paper text — the change softens a published claim, so double-check against
> what the published paper actually says and keep the thesis version clearly marked in
> `\blue{}`.

---

### E-4.12 · §4.5.5 — Cluster-variation scenario is the realistic one `[science]` ⬜

**Eckner's point:** (Supportive.) The discussion of cluster-to-cluster variation effects
is the more realistic assessment — it would be a big surprise if 50+ GCs and their MSPs
behaved identically, if only because of the age/energy-loss argument. Consider leaning
into this.

**Response:** Agree — and leaning into it costs us little: even the
cluster-variation model retains ≥2σ tension (N ≈ 3–30 expected vs 3 candidates), so
presenting it as the headline conservative result *strengthens* credibility rather than
weakening the conclusion. Pairs naturally with the E-4.10 paragraph.

**Action:** In `chapter_04/sections/paper_msp/sections/implications_gce.tex`, at the end
of the cluster-variation paragraph (last paragraph of the file), add:
> \blue{We regard this cluster-to-cluster variation model as the more realistic
> assessment: it would be surprising if more than fifty clusters, with different ages,
> metallicities, and dynamical histories, hosted identically distributed pulsar
> populations --- the spin-down argument alone predicts systematic differences with
> cluster age. That the tension with the Inner Galaxy pulsar census persists even under
> this conservative model is what gives the constraint its weight.}
>
> Also mirror the emphasis in the chapter summary (§4.6 / `summary_conclusions.tex`)
> and the thesis conclusion bullet if they present the common-LF numbers as headline.

---

## General / cross-thesis

### E-G.1 · Acronym harmonisation `[mechanical]` ⬜

**Eckner's point:** Several acronyms are introduced more than once (e.g. MSP again in the
Chapter 4 intro). Go through the thesis and harmonise acronym usage.

**Response:** Confirmed. Grep shows "millisecond pulsars (MSPs)" spelled out at least
four times: `chapter_02/sections/2.2_astrophysical_sky.tex:23` (legitimate first use),
`chapter_04/sections/4.0_introduction.tex:10`,
`chapter_04/sections/4.2_msp_hypothesis.tex:8`, and in the integrated paper
(`paper_msp/sections/introduction.tex:6`, `msps_in_globular_clusters.tex:4` — E-4.9).
The repo has a glossary system (`acronyms.tex`, `\newacro`) and a dedicated `/acronyms`
skill, which is the right tool.

**Policy decision needed:** inside integrated papers, re-expansion is arguably
acceptable (papers are self-contained); elsewhere, first-use-only. Default proposal:
harmonise everywhere, converting to glossary macros so LaTeX handles first-use expansion
automatically.

**Action:** Run the `/acronyms` workflow chapter by chapter (it converts literal
acronyms to glossary macros and extends `acronyms.tex`). Sweep at minimum: MSP, GCE,
NFW, WIMP, NPTF, SCD, CNN, SBI, dSph. Treat as its own batch task after the prose
changes land, to avoid edit conflicts.

---

## Chapter 1 — The Dark Matter Problem

### E-1.1 · §1.4.5 — Narrative too WIMP-centric `[structure]` ⬜

**Eckner's point:** Fine given the thesis scope, but in this *introductory* section one
could at least mention alternatives — primordial black holes, axions/axion-like particles
— noting that the search targets differ for them.

**Response:** Agreed — a single closing paragraph in §1.4.5 (Observational Targets,
`chapter_01/sections/1.4_indirect_detection.tex:309-376`) acknowledging that the target
list above is WIMP-shaped, and that PBHs and ALPs reshuffle it. Chapter 1 likely already
introduces axions/ALPs and PBHs as candidates earlier (§1.2?) — check and cross-reference
rather than re-introduce.

**Action:** Add a closing paragraph to §1.4.5, after line 376, along these lines
(draft; final prose at implementation):
> \blue{The target list above is tailored to WIMP annihilation, and it is worth noting
> that alternative dark matter candidates reshape it. For axion-like particles, the
> observables of choice are spectral irregularities imprinted on bright gamma-ray
> sources by photon--ALP mixing in astrophysical magnetic fields, with galaxy-cluster
> AGN and transient events such as supernovae among the preferred targets (cf.
> Section~\ref{sec:extragalactic_sources}). For primordial black holes, the signature is
> Hawking evaporation, which makes the diffuse MeV background and short gamma-ray bursts
> the relevant channels. The analyses of this thesis remain within the WIMP framework,
> but the statistical methods developed here are largely agnostic to the underlying
> candidate.}
>
> Bib (fetch from InspireHEP if a citation is wanted; optional for an intro aside):
> arXiv:1603.06978 (Fermi-LAT NGC 1275 ALP limits), arXiv:1410.3747 (SN1987A ALP limit).

---

### E-1.2 · §1.4.6 — Why neutrino constraints are weaker `[clarify]` ⬜

**Eckner's point:** In the neutrino paragraph, add the remark that neutrinos interact very
weakly, so *detection* is the challenge (large volumes of material required) — which is
why their constraints are naturally less stringent with the current generation of neutrino
telescopes.

**Response:** Agreed — the current paragraph
(`chapter_01/sections/1.4_indirect_detection.tex:384-387`) states that constraints are
"generally weaker" without giving the reason.

**Action:** In line 387, expand:
> Current: "For galactic targets, however, neutrino constraints remain generally weaker
> than the corresponding gamma-ray bounds, becoming competitive only above roughly
> 1--10 TeV depending on the annihilation channel."
>
> Proposed: "\blue{The same property that makes neutrinos clean messengers, however, is
> also their weakness: their tiny interaction cross section makes detection itself the
> challenge, requiring kilometer-scale instrumented volumes of ice or water to collect a
> handful of events.} For galactic targets, neutrino constraints therefore remain
> generally weaker than the corresponding gamma-ray bounds, becoming competitive only
> above roughly 1--10 TeV depending on the annihilation channel."

---

### E-1.3 · §1.4.6 — Isotropisation length/time scale for CRs `[clarify]` ⬜

**Eckner's point:** When saying charged cosmic rays are randomised by the Galactic
magnetic field (and nearby pulsars explain the positron excess), add a small comment on
the length/time scale of this isotropisation, since *local* directional information about
charged cosmic rays is accessible to some extent.

**Response:** ✔ Verified numbers: the Larmor radius is $r_g \approx 1.1\,\mathrm{AU}
\times (E/\mathrm{TeV})(Z B/\mu\mathrm{G})^{-1}$ — of order $10^{-3}$ pc for a TeV proton
in a μG field, six orders of magnitude below kpc propagation scales, hence the
randomisation. But small residual anisotropies survive and are measured: dipole
amplitudes of $10^{-4}$–$10^{-3}$ from ~100 GeV to PeV (HAWC/IceCube), plus small-scale
structure. Refs: arXiv:1612.08002 (Ahlers & Mertsch review), arXiv:1812.05682
(HAWC+IceCube 10 TeV sky map).

**Action:** In `chapter_01/sections/1.4_indirect_detection.tex:389`, extend the sentence:
> Current: "…galactic magnetic fields randomize their arrival directions, erasing all
> spatial information and leaving only the energy spectrum as the main observable…"
>
> Proposed: "…galactic magnetic fields randomize their arrival directions\blue{: a TeV
> proton gyrates with a radius of order $10^{-3}$~pc, so after propagating over
> kiloparsec distances its arrival direction retains essentially no memory of its
> source. Only weak residual anisotropies, at the $10^{-4}$--$10^{-3}$ level, survive
> at TeV--PeV energies~\cite{<Ahlers-Mertsch>,<HAWC-IceCube>}, leaving} the energy
> spectrum as the main observable…"
>
> Bib to fetch from InspireHEP: arXiv:1612.08002, arXiv:1812.05682 (optional — one of
> the two suffices).

---

### E-1.4 · §1.4.7 — Add recent dwarf-constraint papers to first list `[ref]` ⬜

**Eckner's point:** [129] is cited for dwarf constraints on WIMPs, but more recent papers
cited later in the thesis should be added to this first list for completeness.

**Response:** [129] is almost certainly `Fermi-LAT:2015att` (the 2015 15-dSph combined
analysis). In §1.4.7 it is cited alone at
`chapter_01/sections/1.4_indirect_detection.tex:410`, with the 2024 legacy analysis
(`2024PhRvD.109f3024M`) only in the following sentence; §1.4.5 line 346 already cites
both together.

**Action:** At line 410, change `\cite{Fermi-LAT:2015att}` →
`\cite{Fermi-LAT:2015att,2024PhRvD.109f3024M}` (first mention carries both). Verify
against the compiled PDF that [129] is indeed `Fermi-LAT:2015att`; if it resolves to a
different key, apply the same append-newer-refs fix at that location.

---

### E-1.5 · §1.4.7 — GC ionisation fraction as another anomaly `[ref]` ⬜

**Eckner's point:** Among unresolved anomalies, another curiosity discussed in the DM
context is the unusually high ionisation fraction in the Galactic centre. Pedro De la
Torre Luque has papers linking it to DM.

**Response:** ✔ Verified. The core paper is De la Torre Luque, Balaji & Silk,
*"Anomalous Ionization in the Central Molecular Zone by sub-GeV Dark Matter"*, PRL 134,
101001 (2025), arXiv:2409.07515: MeV-scale DM annihilating to e⁺e⁻ can reproduce the
anomalously high H₂ ionisation rate (~10–100× the disc value, inferred from H₃⁺
observations) in the Central Molecular Zone for cuspy profiles, while evading CMB and
X-ray/gamma-ray bounds, with a possible common origin with the 511 keV line. Companion:
arXiv:2509.17692 (molecular clouds as sub-GeV DM/PBH probes).

**Action:** In §1.4.7 "Unresolved anomalies"
(`chapter_01/sections/1.4_indirect_detection.tex:428-430`), extend the multi-anomaly
sentence at line 430 with one clause:
> \blue{…; and the anomalously high ionisation rate of the molecular gas in the Central
> Molecular Zone, which sub-GeV dark matter annihilating into electron--positron pairs
> could account for~\cite{<DelaTorreLuque-key>}.}
>
> Bib to fetch from InspireHEP: arXiv:2409.07515.

---

### E-1.6 · §1.4.7 — Missing TeV/CTAO outlook paragraph `[structure]` ⬜

**Eckner's point:** As a thesis intro, a paragraph on higher energies is missing. Beyond
the GCE at GeV energies, the entire TeV range for WIMPs is only marginally probed by
current instruments; many minimal DM models can only be tested with CTAO, leaving the TeV
window open. Most of the thesis targets GeV gamma rays, but this high-energy outlook
should be there to complete the overview.

**Response:** ✔ Verified and agreed — this also ties neatly into Chapter 8 (CTAO
cross-correlations), so the paragraph earns its place doubly. Verified anchors: minimal
dark matter (Cirelli, Fornengo & Strumia, hep-ph/0512090) predicts thermal electroweak
multiplets at the TeV scale — higgsino ~1.1 TeV, wino ~2.9 TeV, quintuplet ~13.6 TeV with
Sommerfeld + bound states (arXiv:2107.09688). Current IACTs only marginally reach the
wino and leave the thermal higgsino out of reach (arXiv:2210.03140); CTAO forecasts
order-of-magnitude gains (arXiv:2007.16129, arXiv:2008.00692, arXiv:2507.15937).

**Action:** Add a paragraph to §1.4.7, most naturally inside "The methodological case for
this thesis" block or just before it (after line 449, which already notes "heavier
candidates … remain largely unexplored"). Draft:
> \blue{The open territory is clearest at the highest masses. While Fermi-LAT probes the
> GeV window where the GCE resides, the TeV regime remains only marginally explored:
> electroweak-multiplet candidates such as the higgsino and wino --- among the most
> minimal surviving WIMP realizations --- have thermal masses of $\sim 1$ and
> $\sim 3$~TeV respectively, beyond the comfortable reach of both Fermi-LAT and current
> ground-based telescopes. Closing this window is a primary science goal of CTAO, whose
> Galactic Center observations are forecast to reach the thermal cross section at these
> masses. The forecast developed in Chapter~\ref{ch:8} contributes to this program.}
>
> Bib to fetch from InspireHEP: hep-ph/0512090, arXiv:2007.16129; optionally
> arXiv:2107.09688, arXiv:2008.00692. Check which are already in `bibliography.bib`
> (Ch. 8 likely cites the CTAO sensitivity paper already).

---

## Chapter 2 — The Gamma-Ray Sky and Fermi-LAT

### E-2.1 · §2.1.3 — Dark gas in diffuse-emission uncertainties `[clarify]` ⬜

**Eckner's point:** When discussing Galactic diffuse emission uncertainties, also mention
dark gas on small scales, which cannot be inferred with the typical techniques — neither
via proxies like CO nor directly from emission/absorption lines.

**Response:** ✔ Verified — standard systematic. "Dark gas" (optically thick HI plus
CO-dark H₂, invisible to 21 cm and CO surveys, traced via dust or the gamma rays
themselves) was established by Grenier, Casandjian & Terrier, Science 307, 1292 (2005).
The Fermi interstellar model paper (arXiv:1602.07246) handles it via dust-residual
templates. Our uncertainty paragraph
(`chapter_02/sections/2.1_production_mechanisms.tex:139-141`) mentions the CO-to-H₂
conversion but not dark gas.

**Action:** In `2.1_production_mechanisms.tex:141`, extend:
> Current: "Uncertainties in the gas column densities (particularly the conversion from
> CO emission to molecular hydrogen), the interstellar radiation field, and the
> cosmic-ray propagation parameters all contribute."
>
> Proposed: "Uncertainties in the gas column densities (particularly the conversion from
> CO emission to molecular hydrogen), the interstellar radiation field, and the
> cosmic-ray propagation parameters all contribute. \blue{A further contribution comes
> from \emph{dark gas} --- gas invisible to both the 21~cm line and CO surveys, such as
> optically thick atomic hydrogen and CO-dark molecular hydrogen --- which must be
> traced indirectly through dust emission or through the gamma rays themselves, and
> whose small-scale structure therefore remains poorly constrained~\cite{<Grenier2005>,
> <Acero2016>}.}"
>
> Bib: Grenier, Casandjian & Terrier 2005 has **no arXiv preprint** — search InspireHEP
> by DOI 10.1126/science.1106924; if absent, list for manual addition (authors: I. A.
> Grenier, J.-M. Casandjian, R. Terrier; Science 307 (2005) 1292). arXiv:1602.07246
> fetchable normally.

---

### E-2.2 · §2.2.1 — PWNe/SNRs non-negligible beyond this thesis `[clarify]` ⬜

**Eckner's point:** The claim that PWNe and SNRs are subdominant backgrounds holds for the
thesis topics, but add an aside that beyond them they can become non-negligible (e.g. CTAO
and the Galactic centre).

**Response:** Agreed — one-clause fix at
`chapter_02/sections/2.2_astrophysical_sky.tex:37`, and it foreshadows Chapter 8 nicely.

**Action:** Extend line 37:
> Current: "Among the remaining Galactic gamma-ray sources, supernova remnants and pulsar
> wind nebulae are routinely detected by the Fermi-LAT but represent subdominant
> backgrounds for the dark matter searches undertaken in this thesis."
>
> Proposed: "…undertaken in this thesis. \blue{This is a statement about the GeV sky and
> the targets considered here, not a general one: at TeV energies, where instruments
> like CTAO observe the Galactic Center, pulsar wind nebulae and supernova remnants
> rank among the brightest sources and become non-negligible backgrounds for dark
> matter searches (cf. Chapter~\ref{ch:8}).}"

---

### E-2.3 · §2.2.2 — Transient extragalactic sources missing `[structure]` ⬜

**Eckner's point:** The section entirely misses transient extragalactic gamma-ray
sources, which can be used, e.g., to search for axions.

**Response:** ✔ Verified use case: photon–ALP mixing searches use spectral
irregularities in bright sources (Fermi-LAT NGC 1275, arXiv:1603.06978) and transients —
the ALP-induced gamma-ray burst coincident with core-collapse SN neutrinos (SN1987A
limit: Payez et al., arXiv:1410.3747; extragalactic SNe: Meyer & Petrushevska,
arXiv:2006.06722). §2.2.2 (`chapter_02/sections/2.2_astrophysical_sky.tex:51-91`)
currently covers only steady populations (blazars, misaligned AGN, SFGs). A short
paragraph on GRBs/flares as transient classes, closing with the ALP connection, completes
the census without derailing the section.

**Action:** Add a paragraph after line 74 (before the "Detailed population models…"
synthesis sentence), draft:
> \blue{Beyond these steady populations, the extragalactic sky is punctuated by
> transients. Gamma-ray bursts --- the prompt, seconds-long flashes accompanying
> stellar collapse or compact-object mergers --- and week-long blazar flares
> temporarily outshine every steady source in the sky. Transient and strongly variable
> sources play a marginal role as backgrounds for the population studies of this
> thesis, but they are physics targets in their own right: the spectra of bright
> flaring sources and the gamma-ray counterparts of core-collapse supernovae are used,
> for instance, to search for axion-like particles converting to photons in
> astrophysical magnetic fields~\cite{<ALP-refs>}.}
>
> Bib to fetch from InspireHEP: arXiv:1603.06978, arXiv:1410.3747 (optionally
> arXiv:2006.06722). Cross-link with the E-1.1 paragraph (which references this
> section).

---

## Chapter 3 — Statistical Methods

### E-3.1 · Ch. 3 intro — "Noise-dominated regimes" label misleading `[clarify]` ⬜

**Eckner's point:** A priori, "noise-dominated" suggests statistics-limited analyses with
a weak signal and instrument noise. What the thesis deals with is closer to
*systematics-dominated* (or background-dominated): enough statistics, but the systematic
uncertainty of each component must be controlled. Explain the term right at the start of
the intro to set the stage.

**Response:** He is right that the term is non-standard and, read cold, suggests
photon-starved statistics. Our regimes are background/systematics-dominated: the photons
are plentiful; the astrophysical components are what we cannot model perfectly. Two
options: (a) keep the label but define it explicitly in the first paragraph of the Ch. 3
intro as an umbrella term covering both faint-signal and background/systematics-dominated
regimes; (b) rename throughout (chapter title included) to "background-dominated
regimes". Renaming touches the chapter title, the thesis outline, and cross-references in
other chapters — decide with the author.

**Action:** ⏳ DEFERRED — substantive pass. Affects Ch. 3 title/framing and
cross-references. Proposed default: option (a), one defining paragraph added at the top
of `chapter_03/sections/3.0_introduction.tex`, stating explicitly that the regime is
systematics/background-dominated rather than statistics-limited, and that we use
"noise" in the generalized sense of any emission component that is not the signal.

---

### E-3.2 · Eq. 3.1.5 — TS definition is detection-specific `[clarify]` ⬜

**Eckner's point:** As written, this is specifically the TS used for *source detection* —
say so explicitly. Other TS definitions exist for hypothesis testing depending on the
goal.

**Response:** Agreed — easy fix. The surrounding text already uses source detection as
the example; we make explicit that Eq. (eq:ts) with the globally maximized alternative is
the *detection* TS of Mattox et al., and that the general likelihood-ratio construction
admits other choices of null/alternative depending on the question.

**Action:** In `chapter_03/sections/3.1_inference.tex:76`, after "…the globally maximized
likelihood) \cite{Mattox:1996zz}.", add:
> \blue{In this form, with the null hypothesis representing background only and the
> alternative including an additional source term, the TS is the statistic used for
> \emph{source detection} in gamma-ray astronomy; other choices of null and alternative
> hypotheses define different likelihood-ratio tests, depending on the question being
> asked.}

---

### E-3.3 · §3.1.2 — KL divergence used before being defined `[clarify]` ⬜

**Eckner's point:** In "non-nested model comparison" the Kullback–Leibler divergence
appears with no prior mention. Define it directly or explain it in words (it also
reappears later).

**Response:** Agreed. One explanatory clause in words is enough at this point (the formal
definition can stay where the KL divergence is first used quantitatively, in the SBI
section).

**Action:** In `chapter_03/sections/3.1_inference.tex:108`, rework the AIC sentence:
> Current: "The AIC provides an estimator of the relative Kullback--Leibler divergence
> between each candidate model and the data-generating process, …"
>
> Proposed: "\blue{The AIC provides an estimator of the relative Kullback--Leibler
> divergence --- an information-theoretic measure of the dissimilarity between two
> probability distributions, introduced formally in Section~\ref{sec:3.2} --- between
> each candidate model and the data-generating process, }with the $2k$ term penalising
> additional parameters and thus discouraging overfitting."
>
> (Check that the KL divergence is indeed defined in §3.2; if not, add the one-line
> definition $D_{\mathrm{KL}}(p\,\|\,q)=\int p\ln(p/q)$ here instead.)

---

### E-3.4 · §3.1.3 — Imprecise description of the evidence p(x) `[clarify]` ⬜

**Eckner's point:** Be more precise: the evidence is the probability of seeing the data
across the *full landscape spanned by the model*.

**Response:** Agreed — the current wording ("a normalization constant that integrates the
likelihood weighted by the prior") describes the computation but not the meaning.

**Action:** In `chapter_03/sections/3.1_inference.tex:132`, extend the sentence:
> Current: "…is the evidence, a normalization constant that integrates the likelihood
> weighted by the prior over the full parameter space \cite{bishop}."
>
> Proposed: "…is the evidence\blue{: the total probability of observing the data under
> the model as a whole, obtained by integrating the likelihood, weighted by the prior,
> over the full parameter space spanned by the model \cite{bishop}. Within a single
> model it acts as a normalization constant; across models it quantifies how well each
> model, in its entirety, accounts for the data.}"
>
> The second sentence also sets up the Bayes-factor discussion at line 140 naturally.

---

### E-3.5 · §3.3.2 — Missing space + epistemic uncertainty from initialization `[science]` ⬜

**Eckner's point:** Two items: (1) space missing in "aleatoric (statistical) uncertainty";
(2) epistemic uncertainty also has a component from random initialization of network
weights — people typically train over multiple random seeds and quantify the variability
of results under this change of initialization.

**Response:** (1) Confirmed typo at `chapter_03/sections/3.3_ml_astrophysics.tex:65`:
"(statistical)uncertainty". (2) Correct and standard practice (deep-ensemble literature);
worth one added sentence since Chapter 6 actually uses MC dropout, which approximates
exactly this.

**Action:** In `chapter_03/sections/3.3_ml_astrophysics.tex:65`:
1. Fix "(statistical)uncertainty" → "(statistical) uncertainty".
2. After the sentence defining epistemic uncertainty, add:
> \blue{In deep learning, the epistemic component includes the variability induced by the
> random initialization of the network weights and by the stochastic optimization
> itself: retraining the same architecture from different random seeds yields different
> solutions, and the spread of their predictions is a common empirical estimate of this
> contribution.}
3. Also fix the nearby typo "undertainties" → "uncertainties" at line 67 (spotted while
   reading; not in Eckner's list).

---

## Chapter 5 — Dark Matter Substructures

### E-5.1 · §5.1.2 — 10⁸ M☉ threshold is an infall mass `[clarify]` ⬜

**Eckner's point:** The 10⁸ M☉ threshold for subhalos to accrete baryons should always be
read as mass *at infall/accretion time*. Subhalos lose DM mass over time along their orbit
in the Milky Way.

**Response:** Agreed — a standard and correct precision. Galaxy formation happened when
the halo was still massive; tidal stripping afterwards reduces the present-day mass, so a
visible dwarf can today sit in a subhalo well below the formation threshold.

**Action:** In `chapter_05/sections/5.2_dark_matter_substructure.tex:35`, modify:
> Current: "Above a mass threshold of approximately $10^8\,M_\odot$, a subhalo possesses
> sufficient gravitational potential to accrete and retain baryonic matter, …"
>
> Proposed: "Above a mass threshold of approximately $10^8\,M_\odot$\blue{\ --- to be
> understood as the subhalo mass at infall, since tidal stripping subsequently removes
> dark matter mass along its orbit in the Milky Way ---} a subhalo possesses sufficient
> gravitational potential to accrete and retain baryonic matter, …"
>
> Check the reionization sentence at lines 40–41 stays consistent (those virial-mass
> thresholds refer to the halo mass at the epoch of accretion/reionization as well; no
> change needed there).

---

### E-5.2 · §5.1.2 — Baryonic effects on subhalo survival `[science]` ⬜

> "Baryonic processes also modify the survival of the subhalos themselves."

**Eckner's point:** Yes, but it is mostly just the *gravitational potential* of the
baryons that adds stress and strips mass. Dissipative baryonic processes are not efficient
enough to destroy a subhalo.

**Response:** Agreed, and our own next sentence already names the right mechanisms (tidal
stripping and disk shocking — both gravitational). The topic sentence is just loosely
worded: "baryonic processes" suggests feedback/dissipation when what matters is the
gravitational potential of the baryonic disk and bulge.

**Action:** In `chapter_05/sections/5.2_dark_matter_substructure.tex:51`, rephrase:
> Current: "Baryonic processes also modify the survival of the subhalos themselves."
>
> Proposed: "\blue{The gravitational potential of the baryonic disk and bulge also
> modifies the survival of the subhalos themselves.}"
>
> The following sentence (tidal stripping and gravitational shocks) then reads as an
> explanation rather than a non sequitur.

---

### E-5.3 · §5.3.2 — Typo `[mechanical]` ⬜

**Eckner's point:** "at lest partly" → "at least partly".

**Response:** Confirmed at `chapter_05/sections/5.4_unassociated_sources.tex:53`.

**Action:** Fix the typo (no `\blue{}` needed for pure typo corrections — confirm
preference with author; default: mark it anyway for the supervisor diff).

---

### E-5.4 · §5.4.8 — Empty sub-sub-section `[mechanical]` ⬜

**Eckner's point:** §5.4.8 is empty — or was it meant to be a sub-section?

**Response:** Diagnosed. Compiled §5.4 is the integrated paper
(`chapter_05/sections/5.6_paper_dmhalos.tex`); its subsections come from the paper's
`\section` commands demoted to `\subsection`. §5.4.8 is "Mixture model of gamma-ray
sources and limits on DM annihilation"
(`paper_dm_halos/sections/mixture_model_and_limits.tex:1`), which is immediately followed
by the subsection "Model optimization" at line 4 with no body text — a leftover of the
paper's section→subsection demotion. The same empty-container pattern occurs at §5.4.1
("Statistical analysis", `statistical_analysis.tex:1`→`:4`) and §5.4.5 ("Dark matter
subhalos model", `dm_subhalos_model.tex:1`→`:4`), which Eckner did not flag but should be
fixed consistently.

**Action:** For each of the three container headers, either (a) demote the inner headers
to `\subsubsection` so the container becomes a real parent (preferred — mirrors the
paper's original hierarchy), or (b) add a one-sentence connective lead-in under the
container header. Option (a) is mechanical and safe; adopt it for all three.

---

## Chapter 6 — From Individual Sources to Populations

### E-6.1 · §6.1.1 — "Not a lack of signal strength" phrasing `[science]` ⬜

> "The difficulty is not a lack of signal strength but an excess of competing models:"

**Eckner's point:** Disagrees with the framing — the (limited) excess strength *is* part
of what makes it hard to pin down; it would be much easier if the excess were more
pronounced.

**Response:** Fair. The sentence sets up a false dichotomy: both things are true — the
signal is faint *and* multiple models fit it. The rhetorical point we want (degeneracy,
not detectability, is the bottleneck) survives a more precise phrasing.

**Action:** In `chapter_06/sections/6.1_limits_individual.tex:11`, rephrase:
> Current: "The difficulty is not a lack of signal strength but an excess of competing
> models: the morphology of the excess is equally well described by…"
>
> Proposed: "\blue{The difficulty is not only the limited strength of the signal, which
> would itself be easier to characterize were the excess brighter, but the abundance of
> competing models that describe it equally well:} the morphology of the excess is
> equally well described by…"
>
> (Adjust the tail to avoid repeating "equally well" twice — final wording at
> implementation.)

---

### E-6.2 · Eq. 6.2.1 — Clarify what Γ refers to `[clarify]` ⬜

**Eckner's point:** Be more precise about Γ — probably the *intrinsic* spectrum of each
source, whereas the LAT only ever measures an *observed* spectrum modified by known
processes like EBL absorption.

**Response:** Agreed. The current text says only "a parameter that characterizes the
energy spectrum shape of the source". Since §2.2.2 already discusses EBL attenuation, a
cross-reference is natural.

**Action:** In `chapter_06/sections/6.2_source_count.tex:30`, expand:
> Current: "where $\Gamma$ is a parameter that characterizes the energy spectrum shape of
> the source, …"
>
> Proposed: "where $\Gamma$ is a parameter that characterizes the \blue{\emph{intrinsic}
> energy spectrum of the source (for blazars, typically the photon index of a power
> law); the spectrum we observe differs from the intrinsic one through known propagation
> effects, most notably the attenuation by the extragalactic background light discussed
> in Section~\ref{sec:extragalactic_sources}}, …"

---

### E-6.3 · §6.5.2.1 — One-photon limit is not the floor `[science]` ⬜

> "This lower limit, indeed, is also close to the theoretical sensitivity given by the
> flux of a point source contributing exactly one photon"

**Eckner's point:** Nick Rodd et al. showed that even below the one-photon limit the
non-Poissonian nature of sub-threshold sources is visible; the actual limit is much lower,
< 0.25 photons (arXiv:2107.09070, Fig. 9).

**Response:** ✔ Verified. arXiv:2107.09070 is List, Rodd & Lewis, *"Dim but not entirely
dark: Extracting the Galactic Center Excess' source-count distribution with neural
nets"*, PRD 104, 123022 (2021). Its Fig. 9 caption states that for populations as faint
as 0.25 expected counts per source, more than half of the flux can be distinguished from
Poissonian emission at 95% confidence. Caveat worth keeping in mind: that figure is an
idealized benchmark (single isotropic population, no PSF, delta-function source-count
distribution), so it is an in-principle statistical floor, not a realistic Fermi-map
sensitivity. Our one-photon estimate remains a useful order-of-magnitude anchor; we
should present it as such rather than as "the" theoretical sensitivity.

**Action:** In `chapter_06/sections/paper_dnds/sections/synthetic_map_generation.tex:104`
(note: this is verbatim published paper text — modify with a thesis-note rather than
rewriting, or add a footnote). Proposed footnote/addition after the sentence:
> \blue{We note that the one-photon flux is an indicative rather than a strict floor:
> the collective, non-Poissonian imprint of a sub-threshold population remains partially
> detectable below it, down to $\sim 0.25$ expected photons per source in idealized
> settings~\cite{List:2021aer}.}
>
> Bib key to fetch from InspireHEP: arXiv:2107.09070 (check whether already in
> `bibliography.bib`; the conclusion cites List:2025qbx which is a *different* paper).

---

### E-6.4 · §6.5.2.2 — "Better stability of the neural network" vague `[clarify]` ⬜

> "Furthermore, we also found that fixing Agal provides a better stability of the neural
> network."

**Eckner's point:** Be more precise — what does "more stable" actually mean here?

**Response:** The passage is at
`chapter_06/sections/paper_dnds/sections/synthetic_map_generation.tex:179`. Being precise
requires recalling what was actually observed during training in the paper analysis
(e.g., reduced run-to-run variance of the validation loss? fewer divergent trainings?
smaller spread of predictions across seeds?). Only the author knows; guessing would
fabricate a result.

**Action:** ⏳ DEFERRED — needs author input. Question for the author: in the dNdS paper,
what concretely improved when fixing $A_\mathrm{gal}$ — convergence reliability,
validation-loss variance, or prediction spread? Once answered, replace "provides a better
stability of the neural network" with the specific statement.

---

### E-6.5 · §6.5.2.2 — Broken reference "Appendix 6..6.4" `[mechanical]` ⬜

**Eckner's point:** Weird reference at the bottom of the section.

**Response:** Diagnosed — same root cause as E-6.9. The reference at
`chapter_06/sections/paper_dnds/sections/synthetic_map_generation.tex:185` is
`Appendix \ref{sec:agal-var}`, whose label lives inside the `subappendices` environment
of `6.5_paper_dnds.tex`. The appendix subsection numbering renders as "6..6.x" (empty
appendix-letter field), so the reference inherits the broken number. Fixing E-6.9 fixes
this automatically.

**Action:** Covered by E-6.9; after that fix, recompile and confirm this reference
renders as "Appendix 6.A.4" (or similar).

---

### E-6.6 · p. 173 — Typo `[mechanical]` ⬜

**Eckner's point:** "loose" → "lose".

**Response:** Two instances found in
`chapter_06/sections/paper_dnds/sections/nn_architecture_training.tex` (lines 25 and 35):
"may loose some of the large scale information" and "we partially loose large-scale
information".

**Action:** Fix both: "loose" → "lose".

---

### E-6.7 · §6.5.3.2 — Negative pixels after diffuse subtraction + log `[clarify]` ⬜

> "Finally, each map is parsed into 12 patches using the map2patch algorithm discussed in
> the previous Sections."

**Eckner's point:** Since the diffuse emission is subtracted and logs are taken: how are
negative pixel values treated, and how is the network informed that some pixels are
oversubtracted?

**Response:** A genuine technical question about the paper's preprocessing pipeline
(map2patch, log transform after diffuse subtraction). The answer exists in the paper's
code/appendix but must be stated by the author — e.g., clipping at zero, offset before
log, or symmetric log transform.

**Action:** ⏳ DEFERRED — needs author input (or a look at the paper's preprocessing
code). Once recalled, add one clarifying sentence in
`chapter_06/sections/paper_dnds/sections/nn_architecture_training.tex` (data
pre-processing subsubsection, line 46 ff.) stating how negative/oversubtracted pixels are
handled.

---

### E-6.8 · §6.5.3.4 — Typo `[mechanical]` ⬜

**Eckner's point:** "aleatory" → "aleatoric".

**Response:** Found at
`chapter_06/sections/paper_dnds/sections/nn_architecture_training.tex:75` ("aleatory
error components"). Grep the whole thesis for further instances of "aleatory".

**Action:** Fix to "aleatoric"; sweep `grep -rn aleatory` across all .tex files.

---

### E-6.9 · §6.6 numbering broken `[mechanical]` ⬜

**Eckner's point:** Sections "6..6", "6..6.1", etc. are wrongly numbered.

**Response:** Diagnosed. The paper appendix
(`chapter_06/sections/paper_dnds/sections/appendix_further_tests.tex`) is wrapped in a
`subappendices` environment (`6.5_paper_dnds.tex:15-17`) but uses `\subsection`/
`\subsubsection` headers. Inside `subappendices` the appendix letter attaches at the
*section* level; with only subsections present, the letter field stays empty and the
counter renders as "6..6". Note the Chapter 5 paper appendices
(`5.6_paper_dmhalos.tex:15-17`) use `\section` inside `subappendices` — check how those
render (likely correctly as "5.A" etc.) and mirror that pattern.

**Action:** In `appendix_further_tests.tex`, promote `\subsection{Further Tests}` →
`\section{Further Tests}` and each `\subsubsection` → `\subsection`, matching the
Chapter 5 convention. Recompile and verify the appendix numbers ("6.A", "6.A.1", …) and
the E-6.5 cross-reference.

---

## Chapter 7 — Probabilistic Cataloging

### E-7.1 · §7.1.2 — DR3→DR4 source changes also reflect new diffuse model `[science]` ⬜

**Eckner's point:** The final paragraph attributes source changes from 4FGL-DR3 to DR4 to
the catalog update, but DR4 is also based on a *different Galactic diffuse model*: the
collaboration performed a global fit of gll_iem_v07 with patchwise spectral variations
following a log-parabola. Sources vanishing and appearing is thus also related to a
different background treatment.

**Response:** ✔ Verified against the DR4 paper (arXiv:2307.12546, Sec. 2.2). DR4 keeps
gll_iem_v07 but rescales it with a log-parabola modulation fitted per region of interest
and then smoothly interpolated across the sky; the paper explicitly quantifies the effect
on sources (significance up 0.02σ on average, 71 more sources above threshold, 245 fewer
curved spectra). One nuance: our thesis paragraph
(`chapter_07/sections/7.1_limits_of_threshold.tex:46-50`) actually discusses sources
dropping below threshold *in DR3* (cite Fermi-LAT:2022byn), not DR3→DR4 — Eckner's
recollection of the passage is slightly off, but his underlying point applies to any
cross-release comparison: source appearance/disappearance reflects both longer exposure
and changed background treatment.

**Action:** In `chapter_07/sections/7.1_limits_of_threshold.tex`, after line 49 (the
"structural problem" sentence), add:
> \blue{Catalog-to-catalog comparisons entangle a second effect as well: successive
> releases refine the background treatment itself. In 4FGL-DR4, for instance, the
> Galactic interstellar emission model was rescaled through a spatially varying
> log-parabola modulation fitted across the sky, and this change alone pushed tens of
> sources across the detection threshold~\cite{<DR4-key>}. A source's presence in a
> catalog therefore depends not only on its flux history but also on the evolving model
> of the sky beneath it.}
>
> Bib: check whether arXiv:2307.12546 (4FGL-DR4) is already in `bibliography.bib`; if
> not, fetch from InspireHEP. This addition also strengthens the chapter's motivation
> (threshold decisions are model-dependent), so it earns its place.

---

### E-7.2 · §7.2.2 — Typo `[mechanical]` ⬜

**Eckner's point:** "more spurious directions" → probably "detections".

**Response:** Partly deliberate: the paper's output is a map of "firing pixels"
(directions), not detections — the surrounding text
(`chapter_07/sections/7.2_population_to_spatial.tex:67-75`) makes exactly this
distinction. But "spurious directions" without that context reads as a typo. Note the
conclusion uses the same phrase (`conclusion/conclusion.tex:124`).

**Action:** In `7.2_population_to_spatial.tex:67`, rephrase to keep the concept but drop
the odd noun: "…at the cost of more \blue{false-positive directions, i.e., firing pixels
not associated with any real source}." Keep the conclusion's phrasing consistent with
whatever final wording is chosen.

---

### E-7.3 · §7.3.4 — Typo `[mechanical]` ⬜

**Eckner's point:** "starts to loose sensitivity" → "lose".

**Response:** The phrase is in the chapter 7 paper section (grep found the ch6 instances;
this one is in `chapter_07/sections/7.4_paper_dnds_catalog.tex` — locate at
implementation with `grep -n "loose" chapter_07 -r`).

**Action:** Fix "loose" → "lose"; include in the same whole-thesis "loose/lose" sweep as
E-6.6.

---

## Chapter 8 — Cross-Correlations and Future Prospects

### E-8.1 · §8.2.2 — Garbled sentence `[mechanical]` ⬜

> "the cosmic-ray rejection rate is difficult to perform"

**Eckner's point:** Word-choice issue — cosmic-ray *rejection* can be difficult to
perform, not the *rate*.

**Response:** Confirmed at `chapter_08/sections/8.2_cross_correlation_technique.tex:53`.

**Action:** Rephrase:
> Current: "For a ground-based instrument like CTAO, the cosmic-ray rejection rate is
> difficult to perform, so $C_N$ is dominated by…"
>
> Proposed: "\blue{For a ground-based instrument like CTAO, rejecting the charged
> cosmic-ray background is difficult --- a residual contamination always survives the
> gamma/hadron separation cuts ---} so $C_N$ is dominated by…"

---

## Meta comments — AI-sounding phrasing `[style]`

Eckner notes that some phrases in the non-paper chapters (intros, conclusion) read as
clearly AI-generated. Explicitly: "You do not have to do anything, I just list some
occasions" — but flagged instances are worth fixing.

### E-M.1 · §3.1.1 — "formalized" ⬜

**Eckner's point:** "The connection between parameters and data is *formalized* ..." —
odd word choice; "established" might work better.

**Response:** Accept the suggestion. Note the identical construction also appears at
`chapter_02/sections/2.2_astrophysical_sky.tex:77` ("The connection between resolved
source catalogs and the unresolved background is formalized by the source-count
distribution") — fix both for consistency. Add "formalized (in this construction)" to the
vocabulary watch-list.

**Action:**
1. `chapter_03/sections/3.1_inference.tex:17`: "is formalized by" → "\blue{is established
   by}".
2. `chapter_02/sections/2.2_astrophysical_sky.tex:77`: "is formalized by" → "\blue{is
   made quantitative by}" (avoids repeating "established" and fits the dN/dS context).

---

### E-M.2 · Conclusions — bullet-point list quirks ⬜

**Eckner's point:** The bullet-point list in the conclusions is full of LLM-favoured word
choices and quirks; "The delivery mechanism ..." in particular sounds odd and unnatural.

**Response:** The flagged phrase is at `conclusion/conclusion.tex:59` ("The delivery
mechanism --- globular clusters spiraling into the Inner Galaxy and dissolving under
tidal forces --- is well understood"). "Delivery mechanism" is logistics language;
"deposited population" a few lines later has the same flavour. Rather than spot-fixing
one phrase, the whole conclusions bullet list deserves a humanizer pass in fresh context
(per the project's review-in-fresh-context rule).

**Action:**
1. Immediate fix at line 59: "The delivery mechanism" → "\blue{The astrophysical
   pathway}" or restructure: "\blue{How the pulsars got there is well understood:
   globular clusters spiral into the Inner Galaxy and dissolve under tidal forces…}".
2. Dispatch the `humanizer` skill on `conclusion/conclusion.tex` (and the chapter
   intros Eckner refers to) as an independent subagent task; review its diff before
   accepting. Extend the vocabulary blacklist with confirmed vetoes from that pass.

---

## Summary table

| ID | Section | Type | Status | Note |
|----|---------|------|--------|------|
| E-4.1 | 4.1.4 | science | ⏳ | core rebalance: prediction → consistency |
| E-4.2 | 4.1.4 | science | 🟡 | verified: local ρ⊙ ≥ 0.4 favoured |
| E-4.3 | 4.2.1 | science | ⏳ | joint with E-4.6 (skyFACT scoping) |
| E-4.4 | 4.2.2 | clarify | 🟡 | name the two replenishment channels |
| E-4.5 | 4.2.2 | structure | ⏳ | move deposition mechanism into Ch. 4 |
| E-4.6 | 4.3 | science | ⏳ | joint with E-4.3 |
| E-4.7 | 4.3.2 | science | 🟡 | verified: IC tail natural for MSPs |
| E-4.8 | 4.3.3 | science | ⏳ | verified incl. S12; core rebalance |
| E-4.9 | 4.5.2 | mechanical | 🟡 | folded into E-G.1 |
| E-4.10 | 4.5.4 | science | 🟡 | common (L₀,σ_L) caveat paragraph |
| E-4.11 | 4.5.5 | ref | 🟡 | verified: searches targeted, not systematic |
| E-4.12 | 4.5.5 | science | 🟡 | lean into cluster-variation model |
| E-G.1 | global | mechanical | 🟡 | /acronyms sweep, batch task |
| E-1.1 | 1.4.5 | structure | 🟡 | PBH/ALP closing paragraph |
| E-1.2 | 1.4.6 | clarify | 🟡 | why neutrino bounds are weaker |
| E-1.3 | 1.4.6 | clarify | 🟡 | verified: r_g ~ mpc, anisotropy 10⁻⁴–10⁻³ |
| E-1.4 | 1.4.7 | ref | 🟡 | append newer dwarf refs at first cite |
| E-1.5 | 1.4.7 | ref | 🟡 | verified: CMZ ionisation, 2409.07515 |
| E-1.6 | 1.4.7 | structure | 🟡 | TeV/CTAO outlook paragraph |
| E-2.1 | 2.1.3 | clarify | 🟡 | dark-gas sentence + Grenier 2005 (no arXiv) |
| E-2.2 | 2.2.1 | clarify | 🟡 | PWNe/SNR aside for TeV |
| E-2.3 | 2.2.2 | structure | 🟡 | transients paragraph + ALP refs |
| E-3.1 | ch3 intro | clarify | ⏳ | define/rename "noise-dominated" |
| E-3.2 | eq 3.1.5 | clarify | 🟡 | mark TS as detection TS |
| E-3.3 | 3.1.2 | clarify | 🟡 | KL in words + forward ref |
| E-3.4 | 3.1.3 | clarify | 🟡 | evidence = prob. of data under model |
| E-3.5 | 3.3.2 | science | 🟡 | typo + seed-variability sentence |
| E-5.1 | 5.1.2 | clarify | 🟡 | mass-at-infall clause |
| E-5.2 | 5.1.2 | science | 🟡 | baryonic → gravitational potential |
| E-5.3 | 5.3.2 | mechanical | 🟡 | typo |
| E-5.4 | 5.4.8 | mechanical | 🟡 | demote inner headers (3 sites) |
| E-6.1 | 6.1.1 | science | 🟡 | drop false dichotomy |
| E-6.2 | eq 6.2.1 | clarify | 🟡 | Γ intrinsic vs observed + EBL xref |
| E-6.3 | 6.5.2.1 | science | 🟡 | verified: 0.25-photon floor, add footnote |
| E-6.4 | 6.5.2.2 | clarify | ⏳ | needs author: what "stability" meant |
| E-6.5 | 6.5.2.2 | mechanical | 🟡 | fixed by E-6.9 |
| E-6.6 | p. 173 | mechanical | 🟡 | 2× loose→lose |
| E-6.7 | 6.5.3.2 | clarify | ⏳ | needs author: negative-pixel handling |
| E-6.8 | 6.5.3.4 | mechanical | 🟡 | aleatory→aleatoric + sweep |
| E-6.9 | 6.6 | mechanical | 🟡 | subappendices sectioning fix |
| E-7.1 | 7.1.2 | science | 🟡 | verified: DR4 diffuse change; add sentence |
| E-7.2 | 7.2.2 | mechanical | 🟡 | rephrase "spurious directions" |
| E-7.3 | 7.3.4 | mechanical | 🟡 | loose→lose sweep |
| E-8.1 | 8.2.2 | mechanical | 🟡 | rephrase CR rejection sentence |
| E-M.1 | 3.1.1 | style | 🟡 | formalized→established (2 sites) |
| E-M.2 | conclusions | style | 🟡 | fix + humanizer pass on conclusions |

**Counts:** 38 proposed (🟡) · 8 deferred (⏳): E-4.1, E-4.3, E-4.5, E-4.6, E-4.8
(chapter-4 rebalance), E-3.1 (terminology), E-6.4, E-6.7 (need author input).
