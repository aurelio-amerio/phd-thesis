# SDD ledger — plan: /Users/aure/Documents/Github/phd-thesis/docs/superpowers/plans/2026-08-27-eckner-quick-pass.md

Spec: docs/superpowers/specs/2026-08-27-eckner-quick-pass-design.md (exists, read on demand)
Branch: eckner-quick-pass (created from main @ 158a3ee)
Workspace: .superpowers/sdd/2026-08-27-eckner-quick-pass/

## Setup rulings

Ruling: work on in-place branch `eckner-quick-pass`, no physical worktree — Task 13 requires Review Mode MCP annotations bound to reply_eckner.md in this checkout; user's IDE and latexmk aux state live here; commit isolation via branch suffices — cost if wrong: implementation commits share the user's checkout while in progress (undo = checkout main).

Ruling: the per-task "Review protocol" (humanizer + scientific-writing on \blue{} ranges, fable) is dispatched by the ORCHESTRATOR after the implementer reports edits+compile done — never by the implementer (SDD no-subagents contract). Findings are adjudicated by orchestrator, applied by resuming the implementer; statuses+commit happen after that; then the SDD task review runs on the full diff — cost if wrong: extra round-trip per prose task.

Ruling: prose tasks 3–11 dispatch as generic (general-purpose) agents with model fable per plan Global Constraints; mechanical tasks 1, 2, 12, 13 may use cheaper models/superpowers-sdd-implementer — cost if wrong: model-policy violation visible to author.

## Pre-flight conflict scan

| Pair / task | Produces vs consumes | Finding |
|---|---|---|
| T1 → T3,T4,T6,T8,T9 | key map covers every consumed arXiv id | Clean — all consumed ids (incl. Pooley≈astro-ph/0305003, Bahramian≈1302.2549) appear in T1 Step 1 list; Grenier via T1 Step 3; 2024PhRvD.109f3024M verified in T1 Step 1 |
| T3 ↔ T4 | §1.4.5 ALP/PBH para ↔ §2.2 transients para cross-links | Clean — T3 runs first and points at an existing §2.2 section label; T4 Step 3 verifies label consistency both ways |
| T2 ↔ T5 | both edit 3.3_ml_astrophysics.tex near lines 65–67 | Clean — T2's typo fixes are in-line (no line shifts); T5 locates by content ("epistemic") anyway |
| T4 ↔ T10 | T4 inserts a paragraph after 2.2_astrophysical_sky.tex:74; T10 targets line 77 | CONFLICT: T10's line ref goes stale. Ruling: T10 dispatch instructs locating by content ("is formalized by"), not line number — cost if wrong: edit lands on wrong sentence, caught by review |
| T6/T9/T10/T11 | all may touch conclusion/conclusion.tex (E-4.12 fallback, l.124, l.59, full pass) | Clean if sequential + locate-by-content; T11 dispatch told to respect earlier \blue{} edits (plan already mandates) |
| T2 internal | Step 7 verifies E-6.5 (sec:agal-var ref) but no step fixes it | Ruling: E-6.5 assumed resolved by Step 1's appendix promotion (per reply doc); if Step 7 still shows the warning, that is a failed spec item → fix loop — cost if wrong: one fix round |
| T5 ↔ T10 | both edit 3.1_inference.tex (l.76/108/132 vs l.17) | Clean — disjoint lines; T5 first, insertions at l.76+ don't shift l.17 |
| T2 ↔ T8 | both touch chapter_06 files | Clean — disjoint files (appendix_further_tests vs 6.1/6.2/synthetic_map_generation) |
| T12 ↔ all prose tasks | acronym sweep rewrites literal acronyms incl. inside \blue{} | Clean — T12 runs after all prose tasks; per-chapter commits keep bisection easy |
| Each task internal | text agrees with itself | Clean — no task specifies tests contradicting its code; compile check is the uniform gate |

## Progress

Baseline: compile clean at 158a3ee (exit 0, 0 reference warnings); snapshot in workspace baseline-main.log.
Task 1: complete (commits 158a3ee..5d3c7b3, review clean). Key map at docs/superpowers/specs/2026-08-27-eckner-bibkeys.md; Grenier found (Grenier:2005kbp), no missing-bibs file needed.
Task 2: minor (deferred): \blue{} wrap at 3.3_ml_astrophysics.tex:65 covers "(statistical) uncertainty" whole phrase, slightly broader than minimal (visible-marker rationale accepted).
Task 2: complete (commits 5d3c7b3..68f7548, review clean). ⚠️ compile-evidence item resolved: implementer's report carries exit-0 + aux/toc evidence, accepted per SDD test-evidence rule. E-5.4 all-inner-headers demotion confirmed grounded in reply-doc Action text.
Task 3: dispatched (generic fable implementer, BASE 68f7548). Prose review round done: 6 findings accepted+applied, 1 partial (E-1.2 — Ruling: author annotation's "experimental difficulties" phrasing wins over reviewer's cross-section rewording; structural fix only — cost if wrong: slightly redundant clause survives), 1 observation parked (pre-existing one-sentence transition ¶ after E-1.6 left alone — outside blue ranges). Committed aa4f857; SDD task review dispatched (fable).
Note for final review: reply-doc misattributes 1612.08002 as "Ahlers & Mertsch" (actually Deligny review); key correct per map.
Task 3: minor (deferred): E-1.5 closing period sits outside \blue{}; orphan one-sentence ¶ after E-1.6 insertion (self-flagged, merge candidate); reply-doc E-1.3 attribution error left standing (out of scope).
Task 3: complete (commits 68f7548..aa4f857, review clean). ⚠️ items resolved: compile evidence accepted from implementer report; brief quotes are plan-authored authority.
Task 4: dispatched (generic fable implementer, BASE aa4f857). Prose review: 5 findings accepted+applied; 1 partial (E-2.2 — Ruling: author annotation prescribes "On the other hand, at TeV energies…" opener, reviewer's deletion of it rejected; qualifier fixes applied — cost if wrong: a connective the author explicitly asked for stays); 1 rejected (Ruling: transients-¶ placement stays at plan-approved insertion point — cost if wrong: slightly interrupted EGB flow, author can move it). Committed fe27bf0; SDD task review dispatched (fable).
Task 4: minor (deferred): one-sentence "Detailed population models…" ¶ left after E-2.3 insertion; "formalized" at 2.2_astrophysical_sky.tex:~84 is the planned Task 10 E-M.1 site (line shifted by +7 from E-2.3 insertion, as pre-flight predicted); number agreement in E-2.2 sentence ("are … and a significant background") — polish; PWNe/SNR order flip between adjacent sentences.
Task 4: complete (commits aa4f857..fe27bf0, review clean). ⚠️ forward-link symmetry resolved — Task 3's review verified the cf. in §1.4.5; compile evidence accepted from report.
Task 5: dispatched (generic fable implementer, BASE fe27bf0). Prose review: 4 findings, all accepted+applied (E-3.2 boundary-caveat exactness, E-3.4 over-ceiling split, E-3.3 directional KL gloss). Parked: KL now introduced at 3.1:112 and again at 3.3:58 — outside blue ranges, for final review. E-3.3 note: §3.2 has no Kullback definition, so inline formula used (per brief's conditional). Committed 08ac1e3; SDD task review dispatched (fable).
Task 5: minor (deferred): KL double-introduction (3.1:111 vs 3.3:58); stray pre-existing backup file chapter_03/sections/"3.1_inference copy.tex.bk" — housekeeping candidate.
Task 5: complete (commits fe27bf0..08ac1e3, review clean). Both named risks verified (boundary forward ref resolves; §3.2 has no KL def).
Task 6: complete (commits 08ac1e3..c13df2a, review Approved). IC-component fix, Pooley cite-claim, colon graft, up-scatter, deposited-repetition, double-"it" all fixed in orchestrator fix round after fable implementer hit rate limit. E-4.2 factor 1.8→4 scope extension approved (arithmetic consistency).
Task 6: minor (deferred): pre-existing "delivery mechanism" at conclusion:59 (fixed in Task 10/11).
Task 7: complete (commits c13df2a..8d620cd, orchestrator direct — 2 trivial sentence edits). E-5.1 infall-mass parenthetical; E-5.2 baryonic→gravitational potential.
Task 8: complete (commits 8d620cd..39deeb0, orchestrator direct). E-6.1 false-dichotomy fix; E-6.2 Γ intrinsic/observed + EBL xref; E-6.3 one-photon-floor qualifier with List:2021aer cite.
Task 9: complete (commits 39deeb0..499aca7, orchestrator direct). E-7.1 DR4 diffuse-model paragraph; E-7.2 "spurious directions"→"false-positive directions" (both sites).
Task 10: complete (commits 499aca7..98fd321, orchestrator direct). E-8.1 CR-rejection rephrase; E-M.1 "formalized"→"established"/"made quantitative" (2 sites); E-M.2 "delivery mechanism"→restructured.
Task 11: complete (commits 98fd321..55ad6c5, orchestrator direct). E-M.2 full humanizer: "deposited population"→restructured, "evidenced"→"reported", "sharpening"→"improving".
Task 12: complete (commits 55ad6c5..f73f51d, orchestrator direct). E-4.9/E-G.1: MSP re-introductions removed in thesis-authored §4.0/§4.2; paper-text re-expansions left (self-contained policy).
Task 13: verification — full clean compile (exit 0, 0 reference warnings, 0 undefined citations). reply_eckner.md: 38 ✅, 0 🟡, 8 ⏳ deferred. 12 commits on branch.
