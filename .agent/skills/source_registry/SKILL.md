---
name: source_registry
description: Fetches all source IDs from the thesis NotebookLM notebook and categorizes them into author papers (001), review articles (002), and general references. Call once per conversation before using other thesis skills.
---

# Source Registry

Retrieves and categorizes all sources from the **thesis references** NotebookLM notebook. This skill is a **prerequisite** for all other thesis research skills — call it **once per conversation** to obtain the source IDs needed for filtered queries.

## Target Notebook

- **Name**: `thesis references`
- **ID**: `1b7df790-7858-4fc8-879c-39f41238c4ae`

## Workflow

### Step 1: Fetch All Sources

Call the MCP tool:

```
mcp_notebooklm_notebook_get(notebook_id="1b7df790-7858-4fc8-879c-39f41238c4ae")
```

This returns a list of all sources with their `source_id` and `title`.

### Step 2: Categorize by Title Prefix

Parse each source title and assign it to one of three categories:

| Category | Title Pattern | Description |
|---|---|---|
| **Author Papers** | Starts with `001)` | The thesis author's own published papers. Included verbatim in the LaTeX thesis. |
| **Review Articles** | Starts with `002)` | Review papers, textbooks, and lecture notes. Must be cited and paraphrased. |
| **General References** | No numeric prefix | Specific papers, experimental results, and other references. Must be cited. |

### Step 3: Store for Session Use

Keep the three categorized lists available for the duration of the conversation. Other skills will request specific categories:

- `paper_analysis` → needs **Author Papers** source IDs
- `review_analysis` → needs **Review Articles** source IDs
- `literature_research` → needs **Review Articles** + **General References** source IDs (excludes Author Papers)
- `chapter_outline` → needs all categories

## Output Format

Present the registry as three lists:

```
## Author Papers (001)
- [source_id] → "001) paper 1 - 2302.01947.pdf"
- [source_id] → "001) paper 2 - 2306.16483.pdf"
...

## Review Articles (002)
- [source_id] → "002) review - Cirelli DM - 2406.01705v3.pdf"
...

## General References
- [source_id] → "0106131v1.pdf"
...
```

## Important Notes

- **Call this skill once per conversation**. The source list rarely changes mid-session.
- If a new source is added to the notebook during a session, re-run this skill to refresh.
- Other skills should **never** call `notebook_get` themselves — they should ask for the registry output.
