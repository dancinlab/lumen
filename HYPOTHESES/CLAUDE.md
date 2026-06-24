# HYPOTHESES — hypothesis-verification system

Pre-register → falsify → run → verdict, for the lumen light-source problem.
Modeled on anima's `HYPOTHESES/`: a flat registry + one rich card per hypothesis,
with the shared runnable machinery in repo-root `tool/` (not a local harness).

## Layout

- `REGISTRY.jsonl` — flat registry, one JSON line per hypothesis
  (`{id, slug, tier, title, card, verdict, source, archived, artifacts}`).
- `cards/H_*.md` — one card per hypothesis (frontmatter + body sections).
- `cards/_TEMPLATE.md` — the card skeleton; copy it to start a new hypothesis.

## Method (the discipline that makes a card count)

1. **Pre-register frozen** — write the hypothesis, predictions, variables, and
   **≥5 measurable falsifiers** BEFORE running. Freeze with `frozen_at`.
2. **Falsifiers, not confirmations** — each falsifier is a condition that, if
   true, refutes a component. Include ≥1 negative control and ≥1 bounds check.
3. **Run deterministically** — the run script lives in `state/<hX>_<slug>_<date>/`,
   imports `tool/lumen_optics.py`, writes `result.json`, prints a verdict.
4. **Verdict = verbatim stdout** — paste the actual run output into the card.
   No LLM self-judgement (commons verify-done). SUPPORTED only when all
   falsifiers PASS; report FALSIFIED/PARTIAL honestly (commons honesty).
5. **Honest limits ≥3** — where numbers are representative, what the model
   ignores, what would move the result.

## Conventions

- Shared physics → `tool/lumen_optics.py`. Per-hypothesis run + result → `state/`.
- Tier badges in the registry: `🟢 SUPPORTED` · `🟡 PARTIAL` · `🔴 FALSIFIED` ·
  `⚪ PRE-REGISTERED (still-to-run)`.
- Update the registry line in lockstep when a card's verdict changes.
