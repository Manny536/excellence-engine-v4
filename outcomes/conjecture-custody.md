# Conjecture custody — revisable claim protocol

- **Claim ID:** `OUT-CUSTODY-001`
- **Status:** `FORMAL` as a custody protocol
- **Reference state:** `K→R` `PROPOSED` · `HELD-RETAINED`

Conjecture custody preserves an unresolved inquiry through correction without converting
custody into theorem status.

## Custodied object

```text
CustodiedClaim := (
  id,
  wording,
  object_scope,
  quantifiers,
  research_status,
  custody_state,
  supporting_evidence,
  counterevidence,
  falsifier,
  release_condition,
  next_burden,
  source_refs
).
```

Admission requires every field to be visible. An inspiring sentence without object scope or
falsifier is an inquiry note, not a first-class custodied claim.

## Independent state axes

Research status and custody answer different questions:

```text
research_status(q) = what the evidence presently warrants
custody_state(q)    = how the engine is carrying the object
```

For the EEV4 ground frame:

```text
research_status(K→R) = PROPOSED
custody_state(K→R)    = HELD-RETAINED
status(RH)            = OPEN
status(Coleman)       = OPEN
```

`HELD-RETAINED` therefore does not mean true, proved, or accepted.

## Custody cycle

```text
RECEIVED
  → type object and sources
HELD-ACTIVE
  → expose evidence and counterevidence
HELD-REVISED
  → record explicit correction delta
HELD-RETAINED | HELD-RELEASED | HELD-CLOSED
```

| Transition | Required receipt |
|---|---|
| `RECEIVED → HELD-ACTIVE` | typed object, owner, status, and first burden |
| `HELD-ACTIVE → HELD-REVISED` | evidence trigger plus before/after formulation |
| `HELD-REVISED → HELD-RETAINED` | corrected object remains coherent and falsifiable |
| `HELD-REVISED → HELD-RELEASED` | release basis and preserved successful work |
| `HELD-REVISED → HELD-CLOSED` | scoped proof, obstruction, or completed object |

## Evidence symmetry

Custody requires:

```text
Evidence(q) := Supporting(q) ⊕ Counter(q),
Supporting(q)≠∅,
Counter(q)≠∅.
```

Symmetry means exposure of both classes, not equal evidentiary weight. A decisive
counterexample can outweigh many supportive analogies.

## Correction survival

A successful correction may change the formulation while preserving continuity:

```text
before : Kakeya(ℝ³) ⇒ RH
after  : Kakeya incidence is held in a typed antecedence program;
         faithful invariant and exact-carrier burdens remain open.
```

The sufficient package closes. The dependency, invariant, and construction questions are
retained under their own statuses. This is `β_continuity > 0`: prior work remains legible
without protecting its failed arrow.

## Failure modes

```text
CC-1  no peer review → inquiry erased
CC-2  HELD → truth promotion
CC-3  correction → old wording silently retained
CC-4  release → evidence deleted
CC-5  closure of candidate → parent conjecture declared closed
CC-6  model agreement → source authority
```

## Release discipline

Release is a valid Outcome. A release receipt states:

1. which claim or quantifier is released;
2. the evidence or alternate construction that triggered release;
3. which subordinate results remain valid;
4. which status and downstream surfaces change;
5. the new open burden, if any.

## Current application

```text
K→R antecedence frame           HELD-RETAINED · PROPOSED
sufficient Kakeya⇒RH package    HELD-CLOSED · CLOSED
faithful κ                      HELD-ACTIVE · OPEN
prime-carrying continuation     HELD-ACTIVE · LIVE / OWED
RH and Coleman                  OPEN
```

- Formal antecedent contract: [`../antecedent/README.md`](../antecedent/README.md)
- Correction receipt: [`cases/kakeya-object-correction.md`](cases/kakeya-object-correction.md)
- Machine trace: [`../benchmarks/cases/outcomes-001.json`](../benchmarks/cases/outcomes-001.json)
