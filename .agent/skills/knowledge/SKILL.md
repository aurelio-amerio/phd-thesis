---
name: knowledge
description: Use when saving insights from the current conversation to persistent storage, or when retrieving past insights before starting research or writing tasks.
---

# Knowledge — Persistent Insight Store

Manages the `.agent/knowledge/` folder as a persistent, searchable store of insights gathered across conversations. Two modes: **save** (write insights) and **retrieve** (find past insights).

## Knowledge Folder

- **Path**: `.agent/knowledge/`
- **Format**: Standalone `.md` files with YAML frontmatter

## File Format

Every knowledge file follows this structure:

```markdown
---
title: "NFW Profile Definition"
date: 2026-03-04
source_skill: literature_research
chapter: chapter_01
tags: [dark-matter, density-profile, nfw, halo]
---

## Summary
[Concise description of the insight]

## Source References
- [Author (Year)] — arXiv: [number], bib key: `[key]`

## Context
[Which chapter/section this was gathered for, and why it matters]
```

**Frontmatter fields**:

| Field | Required | Description |
|---|---|---|
| `title` | Yes | Descriptive title of the insight |
| `date` | Yes | Date gathered (YYYY-MM-DD) |
| `source_skill` | Yes | Which skill produced this (`literature_research`, `paper_analysis`, `review_analysis`, `chapter_outline`, or `manual`) |
| `chapter` | No | Target chapter (e.g., `chapter_01`) |
| `tags` | Yes | List of topic tags for retrieval |

**Filename convention**: Descriptive, topic-based, lowercase with underscores. Examples:
- `nfw_profile_definition.md`
- `gce_interpretations_summary.md`
- `paper4_domain_adaptation_approach.md`

## Mode 1: Save

**Trigger**: User says `/knowledge save`, "save this to knowledge", or at the end of a research skill workflow.

### Steps

1. **Identify insights**: Review the current conversation for key findings worth persisting — definitions, methodology summaries, reference collections, structural decisions, or any reusable knowledge.

2. **Check for duplicates**: Scan `.agent/knowledge/` filenames. If a file on the same topic exists, **update** it rather than creating a duplicate.

3. **Write files**: For each insight, create a `.md` file in `.agent/knowledge/` following the format above.

4. **Confirm**: Report to the user what was saved and the filenames used.

### What to Save

- Definitions and standard physics (equations, parameters)
- Methodology summaries from author papers
- Key results and numerical values
- Reference collections for specific topics (with bib keys)
- Structural decisions (how experts organize arguments)
- Transition logic between chapters/sections

### What NOT to Save

- Raw NotebookLM responses (too verbose, not curated)
- Conversation-specific context that won't generalize
- Duplicate information already in `references.md` files

## Mode 2: Retrieve

**Trigger**: User says `/knowledge`, "check knowledge for X", or automatically at the start of `chapter_outline` (Step 0).

### Steps

1. **List knowledge files**: `find_by_name(SearchDirectory=".agent/knowledge/", Pattern="*.md")`

2. **Match by relevance**: Compare filenames and read frontmatter to find files matching the current topic. Use these signals:
   - **Filename keywords**: Does the filename contain relevant terms?
   - **Tags**: Do the frontmatter tags overlap with the current topic?
   - **Chapter**: Is the file tagged for the chapter being worked on?

3. **Read matched files**: Read the body of relevant files (typically 3–8 matches max).

4. **Synthesize**: Present a summary of what was found, organized by relevance. Highlight:
   - Insights that can be used directly
   - References already collected (with bib keys)
   - Gaps — topics the user is asking about that have NO existing knowledge

### Retrieval Strategy

```
Files found: 12
├── Filename match: 3 files (contain topic keywords)
├── Tag match: 5 files (overlapping tags)
├── Chapter match: 2 files (same chapter)
└── No match: 2 files (skip)
→ Read top 8 matched files
→ Synthesize into context summary
```

## Integration with Other Skills

This skill is called BY other skills:

| Calling Skill | Mode | When |
|---|---|---|
| `literature_research` | Save | After producing `references.md`, save key insights |
| `paper_analysis` | Save | After extracting methodology/results from author papers |
| `review_analysis` | Save | After extracting content from review articles |
| `chapter_outline` | Retrieve | Step 0, before starting research — check for existing knowledge |
| Manual (`/knowledge`) | Either | User explicitly asks to save or retrieve |

## Common Mistakes

- **Saving too much**: Knowledge files should be curated summaries, not raw dumps. If it's longer than ~50 lines, it's probably too detailed.
- **Forgetting bib keys**: Always include bib keys when referencing papers. Run the lookup against `bibliography.bib`.
- **Not checking for duplicates**: Always scan existing files before creating new ones. Update > duplicate.
- **Vague tags**: Tags should be specific enough to distinguish topics. Use `[nfw, density-profile]` not just `[physics]`.
