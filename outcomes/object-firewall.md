# Object firewall — identity before inference

- **Claim ID:** `OUT-OBJECT-001`
- **Status:** `FORMAL` as a typing discipline
- **Purpose:** prevent true statements from migrating across non-equivalent objects

## Object signature

Represent a research object as:

```text
ObjectSignature(X) := (
  domain,
  elements,
  quantifiers,
  invariants,
  equivalence_relation,
  target_claim,
  status
).
```

Two labels are interchangeable only after a proved equivalence of the relevant signatures:

```text
X ≡ Y requires a scope-specific equivalence certificate.
Shared vocabulary(X,Y) does not imply X ≡ Y.
```

## Registered object ledger

| ID | Object | Defining signature | Status |
|---|---|---|---|
| `OBJ-KSTD` | standard Kakeya set | compact/bounded set containing a unit segment in each direction; base point may vary | `KNOWN` |
| `OBJ-KCTR` | common-center full-line completion | every complete line through one fixed center | `FORMAL` |
| `OBJ-K3` | Kakeya dimension theorem in `ℝ³` | standard Kakeya sets have full Minkowski and Hausdorff dimension three | `THEOREM-BACKGROUND` |
| `OBJ-KR` | Kakeya as antecedent Riemann | `A_dep`, `A_inv`, `A_con` typed research package | `PROPOSED` |
| `OBJ-RH` | Riemann Hypothesis | exact nontrivial-zero placement on the critical line | `OPEN` |
| `OBJ-BD` | Benevolence Drift in AI evaluation | threshold/response mismatch on an observable interaction trace | cases `REGISTERED-QUALITATIVE`; benchmark `OWED` |

## Separation lemmas

### `OFW-1` — centered completion

For fixed `x₀ ∈ ℝⁿ`, the union of every complete line through `x₀` equals `ℝⁿ`:

```text
⋃_{v∈S^{n−1}} {x₀+tv : t∈ℝ} = ℝⁿ.
```

This is a formal statement about `OBJ-KCTR`. It does not change the standard Kakeya object
or its measure question.

### `OFW-2` — full dimension versus measure

Full Minkowski/Hausdorff dimension in `ℝ³` is theorem background. Full dimension is not the
same predicate as infinite measure, and neither predicate supplies an exact zeta-zero
mechanism.

### `OFW-3` — antecedence versus implication

```text
K→R = typed antecedence program
K⇒RH = sufficient implication
K→R ≠ K⇒RH
```

The sufficient package is closed as an EEV4 formulation; `A_inv`, `A_con`, RH, and Coleman
remain open under their own scopes.

### `OFW-4` — alignment versus theorem objects

BD-AI uses a threshold symbol and trajectory language in an alignment evaluation. It does
not inherit theorem weight from Kakeya, zeta, or operator terminology.

```text
BD-AI  ≠ NB/BD
τ_call ≠ Kakeya-lane τ
trajectory analogy ⊬ mathematical implication
```

## Firewall procedure

Before accepting an inference `X ⊢ Y`:

1. compute `ObjectSignature(X)` and `ObjectSignature(Y)`;
2. name the transport map;
3. state preserved and lost invariants;
4. lower claim weight when the map is analogical;
5. require a separate proof or evaluation receipt in the target domain.

## Failure receipt

```text
FirewallFailure := (
  source_object,
  target_object,
  silent_substitution,
  invalidated_inference,
  corrected_objects,
  propagated_status_changes
).
```

## Current non-equivalences

```text
centered full-line completion ≠ standard Kakeya set
full Kakeya dimension         ≠ infinite volume
Kakeya theorem                ≠ RH theorem
HELD custody                  ≠ mathematical truth
BD-AI qualitative case       ≠ population prevalence
surface benevolence           ≠ preserved human possibility
```

- Antecedent types: [`../antecedent/README.md`](../antecedent/README.md)
- Formative case: [`cases/kakeya-object-correction.md`](cases/kakeya-object-correction.md)
- BD-AI types: [`benevolence-drift.md`](benevolence-drift.md)
