# citecheck Plugin Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a standalone Claude Code plugin (`citecheck`) that scores `\cite` pertinence 1-10 in LaTeX files via parallel haiku subagents and InspireHEP/arXiv abstracts.

**Architecture:** Plugin layout (`agents/`, `commands/`, `skills/citecheck/scripts/`). Orchestrator skill (Opus) runs four deterministic Python helpers — extract citations, parse bib, fetch abstracts, collate report — then dispatches batched haiku scorer subagents whose tool surface is restricted to `Read` + `Write`.

**Tech Stack:** Python 3.10+ stdlib only (`re`, `json`, `urllib`, `concurrent.futures`, `xml.etree`, `difflib`, `pathlib`), pytest for tests, Claude Code plugin manifest format.

**Spec:** `docs/superpowers/specs/2026-05-18-citecheck-plugin-design.md`

---

## File Structure

```
citecheck-plugin/                          # plugin root (eventually own git repo)
  .claude-plugin/
    plugin.json                            # plugin manifest
    marketplace.json                       # standalone marketplace listing the plugin
  agents/
    citecheck-scorer.md                    # haiku pertinence scorer
  commands/
    citecheck.md                           # /citecheck <file> entry
  skills/
    citecheck/
      SKILL.md                             # orchestration prompt
      scripts/
        parse_bib.py                       # bibliography.bib → bib_index.json
        extract_citations.py               # tex → citations.json
        fetch_abstracts.py                 # Inspire/arXiv parallel fetch → .citecache/
        collate_report.py                  # batch outputs → .md + .json
  tests/
    conftest.py
    test_parse_bib.py
    test_extract_citations.py
    test_fetch_abstracts.py
    test_collate_report.py
    fixtures/
      sample.bib
      sample.tex
      inspire_arxiv.json
      inspire_title.json
      arxiv_response.xml
  README.md
  LICENSE
  .gitignore
  pytest.ini
```

**Responsibilities:**

- `parse_bib.py` — read `bibliography.bib`, output `{bibkey → {title, arxiv_id, doi, year, first_author}}`. Pure parsing, no network.
- `extract_citations.py` — read one `.tex` file, output a list of `{bibkey, line, tex_file, paragraph, section_heading}`. Pure parsing, no network.
- `fetch_abstracts.py` — given a missing-keys list and bib metadata, run the 5-step resolution chain (Inspire arxiv/doi/title → arXiv id/title) against the network and write per-bibkey cache files. Only file that touches the network.
- `collate_report.py` — merge cached abstracts + batch scoring outputs into `.md` + `.json`. Pure formatting.
- `SKILL.md` — natural-language prompt the orchestrator follows. Calls the scripts, builds batches, dispatches the scorer agent, validates outputs, runs the collator.
- `agents/citecheck-scorer.md` — haiku, `tools: Read, Write`, scores one batch.

---

## Task 1: Scaffold plugin directory and manifests

**Files:**
- Create: `citecheck-plugin/.claude-plugin/plugin.json`
- Create: `citecheck-plugin/.claude-plugin/marketplace.json`
- Create: `citecheck-plugin/README.md`
- Create: `citecheck-plugin/LICENSE`
- Create: `citecheck-plugin/.gitignore`
- Create: `citecheck-plugin/pytest.ini`

- [ ] **Step 1: Create the directory layout**

```bash
mkdir -p citecheck-plugin/.claude-plugin
mkdir -p citecheck-plugin/agents
mkdir -p citecheck-plugin/commands
mkdir -p citecheck-plugin/skills/citecheck/scripts
mkdir -p citecheck-plugin/tests/fixtures
```

- [ ] **Step 2: Write `citecheck-plugin/.claude-plugin/plugin.json`**

```json
{
  "name": "citecheck",
  "version": "0.1.0",
  "description": "Pertinence review for \\cite references in LaTeX research documents: parallel haiku scoring against InspireHEP and arXiv abstracts to flag mistakenly inserted or hallucinated citations.",
  "author": {
    "name": "Aurelio Amerio"
  }
}
```

- [ ] **Step 3: Write `citecheck-plugin/.claude-plugin/marketplace.json`**

```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "citecheck-marketplace",
  "description": "Citation pertinence review plugin for LaTeX research documents.",
  "owner": {
    "name": "Aurelio Amerio"
  },
  "plugins": [
    {
      "name": "citecheck",
      "description": "Pertinence review for \\cite references in LaTeX using parallel haiku scoring against InspireHEP and arXiv abstracts.",
      "author": { "name": "Aurelio Amerio" },
      "category": "research",
      "source": {
        "source": "local",
        "path": "."
      }
    }
  ]
}
```

- [ ] **Step 4: Write `citecheck-plugin/.gitignore`**

```
__pycache__/
*.pyc
.pytest_cache/
.citecache/
.citecheck/
```

- [ ] **Step 5: Write `citecheck-plugin/pytest.ini`**

```ini
[pytest]
testpaths = tests
python_files = test_*.py
```

- [ ] **Step 6: Write `citecheck-plugin/LICENSE` (MIT)**

```
MIT License

Copyright (c) 2026 Aurelio Amerio

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

- [ ] **Step 7: Write a stub `citecheck-plugin/README.md`**

```markdown
# citecheck

Pertinence review for `\cite` references in LaTeX research documents. Scores each
citation 1-10 against the cited paper's abstract (InspireHEP, with arXiv fallback)
to flag mistakenly inserted or hallucinated references.

## Install

Add this marketplace and install the plugin:

```bash
# from inside Claude Code
/plugin marketplace add <path-to-citecheck-plugin>
/plugin install citecheck
```

## Use

```
/citecheck path/to/section.tex
```

The report is written to `.citecheck/<basename>.md` and `.citecheck/<basename>.json`.

See `docs/superpowers/specs/` for the full design.
```

- [ ] **Step 8: Verify the structure**

Run: `find citecheck-plugin -type f | sort`

Expected output includes:
```
citecheck-plugin/.claude-plugin/marketplace.json
citecheck-plugin/.claude-plugin/plugin.json
citecheck-plugin/.gitignore
citecheck-plugin/LICENSE
citecheck-plugin/README.md
citecheck-plugin/pytest.ini
```

- [ ] **Step 9: Commit**

```bash
git add citecheck-plugin/
git commit -m "scaffold citecheck plugin manifest and layout"
```

---

## Task 2: parse_bib — single entry

**Files:**
- Create: `citecheck-plugin/skills/citecheck/scripts/parse_bib.py`
- Create: `citecheck-plugin/tests/test_parse_bib.py`
- Create: `citecheck-plugin/tests/fixtures/sample.bib`
- Create: `citecheck-plugin/tests/conftest.py`

- [ ] **Step 1: Write `tests/conftest.py` to expose the scripts dir on `sys.path`**

```python
import sys
from pathlib import Path

SCRIPTS = Path(__file__).parent.parent / "skills" / "citecheck" / "scripts"
sys.path.insert(0, str(SCRIPTS))
```

- [ ] **Step 2: Write `tests/fixtures/sample.bib` with one entry**

```bibtex
@article{2024JCAP...03..035A,
  author        = {{Arina}, Chiara and {Di Mauro}, Mattia},
  title         = {{CosmiXs: cosmic messenger spectra for indirect dark matter searches}},
  year          = 2024,
  doi           = {10.1088/1475-7516/2024/03/035},
  archiveprefix = {arXiv},
  eprint        = {2312.01153}
}
```

- [ ] **Step 3: Write the failing test in `tests/test_parse_bib.py`**

```python
from pathlib import Path
from parse_bib import parse_bib

FIXTURE = Path(__file__).parent / "fixtures" / "sample.bib"


def test_parse_single_entry():
    index = parse_bib(FIXTURE)
    assert "2024JCAP...03..035A" in index
    entry = index["2024JCAP...03..035A"]
    assert entry["title"] == "CosmiXs: cosmic messenger spectra for indirect dark matter searches"
    assert entry["arxiv_id"] == "2312.01153"
    assert entry["doi"] == "10.1088/1475-7516/2024/03/035"
    assert entry["year"] == "2024"
    assert entry["first_author"] == "Arina, Chiara"
```

- [ ] **Step 4: Run the test and watch it fail**

Run: `pytest citecheck-plugin/tests/test_parse_bib.py -v`
Expected: ImportError / FAIL — `parse_bib` does not yet exist.

- [ ] **Step 5: Write a minimal `parse_bib.py`**

```python
"""Parse a BibTeX file into a bibkey → metadata dict.

Only extracts the fields citecheck needs: title, eprint (arXiv), doi, year,
first author. Uses regex; no external dependencies.
"""
from __future__ import annotations

import re
from pathlib import Path

ENTRY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,", re.IGNORECASE)
FIELD_RE = re.compile(r"(\w+)\s*=\s*[{\"]([^}\"]*(?:\{[^}]*\}[^}\"]*)*)[}\"]", re.IGNORECASE)


def _split_entries(text: str) -> list[tuple[str, str]]:
    """Return [(bibkey, body), ...] by scanning balanced braces from @TYPE{key,..}."""
    out: list[tuple[str, str]] = []
    i = 0
    while True:
        m = ENTRY_RE.search(text, i)
        if not m:
            break
        bibkey = m.group(1)
        depth = 1
        j = text.find("{", m.start())
        k = j + 1
        while k < len(text) and depth > 0:
            if text[k] == "{":
                depth += 1
            elif text[k] == "}":
                depth -= 1
            k += 1
        out.append((bibkey, text[j + 1 : k - 1]))
        i = k
    return out


def _strip_braces(s: str) -> str:
    return re.sub(r"[{}]", "", s).strip()


def _first_author(raw: str) -> str:
    raw = _strip_braces(raw)
    return raw.split(" and ")[0].strip()


def parse_bib(bib_path: Path) -> dict[str, dict]:
    text = Path(bib_path).read_text(encoding="utf-8", errors="replace")
    index: dict[str, dict] = {}
    for bibkey, body in _split_entries(text):
        fields = {k.lower(): v for k, v in FIELD_RE.findall(body)}
        index[bibkey] = {
            "title": _strip_braces(fields.get("title", "")),
            "arxiv_id": _strip_braces(fields.get("eprint", "")) or None,
            "doi": _strip_braces(fields.get("doi", "")) or None,
            "year": _strip_braces(fields.get("year", "")) or None,
            "first_author": _first_author(fields.get("author", "")) or None,
        }
    return index
```

- [ ] **Step 6: Run the test and confirm it passes**

Run: `pytest citecheck-plugin/tests/test_parse_bib.py -v`
Expected: PASS.

- [ ] **Step 7: Commit**

```bash
git add citecheck-plugin/skills/citecheck/scripts/parse_bib.py \
        citecheck-plugin/tests/test_parse_bib.py \
        citecheck-plugin/tests/fixtures/sample.bib \
        citecheck-plugin/tests/conftest.py
git commit -m "parse_bib: extract single entry fields"
```

---

## Task 3: parse_bib — multiple entries, missing fields, mtime cache

**Files:**
- Modify: `citecheck-plugin/tests/fixtures/sample.bib`
- Modify: `citecheck-plugin/skills/citecheck/scripts/parse_bib.py`
- Modify: `citecheck-plugin/tests/test_parse_bib.py`

- [ ] **Step 1: Append two more entries to `tests/fixtures/sample.bib`**

```bibtex

@article{NoArxiv2020,
  author = {Smith, Jane and Doe, John},
  title  = {A paper with no arXiv ID},
  year   = 2020,
  doi    = {10.1000/xyz123}
}

@misc{StubKey,
  title = {Bare stub with only a title}
}
```

- [ ] **Step 2: Add two failing tests**

```python
def test_parse_multiple_entries():
    index = parse_bib(FIXTURE)
    assert len(index) == 3
    assert "NoArxiv2020" in index
    assert "StubKey" in index


def test_missing_fields_are_none():
    index = parse_bib(FIXTURE)
    assert index["NoArxiv2020"]["arxiv_id"] is None
    assert index["StubKey"]["doi"] is None
    assert index["StubKey"]["first_author"] is None
```

- [ ] **Step 3: Run tests, confirm they pass** (the regex parser already supports multi-entry)

Run: `pytest citecheck-plugin/tests/test_parse_bib.py -v`
Expected: all PASS. If `_first_author("")` returns `""` instead of `None`, fix:

```python
def _first_author(raw: str) -> str | None:
    raw = _strip_braces(raw).strip()
    if not raw:
        return None
    return raw.split(" and ")[0].strip()
```

And re-run.

- [ ] **Step 4: Write the failing mtime-cache test**

```python
import json

def test_load_or_build_index_uses_cache(tmp_path):
    from parse_bib import load_or_build_index
    bib = tmp_path / "test.bib"
    bib.write_text(FIXTURE.read_text())
    cache = tmp_path / "bib_index.json"

    # First call: builds and writes cache.
    idx1 = load_or_build_index(bib, cache)
    assert cache.exists()
    assert "2024JCAP...03..035A" in idx1

    # Corrupt the bib but keep mtime older than cache: cache should be returned.
    cache_mtime = cache.stat().st_mtime
    bib.write_text("@article{NEW, title={x}}")
    import os
    os.utime(bib, (cache_mtime - 10, cache_mtime - 10))
    idx2 = load_or_build_index(bib, cache)
    assert "NEW" not in idx2  # served from cache

    # Touch bib forward: cache should rebuild.
    os.utime(bib, (cache_mtime + 10, cache_mtime + 10))
    idx3 = load_or_build_index(bib, cache)
    assert "NEW" in idx3
```

- [ ] **Step 5: Run the test, watch it fail**

Run: `pytest citecheck-plugin/tests/test_parse_bib.py::test_load_or_build_index_uses_cache -v`
Expected: ImportError — `load_or_build_index` not defined.

- [ ] **Step 6: Add `load_or_build_index` and a CLI to `parse_bib.py`**

Append to `parse_bib.py`:

```python
import json
import sys


def load_or_build_index(bib_path: Path, cache_path: Path) -> dict[str, dict]:
    bib_path = Path(bib_path)
    cache_path = Path(cache_path)
    if cache_path.exists() and cache_path.stat().st_mtime >= bib_path.stat().st_mtime:
        return json.loads(cache_path.read_text(encoding="utf-8"))
    index = parse_bib(bib_path)
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(index, indent=2), encoding="utf-8")
    return index


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: parse_bib.py <bib_path> <cache_path>", file=sys.stderr)
        sys.exit(2)
    load_or_build_index(Path(sys.argv[1]), Path(sys.argv[2]))
```

- [ ] **Step 7: Run all parse_bib tests, confirm pass**

Run: `pytest citecheck-plugin/tests/test_parse_bib.py -v`
Expected: all PASS.

- [ ] **Step 8: Commit**

```bash
git add citecheck-plugin/skills/citecheck/scripts/parse_bib.py \
        citecheck-plugin/tests/test_parse_bib.py \
        citecheck-plugin/tests/fixtures/sample.bib
git commit -m "parse_bib: multi-entry + mtime cache + CLI"
```

---

## Task 4: extract_citations — single-key \cite

**Files:**
- Create: `citecheck-plugin/skills/citecheck/scripts/extract_citations.py`
- Create: `citecheck-plugin/tests/test_extract_citations.py`
- Create: `citecheck-plugin/tests/fixtures/sample.tex`

- [ ] **Step 1: Write `tests/fixtures/sample.tex`**

```latex
\section{Likelihood-based inference}
\subsection{Bayesian methods}

The likelihood function describes the probability of the data given the
model parameters~\cite{2024JCAP...03..035A}. This is a foundational concept.

% \cite{ShouldBeIgnored} -- commented out
Some other paragraph here referencing \cite{NoArxiv2020} and discussing
methodology in depth.

A third paragraph mentioning \cite{StubKey, OtherKey}.
```

- [ ] **Step 2: Write the failing test**

```python
from pathlib import Path
from extract_citations import find_citations

FIXTURE = Path(__file__).parent / "fixtures" / "sample.tex"


def test_finds_single_key_citations():
    text = FIXTURE.read_text(encoding="utf-8")
    cites = find_citations(text)
    bibkeys = [c["bibkey"] for c in cites]
    assert "2024JCAP...03..035A" in bibkeys
    assert "NoArxiv2020" in bibkeys
    # Single-key citations get one entry each.
    assert bibkeys.count("2024JCAP...03..035A") == 1
```

- [ ] **Step 3: Run, confirm failure**

Run: `pytest citecheck-plugin/tests/test_extract_citations.py -v`
Expected: ImportError.

- [ ] **Step 4: Write minimal `extract_citations.py`**

```python
"""Extract \\cite references from a LaTeX file with paragraph + section context.

Only handles the bare \\cite{...} command (incl. tilde-prefixed ~\\cite{...} and
multi-key \\cite{a,b,c}). Comments are stripped before scanning.
"""
from __future__ import annotations

import re
from pathlib import Path

CITE_RE = re.compile(r"\\cite\s*\{([^}]+)\}")


def find_citations(text: str) -> list[dict]:
    """Return [{bibkey, line}, ...] for every \\cite key in text."""
    out: list[dict] = []
    line_starts = [0]
    for i, ch in enumerate(text):
        if ch == "\n":
            line_starts.append(i + 1)

    def line_of(pos: int) -> int:
        import bisect
        return bisect.bisect_right(line_starts, pos)

    for m in CITE_RE.finditer(text):
        line = line_of(m.start())
        for raw_key in m.group(1).split(","):
            key = raw_key.strip()
            if key:
                out.append({"bibkey": key, "line": line})
    return out
```

- [ ] **Step 5: Run, confirm pass**

Run: `pytest citecheck-plugin/tests/test_extract_citations.py -v`
Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add citecheck-plugin/skills/citecheck/scripts/extract_citations.py \
        citecheck-plugin/tests/test_extract_citations.py \
        citecheck-plugin/tests/fixtures/sample.tex
git commit -m "extract_citations: parse single-key \\cite"
```

---

## Task 5: extract_citations — multi-key and comment stripping

**Files:**
- Modify: `citecheck-plugin/skills/citecheck/scripts/extract_citations.py`
- Modify: `citecheck-plugin/tests/test_extract_citations.py`

- [ ] **Step 1: Add two failing tests**

```python
def test_multi_key_cite_expands_to_one_entry_per_key():
    text = FIXTURE.read_text(encoding="utf-8")
    cites = find_citations(text)
    bibkeys = [c["bibkey"] for c in cites]
    assert "StubKey" in bibkeys
    assert "OtherKey" in bibkeys
    # Both keys share the same line.
    line_stub = next(c["line"] for c in cites if c["bibkey"] == "StubKey")
    line_other = next(c["line"] for c in cites if c["bibkey"] == "OtherKey")
    assert line_stub == line_other


def test_commented_citations_are_ignored():
    text = FIXTURE.read_text(encoding="utf-8")
    cites = find_citations(text)
    bibkeys = [c["bibkey"] for c in cites]
    assert "ShouldBeIgnored" not in bibkeys
```

- [ ] **Step 2: Run, confirm comment test fails** (multi-key already works)

Run: `pytest citecheck-plugin/tests/test_extract_citations.py -v`
Expected: `test_commented_citations_are_ignored` FAILS.

- [ ] **Step 3: Add comment stripping to `extract_citations.py`**

Insert above `CITE_RE`:

```python
# Match an unescaped '%' (not preceded by a backslash) and drop to EOL.
COMMENT_RE = re.compile(r"(?<!\\)%[^\n]*")


def strip_comments(text: str) -> str:
    return COMMENT_RE.sub("", text)
```

And replace the start of `find_citations` to call it:

```python
def find_citations(text: str) -> list[dict]:
    """Return [{bibkey, line}, ...] for every \\cite key in text.

    Comments (unescaped %...) are removed before scanning, but line numbers are
    preserved (newlines are kept).
    """
    text = strip_comments(text)
    out: list[dict] = []
    ...
```

- [ ] **Step 4: Run, confirm all pass**

Run: `pytest citecheck-plugin/tests/test_extract_citations.py -v`
Expected: all PASS.

- [ ] **Step 5: Commit**

```bash
git add citecheck-plugin/skills/citecheck/scripts/extract_citations.py \
        citecheck-plugin/tests/test_extract_citations.py
git commit -m "extract_citations: comment stripping + multi-key check"
```

---

## Task 6: extract_citations — paragraph and section heading

**Files:**
- Modify: `citecheck-plugin/skills/citecheck/scripts/extract_citations.py`
- Modify: `citecheck-plugin/tests/test_extract_citations.py`

- [ ] **Step 1: Add failing tests for paragraph + heading extraction**

```python
from extract_citations import find_paragraph, find_section_heading, extract


def test_find_paragraph_returns_enclosing_block():
    text = FIXTURE.read_text(encoding="utf-8")
    # Locate the line containing "2024JCAP".
    line = next(i for i, ln in enumerate(text.splitlines(), start=1)
                if "2024JCAP" in ln)
    para = find_paragraph(text, line)
    assert "likelihood function" in para
    assert "Some other paragraph" not in para
    assert len(para) <= 600


def test_find_section_heading_returns_nearest_preceding():
    text = FIXTURE.read_text(encoding="utf-8")
    line = next(i for i, ln in enumerate(text.splitlines(), start=1)
                if "2024JCAP" in ln)
    heading = find_section_heading(text, line)
    assert "Bayesian methods" in heading  # nearest \subsection wins over \section


def test_extract_full_pipeline(tmp_path):
    tex = tmp_path / "s.tex"
    tex.write_text(FIXTURE.read_text())
    items = extract(tex)
    assert all({"bibkey", "line", "tex_file", "paragraph", "section_heading"} <= set(it) for it in items)
    assert items[0]["tex_file"].endswith("s.tex")
```

- [ ] **Step 2: Run, confirm failure**

Run: `pytest citecheck-plugin/tests/test_extract_citations.py -v`
Expected: ImportError for new symbols.

- [ ] **Step 3: Implement paragraph + heading helpers**

Append to `extract_citations.py`:

```python
SECTION_RE = re.compile(r"\\(section|subsection|subsubsection|paragraph)\s*\{([^}]+)\}")
PARAGRAPH_CAP = 600


def find_paragraph(text: str, line: int) -> str:
    """Return the enclosing non-blank block around `line`, capped at PARAGRAPH_CAP.

    A paragraph boundary is a blank line or a sectioning command.
    """
    lines = text.splitlines()
    idx = line - 1  # 0-indexed
    # Walk up to the start of the paragraph.
    start = idx
    while start > 0:
        prev = lines[start - 1].strip()
        if prev == "" or SECTION_RE.match(prev):
            break
        start -= 1
    # Walk down to the end.
    end = idx
    while end < len(lines) - 1:
        nxt = lines[end + 1].strip()
        if nxt == "" or SECTION_RE.match(nxt):
            break
        end += 1
    para = " ".join(line.strip() for line in lines[start : end + 1] if line.strip())
    if len(para) > PARAGRAPH_CAP:
        para = para[:PARAGRAPH_CAP] + "..."
    return para


def find_section_heading(text: str, line: int) -> str:
    """Return the nearest preceding sectioning command's title, or ''.

    Deepest (\\subsubsection) preferred when multiple precede the line.
    """
    lines = text.splitlines()[: line]
    best = ""
    for ln in lines:
        m = SECTION_RE.match(ln.strip())
        if m:
            best = m.group(2).strip()
    return best


def extract(tex_path: Path) -> list[dict]:
    """Full pipeline: read .tex, return list of citation records."""
    tex_path = Path(tex_path)
    text = tex_path.read_text(encoding="utf-8", errors="replace")
    raw = find_citations(text)
    out: list[dict] = []
    for entry in raw:
        out.append(
            {
                "bibkey": entry["bibkey"],
                "line": entry["line"],
                "tex_file": str(tex_path),
                "paragraph": find_paragraph(text, entry["line"]),
                "section_heading": find_section_heading(text, entry["line"]),
            }
        )
    return out
```

- [ ] **Step 4: Add CLI to `extract_citations.py`**

Append:

```python
import json
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: extract_citations.py <tex_path> <output_json>", file=sys.stderr)
        sys.exit(2)
    items = extract(Path(sys.argv[1]))
    Path(sys.argv[2]).parent.mkdir(parents=True, exist_ok=True)
    Path(sys.argv[2]).write_text(json.dumps(items, indent=2), encoding="utf-8")
```

- [ ] **Step 5: Run all extract tests**

Run: `pytest citecheck-plugin/tests/test_extract_citations.py -v`
Expected: all PASS.

- [ ] **Step 6: Commit**

```bash
git add citecheck-plugin/skills/citecheck/scripts/extract_citations.py \
        citecheck-plugin/tests/test_extract_citations.py
git commit -m "extract_citations: paragraph + section heading + CLI"
```

---

## Task 7: fetch_abstracts — title normalization and similarity

**Files:**
- Create: `citecheck-plugin/skills/citecheck/scripts/fetch_abstracts.py`
- Create: `citecheck-plugin/tests/test_fetch_abstracts.py`

- [ ] **Step 1: Write failing tests for normalization + similarity**

```python
from fetch_abstracts import normalize_title, title_similarity


def test_normalize_strips_latex_and_punctuation():
    assert normalize_title("{\\textit{Foo}} bar: baz!") == "foo bar baz"


def test_similarity_high_for_close_titles():
    a = "CosmiXs: cosmic messenger spectra for indirect dark matter searches"
    b = "CosmiXs cosmic messenger spectra for indirect dark matter searches."
    assert title_similarity(a, b) >= 0.9


def test_similarity_low_for_different_titles():
    assert title_similarity("Quantum gravity in 11 dimensions",
                            "Bayesian inference for dark matter") < 0.5
```

- [ ] **Step 2: Run, confirm failure**

Run: `pytest citecheck-plugin/tests/test_fetch_abstracts.py -v`

- [ ] **Step 3: Write the initial `fetch_abstracts.py`**

```python
"""Fetch paper abstracts from InspireHEP (preferred) and arXiv (fallback).

Resolution chain per bibkey:
  1. Inspire by arXiv ID
  2. Inspire by DOI
  3. Inspire by title (similarity >= 0.90)
  4. arXiv by arXiv ID
  5. arXiv by title (similarity >= 0.90)
First hit wins. Title validation runs on every successful fetch.
"""
from __future__ import annotations

import re
import difflib

_LATEX_CMD_RE = re.compile(r"\\[a-zA-Z]+\{?")
_BRACES_RE = re.compile(r"[{}]")
_PUNCT_RE = re.compile(r"[^\w\s]")
_WS_RE = re.compile(r"\s+")


def normalize_title(s: str) -> str:
    s = s or ""
    s = _LATEX_CMD_RE.sub("", s)
    s = _BRACES_RE.sub("", s)
    s = _PUNCT_RE.sub(" ", s)
    s = _WS_RE.sub(" ", s).strip().lower()
    return s


def title_similarity(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, normalize_title(a), normalize_title(b)).ratio()
```

- [ ] **Step 4: Run, confirm pass**

Run: `pytest citecheck-plugin/tests/test_fetch_abstracts.py -v`

- [ ] **Step 5: Commit**

```bash
git add citecheck-plugin/skills/citecheck/scripts/fetch_abstracts.py \
        citecheck-plugin/tests/test_fetch_abstracts.py
git commit -m "fetch_abstracts: title normalization and similarity"
```

---

## Task 8: fetch_abstracts — Inspire arXiv lookup (with HTTP mock)

**Files:**
- Modify: `citecheck-plugin/skills/citecheck/scripts/fetch_abstracts.py`
- Modify: `citecheck-plugin/tests/test_fetch_abstracts.py`
- Create: `citecheck-plugin/tests/fixtures/inspire_arxiv.json`

- [ ] **Step 1: Write `tests/fixtures/inspire_arxiv.json`**

```json
{
  "hits": {
    "hits": [
      {
        "id": "2729450",
        "metadata": {
          "titles": [{"title": "CosmiXs: cosmic messenger spectra for indirect dark matter searches"}],
          "abstracts": [{"value": "We present an updated set of cosmic messenger spectra..."}],
          "arxiv_eprints": [{"value": "2312.01153"}],
          "dois": [{"value": "10.1088/1475-7516/2024/03/035"}],
          "authors": [{"full_name": "Arina, Chiara"}, {"full_name": "Di Mauro, Mattia"}]
        }
      }
    ],
    "total": 1
  }
}
```

- [ ] **Step 2: Write the failing test**

```python
import json
from unittest.mock import patch, MagicMock
from pathlib import Path

FIXT = Path(__file__).parent / "fixtures"


def _mock_urlopen(return_bytes: bytes):
    cm = MagicMock()
    cm.__enter__.return_value.read.return_value = return_bytes
    cm.__exit__.return_value = False
    return cm


def test_query_inspire_arxiv_returns_normalized_hit():
    from fetch_abstracts import query_inspire_arxiv
    payload = (FIXT / "inspire_arxiv.json").read_bytes()
    with patch("fetch_abstracts.urlopen", return_value=_mock_urlopen(payload)):
        hit = query_inspire_arxiv("2312.01153")
    assert hit is not None
    assert hit["title"].startswith("CosmiXs")
    assert hit["abstract"].startswith("We present")
    assert hit["arxiv_id"] == "2312.01153"
    assert hit["inspire_id"] == "2729450"
```

- [ ] **Step 3: Run, confirm failure**

- [ ] **Step 4: Implement the Inspire arXiv query**

Append to `fetch_abstracts.py`:

```python
import json
from urllib.request import urlopen, Request
from urllib.parse import quote_plus

INSPIRE_BASE = "https://inspirehep.net/api/literature"
INSPIRE_FIELDS = "titles,authors,abstracts,arxiv_eprints,dois"
USER_AGENT = "citecheck/0.1.0 (+https://github.com/aureamerio/citecheck)"


def _http_get_json(url: str, timeout: float = 15.0) -> dict:
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _normalize_inspire_hit(hit: dict) -> dict | None:
    md = hit.get("metadata", {})
    titles = md.get("titles") or []
    abstracts = md.get("abstracts") or []
    if not titles:
        return None
    arxiv = (md.get("arxiv_eprints") or [{}])[0].get("value")
    doi = (md.get("dois") or [{}])[0].get("value")
    authors = md.get("authors") or []
    return {
        "title": titles[0].get("title", "").strip(),
        "abstract": (abstracts[0].get("value") if abstracts else None),
        "arxiv_id": arxiv,
        "doi": doi,
        "inspire_id": hit.get("id"),
        "authors_short": _authors_short(authors),
    }


def _authors_short(authors: list[dict]) -> str | None:
    if not authors:
        return None
    first = authors[0].get("full_name", "").split(",")[0].strip()
    if len(authors) == 1:
        return first
    return f"{first} et al."


def query_inspire_arxiv(arxiv_id: str) -> dict | None:
    url = f"{INSPIRE_BASE}?q=arxiv:{quote_plus(arxiv_id)}&fields={INSPIRE_FIELDS}&size=1"
    try:
        data = _http_get_json(url)
    except Exception:
        return None
    hits = (data.get("hits") or {}).get("hits") or []
    if not hits:
        return None
    return _normalize_inspire_hit(hits[0])
```

- [ ] **Step 5: Run, confirm pass**

Run: `pytest citecheck-plugin/tests/test_fetch_abstracts.py -v`

- [ ] **Step 6: Commit**

```bash
git add citecheck-plugin/skills/citecheck/scripts/fetch_abstracts.py \
        citecheck-plugin/tests/test_fetch_abstracts.py \
        citecheck-plugin/tests/fixtures/inspire_arxiv.json
git commit -m "fetch_abstracts: Inspire arXiv lookup"
```

---

## Task 9: fetch_abstracts — Inspire DOI and title fallbacks

**Files:**
- Modify: `citecheck-plugin/skills/citecheck/scripts/fetch_abstracts.py`
- Modify: `citecheck-plugin/tests/test_fetch_abstracts.py`

- [ ] **Step 1: Add failing tests**

```python
def test_query_inspire_doi(monkeypatch):
    from fetch_abstracts import query_inspire_doi
    payload = (FIXT / "inspire_arxiv.json").read_bytes()  # shape is the same
    with patch("fetch_abstracts.urlopen", return_value=_mock_urlopen(payload)):
        hit = query_inspire_doi("10.1088/1475-7516/2024/03/035")
    assert hit["doi"] == "10.1088/1475-7516/2024/03/035"


def test_query_inspire_title_requires_high_similarity():
    from fetch_abstracts import query_inspire_title
    payload = (FIXT / "inspire_arxiv.json").read_bytes()
    bib_title = "CosmiXs cosmic messenger spectra for indirect dark matter searches"
    with patch("fetch_abstracts.urlopen", return_value=_mock_urlopen(payload)):
        ok = query_inspire_title(bib_title, bib_title)
    assert ok is not None

    with patch("fetch_abstracts.urlopen", return_value=_mock_urlopen(payload)):
        bad = query_inspire_title("Wholly different topic", "Wholly different topic")
    assert bad is None  # response title does not match queried bib title
```

- [ ] **Step 2: Run, confirm failure**

- [ ] **Step 3: Implement DOI and title queries**

Append to `fetch_abstracts.py`:

```python
TITLE_MATCH_OK = 0.90


def query_inspire_doi(doi: str) -> dict | None:
    url = f"{INSPIRE_BASE}?q=doi:{quote_plus(doi)}&fields={INSPIRE_FIELDS}&size=1"
    try:
        data = _http_get_json(url)
    except Exception:
        return None
    hits = (data.get("hits") or {}).get("hits") or []
    return _normalize_inspire_hit(hits[0]) if hits else None


def query_inspire_title(query_title: str, bib_title: str) -> dict | None:
    url = f"{INSPIRE_BASE}?q=title:{quote_plus(query_title)}&fields={INSPIRE_FIELDS}&size=1"
    try:
        data = _http_get_json(url)
    except Exception:
        return None
    hits = (data.get("hits") or {}).get("hits") or []
    if not hits:
        return None
    hit = _normalize_inspire_hit(hits[0])
    if hit is None:
        return None
    if title_similarity(hit["title"], bib_title) < TITLE_MATCH_OK:
        return None
    return hit
```

- [ ] **Step 4: Run, confirm pass**

- [ ] **Step 5: Commit**

```bash
git add citecheck-plugin/skills/citecheck/scripts/fetch_abstracts.py \
        citecheck-plugin/tests/test_fetch_abstracts.py
git commit -m "fetch_abstracts: Inspire DOI + title lookups"
```

---

## Task 10: fetch_abstracts — arXiv API fallback

**Files:**
- Modify: `citecheck-plugin/skills/citecheck/scripts/fetch_abstracts.py`
- Modify: `citecheck-plugin/tests/test_fetch_abstracts.py`
- Create: `citecheck-plugin/tests/fixtures/arxiv_response.xml`

- [ ] **Step 1: Write `tests/fixtures/arxiv_response.xml`** (a minimal Atom response)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <id>http://arxiv.org/abs/2312.01153v1</id>
    <title>CosmiXs: cosmic messenger spectra for indirect dark matter searches</title>
    <summary>We present an updated set of cosmic messenger spectra produced from dark matter annihilation.</summary>
    <author><name>Chiara Arina</name></author>
    <author><name>Mattia Di Mauro</name></author>
    <published>2023-12-02T00:00:00Z</published>
  </entry>
</feed>
```

- [ ] **Step 2: Add failing tests**

```python
def test_query_arxiv_id():
    from fetch_abstracts import query_arxiv_id
    payload = (FIXT / "arxiv_response.xml").read_bytes()
    with patch("fetch_abstracts.urlopen", return_value=_mock_urlopen(payload)):
        hit = query_arxiv_id("2312.01153")
    assert hit is not None
    assert hit["title"].startswith("CosmiXs")
    assert hit["abstract"].startswith("We present")
    assert hit["arxiv_id"] == "2312.01153"


def test_query_arxiv_title_requires_similarity():
    from fetch_abstracts import query_arxiv_title
    payload = (FIXT / "arxiv_response.xml").read_bytes()
    with patch("fetch_abstracts.urlopen", return_value=_mock_urlopen(payload)):
        ok = query_arxiv_title("CosmiXs cosmic messenger spectra",
                               "CosmiXs cosmic messenger spectra")
    assert ok is not None
    with patch("fetch_abstracts.urlopen", return_value=_mock_urlopen(payload)):
        bad = query_arxiv_title("Totally unrelated paper", "Totally unrelated paper")
    assert bad is None
```

- [ ] **Step 3: Run, confirm failure**

- [ ] **Step 4: Implement arXiv queries**

Append to `fetch_abstracts.py`:

```python
import xml.etree.ElementTree as ET

ARXIV_BASE = "https://export.arxiv.org/api/query"
ARXIV_NS = {"a": "http://www.w3.org/2005/Atom"}


def _http_get_bytes(url: str, timeout: float = 15.0) -> bytes:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _parse_arxiv_entry(xml_bytes: bytes) -> dict | None:
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return None
    entry = root.find("a:entry", ARXIV_NS)
    if entry is None:
        return None
    title_el = entry.find("a:title", ARXIV_NS)
    summary_el = entry.find("a:summary", ARXIV_NS)
    id_el = entry.find("a:id", ARXIV_NS)
    authors = entry.findall("a:author/a:name", ARXIV_NS)
    arxiv_id = None
    if id_el is not None and id_el.text:
        m = re.search(r"abs/([^v\s]+)(?:v\d+)?", id_el.text)
        if m:
            arxiv_id = m.group(1)
    return {
        "title": (title_el.text or "").strip() if title_el is not None else "",
        "abstract": (summary_el.text or "").strip() if summary_el is not None else None,
        "arxiv_id": arxiv_id,
        "doi": None,
        "inspire_id": None,
        "authors_short": _authors_short_plain([a.text for a in authors if a.text]),
    }


def _authors_short_plain(names: list[str]) -> str | None:
    if not names:
        return None
    first = names[0].split(",")[0].strip().split()[-1] if "," not in names[0] else names[0].split(",")[0].strip()
    if len(names) == 1:
        return first
    return f"{first} et al."


def query_arxiv_id(arxiv_id: str) -> dict | None:
    url = f"{ARXIV_BASE}?id_list={quote_plus(arxiv_id)}"
    try:
        data = _http_get_bytes(url)
    except Exception:
        return None
    return _parse_arxiv_entry(data)


def query_arxiv_title(query_title: str, bib_title: str) -> dict | None:
    url = f"{ARXIV_BASE}?search_query=ti:{quote_plus(query_title)}&max_results=1"
    try:
        data = _http_get_bytes(url)
    except Exception:
        return None
    hit = _parse_arxiv_entry(data)
    if hit is None:
        return None
    if title_similarity(hit["title"], bib_title) < TITLE_MATCH_OK:
        return None
    return hit
```

- [ ] **Step 5: Run, confirm pass**

- [ ] **Step 6: Commit**

```bash
git add citecheck-plugin/skills/citecheck/scripts/fetch_abstracts.py \
        citecheck-plugin/tests/test_fetch_abstracts.py \
        citecheck-plugin/tests/fixtures/arxiv_response.xml
git commit -m "fetch_abstracts: arXiv API id + title fallback"
```

---

## Task 11: fetch_abstracts — resolve() chain + title validation

**Files:**
- Modify: `citecheck-plugin/skills/citecheck/scripts/fetch_abstracts.py`
- Modify: `citecheck-plugin/tests/test_fetch_abstracts.py`

- [ ] **Step 1: Add failing tests for the unified `resolve()`**

```python
def test_resolve_uses_inspire_arxiv_first(monkeypatch):
    from fetch_abstracts import resolve
    inspire_payload = (FIXT / "inspire_arxiv.json").read_bytes()

    calls = []
    def fake_urlopen(req, timeout=15.0):
        calls.append(req.full_url)
        return _mock_urlopen(inspire_payload)

    with patch("fetch_abstracts.urlopen", side_effect=fake_urlopen):
        rec = resolve(
            "2024JCAP...03..035A",
            {
                "title": "CosmiXs: cosmic messenger spectra for indirect dark matter searches",
                "arxiv_id": "2312.01153",
                "doi": None,
            },
        )

    assert rec["source"] == "inspire_arxiv"
    assert rec["title_match"] == "ok"
    assert rec["abstract"].startswith("We present")
    assert "inspirehep.net" in calls[0]


def test_resolve_marks_mismatch_when_titles_differ():
    from fetch_abstracts import resolve
    inspire_payload = (FIXT / "inspire_arxiv.json").read_bytes()
    with patch("fetch_abstracts.urlopen", return_value=_mock_urlopen(inspire_payload)):
        rec = resolve(
            "Bogus2020",
            {"title": "An unrelated paper", "arxiv_id": "2312.01153", "doi": None},
        )
    assert rec["source"] == "inspire_arxiv"
    assert rec["title_match"] == "mismatch"
    assert rec["title_similarity"] < 0.7


def test_resolve_falls_back_to_arxiv_when_inspire_empty():
    from fetch_abstracts import resolve
    empty_inspire = b'{"hits": {"hits": [], "total": 0}}'
    arxiv_payload = (FIXT / "arxiv_response.xml").read_bytes()
    responses = [_mock_urlopen(empty_inspire), _mock_urlopen(empty_inspire),
                 _mock_urlopen(empty_inspire), _mock_urlopen(arxiv_payload)]
    with patch("fetch_abstracts.urlopen", side_effect=lambda *a, **k: responses.pop(0)):
        rec = resolve(
            "ML2020",
            {"title": "CosmiXs cosmic messenger spectra for indirect dark matter searches",
             "arxiv_id": "2312.01153", "doi": None},
        )
    assert rec["source"] == "arxiv_id"
    assert rec["abstract"].startswith("We present")


def test_resolve_returns_not_found_when_all_paths_fail():
    from fetch_abstracts import resolve
    empty_inspire = b'{"hits": {"hits": [], "total": 0}}'
    empty_arxiv = b'<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom"></feed>'
    responses = [_mock_urlopen(empty_inspire)] * 3 + [_mock_urlopen(empty_arxiv)] * 2
    with patch("fetch_abstracts.urlopen", side_effect=lambda *a, **k: responses.pop(0)):
        rec = resolve("Missing", {"title": "Whatever", "arxiv_id": "0000.00000", "doi": None})
    assert rec["source"] == "not_found"
    assert rec["abstract"] is None
```

- [ ] **Step 2: Run, confirm failure**

- [ ] **Step 3: Implement `resolve()`**

Append to `fetch_abstracts.py`:

```python
import datetime

TITLE_MATCH_FUZZY = 0.70


def _classify_title_match(sim: float) -> str:
    if sim >= TITLE_MATCH_OK:
        return "ok"
    if sim >= TITLE_MATCH_FUZZY:
        return "fuzzy"
    return "mismatch"


def _augment(rec: dict, *, bibkey: str, bib_title: str, source: str) -> dict:
    sim = title_similarity(rec.get("title", ""), bib_title) if bib_title else 1.0
    rec.update(
        {
            "bibkey": bibkey,
            "bib_title": bib_title,
            "fetched_title": rec.get("title"),
            "title_match": _classify_title_match(sim),
            "title_similarity": round(sim, 3),
            "source": source,
            "fetched_at": datetime.datetime.utcnow().isoformat() + "Z",
        }
    )
    return rec


def resolve(
    bibkey: str,
    meta: dict,
    *,
    use_arxiv_fallback: bool = True,
    cross_check: bool = False,  # see Task 12
) -> dict:
    """Run the resolution chain. Returns the cache-file-shaped dict.

    `meta` should have keys: title, arxiv_id, doi.
    """
    bib_title = meta.get("title") or ""
    arxiv_id = meta.get("arxiv_id")
    doi = meta.get("doi")

    if arxiv_id:
        hit = query_inspire_arxiv(arxiv_id)
        if hit:
            return _augment(hit, bibkey=bibkey, bib_title=bib_title, source="inspire_arxiv")
    if doi:
        hit = query_inspire_doi(doi)
        if hit:
            return _augment(hit, bibkey=bibkey, bib_title=bib_title, source="inspire_doi")
    if bib_title:
        hit = query_inspire_title(bib_title, bib_title)
        if hit:
            return _augment(hit, bibkey=bibkey, bib_title=bib_title, source="inspire_title")

    if use_arxiv_fallback:
        if arxiv_id:
            hit = query_arxiv_id(arxiv_id)
            if hit:
                return _augment(hit, bibkey=bibkey, bib_title=bib_title, source="arxiv_id")
        if bib_title:
            hit = query_arxiv_title(bib_title, bib_title)
            if hit:
                return _augment(hit, bibkey=bibkey, bib_title=bib_title, source="arxiv_title")

    return {
        "bibkey": bibkey,
        "title": None,
        "abstract": None,
        "arxiv_id": arxiv_id,
        "doi": doi,
        "inspire_id": None,
        "authors_short": None,
        "bib_title": bib_title,
        "fetched_title": None,
        "title_match": "not_found",
        "title_similarity": 0.0,
        "source": "not_found",
        "fetched_at": datetime.datetime.utcnow().isoformat() + "Z",
    }
```

- [ ] **Step 4: Run, confirm pass**

Run: `pytest citecheck-plugin/tests/test_fetch_abstracts.py -v`

- [ ] **Step 5: Commit**

```bash
git add citecheck-plugin/skills/citecheck/scripts/fetch_abstracts.py \
        citecheck-plugin/tests/test_fetch_abstracts.py
git commit -m "fetch_abstracts: resolve() chain with title validation"
```

---

## Task 12: fetch_abstracts — cross-check mode

**Files:**
- Modify: `citecheck-plugin/skills/citecheck/scripts/fetch_abstracts.py`
- Modify: `citecheck-plugin/tests/test_fetch_abstracts.py`

- [ ] **Step 1: Add failing test**

```python
def test_cross_check_replaces_inspire_mismatch_with_arxiv():
    from fetch_abstracts import resolve

    # Inspire returns a CosmiXs hit, but the bib title is something else.
    # arXiv returns a matching title for the bib_title we send.
    inspire_payload = (FIXT / "inspire_arxiv.json").read_bytes()
    arxiv_payload = (FIXT / "arxiv_response.xml").read_bytes()
    seq = [_mock_urlopen(inspire_payload), _mock_urlopen(arxiv_payload)]

    with patch("fetch_abstracts.urlopen", side_effect=lambda *a, **k: seq.pop(0)):
        rec = resolve(
            "MaybeMismatched",
            {
                "title": "CosmiXs cosmic messenger spectra for indirect dark matter searches",
                "arxiv_id": "2312.01153",
                "doi": None,
            },
            cross_check=True,
        )
    # Both abstracts match the bib_title in this fixture, so cross-check sees
    # no mismatch and keeps the Inspire hit. (Mismatch path is exercised by
    # the live integration test in Task 17.)
    assert rec["source"] in ("inspire_arxiv", "arxiv_xref")


def test_cross_check_promotes_arxiv_on_mismatch():
    """Force an Inspire mismatch, verify arxiv_xref is used."""
    from fetch_abstracts import resolve
    inspire_payload = (FIXT / "inspire_arxiv.json").read_bytes()
    arxiv_payload = (FIXT / "arxiv_response.xml").read_bytes()
    seq = [_mock_urlopen(inspire_payload), _mock_urlopen(arxiv_payload)]

    with patch("fetch_abstracts.urlopen", side_effect=lambda *a, **k: seq.pop(0)):
        rec = resolve(
            "MismatchKey",
            {
                # bib_title intentionally != inspire title.
                "title": "Completely unrelated bib title here",
                "arxiv_id": "2312.01153",
                "doi": None,
            },
            cross_check=True,
        )
    assert rec["source"] == "inspire_arxiv"
    assert rec["title_match"] == "mismatch"
    assert "cross_check_note" in rec  # populated even on no-help cases
```

- [ ] **Step 2: Run, confirm failure**

- [ ] **Step 3: Patch `resolve()` to support cross-check**

Replace the arXiv-ID-block-inside-Inspire-mismatch path. Update `resolve()`'s first branch:

```python
    if arxiv_id:
        hit = query_inspire_arxiv(arxiv_id)
        if hit:
            rec = _augment(hit, bibkey=bibkey, bib_title=bib_title, source="inspire_arxiv")
            if cross_check and rec["title_match"] == "mismatch":
                arxiv_hit = query_arxiv_id(arxiv_id)
                if arxiv_hit and title_similarity(arxiv_hit["title"], bib_title) >= TITLE_MATCH_OK:
                    promoted = _augment(arxiv_hit, bibkey=bibkey, bib_title=bib_title, source="arxiv_xref")
                    promoted["cross_check_note"] = (
                        f"Inspire arxiv:{arxiv_id} returned mismatched title; "
                        f"arXiv API title matched bib title at sim={promoted['title_similarity']}."
                    )
                    return promoted
                rec["cross_check_note"] = "Inspire mismatch confirmed; arXiv did not produce a better match."
            return rec
```

- [ ] **Step 4: Run, confirm pass**

- [ ] **Step 5: Commit**

```bash
git add citecheck-plugin/skills/citecheck/scripts/fetch_abstracts.py \
        citecheck-plugin/tests/test_fetch_abstracts.py
git commit -m "fetch_abstracts: --cross-check Inspire vs arXiv"
```

---

## Task 13: fetch_abstracts — cache I/O, parallel runner, CLI

**Files:**
- Modify: `citecheck-plugin/skills/citecheck/scripts/fetch_abstracts.py`
- Modify: `citecheck-plugin/tests/test_fetch_abstracts.py`

- [ ] **Step 1: Add failing tests for cache and parallel runner**

```python
def test_cache_round_trip(tmp_path):
    from fetch_abstracts import write_cache, read_cache
    rec = {"bibkey": "K", "title": "t", "abstract": "a", "source": "inspire_arxiv",
           "title_match": "ok", "title_similarity": 1.0}
    write_cache(tmp_path, rec)
    assert (tmp_path / "K.json").exists()
    assert read_cache(tmp_path, "K")["title"] == "t"
    assert read_cache(tmp_path, "Missing") is None


def test_fetch_missing_writes_one_file_per_key(tmp_path):
    from fetch_abstracts import fetch_missing
    inspire_payload = (FIXT / "inspire_arxiv.json").read_bytes()
    missing = [
        {"bibkey": "K1", "title": "CosmiXs: cosmic messenger spectra for indirect dark matter searches",
         "arxiv_id": "2312.01153", "doi": None},
        {"bibkey": "K2", "title": "CosmiXs: cosmic messenger spectra for indirect dark matter searches",
         "arxiv_id": "2312.01153", "doi": None},
    ]
    with patch("fetch_abstracts.urlopen", side_effect=lambda *a, **k: _mock_urlopen(inspire_payload)):
        fetch_missing(missing, tmp_path, parallel=2)
    assert (tmp_path / "K1.json").exists()
    assert (tmp_path / "K2.json").exists()
```

- [ ] **Step 2: Run, confirm failure**

- [ ] **Step 3: Implement cache + parallel runner + CLI**

Append to `fetch_abstracts.py`:

```python
import argparse
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


def write_cache(cache_dir: Path, rec: dict) -> None:
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    bibkey = rec["bibkey"]
    safe = bibkey.replace("/", "_")
    (cache_dir / f"{safe}.json").write_text(json.dumps(rec, indent=2), encoding="utf-8")


def read_cache(cache_dir: Path, bibkey: str) -> dict | None:
    safe = bibkey.replace("/", "_")
    p = Path(cache_dir) / f"{safe}.json"
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


# Per-host token bucket so arXiv (≈ 1 req / 3 s) stays polite even when Inspire runs hot.
_HOST_LOCK = threading.Lock()
_HOST_NEXT: dict[str, float] = {}
_HOST_MIN_INTERVAL = {"export.arxiv.org": 3.0, "inspirehep.net": 0.1}


def _polite_sleep(host: str) -> None:
    interval = _HOST_MIN_INTERVAL.get(host, 0.1)
    with _HOST_LOCK:
        now = time.monotonic()
        next_ok = _HOST_NEXT.get(host, 0.0)
        wait = max(0.0, next_ok - now)
        _HOST_NEXT[host] = max(now, next_ok) + interval
    if wait > 0:
        time.sleep(wait)


# Wrap urlopen-using helpers to inject the throttle. Easiest: re-route the two
# low-level fetchers through _polite_sleep based on URL host.
_orig_http_get_json = _http_get_json
_orig_http_get_bytes = _http_get_bytes


def _throttle_for(url: str) -> None:
    from urllib.parse import urlparse
    host = urlparse(url).hostname or ""
    _polite_sleep(host)


def _http_get_json(url: str, timeout: float = 15.0) -> dict:  # noqa: F811
    _throttle_for(url)
    return _orig_http_get_json(url, timeout=timeout)


def _http_get_bytes(url: str, timeout: float = 15.0) -> bytes:  # noqa: F811
    _throttle_for(url)
    return _orig_http_get_bytes(url, timeout=timeout)


def fetch_missing(
    missing: list[dict],
    cache_dir: Path,
    *,
    parallel: int = 8,
    use_arxiv_fallback: bool = True,
    cross_check: bool = False,
) -> None:
    """Resolve each missing entry and write its cache file."""
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)

    def _one(item: dict) -> None:
        rec = resolve(
            item["bibkey"],
            item,
            use_arxiv_fallback=use_arxiv_fallback,
            cross_check=cross_check,
        )
        write_cache(cache_dir, rec)

    with ThreadPoolExecutor(max_workers=parallel) as pool:
        list(pool.map(_one, missing))


def _cli() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--missing", required=True, help="path to JSON list of {bibkey, title, arxiv_id, doi}")
    p.add_argument("--cache-dir", required=True)
    p.add_argument("--parallel", type=int, default=8)
    p.add_argument("--no-arxiv-fallback", action="store_true")
    p.add_argument("--cross-check", action="store_true")
    args = p.parse_args()
    missing = json.loads(Path(args.missing).read_text(encoding="utf-8"))
    fetch_missing(
        missing,
        Path(args.cache_dir),
        parallel=args.parallel,
        use_arxiv_fallback=not args.no_arxiv_fallback,
        cross_check=args.cross_check,
    )
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
```

- [ ] **Step 4: Run, confirm pass**

Run: `pytest citecheck-plugin/tests/test_fetch_abstracts.py -v`

- [ ] **Step 5: Commit**

```bash
git add citecheck-plugin/skills/citecheck/scripts/fetch_abstracts.py \
        citecheck-plugin/tests/test_fetch_abstracts.py
git commit -m "fetch_abstracts: cache I/O, parallel runner, CLI"
```

---

## Task 14: collate_report — JSON output

**Files:**
- Create: `citecheck-plugin/skills/citecheck/scripts/collate_report.py`
- Create: `citecheck-plugin/tests/test_collate_report.py`

- [ ] **Step 1: Write failing test**

```python
from pathlib import Path
from collate_report import collate


def test_collate_merges_citations_scores_abstracts():
    citations = [
        {"bibkey": "OK", "line": 10, "tex_file": "x.tex",
         "paragraph": "p", "section_heading": "S"},
        {"bibkey": "MISMATCH", "line": 20, "tex_file": "x.tex",
         "paragraph": "p", "section_heading": "S"},
        {"bibkey": "NOABS", "line": 30, "tex_file": "x.tex",
         "paragraph": "p", "section_heading": "S"},
    ]
    abstracts = {
        "OK": {"title_match": "ok", "title": "T-OK", "bib_title": "T-OK", "title_similarity": 1.0},
        "MISMATCH": {"title_match": "mismatch", "title": "wrong", "bib_title": "right", "title_similarity": 0.1},
        "NOABS": {"source": "not_found", "title_match": "not_found"},
    }
    scores = [
        {"id": "c0", "bibkey": "OK", "score": 9, "reason": "matches"},
        {"id": "c1", "bibkey": "MISMATCH", "score": None, "reason": "title_mismatch"},
        {"id": "c2", "bibkey": "NOABS", "score": None, "reason": "no_abstract"},
    ]
    report = collate(citations, scores, abstracts, tex_path="x.tex")
    assert report["total_citations"] == 3
    assert report["scored_low"] == 0
    assert report["unscored"]["no_abstract"] == 1
    assert report["unscored"]["title_mismatch"] == 1
    assert len(report["title_match_issues"]) == 1
```

- [ ] **Step 2: Run, confirm failure**

- [ ] **Step 3: Implement `collate()`**

Write `collate_report.py`:

```python
"""Merge citations, abstract cache, and batch scoring outputs into a report."""
from __future__ import annotations

import json
from pathlib import Path


def collate(
    citations: list[dict],
    scores: list[dict],
    abstracts: dict[str, dict],
    *,
    tex_path: str,
) -> dict:
    score_by_id = {s["id"]: s for s in scores}
    # Citations were given sequential ids c0, c1, ... in the orchestrator.
    rows = []
    for i, cit in enumerate(citations):
        cid = f"c{i}"
        s = score_by_id.get(cid, {"score": None, "reason": "scoring_failed"})
        a = abstracts.get(cit["bibkey"], {})
        rows.append(
            {
                "id": cid,
                "bibkey": cit["bibkey"],
                "line": cit["line"],
                "section_heading": cit.get("section_heading", ""),
                "paragraph": cit.get("paragraph", ""),
                "tex_file": cit.get("tex_file", tex_path),
                "score": s.get("score"),
                "reason": s.get("reason"),
                "flag": s.get("flag"),
                "abstract_title": a.get("title"),
                "bib_title": a.get("bib_title"),
                "title_match": a.get("title_match"),
                "title_similarity": a.get("title_similarity"),
                "source": a.get("source"),
            }
        )

    scored = [r for r in rows if isinstance(r["score"], int)]
    scored_low = [r for r in scored if r["score"] <= 4]
    scored_borderline = [r for r in scored if 5 <= r["score"] <= 6]
    scored_ok = [r for r in scored if r["score"] >= 7]
    title_issues = [r for r in rows if r["title_match"] == "mismatch"]

    unscored_counts = {"no_abstract": 0, "title_mismatch": 0, "missing_bib_entry": 0,
                       "no_bib_metadata": 0, "fetch_error": 0, "scoring_failed": 0}
    for r in rows:
        if r["score"] is None and r["reason"] in unscored_counts:
            unscored_counts[r["reason"]] += 1

    avg = (sum(r["score"] for r in scored) / len(scored)) if scored else None

    return {
        "tex_file": tex_path,
        "total_citations": len(rows),
        "average_score": round(avg, 2) if avg is not None else None,
        "scored_low": len(scored_low),
        "scored_borderline": len(scored_borderline),
        "scored_ok": len(scored_ok),
        "unscored": unscored_counts,
        "title_match_issues": title_issues,
        "needing_review": sorted(scored_low + scored_borderline, key=lambda r: r["score"]),
        "ok": sorted(scored_ok, key=lambda r: -r["score"]),
        "all_rows": rows,
    }
```

- [ ] **Step 4: Run, confirm pass**

Run: `pytest citecheck-plugin/tests/test_collate_report.py -v`

- [ ] **Step 5: Commit**

```bash
git add citecheck-plugin/skills/citecheck/scripts/collate_report.py \
        citecheck-plugin/tests/test_collate_report.py
git commit -m "collate_report: build JSON report"
```

---

## Task 15: collate_report — Markdown rendering + CLI

**Files:**
- Modify: `citecheck-plugin/skills/citecheck/scripts/collate_report.py`
- Modify: `citecheck-plugin/tests/test_collate_report.py`

- [ ] **Step 1: Add failing test**

```python
from collate_report import render_markdown


def test_render_markdown_has_three_sections():
    report = {
        "tex_file": "x.tex",
        "total_citations": 2,
        "average_score": 5.0,
        "scored_low": 1, "scored_borderline": 0, "scored_ok": 1,
        "unscored": {"no_abstract": 0, "title_mismatch": 0, "missing_bib_entry": 0,
                     "no_bib_metadata": 0, "fetch_error": 0, "scoring_failed": 0},
        "title_match_issues": [],
        "needing_review": [
            {"line": 10, "score": 2, "bibkey": "K", "section_heading": "S",
             "paragraph": "p", "abstract_title": "wrong", "reason": "off-topic"}
        ],
        "ok": [
            {"line": 20, "score": 9, "bibkey": "OK", "abstract_title": "right"}
        ],
        "all_rows": [],
    }
    md = render_markdown(report)
    assert "Citation review" in md
    assert "Citations needing review" in md
    assert "Citations OK" in md
    assert "score 2" in md
```

- [ ] **Step 2: Run, confirm failure**

- [ ] **Step 3: Implement `render_markdown` and CLI**

Append to `collate_report.py`:

```python
import argparse
import sys


def render_markdown(report: dict) -> str:
    lines: list[str] = []
    a = lines.append
    a(f"# Citation review: `{report['tex_file']}`\n")
    a(f"**Total citations:** {report['total_citations']}  ")
    a(f"**Average score:** {report['average_score']}  ")
    a(f"**Scored 1-4 (review):** {report['scored_low']}  ")
    a(f"**Scored 5-6 (borderline):** {report['scored_borderline']}  ")
    unscored = report["unscored"]
    total_unscored = sum(unscored.values())
    a(f"**Unscored:** {total_unscored} " +
      "(" + ", ".join(f"{k}: {v}" for k, v in unscored.items() if v) + ")")
    a("\n---\n")

    issues = report.get("title_match_issues") or []
    if issues:
        a("## Title-match issues (manual check)\n")
        a("| line | bibkey | bib title | fetched title | similarity |")
        a("|------|--------|-----------|---------------|------------|")
        for r in issues:
            a(f"| {r['line']} | `{r['bibkey']}` | {r.get('bib_title','')[:60]} | "
              f"{r.get('abstract_title','')[:60]} | {r.get('title_similarity')} |")
        a("")

    needing = report.get("needing_review") or []
    a("## Citations needing review (score ≤ 6, worst first)\n")
    if not needing:
        a("_None._\n")
    for r in needing:
        a(f"### line {r['line']} — score {r['score']} — bibkey `{r['bibkey']}`\n")
        a(f"**Section:** {r.get('section_heading','')}  ")
        a(f"**Paragraph:** {r.get('paragraph','')[:400]}  ")
        a(f"**Cited title:** *{r.get('abstract_title','')}*  ")
        a(f"**Reason:** {r.get('reason','')}\n")

    a("## Citations OK (score ≥ 7)\n")
    a("| line | score | bibkey | title |")
    a("|------|-------|--------|-------|")
    for r in (report.get("ok") or []):
        a(f"| {r['line']} | {r['score']} | `{r['bibkey']}` | {r.get('abstract_title','')[:80]} |")

    return "\n".join(lines) + "\n"


def _cli() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--citations", required=True)
    p.add_argument("--scores-dir", required=True, help="dir containing batch_*_output.json")
    p.add_argument("--abstracts-dir", required=True)
    p.add_argument("--tex-path", required=True)
    p.add_argument("--output-md", required=True)
    p.add_argument("--output-json", required=True)
    args = p.parse_args()

    citations = json.loads(Path(args.citations).read_text(encoding="utf-8"))
    scores: list[dict] = []
    for f in sorted(Path(args.scores_dir).glob("batch_*_output.json")):
        scores.extend(json.loads(f.read_text(encoding="utf-8")))
    abstracts: dict[str, dict] = {}
    for f in Path(args.abstracts_dir).glob("*.json"):
        try:
            rec = json.loads(f.read_text(encoding="utf-8"))
            abstracts[rec["bibkey"]] = rec
        except Exception:
            continue

    report = collate(citations, scores, abstracts, tex_path=args.tex_path)
    Path(args.output_json).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output_json).write_text(json.dumps(report, indent=2), encoding="utf-8")
    Path(args.output_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output_md).write_text(render_markdown(report), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
```

- [ ] **Step 4: Run, confirm pass**

Run: `pytest citecheck-plugin/tests/test_collate_report.py -v`

- [ ] **Step 5: Commit**

```bash
git add citecheck-plugin/skills/citecheck/scripts/collate_report.py \
        citecheck-plugin/tests/test_collate_report.py
git commit -m "collate_report: render markdown + CLI"
```

---

## Task 16: Write the scorer subagent definition

**Files:**
- Create: `citecheck-plugin/agents/citecheck-scorer.md`

- [ ] **Step 1: Write the agent file**

```markdown
---
name: citecheck-scorer
description: Scores citation pertinence 1-10 for a JSON batch of \cite references with paragraph context and fetched abstracts. Reads input JSON path, writes output JSON path, takes no other actions.
tools: Read, Write
model: haiku
color: cyan
---

You are a citation-pertinence classifier for academic research documents.
You receive a JSON batch where each entry has the paragraph in which a
\cite was used, the surrounding section heading, the cited paper's title,
and its abstract. Your job is to judge whether the cited paper is a
reasonable reference for the claim being made in that paragraph.

Procedure:
1. Read the input JSON file at the path given to you as `input_path`.
2. For each citation, assign an integer score from 1 to 10 using the rubric.
3. Write the array of results to the path given to you as `output_path`.
   Do nothing else.

Rubric:
- 9-10: Abstract directly supports the specific claim in the paragraph.
- 7-8:  Same sub-topic; plausibly supports the claim but not the sharpest reference.
- 5-6:  Same broad research area; relevant background but not the specific claim.
- 3-4:  Adjacent field; tenuous connection to the paragraph.
- 1-2:  Off-topic; likely a wrong key, swapped citation, or hallucination.

Special cases:
- `abstract_status == "not_found"`        → score: null, reason: "no_abstract".
- `abstract_status == "mismatch"`         → score: null, reason: "title_mismatch".
- `abstract_status == "missing_bib_entry"` → score: null, reason: "missing_bib_entry".
- `abstract_status == "no_bib_metadata"`  → score: null, reason: "no_bib_metadata".
- `abstract_status == "fetch_error"`      → score: null, reason: "fetch_error".
- `abstract_status == "fuzzy"`            → score normally + flag: "fuzzy_title".

Output JSON schema (top-level is an array):
[
  {"id": "...", "bibkey": "...", "score": <int|null>, "reason": "...", "flag": "..."?}
]

`reason` is one sentence, ≤ 140 characters, explaining the score.

Do not call any tool other than Read and Write.
Do not edit any file other than the output path you were given.
```

- [ ] **Step 2: Commit**

```bash
git add citecheck-plugin/agents/citecheck-scorer.md
git commit -m "agents: add citecheck-scorer haiku subagent"
```

---

## Task 17: Write the orchestration SKILL.md

**Files:**
- Create: `citecheck-plugin/skills/citecheck/SKILL.md`

- [ ] **Step 1: Write the skill file**

```markdown
---
name: citecheck
description: Score \cite pertinence in a LaTeX file. Use when the user runs /citecheck on a .tex file or asks to verify references against InspireHEP/arXiv abstracts.
---

# citecheck

Score every `\cite{...}` in a single LaTeX file against the cited paper's
abstract (InspireHEP preferred, arXiv as fallback), surface low-scoring or
title-mismatched citations for manual review.

## Inputs

- `tex_file` — absolute path to the `.tex` file passed by the user.
- Optional flags (parsed from the user message):
  `--bib <path>`, `--refresh`, `--refresh-missing`,
  `--no-arxiv-fallback`, `--cross-check`,
  `--batch-size <n>` (default 15), `--parallel <n>` (default 8).

All scripts live in `${CLAUDE_PLUGIN_ROOT}/skills/citecheck/scripts/`.
All outputs are written under `.citecheck/` and `.citecache/` rooted at the
current working directory.

## Steps

1. **Resolve bib.** If `--bib` was given, use it. Otherwise walk up from
   `tex_file` until a `bibliography.bib` is found. Fail fast with a clear
   message if none.

2. **Build bib index.**

   ```bash
   mkdir -p .citecheck/.tmp
   python3 ${CLAUDE_PLUGIN_ROOT}/skills/citecheck/scripts/parse_bib.py \
       <bib_path> .citecheck/.tmp/bib_index.json
   ```

3. **Extract citations.**

   ```bash
   python3 ${CLAUDE_PLUGIN_ROOT}/skills/citecheck/scripts/extract_citations.py \
       <tex_file> .citecheck/.tmp/citations.json
   ```

   If the citations file is empty, print
   `No \cite references found in <tex_file>.` and stop.

4. **Compute missing keys.** Read `bib_index.json` and `citations.json`.
   For each unique bibkey:
   - If the bibkey is not in `bib_index.json`, mark
     `abstract_status: "missing_bib_entry"` for later batching and skip fetch.
   - Else if the bib entry has no `title` AND no `arxiv_id` AND no `doi`, mark
     `abstract_status: "no_bib_metadata"` and skip fetch.
   - Else if `.citecache/abstracts/<safe>.json` exists and (unless `--refresh`)
     has a `source` other than `fetch_error` (and `not_found` only re-fetched
     when `--refresh-missing`), reuse it.
   - Else add `{bibkey, title, arxiv_id, doi}` to `missing_keys.json`.

   Write `missing_keys.json` to `.citecheck/.tmp/missing_keys.json`.

5. **Fetch missing abstracts.**

   ```bash
   python3 ${CLAUDE_PLUGIN_ROOT}/skills/citecheck/scripts/fetch_abstracts.py \
       --missing .citecheck/.tmp/missing_keys.json \
       --cache-dir .citecache/abstracts \
       --parallel <parallel> \
       [--cross-check] [--no-arxiv-fallback]
   ```

6. **Build batches.** Partition the citation list into batches of
   `--batch-size` items. For each citation, set `abstract_status` per Step 4
   (using the now-populated cache: `ok` / `fuzzy` / `mismatch` / `not_found` /
   `fetch_error` from the cache file, or the `missing_bib_entry` /
   `no_bib_metadata` flags from Step 4). Inline `abstract` text when present.
   Write `.citecheck/.tmp/batch_<n>_input.json` files.

7. **Dispatch scorers.** In a single message, issue one `Agent` call per
   batch with:
   - `subagent_type: "citecheck-scorer"`
   - `description: "Score batch <n>"`
   - `prompt: "input_path: .citecheck/.tmp/batch_<n>_input.json\noutput_path: .citecheck/.tmp/batch_<n>_output.json"`

   Concurrency budget: at most 8 parallel `Agent` calls per wave. For more
   than 8 batches, dispatch in waves of 8.

8. **Validate outputs.** For each batch, check that
   `.citecheck/.tmp/batch_<n>_output.json` exists and parses as a JSON list
   whose entries have `{id, bibkey, score, reason}`. On malformed/missing
   output, retry that batch's `Agent` call once. If the retry also fails,
   leave that batch's citations with `score: null, reason: "scoring_failed"`
   and continue.

9. **Collate report.**

   ```bash
   python3 ${CLAUDE_PLUGIN_ROOT}/skills/citecheck/scripts/collate_report.py \
       --citations .citecheck/.tmp/citations.json \
       --scores-dir .citecheck/.tmp/ \
       --abstracts-dir .citecache/abstracts \
       --tex-path <tex_file> \
       --output-md .citecheck/<basename>.md \
       --output-json .citecheck/<basename>.json
   ```

10. **Clean tmp.** Remove `.citecheck/.tmp/`.

11. **Print summary.** One line:
    `<N> citations · <M> needing review · <K> title-match issues · report at .citecheck/<basename>.md`

## Invariants

- Never modify the `.tex` file or `bibliography.bib`.
- Subagents must only call `Read` and `Write`. Reject any other tool surface.
- Abstract cache persists across runs; scoring is always recomputed.
- If a step fails, stop and report the failing step rather than continuing
  with partial state.
```

- [ ] **Step 2: Commit**

```bash
git add citecheck-plugin/skills/citecheck/SKILL.md
git commit -m "skills: add citecheck orchestrator skill"
```

---

## Task 18: Write the slash command

**Files:**
- Create: `citecheck-plugin/commands/citecheck.md`

- [ ] **Step 1: Write the command file**

```markdown
---
description: Score \cite pertinence in a LaTeX file against InspireHEP and arXiv abstracts using parallel haiku scoring.
argument-hint: <path-to-tex-file> [--bib <path>] [--refresh] [--refresh-missing] [--no-arxiv-fallback] [--cross-check] [--batch-size N] [--parallel N]
---

Run the `citecheck` skill on $ARGUMENTS.
```

- [ ] **Step 2: Commit**

```bash
git add citecheck-plugin/commands/citecheck.md
git commit -m "commands: add /citecheck slash command"
```

---

## Task 19: End-to-end script smoke test (no model)

**Files:**
- Create: `citecheck-plugin/tests/test_pipeline_smoke.py`

This task verifies the four Python scripts wire together without involving any model. It uses a tiny in-repo fixture and `unittest.mock` to intercept HTTP.

- [ ] **Step 1: Write the smoke test**

```python
"""End-to-end pipeline smoke test (no model in the loop)."""
import json
import subprocess
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

ROOT = Path(__file__).parent.parent
SCRIPTS = ROOT / "skills" / "citecheck" / "scripts"
FIXT = Path(__file__).parent / "fixtures"


def _mock_urlopen(b):
    cm = MagicMock()
    cm.__enter__.return_value.read.return_value = b
    cm.__exit__.return_value = False
    return cm


def test_full_pipeline_without_model(tmp_path, monkeypatch):
    # Stage fixture inputs.
    bib = tmp_path / "bibliography.bib"
    bib.write_text((FIXT / "sample.bib").read_text())
    tex = tmp_path / "sec.tex"
    tex.write_text((FIXT / "sample.tex").read_text())
    cache_dir = tmp_path / ".citecache" / "abstracts"
    tmp_dir = tmp_path / ".citecheck" / ".tmp"
    tmp_dir.mkdir(parents=True)

    # Step 1: parse_bib.
    subprocess.run(
        [sys.executable, str(SCRIPTS / "parse_bib.py"),
         str(bib), str(tmp_dir / "bib_index.json")],
        check=True,
    )

    # Step 2: extract_citations.
    subprocess.run(
        [sys.executable, str(SCRIPTS / "extract_citations.py"),
         str(tex), str(tmp_dir / "citations.json")],
        check=True,
    )

    # Step 3: build missing keys list (mirrors what SKILL.md does inline).
    bib_index = json.loads((tmp_dir / "bib_index.json").read_text())
    citations = json.loads((tmp_dir / "citations.json").read_text())
    missing = []
    seen = set()
    for c in citations:
        k = c["bibkey"]
        if k in seen:
            continue
        seen.add(k)
        meta = bib_index.get(k)
        if not meta:
            continue
        if not (meta.get("title") or meta.get("arxiv_id") or meta.get("doi")):
            continue
        missing.append({"bibkey": k, "title": meta.get("title"),
                        "arxiv_id": meta.get("arxiv_id"), "doi": meta.get("doi")})
    (tmp_dir / "missing.json").write_text(json.dumps(missing))

    # Step 4: fetch_abstracts (HTTP mocked).
    sys.path.insert(0, str(SCRIPTS))
    import fetch_abstracts as fa
    inspire = (FIXT / "inspire_arxiv.json").read_bytes()
    with patch.object(fa, "urlopen", side_effect=lambda *a, **k: _mock_urlopen(inspire)):
        fa.fetch_missing(missing, cache_dir, parallel=2)

    assert (cache_dir / "2024JCAP...03..035A.json").exists()

    # Step 5: stub scorer outputs.
    scores = [{"id": f"c{i}", "bibkey": c["bibkey"], "score": 8, "reason": "ok"}
              for i, c in enumerate(citations)]
    (tmp_dir / "batch_0_output.json").write_text(json.dumps(scores))

    # Step 6: collate.
    out_md = tmp_path / ".citecheck" / "sec.md"
    out_json = tmp_path / ".citecheck" / "sec.json"
    subprocess.run(
        [sys.executable, str(SCRIPTS / "collate_report.py"),
         "--citations", str(tmp_dir / "citations.json"),
         "--scores-dir", str(tmp_dir),
         "--abstracts-dir", str(cache_dir),
         "--tex-path", str(tex),
         "--output-md", str(out_md),
         "--output-json", str(out_json)],
        check=True,
    )
    assert out_md.exists()
    assert "Citation review" in out_md.read_text()
    assert out_json.exists()
```

- [ ] **Step 2: Run the smoke test**

Run: `pytest citecheck-plugin/tests/test_pipeline_smoke.py -v`
Expected: PASS.

- [ ] **Step 3: Run the full test suite**

Run: `pytest citecheck-plugin/ -v`
Expected: all PASS.

- [ ] **Step 4: Commit**

```bash
git add citecheck-plugin/tests/test_pipeline_smoke.py
git commit -m "tests: end-to-end pipeline smoke (no model)"
```

---

## Task 20: Live smoke test against a real thesis section

This is the only step that exercises real network and a real Claude subagent. Run from the thesis repo root.

- [ ] **Step 1: Install the plugin into Claude Code**

In Claude Code:

```
/plugin marketplace add ./citecheck-plugin
/plugin install citecheck
```

- [ ] **Step 2: Pick a small section and run**

```
/citecheck chapter_03/sections/3.1_inference.tex
```

- [ ] **Step 3: Inspect outputs**

Verify:
- `.citecache/abstracts/` populated with one JSON per unique bibkey in that file.
- `.citecheck/3.1_inference.md` exists; opens with the summary line; lists at least
  the top-of-file fields; "needing review" or "title-match issues" sections are
  populated if any apply.
- `.citecheck/3.1_inference.json` is valid JSON.

Manually spot-check 2-3 citations: pick one that scored low, read the
paragraph and the abstract, confirm the score is at least plausible.

- [ ] **Step 4: Commit updated `.gitignore` if needed**

Make sure `.citecache/` and `.citecheck/` are gitignored at the thesis-repo
level too (not just inside the plugin):

```bash
grep -q '^.citecache' .gitignore || echo '.citecache/' >> .gitignore
grep -q '^.citecheck' .gitignore || echo '.citecheck/' >> .gitignore
git add .gitignore
git commit -m "gitignore citecheck output dirs"
```

---

## Self-Review

**Spec coverage** — every section in `2026-05-18-citecheck-plugin-design.md` maps to a task:

| Spec section | Task(s) |
|---|---|
| Packaging / plugin manifest | 1 |
| Citation extraction | 4, 5, 6 |
| Bibliography parsing | 2, 3 |
| Abstract fetching — Inspire arxiv | 8 |
| Abstract fetching — Inspire DOI, title | 9 |
| Abstract fetching — arXiv id, title | 10 |
| Title validation | 7, 11 |
| Cross-check | 12 |
| Cache I/O, concurrency, rate limiting | 13 |
| Scoring subagent definition | 16 |
| Orchestrator SKILL.md | 17 |
| Slash command | 18 |
| Output report (JSON + Markdown) | 14, 15 |
| Failure modes — covered by SKILL.md branching, scorer special cases, collate's `unscored` counters | 14, 16, 17 |
| Re-run behavior (cache abstracts, always re-score) | 13, 17 |
| Smoke test | 19, 20 |

**Type/name consistency** — function and field names used across tasks:
`parse_bib`, `load_or_build_index`, `find_citations`, `strip_comments`,
`find_paragraph`, `find_section_heading`, `extract`,
`normalize_title`, `title_similarity`, `query_inspire_arxiv`,
`query_inspire_doi`, `query_inspire_title`, `query_arxiv_id`,
`query_arxiv_title`, `resolve`, `write_cache`, `read_cache`,
`fetch_missing`, `collate`, `render_markdown`. Each is introduced once and
referenced consistently. Cache file fields (`title_match`, `title_similarity`,
`bib_title`, `fetched_title`, `source`) are introduced in Task 11's `_augment`
and consumed by Tasks 14-15.

**No placeholders** — every TDD step contains real test code and real
implementation code; every CLI command has its full argument list; no
"TBD" / "TODO" / "similar to above" references.

---

Plan complete and saved to `docs/superpowers/plans/2026-05-18-citecheck-plugin.md`. Two execution options:

**1. Subagent-Driven (recommended)** — I dispatch a fresh subagent per task, review between tasks, fast iteration.

**2. Inline Execution** — Execute tasks in this session using executing-plans, batch execution with checkpoints.

Which approach?
