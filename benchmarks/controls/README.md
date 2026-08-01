# Controls

- `premature-dismissal-001.json`: release before evidence, correction, or basis;
- `premature-promotion-001.json`: OPEN claims silently promoted;
- `evidence-insulation-001.json`: support retained while counterevidence is removed.

Controls are expected to be invalid HELD traces. Their envelopes declare the exact
validator errors they must produce; extra or missing errors fail the control suite.
