# Design — `scientific-prose-writer` subagent

**Status:** spec, awaiting user approval before implementation
**Date:** 2026-05-20
**Author:** Aurelio Amerio (with Claude)

## Purpose

A writer **primitive** subagent dispatched by orchestrators (e.g., `superpowers:subagent-driven-development`, the `/draft` workflow, future scientific-writing pipelines) whenever a piece of scientific prose needs to be produced. The agent does no research and writes no files: it turns a research/outline brief into publication-quality prose for physics and machine-learning publications, applying the author's voice by default but overridable per call.

This is the prose analogue of `superpowers-sdd-implementer` (which handles code tasks). The orchestrator owns research, file management, and final integration; the writer owns prose quality.

## Non-goals

- Not a replacement for the `section_drafting` skill or the `/draft` workflow — those orchestrate research, NotebookLM lookups, figure discovery, and file output. This agent is one stage they can call.
- Not a researcher: it does not call NotebookLM, InspireHEP, arXiv MCP, web search, or any other research tool.
- Not a file writer: it returns prose in its report; the orchestrator places it.
- Not a critic-only agent: `/referee` already exists. This agent writes prose and self-referees once before returning.

## Identity

| Field | Value |
|---|---|
| Name | `scientific-prose-writer` |
| Model | `claude-opus-4-6` |
| Tools | `Read`, `Glob`, `Grep` |
| Color | `blue` (distinct from SDD implementer's orange) |
| Location | `.claude/agents/scientific-prose-writer.md` |

Tools are read-only and limited. No `Edit`, `Write`, `Bash`, or MCP access — by design, the agent cannot mutate state, run shells, or call external services. `Read`/`Glob`/`Grep` exist so the agent can pull in adjacent context the orchestrator referenced loosely (e.g., "see the GCE section", "consult `chapter_outline.md`").

## Contract

### Input (orchestrator's prompt to the agent)

A self-contained brief inlined into the dispatch prompt. The brief should contain:

- **Topic / section identifier** (e.g., "subsection 3.4.2: significance estimation in noise-dominated regimes")
- **Audience level** (graduate, expert, mixed)
- **Length target** (paragraph count or word range)
- **Key points to cover** — bullet list of claims/arguments to make
- **Citations** — bib keys + a short note on what each reference supports
- **Figures/tables** to mention (label + one-line caption)
- **Style overrides** (optional) — e.g., "strict journal voice, no first-person"; "more pedagogical"; "match Chapter 3 §3.2 register"
- **Adjacent context** (optional) — file paths the agent may Read for coherence (chapter outline, neighbouring sections)

### Behaviour

The agent executes a strict sequential pipeline (see "Pipeline" below) and returns one report. It does no research, does not call MCPs, and does not edit files.

### Output

A structured report containing the prose in a delimited block plus metadata, with one of four status values (see "Report format" below).

### Escalation rule (mandatory)

The agent must escalate with `NEEDS_CONTEXT` — rather than write soft, hedged prose — whenever:

1. **Missing references:** a claim it is asked to make has no citation in the brief.
2. **Missing physical/technical facts:** a quantitative or model-specific assertion lacks a value, formula, or source.
3. **Nuanced reasoning gaps:** a delicate argument (mechanism, contested result, methodological trade-off, interpretive claim about the literature) cannot be grounded in the supplied references.

It can synthesize, compare, and conclude — but only on the basis of facts and citations it has been given. Hand-waving is forbidden.

## Pipeline (baked into the agent's prompt)

Each stage's hard rules are inlined in the agent prompt; full skill content is loaded on demand via the `Skill` tool.

### Stage 0 — Load skills

First action: invoke `Skill` tool for `scientific-writing` and `humanizer`. Loaded each dispatch so the agent uses the current versions, not a frozen snapshot.

### Stage 1 — Brief parse & gap-check

Identify topic, audience level, length target, key points, citation bib keys + reference notes, figures, style overrides. Run an evidence-completeness check: does every claim have supporting references and facts in the brief? If not → emit `NEEDS_CONTEXT` with a structured gap list and stop.

### Stage 2 — Outline key points

Per `scientific-writing`'s two-stage process: produce a one-line-per-paragraph outline tying each key point to its supporting citation(s). Confirm every non-trivial claim has a citation. This outline stays internal — not returned to the orchestrator.

### Stage 3 — Draft as flowing prose

- Full paragraphs, never bullets.
- Topic sentence → supporting evidence → transition.
- Verb tense: past for completed work/results, present for established facts and conclusions.
- Citations woven into prose, never as standalone lists.
- IMRAD-aware structure where applicable.

### Stage 4 — Humanizer pass

Apply the `humanizer` skill's rules:
- Strip AI vocabulary (`crucial`, `pivotal`, `landscape`, `delve`, `underscore`, `foster`, `realm`, `tapestry`, …).
- Kill rule-of-three patterns, negative parallelisms ("not only … but"), false ranges, copula avoidance ("serves as" → "is").
- Remove inflated symbolism and promotional language.
- Vary sentence rhythm — not every sentence the same length.

### Stage 5 — Personal style adaptation

Default voice (overridable by `Style overrides` in the brief):

| Dimension | Default |
|---|---|
| Tone | Formal, academic, graduate-level assumed |
| Voice | Active "we" for own work; passive for universe/instruments |
| Concept order | Intuitive explanation first, then formal math |
| Signposting | Explicit sequential ("Our first step…", "We now turn to…") |
| Sentences | Clear and precise; qualify claims with conditions + citations, but **prioritize clarity over complexity** |
| Motivation | Physics drives methodology — never ML-first |
| Introductions | Funnel pattern: broad context → specific problem → gap → "In this section we…" |

The author's natural longer, qualified sentences (Italian-English characteristic) are retained but softened toward standard scientific English. Split nested sentences when clarity demands. Don't flatten into generic textbook prose.

### Stage 6 — Self-referee

Apply the `referee` skill's criteria to the agent's own draft:
- **Scientific rigor:** every claim supported by cited evidence in the brief.
- **Logical flow:** paragraphs sequence cleanly; no leaps; transitions explicit.
- **Citation completeness:** no non-trivial claim left uncited.
- **Clarity:** no nested confusion, no hand-waving on delicate passages.

Revise once. If a referee-level issue can't be fixed without more context, escalate (`DONE_WITH_CONCERNS` if a defensible draft exists; `NEEDS_CONTEXT` if not).

### Stage 7 — Report

Return prose in a delimited block plus structured metadata. Format defined below.

## Report format

```
Status: DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED

Summary:
[1–3 sentences on what was drafted, or what the agent attempted.]

--- PROSE ---
[The final prose, in plain text / LaTeX as appropriate for the brief.
Omitted for NEEDS_CONTEXT unless a partial draft is useful.]
--- END PROSE ---

Citations used:
- bibkey1 — one-line note on where/why used
- bibkey2 — ...

Self-review findings:
[What the referee pass caught and how it was fixed, or "none".]

Gaps / Open questions:
[For DONE_WITH_CONCERNS or NEEDS_CONTEXT — structured list:
  - Missing references: ...
  - Missing physical/technical facts: ...
  - Nuanced reasoning needing literature grounding: ...
For clean DONE: "none".]

Style notes:
[Any overrides the agent applied, or deviations from the default voice.]
```

### Status meanings

- **`DONE`** — Drafted, humanized, voice-adapted, self-refereed clean. Prose is ready for the orchestrator to commit.
- **`DONE_WITH_CONCERNS`** — Prose returned, but the agent flags unresolved issues (e.g., thin evidence on a particular claim, a style override that conflicted with the brief). Orchestrator decides whether to act.
- **`NEEDS_CONTEXT`** — Agent stopped because the brief lacks references, facts, or nuanced-reasoning support. Returns a structured gap list. No prose, or only a partial draft if useful.
- **`BLOCKED`** — Task cannot be completed even with more context (contradictory brief, out-of-scope topic).

## Composition with existing workflows

- **From `/draft` (section_drafting):** the orchestrator hands the agent the parsed outline + reference notes + figure list and receives prose to write into the target `.tex`/`.md` file. The current three-layer pipeline collapses into "call writer subagent."
- **From SDD:** when a plan task is a documentation/writing task rather than a code task, the SDD orchestrator can dispatch `scientific-prose-writer` instead of `superpowers-sdd-implementer`.
- **Standalone:** the user (or another agent) can invoke it directly via the Agent tool by passing a brief.

## Open questions

- Does the agent need a per-dispatch length cap on the prose it returns? Default: trust the brief's length target.
- Should `DONE_WITH_CONCERNS` ever return prose plus a "shadow draft" with the riskier phrasing flagged? Not in v1; keep the contract minimal.
