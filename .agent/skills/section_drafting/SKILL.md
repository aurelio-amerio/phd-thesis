---
name: section_drafting
description: Use when writing actual thesis prose for a specific section or subsection. Orchestrates research, drafting with scientific-writing principles, humanization, and personal style adaptation. Callable via /draft X.Y or /draft X.Y.Z.
---

# Thesis Section Drafting

Writes thesis prose for a specific section (X.Y) or subsubsection (X.Y.Z). Orchestrates NotebookLM research, drafting, and iterative refinement through a three-layer writing pipeline.

## Target Notebook

- **Name**: `thesis references`
- **ID**: `1b7df790-7858-4fc8-879c-39f41238c4ae`

## Prerequisites

- A target chapter directory (e.g., `chapter_01`) with `chapter_outline.md` and `references.md` already produced
- `outline.md` (root thesis outline)
- The `source_registry` skill must be called once per conversation before this skill

## Writing Pipeline (Three Layers)

All prose passes through three layers in sequence:

### Layer 1: `scientific-writing` (Primary Driver)

**REQUIRED BACKGROUND**: Load the `scientific-writing` skill (in `scientific-skills/`) before writing any prose.

Use it for:
- **Two-stage process**: outline key points from research → convert to flowing paragraphs
- **Paragraph coherence**: topic sentence → supporting evidence → transition
- **Verb tense**: past for completed work/results, present for established facts and conclusions
- **Conciseness and precision**: apply principles from `writing_principles.md`
- **Citation integration**: weave `\cite{}` naturally into prose, never as standalone lists

### Layer 2: `humanizer` (Anti-AI Pass)

After the initial draft, check against the `humanizer` skill's anti-patterns:
- Strip AI vocabulary ("crucial", "pivotal", "landscape", "delve", "underscore", "foster")
- Remove rule-of-three patterns, negative parallelisms ("not only…but"), false ranges
- Kill copula avoidance ("serves as" → "is")
- Remove significance inflation and promotional language
- Ensure varied sentence rhythm — not all sentences the same length

### Layer 3: Personal Style Adaptation

Apply the author's voice while prioritizing clarity:

| Dimension | Style |
|---|---|
| **Tone** | Formal, academic, graduate-level assumed |
| **Voice** | Active "we" for own work; passive for universe/instruments |
| **Concepts** | Intuitive explanation first, then formal math |
| **Transitions** | Explicit sequential signposting ("Our first step…", "We now turn to…") |
| **Sentences** | Clear and precise. Qualify claims with conditions + citations, but **prioritize clarity over complexity** |
| **Motivation** | Physics always drives methodology — never ML-first |
| **Introductions** | "Funnel": broad context → specific problem → gap → "In this chapter we…" |

**Style balance**: The author writes naturally with longer, qualified sentences (Italian-English characteristic). **Retain this personal voice** but **soften toward standard scientific English**. Don't flatten into generic textbook prose — keep the personality — but prefer clarity when a sentence becomes too nested. Split complex sentences when it improves readability without losing voice.

**Per-chapter overrides**: If `chapter_outline.md` contains a `## Style Notes` section, apply those overrides (e.g., "more pedagogical for this chapter", "assume less background"). During iteration, record any user style corrections for future sections.

### Related Skills (Awareness)

Know these exist and reference if the situation calls for it:

| Skill | When it might help |
|---|---|
| `scientific-brainstorming` | Section outline feels thin or poorly motivated |
| `scientific-critical-thinking` | Evaluating conflicting evidence in the literature |
| `scientific-visualization` | Data plots or diagrams would strengthen the section |
| `scientific-schematics` | Concept diagrams or flowcharts |

## Section Granularity

### `/draft X introduction` — Chapter Introduction

Draft the untitled opening paragraphs of Chapter X (the "Section X.0" from the chapter outline). This is **not** a subsection intro — it covers the entire chapter at a high level.

- **Length**: 2–4 paragraphs.
- **Structure**: Funnel pattern from the Personal Style profile: broad context → specific problem → gap → "In this chapter we…" roadmap.
- **Input**: Reads the **full** `chapter_outline.md` (all sections) plus `outline.md` (thesis arc) to understand the chapter's scope and connections.
- **No subsubsection research**: Unlike `/draft X.Y`, this mode does not drill into individual reference queries. It synthesises the chapter's Goal, Narrative, and Connections blocks into flowing prose.
- **Output**: Saved to `chapter_XX/sections/X.0_introduction.md`.

### `/draft X.Y` — Subsection Level

**Ask the user** which mode:

**1. Intro-only mode**: Draft just the introductory text of Section X.Y — the prose that appears before the first subsubsection (X.Y.1). Use when subsubsections will be drafted separately.

**2. Full-section mode**: Draft the entire Section X.Y including all subsubsections:
- Draft each subsubsection **sequentially** (X.Y.1 → X.Y.2 → …), each through the full pipeline
- After all subsubsections are complete, **tie them together**: write the section introduction, verify inter-subsubsection transitions, ensure the section reads as one coherent piece
- Present the assembled section to the user

### `/draft X.Y.Z` — Subsubsection Level

Draft a single subsubsection. Before writing, **read existing context**:
- **Subsection intro** (X.Y text, if present) — understand the framing
- **Previous subsubsections** (X.Y.1 … X.Y.(Z-1)) — ensure continuity
- **Next subsubsection outline** (X.Y.(Z+1) from `chapter_outline.md`) — set up proper transitions

## Workflow Steps

### Step 0: Parse Input & Determine Mode

1. Parse the user's `/draft` command:
   - `X introduction` → chapter introduction mode
   - `X.Y` → subsection mode
   - `X.Y.Z` → subsubsection mode
2. Map chapter `X` → directory `chapter_0X/`
3. Locate the target in `chapter_outline.md`
4. If **chapter introduction** (`X introduction`): proceed to draft the X.0 block — read the full chapter outline and thesis connections, skip per-subsection research
5. If **subsection** (`X.Y`): ask user for **intro-only** or **full-section** mode
6. If **subsubsection** (`X.Y.Z`): proceed directly

### Step 1: Context Loading

1. **Read `outline.md`** — thesis arc, how this chapter connects to predecessors and successors
2. **Read `chapter_outline.md`** — section's **Goal**, **Narrative**, key points, transitions, style notes
3. **Read `references.md`** — key references with provenance (✅ directly queryable vs ❌ cited-within-review)
4. **Read existing drafts** in `chapter_XX/sections/`:
   - Subsection intro text (if drafting a subsubsection)
   - Previous subsubsections (for continuity)
   - Next subsubsection outline (for transitions)

### Step 2: Source Registry

```
→ Call source_registry skill
→ Obtain: author_paper_ids (001), review_ids (002), general_ids
```

### Step 3: Knowledge Retrieval

```
→ Call knowledge skill (retrieve mode)
→ Input: section topic keywords
→ Output: existing insights that can skip or accelerate research
```

### Step 4: Targeted NotebookLM Research

For each key point in the section outline:

1. **Phase 1 — Reviews only** (`002)` source IDs): consensus definitions, equations, structural context
   ```
   mcp_notebooklm_notebook_query(
       notebook_id="1b7df790-7858-4fc8-879c-39f41238c4ae",
       query="<specific question about a key point>",
       source_ids=<review_002_ids>
   )
   ```

2. **Phase 2 — All sources** (omit `source_ids`): specific citations, numbers, arXiv IDs
   ```
   mcp_notebooklm_notebook_query(
       notebook_id="1b7df790-7858-4fc8-879c-39f41238c4ae",
       query="<follow-up for specifics>",
       conversation_id=<from_phase_1>
   )
   ```

3. **Author papers** (`001)` source IDs): only if this section references the author's own work
   ```
   mcp_notebooklm_notebook_query(
       notebook_id="1b7df790-7858-4fc8-879c-39f41238c4ae",
       query="<question about our methodology/results>",
       source_ids=<author_001_ids>
   )
   ```

4. **Track provenance**: for each claim, record which source backs it → `\cite{bib_key}`

### Step 5: Draft Writing (Three-Layer Pipeline)

1. **Layer 1** (`scientific-writing`): Outline key points from Step 4 research, then convert to flowing paragraphs
2. **Layer 2** (`humanizer`): Anti-AI pass — strip patterns, vary rhythm
3. **Layer 3** (personal style): Apply voice, physics-first motivation, clarity check — break overlong sentences

**Output format** (LaTeX-ready markdown):
- Equations: `$$` for display, `$` for inline
- Citations: `\cite{bib_key}`
- Cross-references: `\label{sec:X.Y.Z}`, `\ref{sec:...}`
- No bullet points in final prose — everything in flowing paragraphs

**Literature figures**: Automated figure extraction from papers is not currently available. When a figure from the literature would strengthen the section, insert a LaTeX figure environment with a placeholder and a caption that references the source so the user can fetch the image manually:

```latex
\begin{figure}[t]
    \centering
    % TODO: insert Figure 3 from arXiv:2302.01947 (Amerio et al., 2023)
    \includegraphics[width=\columnwidth]{figures/placeholder.pdf}
    \caption{Reconstructed source-count distribution from \cite{Amerio:2023uet}, Figure~3.}
    \label{fig:dnds_result}
\end{figure}
```

The `% TODO` comment must include: (1) the figure number, (2) the arXiv ID or DOI, and (3) the author/year for easy lookup. The user will replace the placeholder with the actual figure file.

### Step 6: Self-Review

Before presenting the draft, check:

1. **Logical flow** — does the argument build naturally through the section?
2. **Citation completeness** — is every factual claim backed by a citation?
3. **Style compliance** — matches personal profile + any chapter-level overrides?
4. **Transition quality** — smooth connections to adjacent sections/subsubsections?
5. **Anti-AI check** — no remaining AI vocabulary or structural tells?

### Step 7: Coherence Check

After the draft is complete (and user is broadly satisfied):

**1. Chapter-level coherence**:
- Does the new text fit with existing chapter prose?
- Are transitions to/from adjacent sections smooth?
- Is terminology consistent with earlier sections?

**2. Document-level coherence**:
- Does the text align with the thesis narrative arc from `outline.md`?
- Are forward/backward references to other chapters appropriate?
- Does it maintain the framing established in the Introduction (Ch. 0)?

Report any issues to the user before finalizing.

### Step 8: Output & Iteration

1. Save draft to `chapter_XX/sections/X.Y.Z_title.md` (or `X.Y_title.md`)
2. Present to user for review
3. Iterate on feedback (tone, content, structure, corrections)
4. When user is satisfied → **ask** if they want LaTeX conversion
5. If yes → produce `.tex` snippet ready for `\input{}` in `chapter_X.tex`

## Output

- `chapter_XX/sections/X.Y.Z_title.md` — draft in LaTeX-ready markdown
- `chapter_XX/sections/X.Y.Z_title.tex` — LaTeX conversion (only when requested)
- `.agent/knowledge/` — key insights saved via the `knowledge` skill (if new research was performed)
