---
name: chapter_outline
description: Research assistant that generates detailed, structural chapter outlines by synthesizing thesis context, local references, and NotebookLM insights.
---

# Thesis Chapter Outlining Skill

This skill orchestrates the creation of deep, structurally robust chapter outlines for a PhD thesis. It calls the other thesis skills in sequence to build a comprehensive foundation, then synthesizes everything into a detailed outline.

## Target Notebook

- **Name**: `thesis references`
- **ID**: `1b7df790-7858-4fc8-879c-39f41238c4ae`

## Prerequisites

- A target chapter directory (e.g., `chapter_01`).
- Access to `outline.md` (root thesis outline).

## Workflow Steps

### Step 0: Knowledge Retrieval

Before starting research, check for existing insights relevant to this chapter.

```
→ Call knowledge skill (retrieve mode) for the target chapter topic
→ Input: chapter title/topic from outline.md
→ Output: any pre-existing insights that can inform or skip research steps
```

If relevant knowledge files exist, use them to **skip or accelerate** subsequent research steps (e.g., if definitions are already extracted, skip that portion of literature research).

### Step 1: Context Analysis

Understand where this chapter fits in the larger picture.

1. **Read Root Outline**: `view_file outline.md`. Identify the chapter's **Scope**, **Key Contribution**, **Section Structure**, and how it connects to the previous and next chapters.
2. **Check Existing Artifacts**: Look for any existing files in the chapter directory (`references.md`, `chapter_outline.md`, etc.) from prior work.

### Step 2: Source Registry

Run the `source_registry` skill to obtain categorized source IDs.

```
→ Call source_registry skill
→ Obtain: author_paper_ids, review_ids, general_ids
```

This step is required before any NotebookLM queries.

### Step 3: Literature Research

Run the `literature_research` skill to produce the chapter's `references.md` and data table.

```
→ Call literature_research skill for the target chapter
→ Input: chapter sections from outline.md, source IDs from Step 2
→ Output: chapter_XX/references.md (with data table + bib-key lookups)
```

Follow the granular per-subsection approach defined in the `literature_research` skill.

### Step 4: Review Analysis

For the **key review articles** identified in Step 3, run `review_analysis` to extract detailed, citation-ready content.

```
→ Call review_analysis skill
→ Input: specific 002) source IDs for the most relevant reviews
→ Output: structured extraction notes, saved to .agent/knowledge/
```

Focus on reviews that will be heavily cited in this chapter.

### Step 5: Paper Analysis (if applicable)

If an author paper is inserted in or near this chapter, run `paper_analysis` to extract key contributions and transition points.

```
→ Call paper_analysis skill
→ Input: specific 001) source ID(s) for papers relevant to this chapter
→ Output: methodology summary, key results, contribution statement, transition notes
```

Refer to the paper-to-chapter mapping in the `paper_analysis` skill.

### Step 6: Structural Research

Use NotebookLM directly to study how experts structure arguments on this chapter's topic.

```
mcp_notebooklm_notebook_query(
    notebook_id="1b7df790-7858-4fc8-879c-39f41238c4ae",
    query="What is the detailed structure of [Reference X] regarding [Topic]? 
           List the section headers and summarize the argumentation flow. 
           How do they transition from [Concept A] to [Concept B]?",
    source_ids=<review_ids>
)
```

Focus on:
- How experts **order** their arguments
- How they **introduce** complex concepts
- How they **transition** between topics

### Step 7: Draft `chapter_outline.md`

Create (or update) `chapter_XX/chapter_outline.md`.

**Synthesis**: Combine:
- Chapter requirements from `outline.md`
- References from `references.md` (Step 3)
- Review extractions (Step 4)
- Paper contributions and transitions (Step 5)
- Structural best practices (Step 6)

**Format**: Use a nested structure:

```markdown
# Chapter [XX]: [Title]

## Connections
- **Previous Chapter**: [How this chapter follows from the previous one]
- **Next Chapter**: [How this chapter leads into the next one]
- **Inserted Paper**: [If applicable, which paper is inserted and its key contribution]

## [X.0] Chapter Introduction
**Goal**: Provide a brief, untitled opening (2–4 paragraphs) that orients the reader before the first numbered section. This text appears at the start of the chapter with no section heading.
**Narrative**: Follow a funnel structure:
- Opening context: broad motivation for the chapter's topic
- The central question this chapter addresses
- Chapter roadmap: one-sentence preview of each main section (X.1, X.2, …) and how they connect
- Bridge to the thesis: how the chapter's content feeds into the rest of the thesis

## [X.1] [Section Title]
**Goal**: [What this section achieves in the argument]
**Narrative**: [How the story progresses through this section]

### [X.1.1] [Subsection Title]
- Key point 1 → cite [Reference] (Sec X.X)
- Key point 2 → cite [Reference]
- **Figure**: [description] → from [arXiv:XXXX.XXXXX], Fig. N
- Transition: [How this leads to the next subsection]

### [X.1.2] [Subsection Title]
- ...

## [X.2] [Section Title]
...

## Chapter Summary
- [Key takeaway 1]
- [Key takeaway 2]
- [Bridge to next chapter / inserted paper]
```

**Rules**:
- **Chapter Introduction (X.0)**: Mandatory for every chapter. Untitled in the final output — provides opening paragraphs before the first numbered section
- **H2 sections**: Main structural divisions
- **H3 subsections**: Specific logical steps
- **Bullets**: Key points with specific reference citations
- **Figure annotations**: Mark key literature figures with `**Figure**: [description] → from [arXiv:ID], Fig. N`. These signal to `section_drafting` Step 4b which figures to fetch and download
- **Transitions**: Explicitly note how each section leads to the next
- **Connections**: First section documents how this chapter connects to the rest of the thesis

### Step 8: Review and Refine

Iterate on the draft:

1. **Logical Flow**: Does Section A naturally lead to Section B? Are prerequisites defined before use?
2. **Coverage**: Are all topics from `outline.md` addressed?
3. **Weakness Check**: Are there "jumps" in logic? Missing definitions?
4. **Self-Contained vs. Connected**: The chapter should stand on its own while explicitly linking to previous/future chapters.
5. **Insert Transitions**: If a paper is inserted after this chapter, does the outline build up to it properly?

## Output

- `chapter_XX/chapter_outline.md` — the detailed structural outline
- `chapter_XX/references.md` — references with data table (produced in Step 3)
- `.agent/knowledge/` — key insights saved via the `knowledge` skill (produced in Steps 3–5)
