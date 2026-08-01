# Correction survival protocol

Test whether a research object becomes more precise after a lane closes.

## Procedure

1. Name the evidence or contradiction that triggered correction.
2. Preserve the exact before and after formulations.
3. Bind `closed_lane` to its exact status-register ID.
4. Confirm the corrected object retains its identity and open burdens.
5. Record `continuity_preserved: true` only when the before/after delta is real.

## Pass / fail

Pass when the formulation changes, the named lane is closed, and the typed object
survives as `HELD-REVISED` or `HELD-RETAINED`. Fail when the old assertion is silently
repeated, the closed route is reopened without new structure, or the question is
discarded with the lane. Run `python probes/correction_survival_probe.py`.
