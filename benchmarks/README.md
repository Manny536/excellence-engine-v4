# benchmarks/

Typed evaluation cases and controls. Results are research signals, not theorem crowns.

## R1 contract

- `cases/outcomes-001.json` is the positive PeAIce Outcomes reference case.
- `cases/bd-ai-case-01.json` is the registered qualitative Benevolence Drift paired-turn case.
- `schemas/` defines the Outcome envelope, embedded HELD trace, BD-AI case, and control envelope.
- `controls/` contains premature dismissal, premature promotion, and evidence
  insulation. Every control must fail for exactly its declared errors.
- `results/` is reserved for versioned execution receipts.

The BD-AI case validates an observable system-response gap. It carries no person-level
diagnosis, hidden-state claim, or deployment authority.

Run `python probes/run_all.py`; schema validation requires `requirements-dev.txt`.
