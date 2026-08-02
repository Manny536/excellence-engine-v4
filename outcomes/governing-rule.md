# Governing rule — Protect, Expose, Build

- **Claim ID:** `OUT-RULE-001`
- **Status:** `FORMAL` as an EEV4 Outcomes contract
- **Applies to:** mathematical custody, alignment evaluation, model readings, and publication

```text
Protect the question.
Expose the answer to evidence.
Help build outcomes.
```

## Typed operators

Let `q ∈ 𝔔` be an inquiry, `a ∈ 𝔄` an attempted answer, and `o ∈ 𝔒` an Outcome.
Define:

```text
Protect(q) :=
  preserve(q.wording, q.provenance, q.object_scope, q.status, q.permission_to_test)

Expose(a) :=
  publish(a.supporting_evidence, a.counterevidence, a.uncertainty,
          a.falsifier, a.source_roles)

Build(q,a) :=
  emit(corrected_object, research_status, custody_state,
       correction_delta, next_burden, receipt)
```

The partnership predicate is:

```text
Partner(q,a) ⇔ Protect(q) ∧ Expose(a) ∧ OutcomeValid(Build(q,a)).
```

## Duty separation

| Duty | Preserves | Does not shield |
|---|---|---|
| `Protect` | inquiry, provenance, scope, and testing permission | a preferred answer from correction |
| `Expose` | evidence symmetry, uncertainty, and inspectability | endless delay after a threshold is met |
| `Build` | correction continuity and next burden | a failed formulation from release or closure |

The duties are non-substitutable:

```text
Protect(q) without Expose(a) = answer insulation
Expose(a) without Protect(q) = premature dismissal risk
Protect(q) ∧ Expose(a) without Build(o) = non-response
```

## Research permission versus acceptance

Let `w_accept(q)` be the warranted acceptance weight and `p_test(q)` the permission to
investigate. Outcomes does not identify them:

```text
w_accept(q) may be low while p_test(q)=1.
```

Lack of peer review lowers acceptance weight. It does not, by itself, revoke permission to
formalize, falsify, compare, or run safe tests.

## Threshold duty

Careful investigation is appropriate below an evidence threshold. Once the declared
threshold is met, `Expose` requires the supported conclusion to become visible:

```text
q_evidence < τ  → qualify, investigate, request missing evidence
q_evidence ≥ τ  → name the supported classification and its scope
```

The threshold never authorizes unlimited intervention. The emitted action remains bounded
by proportionality, consent, uncertainty, and `h < 1`.

## Failure classes

```text
GR-1  question erased before object resolution
GR-2  answer insulated from counterevidence
GR-3  status promoted without proof or evaluation receipt
GR-4  classification withheld after threshold
GR-5  correction performed without a visible before/after delta
GR-6  next burden omitted, leaving false completion
```

## Acceptance receipt

A governing-rule pass records:

1. the exact inquiry and object scope;
2. the attempted answer;
3. evidence for and against;
4. the threshold or decision rule used;
5. the corrected formulation and status;
6. the independent HELD transition;
7. the falsifier or release condition;
8. the next burden and source pins.

- Controlling contract: [`README.md`](README.md)
- Finding gates: [`six-findings.md`](six-findings.md)
- Correction protocol: [`correction-and-exit.md`](correction-and-exit.md)
