# benchmarks/

Typed evaluation cases and controls. Results are research signals, not theorem crowns.

## R1 contract

- `cases/outcomes-001.json` is the positive PeAIce Outcomes reference case.
- `cases/bd-ai-case-01.json` is the registered qualitative Benevolence Drift paired-turn case.
- `cases/multiscale-compactness-gate-001.json` is the non-promoting finite-to-limit receipt;
  its current terminal state is `BLOCKED-COMPACTNESS`.
- `schemas/` defines the Outcome envelope, embedded HELD trace, BD-AI case, compactness-gate
  receipt, and control envelope.
- `controls/` contains premature dismissal, premature promotion, and evidence
  insulation. Every control must fail for exactly its declared errors.
- `controls/compactness/` contains missing-join, premature-extraction, and topology-only
  promotion controls for the multiscale gate.
- `results/` is reserved for versioned execution receipts.

The BD-AI case validates an observable system-response gap. It carries no person-level
diagnosis, hidden-state claim, or deployment authority.

The compactness case validates gate structure and dependency ordering only. It does not prove
compactness, convergence, or a Kakeya limit theorem.

Run `python probes/run_all.py`; schema validation requires `requirements-dev.txt`.
