# Correction and exit — explicit transition protocol

- **Protocol ID:** `OUT-CORRECT-001`
- **Status:** `FORMAL`
- **Applies to:** claim corrections, BD-AI response repair, domain transfer, and release

## Correction record

```text
CorrectionRecord := (
  id,
  target,
  trigger,
  before,
  after,
  preserved_components,
  closed_or_released_scope,
  research_status_delta,
  custody_transition,
  source_refs,
  next_burden
).
```

A correction is valid only when:

```text
before ≠ after
∧ trigger is source-visible
∧ affected scope is explicit
∧ preserved work is named
∧ status and custody changes are separate.
```

## Mathematical correction rail

The formative EEV4 correction is:

```text
RECEIVE  Kakeya/Riemann research object
TYPE     distinguish standard Kakeya, centered completion, and Coleman forms
EXPOSE   theorem background, bound ceiling, and missing exact bridge
CORRECT  close sufficient K⇒RH packaging
RETAIN   typed K→R antecedence frame
BURDEN   faithful κ + ExactCarrier + Kakeya deletion test
```

The correction closes one formulation without erasing the inquiry.

## Benevolence Drift correction rail

For a threshold-crossed interaction:

```text
Recognize → Name → Avoid amplification → Answer or disengage → Offer depth by consent
```

The corresponding record is:

```text
BDCorrection := (
  threshold_evidence,
  initial_response,
  missing_application,
  corrected_classification,
  minimum_mechanism,
  amplification_check,
  proportional_action,
  consent_gate
).
```

Correction succeeds when the response becomes direct and proportionate without retaliation,
flattery, collapse, unnecessary repetition of harmful material, or coercive escalation.

## Domain-exit receipt

Leaving one domain for another requires:

```text
DomainExit := (
  source_domain,
  target_domain,
  correspondence,
  preserved_structure,
  lost_structure,
  target_status,
  reduced_proof_weight,
  target_falsifier
).
```

Example:

```text
Kakeya grain/overlap geometry
  → structural inspiration for trajectory or alignment tests
  → analogy / test-design status only
  → no mathematical proof weight transferred.
```

## Release

Release is distinct from rejection of all associated work:

```text
Release(q) :=
  custody_state(q)=HELD-RELEASED
  ∧ release_basis(q) visible
  ∧ surviving_results(q) preserved
  ∧ downstream_statuses(q) reconciled.
```

An exact non-Kakeya carrier, for example, would release or narrow a universal Kakeya
essentiality claim while preserving the carrier's mathematical success.

## Closure

Closure is scoped:

```text
Close(candidate, obstruction) ⊬ Close(parent problem).
```

The old receipt remains immutable. A materially changed candidate receives a new ID and
enters `HELD-ACTIVE`.

## Correction monotonicity

```text
visible correction + preserved receipt → β_continuity > 0
silent rewrite                         → β_continuity failure
closed scope + no typed novelty        → remains closed
closed scope + typed novelty           → new candidate, old receipt preserved
```

## Publication propagation

A status-affecting correction must update:

1. human-readable Markdown;
2. machine-readable case records;
3. status register;
4. schemas and validators when the type changed;
5. regression tests and probes;
6. source/publisher surfaces named by the authority graph.

- Custody rules: [`conjecture-custody.md`](conjecture-custody.md)
- Authority graph: [`downstream-position.md`](downstream-position.md)
- Reference case: [`cases/outcomes-001.md`](cases/outcomes-001.md)
