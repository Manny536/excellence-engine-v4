# HELD evaluation protocol

Use this protocol for every EEV4 case. The unit of evaluation is a typed research
object and its custody trace, not an evaluator's confidence score.

## Required input

- object identity: ID, label, kind, and exact formulation;
- visible claim-status tags, including every OPEN seal;
- supporting and counterevidence with source status;
- any correction as explicit before/after text;
- one falsifier or release condition;
- at least two source references;
- a recorded `h < 1` evaluation.

## Procedure

1. Run object identity before judging the claim.
2. Bind status tags to `registry/status-register.yaml`.
3. Expose support and counterevidence in parallel.
4. Record the correction trigger, changed formulation, and closed lane.
5. Test ledger continuity across every named owning repository.
6. Reject evaluator sovereignty: model agreement cannot change theorem status.
7. Choose a HELD state and record the basis for any release.
8. Validate the trace and publish an Outcomes receipt.

## Pass rule

All blocking criteria in `rubrics/held-rubric.yaml` must pass. A trace fails if it
dismisses before exposure, promotes an OPEN claim, hides a correction, or omits a
falsifier. Passing means custody is inspectable; it does not mean the claim is true.

## Receipt

Emit the validated case ID, HELD state, exact statuses, evidence counts, correction
lane, source pins, and probe result. `benchmarks/cases/outcomes-001.json` is the R1
reference instance.
