#!/usr/bin/env python3
"""qa.py — single source of truth for the lumen verification lab.

Closes the canonical-ssot + regression gaps (gap top-3 #3): counts and determinism are
COMPUTED here, never hand-copied. CI/contributors run `python3 tool/qa.py`.

Checks:
  1. COUNT     — tally tiers from HYPOTHESES/REGISTRY.jsonl (🟢 verified / 🔴 falsified / 🜂 abstract).
  2. DETERMINISM — each registry row with a state result.json: run its run_*.py TWICE, assert
                   byte-identical stdout (deterministic, $0 local).
  3. VERDICT-MATCH — assert the run's printed verdict matches the row's tier glyph
                     (🟢→SUPPORTED, 🔴→FALSIFIED).

Exit 0 iff every check passes; exit 1 with a diff otherwise. Stdlib-only.
"""
from __future__ import annotations
import glob, hashlib, json, os, re, subprocess, sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_REGISTRY = os.path.join(_ROOT, "HYPOTHESES", "REGISTRY.jsonl")


def _glyph(tier: str) -> str:
    for g in ("🟢", "🔴", "🜂", "⚪"):
        if tier.startswith(g):
            return g
    return "?"


def main() -> int:
    rows = [json.loads(l) for l in open(_REGISTRY) if l.strip()]
    counts = {"🟢": 0, "🔴": 0, "🜂": 0, "⚪": 0, "?": 0}
    for r in rows:
        counts[_glyph(r.get("tier", ""))] += 1

    fails = []
    n_run = 0
    for r in rows:
        arts = [a for a in r.get("artifacts", []) if a.endswith("result.json")]
        if not arts:
            continue  # abstract conjecture — no run to check
        run_dir = os.path.join(_ROOT, os.path.dirname(arts[0]))
        scripts = glob.glob(os.path.join(run_dir, "run_*.py"))
        if not scripts:
            fails.append(f"{r['id']}: no run_*.py in {run_dir}")
            continue
        script = scripts[0]
        outs = []
        for _ in range(2):
            p = subprocess.run([sys.executable, script], capture_output=True, text=True)
            outs.append(p.stdout)
        n_run += 1
        if hashlib.sha256(outs[0].encode()).hexdigest() != hashlib.sha256(outs[1].encode()).hexdigest():
            fails.append(f"{r['id']}: NON-DETERMINISTIC (two runs differ)")
            continue
        m = re.search(r"VERDICT:\s*(SUPPORTED|FALSIFIED)", outs[0])
        if not m:
            fails.append(f"{r['id']}: no VERDICT line in output")
            continue
        verdict = m.group(1)
        glyph = _glyph(r.get("tier", ""))
        expected = {"🟢": "SUPPORTED", "🔴": "FALSIFIED"}.get(glyph)
        if expected and verdict != expected:
            fails.append(f"{r['id']}: tier {glyph} expects {expected} but run says {verdict}")

    total = len(rows)
    print("lumen qa.py — single source of truth")
    print(f"  registry rows : {total}")
    print(f"  verified 🟢   : {counts['🟢']}")
    print(f"  falsified 🔴  : {counts['🔴']}")
    print(f"  abstract 🜂   : {counts['🜂']}")
    if counts["⚪"] or counts["?"]:
        print(f"  other         : ⚪{counts['⚪']} ?{counts['?']}")
    print(f"  runs checked  : {n_run} (determinism + verdict-match)")
    if fails:
        print(f"FAIL ({len(fails)}):")
        for f in fails:
            print(f"  - {f}")
        return 1
    print(f"PASS — {counts['🟢']} verified · {counts['🔴']} falsified · {counts['🜂']} abstract · {n_run}/{n_run} deterministic+matched")
    # machine-readable line for docs to grep instead of hand-copying
    print(f"COUNTS {json.dumps({'verified': counts['🟢'], 'falsified': counts['🔴'], 'abstract': counts['🜂'], 'rows': total})}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
