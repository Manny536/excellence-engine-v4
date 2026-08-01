# benchmarks/

Typed evaluation cases and controls. Results are research signals, not theorem crowns.

## R1 contract

- `cases/outcomes-001.json` is the positive PeAIce Outcomes reference case.
- `schemas/` defines the Outcome envelope, embedded HELD trace, and control envelope.
- `controls/` contains premature dismissal, premature promotion, and evidence
  insulation. Every control must fail for exactly its declared errors.
- `results/` is reserved for versioned execution receipts.

Run `python probes/run_all.py`; schema validation requires `requirements-dev.txt`.
