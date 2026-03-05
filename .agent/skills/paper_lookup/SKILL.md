---
name: paper_lookup
description: Use when you need metadata, figures, full text, citations, or BibTeX for a specific paper. Centralizes InspireHEP and arXiv MCP server usage with decision guidelines.
---

# Paper Lookup Skill

Retrieves information about specific papers using two complementary MCP servers: **InspireHEP** (metadata, figures, citations) and **arXiv** (full text). Use this skill whenever you need to look up, inspect, or download a paper.

## When to Use This Skill

- **Getting paper metadata** (title, authors, abstract, citation count)
- **Downloading figures** from a paper
- **Reading the full text** of a paper
- **Getting BibTeX entries** for the bibliography
- **Checking citation counts or finding citing papers**
- **Looking up an author's publication list**
- **Fetching paper references**

## MCP Server Decision Guide

| Need | Use | Tool |
|------|-----|------|
| Abstract / metadata | **InspireHEP** | `get_paper_details` |
| Full paper text | **arXiv** | `download_paper` → `read_paper` |
| Figures (with download URLs) | **InspireHEP** | `get_paper_figures` |
| BibTeX entry | **InspireHEP** | `get_bibtex` |
| Citation count / graph | **InspireHEP** | `get_citations` |
| Author publications + h-index | **InspireHEP** | `get_author_papers` |
| References list | **InspireHEP** | `get_references` |
| Non-HEP paper search | **arXiv** | `search_papers` |
| HEP-specific search | **InspireHEP** | `search_papers` |

## arXiv ID Handling

> **⚠️ Critical**: arXiv IDs in `XXXX.XXXXX` format (e.g., `1012.4515`) are parsed as **floats** by the JSON layer when passed to InspireHEP tools, causing validation errors. This does NOT affect the arXiv MCP server.

| MCP Server | Bare ID (`1012.4515`) | Full URL | Old format (`hep-ph/0123456`) |
|---|---|---|---|
| **arXiv** | ✅ Works directly | ✅ | N/A |
| **InspireHEP** | ❌ Float coercion | ✅ Use this | ✅ Works directly |

**Rule for InspireHEP**: Always wrap numeric arXiv IDs in the full URL format:
```
mcp_inspirehep_get_paper_details(arxiv_id="https://arxiv.org/abs/1012.4515")
```

Old-format IDs with letters work directly:
```
mcp_inspirehep_get_paper_details(arxiv_id="hep-ph/0512090")
```

## Recipes

### Recipe 1: Get Paper Metadata

```
mcp_inspirehep_get_paper_details(arxiv_id="https://arxiv.org/abs/<ID>")
# Returns: title, authors, abstract, citation_count, DOI, publication info, texkey
```

### Recipe 2: Read Full Paper Text

```python
# Step 1: Download and convert PDF → Markdown
mcp_arxiv-mcp-server_download_paper(paper_id="<ID>")  # bare ID works

# Step 2: Poll until conversion completes (~20-30s for long papers)
mcp_arxiv-mcp-server_download_paper(paper_id="<ID>", check_status=True)

# Step 3: Read the converted markdown
mcp_arxiv-mcp-server_read_paper(paper_id="<ID>")
```

Papers are stored locally in `arxiv-papers/` within the thesis project directory.

### Recipe 3: Download Figures from a Paper

Figures are available via InspireHEP for papers that have them indexed.

```python
# Step 1: Get figure URLs and captions
mcp_inspirehep_get_paper_figures(arxiv_id="https://arxiv.org/abs/<ID>")
# Returns: list of {caption, url, description} for each figure

# Step 2: Download a specific figure
# run_command: curl -L -o "figures/<filename>.png" "<figure_url>"
```

**Important**: The InspireHEP MCP server provides figure **URLs only** — it does not download files. Use `curl -L -o` or equivalent to download the actual image files from the returned URLs.

The figure URLs point to `https://inspirehep.net/files/<hash>` and return the original image format (typically PNG or PDF).

### Recipe 4: Get BibTeX Entry

```
mcp_inspirehep_get_bibtex(identifier="<arxiv_id or DOI>")
# For numeric arXiv IDs, use the full URL:
mcp_inspirehep_get_bibtex(identifier="https://arxiv.org/abs/1012.4515")
# Returns: BibTeX entry, texkey, inspire record ID
```

### Recipe 5: Check Citations

```python
# Get paper details first (includes citation_count)
mcp_inspirehep_get_paper_details(arxiv_id="https://arxiv.org/abs/<ID>")

# For the full citation graph (papers that cite this one)
mcp_inspirehep_get_citations(inspire_id="<numeric_inspire_id>", direction="citing")

# For references (papers this one cites)
mcp_inspirehep_get_references(inspire_id="<numeric_inspire_id>")
```

### Recipe 6: Author Publication Search

```
mcp_inspirehep_get_author_papers(author_name="Cirelli, Marco", sort="mostcited", size=20)
# Returns: paper list + aggregate metrics (h-index, total citations)
```

## Integration with Other Skills

This skill is a **utility** called by other thesis skills:

| Calling Skill | Typical Use |
|---|---|
| `literature_research` | Look up abstract/metadata for papers not in NotebookLM; fetch BibTeX for new entries |
| `section_drafting` | Download figures for LaTeX inclusion; read paper sections for paraphrasing |
| `review_analysis` | Get full text of a review via arXiv when not in NotebookLM |
| `chapter_outline` | Check citation impact to prioritize references |

## Limitations

- **InspireHEP is HEP-only** — for non-physics papers (cs.*, stat.*, etc.), use arXiv search
- **arXiv has no figure extraction** — PDF→Markdown conversion loses figures
- **InspireHEP figures are not universal** — not all papers have indexed figures on InspireHEP
- **arXiv rate limits** — avoid rapid sequential downloads; the server handles one conversion at a time
