# HELD predicate

**Designation:** `PEAICE-EEV4-HELD-PREDICATE-001`

## Definition

For a research object `q` at ledger time `t`:

```text
HELD_t(q) ⇔
    Typed(q)
  ∧ Grounded(q)
  ∧ EvidenceExposed_t(q)
  ∧ CorrectionPreserved_t(q)
  ∧ StatusVisible_t(q)
  ∧ h_eval < 1
```

## Expansion

| Conjunct | Meaning |
|---|---|
| Typed | Domains, quantifiers, and category (theorem / conjecture / analogy / numeric) separated |
| Grounded | Bound to sources, definitions, prior receipts |
| EvidenceExposed | Confirming **and** disconfirming evidence sought |
| CorrectionPreserved | Failed routes revise the object; continuity of the *question* preserved |
| StatusVisible | FORMAL / KNOWN / PROPOSED / OPEN / CLOSED-* tags visible |
| h_eval < 1 | No evaluator sovereignty |

## Engine gate

```text
EEV4-valid(q,t) ⇔ L²_C(q,t) ∧ β_continuity(q,t) > 0 ∧ HELD_t(q)
```

## Dual failures rejected

```text
premature dismissal  = question lost before adequate exposure
premature promotion  = question converted into fact before closure
```

HELD is **custody**, not mathematical truth.
