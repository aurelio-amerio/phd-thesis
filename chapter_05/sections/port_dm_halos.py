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
