# Chapter 5 (Paper 4, DM subhalos) Update — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Propagate the revised paper (`chapter_05/sections/paper_dm_halos_new/main.tex`) into the integrated thesis chapter (`chapter_05/sections/paper_dm_halos/`), preserving thesis structure, labels, macros, and the central bibliography.

**Architecture:** A single one-shot Python migration script reads the revised `main.tex`, accepts all tracked changes (`\old{}` deleted, `\new{}` unwrapped), converts co-author review comments to thesis `\aure{}` WIP markers, remaps 14 citation keys to their existing thesis equivalents, restores the `halos:` label namespace on 3 renamed labels, rewrites figure paths, then slices the body into the 8 existing `sections/*.tex` files using the thesis heading-level convention. Two changed figures are copied; `paper_4.tex` and `bibliography.bib` are unchanged. Verification is a clean `latexmk` build of `main.tex`.

**Tech Stack:** Python 3 (stdlib only), pdflatex/latexmk + BibTeX (JHEP/memoir thesis build).

---

## Key facts established during brainstorming (do not re-derive)

- **Section ↔ main.tex mapping** (re-verify boundaries by heading text, not line numbers):

  | Old file | main.tex `\section` | Role | Heading-level map |
  |---|---|---|---|
  | `introduction.tex` | Introduction | body | `\section`→`\subsection` |
  | `statistical_analysis.tex` | Statistical analysis | body | `\section`→`\subsection`; `\subsection` stays |
  | `dm_subhalos_model.tex` | Dark matter subhalos model | body | same as above |
  | `mixture_model_and_limits.tex` | Mixture model of gamma-ray sources and limits on DM annihilation | body | same as above |
  | `conclusions.tex` | Discussion and conclusions | body | `\section`→`\subsection` |
  | `appendix_simulation.tex` | Simulation of gamma-ray signals from dark matter subhalos | appendix | keep levels |
  | `appendix_em_algorithm.tex` | Details of model optimization with the EM algorithm | appendix | keep levels |
  | `appendix_consistency_checks.tex` | Consistency checks of the model | appendix | keep levels (`\subsection` stays) |

  The thesis body uses **all `\subsection`** (no `\section`); appendices use `\section`+`\subsection`. This is the existing chapter convention and is reproduced faithfully. The two `\section{Dark Matter signal injection tests}` / `\section{Performance and consistency checks...}` lines near the consistency-checks appendix are **commented out** in `main.tex` — the splitter must ignore `%`-commented headings.

- **Tracked changes present in `main.tex`:** `\new{}` ×24 (unwrap, keep content), `\old{}` ×11 (delete content), `\dima{}` ×2 (co-author comments), `\aure{}` ×5 (author TODOs), `\st{}` only inside the `\old` definition. `\new{}`/`\old{}` spans **cross newlines and contain nested braces** (e.g. `\new{Same as Figure \ref{fig:bounds-bb}...}`) → must use balanced-brace matching, NOT regex/sed.

- **Review-comment handling (thesis convention, per CLAUDE.md "do not silently delete \aure WIP markers"):** keep the 5 `\aure{...}` as-is (thesis macro, renders orange); convert the 2 `\dima{...}` → `\aure{(Dima) ...}`. They remain as visible WIP markers for the author to resolve before final submission.

- **Bibliography: NEVER modified.** Of 86 cite keys, 72 already match `bibliography.bib`; 14 are remapped (verified by arXiv/DOI/title):

  | main.tex key | → thesis key | main.tex key | → thesis key |
  |---|---|---|---|
  | `2008Natur.454..735D` | `Diemand:2008in` | `2023arXiv230712546B` | `Ballet:2023qzs` |
  | `2009PhRvD..79a5014A` | `ArkaniHamed:2008qn` | `2024JCAP...03..035A` | `Arina:2023eic` |
  | `2012ApJ...753...83A` | `Fermi-LAT:2011sla` | `Fornasa:2015qua` | `DGRB-review` |
  | `2016PhR...636....1C` | `Charles:2016pgz` | `Hooper:2024avz` | `Hooper:2024` |
  | `2019Galax...7...81Z` | `Zavala:2019gpq` | `Steigman_2012` | `Steigman:2012nb` |
  | `2020ApJS..247...33A` | `Fermi-LAT:2019yla` | `hastie2009elements` | `Hastie:2009` |
  | `2022A&A...660A..87B` | `Bhat:2022` | `2022ApJS..260...53A` | `Fermi-LAT:2022byn` |

- **Label remap (restore `halos:` namespace):** `sec:data`→`sec:halos:data`, `sec:results`→`sec:halos:results`, `sec:conclusions`→`sec:halos:conclusions` (labels **and** internal refs). This keeps `chapter_06/sections/6.1_limits_individual.tex`'s `\ref{sec:halos:results}` working untouched. All other labels in `main.tex` already match the old files.

- **Figure paths:** `main.tex` uses `{img/...}`; thesis needs `{sections/paper_dm_halos/img/...}` (chapter included via `\import{chapter_05/}{chapter_5.tex}`). Rewrite `{img/` → `{sections/paper_dm_halos/img/`.

- **Custom body macros** (`\be \ee \ben \een \sigmav \Msub \Vmax \mdm \bx \panel \DMsubhalo* \FermiMLclassif` …) are **all already defined** in the thesis `macros.tex`. No macro work needed.

- **Abstract is byte-identical** between `main.tex` `\abstract{}` and the `paper_4.tex` intro paragraph → `paper_4.tex` is unchanged.

- **Only 2 figures changed:** `img/bounds/sigmav_bounds_flux_bb_left.pdf` and `img/bounds/sigmav_bounds_flux_bb_right.pdf` (the `*.pdf.old` files in the new dir are backups; ignore them).

---

## File structure

- **Create (transient migration tool):** `chapter_05/sections/port_dm_halos.py` — the one-shot porting script. Deleted in the final task.
- **Overwrite (ported content):** the 8 files in `chapter_05/sections/paper_dm_halos/sections/` listed in the mapping table.
- **Copy:** 2 PDFs into `chapter_05/sections/paper_dm_halos/img/bounds/`.
- **Unchanged:** `chapter_05/sections/paper_dm_halos/paper_4.tex`, `bibliography.bib`, `macros.tex`, `chapter_06/...`.
- **Kept until verified, then optionally removed:** `chapter_05/sections/paper_dm_halos_new/`.

---

## Task 1: Create working branch and snapshot baseline build

**Files:** none (git + build only)

- [ ] **Step 1: Create a branch**

```bash
cd /Users/aure/Documents/Github/phd-thesis
git checkout -b ch5-paper4-update
```

- [ ] **Step 2: Confirm the thesis currently builds (baseline)**

Run:
```bash
cd /Users/aure/Documents/Github/phd-thesis
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex >/tmp/build_baseline.log 2>&1; echo "exit=$?"
```
Expected: `exit=0` (a clean baseline). If it is non-zero, capture `tail -40 /tmp/build_baseline.log` and STOP — do not start porting on top of a broken build. (Use `$TMPDIR` if `/tmp` is not writable.)

- [ ] **Step 3: Record the count of unresolved references in the baseline**

Run:
```bash
grep -c 'LaTeX Warning: Reference' main.log || echo 0
```
Expected: a number N (baseline undefined refs). Record it; the post-port build must not exceed N.

- [ ] **Step 4: Commit the branch point (no content change yet)**

```bash
git add -A
git commit -m "chore: branch point before Ch5 Paper4 update" --allow-empty
```

---

## Task 2: Write the migration script — balanced-brace tracked-change resolver (with self-test)

**Files:**
- Create: `chapter_05/sections/port_dm_halos.py`

- [ ] **Step 1: Write the script skeleton with the brace-matching resolver and an inline self-test**

Create `chapter_05/sections/port_dm_halos.py` with exactly this content:

```python
#!/usr/bin/env python3
"""One-shot migration: revised paper main.tex -> integrated thesis section files.

Run from the repo root:  python chapter_05/sections/port_dm_halos.py
Use --selftest to run the unit checks only.
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]          # repo root
SRC = ROOT / "chapter_05/sections/paper_dm_halos_new/main.tex"
OUTDIR = ROOT / "chapter_05/sections/paper_dm_halos/sections"


def _match_brace(s, open_idx):
    """Given index of the '{' opening a group, return index of its matching '}'."""
    assert s[open_idx] == "{"
    depth = 0
    i = open_idx
    while i < len(s):
        c = s[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise ValueError("unbalanced braces starting at %d" % open_idx)


def resolve_macro(s, macro, keep):
    """Replace every \\macro{...} (balanced) by its inner text (keep=True) or '' (keep=False)."""
    tag = "\\" + macro + "{"
    out = []
    i = 0
    while True:
        j = s.find(tag, i)
        if j == -1:
            out.append(s[i:])
            return "".join(out)
        out.append(s[i:j])
        open_idx = j + len(tag) - 1            # index of the '{'
        close = _match_brace(s, open_idx)
        inner = s[open_idx + 1:close]
        if keep:
            out.append(inner)
        i = close + 1


def _selftest():
    # delete \old, keep \new, including nested braces and multi-line spans
    t = r"a \old{drop \ref{x}} b \new{keep \ref{y}} c"
    t = resolve_macro(t, "old", keep=False)
    t = resolve_macro(t, "new", keep=True)
    assert t == r"a  b keep \ref{y} c", repr(t)
    t2 = "p \\new{line1\nline2 {grp}} q"
    assert resolve_macro(t2, "new", keep=True) == "p line1\nline2 {grp} q"
    # \old containing \new: whole thing dropped
    t3 = r"x \old{was \new{this}} y"
    assert resolve_macro(t3, "old", keep=False) == "x  y"
    print("selftest OK")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        _selftest()
        sys.exit(0)
    main()
```

(`main()` is added in Task 3; the `--selftest` path does not call it.)

- [ ] **Step 2: Run the self-test to verify the resolver fails-then-passes correctly**

Run:
```bash
cd /Users/aure/Documents/Github/phd-thesis
python chapter_05/sections/port_dm_halos.py --selftest
```
Expected: `selftest OK` and exit 0. (If you run before adding `main()`, the `--selftest` branch returns before touching `main`, so it still works.)

- [ ] **Step 3: Commit**

```bash
git add chapter_05/sections/port_dm_halos.py
git commit -m "feat: brace-matching tracked-change resolver for Ch5 port"
```

---

## Task 3: Add the full transformation + split logic to the script

**Files:**
- Modify: `chapter_05/sections/port_dm_halos.py` (add the `main()` function and tables above the `if __name__` block)

- [ ] **Step 1: Insert the transformation tables and `main()` before the `if __name__ == "__main__"` block**

Add this code (place it after `resolve_macro` / `_selftest` and before `if __name__`):

```python
CITE_REMAP = {
    "2008Natur.454..735D": "Diemand:2008in",
    "2009PhRvD..79a5014A": "ArkaniHamed:2008qn",
    "2012ApJ...753...83A": "Fermi-LAT:2011sla",
    "2016PhR...636....1C": "Charles:2016pgz",
    "2019Galax...7...81Z": "Zavala:2019gpq",
    "2020ApJS..247...33A": "Fermi-LAT:2019yla",
    "2022A&A...660A..87B": "Bhat:2022",
    "2022ApJS..260...53A": "Fermi-LAT:2022byn",
    "2023arXiv230712546B": "Ballet:2023qzs",
    "2024JCAP...03..035A": "Arina:2023eic",
    "Fornasa:2015qua": "DGRB-review",
    "Hooper:2024avz": "Hooper:2024",
    "Steigman_2012": "Steigman:2012nb",
    "hastie2009elements": "Hastie:2009",
}

LABEL_REMAP = {           # restore halos: namespace (label + ref tokens)
    "{sec:data}": "{sec:halos:data}",
    "{sec:results}": "{sec:halos:results}",
    "{sec:conclusions}": "{sec:halos:conclusions}",
}

# ordered list: (section-title substring, output filename, is_appendix)
SECTIONS = [
    ("Introduction", "introduction.tex", False),
    ("Statistical analysis", "statistical_analysis.tex", False),
    ("Dark matter subhalos model", "dm_subhalos_model.tex", False),
    ("Mixture model of gamma-ray sources", "mixture_model_and_limits.tex", False),
    ("Discussion and conclusions", "conclusions.tex", False),
    ("Simulation of gamma-ray signals", "appendix_simulation.tex", True),
    ("Details of model optimization with the EM algorithm", "appendix_em_algorithm.tex", True),
    ("Consistency checks of the model", "appendix_consistency_checks.tex", True),
]


def transform(body):
    # 1. accept tracked changes
    body = resolve_macro(body, "old", keep=False)
    body = resolve_macro(body, "new", keep=True)
    # 2. co-author comments -> visible thesis WIP markers (keep \aure as-is)
    body = body.replace(r"\dima{", r"\aure{(Dima) ")
    # 3. citation key remap (token-safe: keys are bounded by { , space or })
    for old, new in CITE_REMAP.items():
        body = re.sub(r"(?<![\w:.\-])" + re.escape(old) + r"(?![\w:.\-])", new, body)
    # 4. label/ref namespace restore
    for old, new in LABEL_REMAP.items():
        body = body.replace(old, new)
    # 5. figure paths
    body = body.replace("{img/", "{sections/paper_dm_halos/img/")
    # 6. light Fermi normalisation
    body = body.replace(r"{\textit{Fermi}}", r"\Fermi")
    return body


def split_sections(body):
    """Return list of (filename, is_appendix, chunk) by active top-level \\section."""
    # indices of non-commented \section at line start
    starts = []
    for m in re.finditer(r"(?m)^[ \t]*\\section\{", body):
        # ensure not commented (no % before it on the line)
        line_start = body.rfind("\n", 0, m.start()) + 1
        if "%" in body[line_start:m.start()]:
            continue
        starts.append(m.start())
    starts.append(len(body))
    chunks = [body[starts[i]:starts[i + 1]] for i in range(len(starts) - 1)]
    # match each chunk to the SECTIONS table by title substring, in order
    result = []
    si = 0
    for chunk in chunks:
        title_line = chunk.split("\n", 1)[0]
        if si < len(SECTIONS) and SECTIONS[si][0] in title_line:
            name, fname, is_app = SECTIONS[si]
            result.append((fname, is_app, chunk))
            si += 1
        else:
            raise SystemExit("Unexpected section order at chunk:\n" + title_line)
    if si != len(SECTIONS):
        raise SystemExit("Only matched %d of %d sections" % (si, len(SECTIONS)))
    return result


def demote_body(chunk):
    # body: \section -> \subsection ; existing \subsection unchanged
    return chunk.replace(r"\section{", r"\subsection{")


def main():
    text = SRC.read_text(encoding="utf-8")
    start = text.index(r"\section{Introduction}")
    end = text.index(r"\end{document}")
    body = transform(text[start:end])
    # excise per-paper back-matter between conclusions and the appendices
    # (\acknowledgments ... \bibliography{DM_halos} ... \pagebreak ... \appendix).
    # The thesis supplies its own bibliography and the subappendices wrapper.
    ack = body.index(r"\acknowledgments")
    app_sec = body.index(r"\section{Simulation of gamma-ray signals")
    body = body[:ack] + body[app_sec:]
    for fname, is_app, chunk in split_sections(body):
        if not is_app:
            chunk = demote_body(chunk)
        (OUTDIR / fname).write_text(chunk.rstrip() + "\n", encoding="utf-8")
        print("wrote", fname, "(%d chars)" % len(chunk))
```

- [ ] **Step 2: Re-run the self-test (logic must still pass)**

Run:
```bash
python chapter_05/sections/port_dm_halos.py --selftest
```
Expected: `selftest OK`.

- [ ] **Step 3: Commit**

```bash
git add chapter_05/sections/port_dm_halos.py
git commit -m "feat: full transform+split logic for Ch5 port"
```

---

## Task 4: Run the migration and write the 8 section files

**Files:**
- Modify (overwrite): the 8 `chapter_05/sections/paper_dm_halos/sections/*.tex`

- [ ] **Step 1: Run the script**

Run:
```bash
cd /Users/aure/Documents/Github/phd-thesis
python chapter_05/sections/port_dm_halos.py
```
Expected: 8 `wrote <file>` lines, one per section, in the mapping order, no traceback.

- [ ] **Step 2: Verify no tracked-change or co-author macros survive**

Run:
```bash
cd /Users/aure/Documents/Github/phd-thesis/chapter_05/sections/paper_dm_halos/sections
grep -rnE '\\(new|old|dima|BZ|masc)\{' . ; echo "exit=$?"
```
Expected: no matches, `exit=1`. (`\aure{` is allowed and expected — do not flag it.)

- [ ] **Step 3: Verify no remapped citation keys survive**

Run:
```bash
cd /Users/aure/Documents/Github/phd-thesis/chapter_05/sections/paper_dm_halos/sections
grep -rnoE '2008Natur\.454\.\.735D|2009PhRvD\.\.79a5014A|2012ApJ\.\.\.753\.\.\.83A|2016PhR\.\.\.636\.\.\.\.1C|2019Galax\.\.\.7\.\.\.81Z|2020ApJS\.\.\.247\.\.\.33A|2022A&A\.\.\.660A\.\.87B|2022ApJS\.\.\.260\.\.\.53A|2023arXiv230712546B|2024JCAP\.\.\.03\.\.\.035A|Fornasa:2015qua|Hooper:2024avz|Steigman_2012|hastie2009elements' . ; echo "exit=$?"
```
Expected: no matches, `exit=1`.

- [ ] **Step 4: Verify the externally-referenced label is present and the renamed generics are gone**

Run:
```bash
cd /Users/aure/Documents/Github/phd-thesis/chapter_05/sections/paper_dm_halos/sections
grep -rn 'sec:halos:results' . | grep -c label    # expect 1
grep -rnE '\{sec:(results|data|conclusions)\}' .   # expect no matches
echo "exit=$?"
```
Expected: the first command prints `1`; the second prints nothing with `exit=1`.

- [ ] **Step 5: Verify figure paths were rewritten**

Run:
```bash
cd /Users/aure/Documents/Github/phd-thesis/chapter_05/sections/paper_dm_halos/sections
grep -rnoE '\\includegraphics(\[[^]]*\])?\{img/' . ; echo "exit=$?"     # expect none
grep -rcE 'sections/paper_dm_halos/img/' . | awk -F: '{s+=$2} END{print s" rewritten paths"}'
```
Expected: first command no matches (`exit=1`); second prints a positive count.

- [ ] **Step 6: Verify body files use only `\subsection` (no `\section`) and appendices keep `\section`**

Run:
```bash
cd /Users/aure/Documents/Github/phd-thesis/chapter_05/sections/paper_dm_halos/sections
echo "body \\section (expect 0):"; grep -cE '^\\section\{' introduction.tex statistical_analysis.tex dm_subhalos_model.tex mixture_model_and_limits.tex conclusions.tex
echo "appendix \\section (expect 1 each):"; grep -cE '^\\section\{' appendix_simulation.tex appendix_em_algorithm.tex appendix_consistency_checks.tex
```
Expected: all body files `0`; each appendix file `1`.

- [ ] **Step 7: Verify per-paper back-matter was excised (no acknowledgments/bibliography/appendix)**

Run:
```bash
cd /Users/aure/Documents/Github/phd-thesis/chapter_05/sections/paper_dm_halos/sections
grep -rnE '\\(acknowledgments|bibliography|appendix)\b|DM_halos\}' . ; echo "exit=$?"
```
Expected: no matches, `exit=1`. (The acknowledgments cite keys `jax`/`scipy`/etc. are dropped with the block, so they need no remap.)

- [ ] **Step 8: Commit the ported sections**

```bash
cd /Users/aure/Documents/Github/phd-thesis
git add chapter_05/sections/paper_dm_halos/sections
git commit -m "feat: port revised Paper4 content into Ch5 section files"
```

---

## Task 5: Copy the two changed figures

**Files:**
- Modify: `chapter_05/sections/paper_dm_halos/img/bounds/sigmav_bounds_flux_bb_left.pdf`, `..._right.pdf`

- [ ] **Step 1: Copy the two updated PDFs (ignore the `.old` backups)**

Run:
```bash
cd /Users/aure/Documents/Github/phd-thesis/chapter_05/sections
cp paper_dm_halos_new/img/bounds/sigmav_bounds_flux_bb_left.pdf  paper_dm_halos/img/bounds/sigmav_bounds_flux_bb_left.pdf
cp paper_dm_halos_new/img/bounds/sigmav_bounds_flux_bb_right.pdf paper_dm_halos/img/bounds/sigmav_bounds_flux_bb_right.pdf
```

- [ ] **Step 2: Verify they now match the new source and nothing else differs**

Run:
```bash
cd /Users/aure/Documents/Github/phd-thesis/chapter_05/sections
diff -rq paper_dm_halos/img paper_dm_halos_new/img | grep -v '\.old' ; echo "exit=$?"
```
Expected: only `Only in paper_dm_halos_new/img/bounds: *.pdf.old` lines (the backups). No `differ` lines for any real figure.

- [ ] **Step 3: Commit**

```bash
cd /Users/aure/Documents/Github/phd-thesis
git add chapter_05/sections/paper_dm_halos/img/bounds
git commit -m "feat: update bb cross-section bound figures (Ch5)"
```

---

## Task 6: Confirm `paper_4.tex` and bibliography need no change

**Files:** none (verification only)

- [ ] **Step 1: Confirm the abstract paragraph in `paper_4.tex` still matches the revised abstract**

Run:
```bash
cd /Users/aure/Documents/Github/phd-thesis/chapter_05/sections
python - <<'PY'
import re,pathlib
new=pathlib.Path("paper_dm_halos_new/main.tex").read_text()
ab=re.search(r"\\abstract\{(.*?)\n\}\s*\n\\begin\{document\}", new, re.S).group(1)
old=pathlib.Path("paper_dm_halos/paper_4.tex").read_text()
para=old.split("introductory paragraph\n",1)[1].split("\\input{",1)[0]
norm=lambda s:" ".join(s.split())
print("ABSTRACT MATCHES" if norm(ab)==norm(para) else "DIFFERS -- update paper_4.tex intro paragraph")
PY
```
Expected: `ABSTRACT MATCHES`. If it prints `DIFFERS`, replace the intro paragraph in `paper_4.tex` with the revised `\abstract{}` text (strip the `\abstract{`/closing `}`), then commit.

- [ ] **Step 2: Confirm every cite key used in the ported sections resolves in `bibliography.bib`**

Run:
```bash
cd /Users/aure/Documents/Github/phd-thesis
python - <<'PY'
import re,pathlib
keys=set()
for f in pathlib.Path("chapter_05/sections/paper_dm_halos/sections").glob("*.tex"):
    for m in re.finditer(r"\\cite[a-z]*\{([^}]*)\}", f.read_text()):
        keys|={k.strip() for k in m.group(1).split(",") if k.strip()}
bib=pathlib.Path("bibliography.bib").read_text()
defined={m.group(1).strip() for m in re.finditer(r"@\w+\s*\{\s*([^,]+),", bib)}
missing=sorted(k for k in keys if k not in defined)
print("MISSING:",missing if missing else "none")
PY
```
Expected: `MISSING: none`. If anything is listed, it is a remap that was missed — add it to `CITE_REMAP`, re-run Tasks 4–6.

---

## Task 7: Full build verification

**Files:** none (build only)

- [ ] **Step 1: Clean build of the whole thesis**

Run:
```bash
cd /Users/aure/Documents/Github/phd-thesis
latexmk -C >/dev/null 2>&1
latexmk -pdf -interaction=nonstopmode main.tex >/tmp/build_port.log 2>&1; echo "exit=$?"
```
Expected: `exit=0`. If non-zero, run `grep -nE 'Error|Undefined|Runaway' /tmp/build_port.log | head -30` and fix (most likely a stray brace from an unbalanced `\new`/`\old` — inspect the cited line in the ported file).

- [ ] **Step 2: Confirm no NEW undefined references vs the baseline (Task 1 Step 3)**

Run:
```bash
cd /Users/aure/Documents/Github/phd-thesis
grep -c 'LaTeX Warning: Reference' main.log || echo 0
```
Expected: ≤ the baseline N recorded in Task 1. Investigate any increase (look for `\ref{sec:results}`-style leftovers or a broken figure label).

- [ ] **Step 3: Confirm the Ch.6 cross-reference into this chapter still resolves**

Run:
```bash
cd /Users/aure/Documents/Github/phd-thesis
grep -n 'sec:halos:results' main.log ; echo "---"
grep -c 'reference.*sec:halos:results.*undefined' main.log || echo 0
```
Expected: the second command prints `0` (the label is defined; Ch.6's `\ref` resolves).

- [ ] **Step 4: Spot-check the rendered chapter visually**

Open `main.pdf` to the Chapter 5 (DM subhalos) pages and confirm: the mixture-model/limits section reads coherently (it was the major rewrite), the two bound figures render, tables `Nsub_values` / `Nsub_values_Msub` look right, and the 5 `\aure{}`/`(Dima)` WIP notes appear in orange (expected — to be resolved before final submission).

- [ ] **Step 5: Commit the verified state**

```bash
cd /Users/aure/Documents/Github/phd-thesis
git add -A
git commit -m "test: verify Ch5 Paper4 update builds cleanly" --allow-empty
```

---

## Task 8: Cleanup

**Files:**
- Delete: `chapter_05/sections/port_dm_halos.py`
- Decision: `chapter_05/sections/paper_dm_halos_new/` (keep or remove)

- [ ] **Step 1: Remove the transient migration script**

```bash
cd /Users/aure/Documents/Github/phd-thesis
git rm -f chapter_05/sections/port_dm_halos.py 2>/dev/null || rm -f chapter_05/sections/port_dm_halos.py
```

- [ ] **Step 2: Decide on `paper_dm_halos_new/`**

Leave `paper_dm_halos_new/` in place (untracked) until the author confirms the integration looks right, then ask whether to delete it. Do NOT auto-delete — it is the authoritative source of the revision under referee review.

- [ ] **Step 3: Final commit**

```bash
cd /Users/aure/Documents/Github/phd-thesis
git add -A
git commit -m "chore: remove transient Ch5 migration script"
```

---

## Self-review notes

- **Spec coverage:** strategy (Tasks 3–4), dialect/macros (Task 3 transform; macros pre-verified), labels incl. `sec:halos:results` (Task 4 Step 4, Task 7 Step 3), bibliography remap-only (Task 3 table, Task 6 Step 2), figures (Task 5), abstract (Task 6 Step 1), verification/build (Task 7). All spec sections map to tasks.
- **One added requirement beyond the spec:** tracked-change resolution (`\new`/`\old`) and review-comment handling — discovered after the spec was written; the user explicitly requested `\old` deletion + `\new` unwrap. Handled in Task 3 with a unit-tested balanced-brace resolver (Task 2).
- **Heading-level convention:** body flattened to all-`\subsection` to match the existing chapter; this is deliberate (the user asked to follow the current paper's structure), verified in Task 4 Step 6.
- **No new bib entries, no edits to `bibliography.bib` or `paper_4.tex`** (confirmed identical/remap-only).
