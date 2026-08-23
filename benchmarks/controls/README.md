# Controls

- `premature-dismissal-001.json`: release before evidence, correction, or basis;
- `premature-promotion-001.json`: OPEN claims silently promoted;
- `evidence-insulation-001.json`: support retained while counterevidence is removed.

Controls are expected to be invalid HELD traces. Their envelopes declare the exact
validator errors they must produce; extra or missing errors fail the control suite.

## Multiscale compactness controls

The `compactness/` subdirectory carries a separate finite-to-limit control family:

- `missing-common-refinement.json`: `G1` cannot pass without a join certificate;
- `premature-subnet-extraction.json`: `G3` cannot pass while `G2` is owed;
- `topology-only-kakeya-promotion.json`: `PASS-LIMIT` cannot be asserted from topology alone.

These controls validate the EEV4 gate implementation, not the mathematical compactness claim.
