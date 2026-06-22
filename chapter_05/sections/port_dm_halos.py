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


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        _selftest()
        sys.exit(0)
    main()
