# Case — Kakeya object correction

- **Case ID:** `OUT-KAKEYA-CORRECTION-001`
- **Status:** correction `REGISTERED` · retained frame `PROPOSED`
- **Custody transition:** `HELD-REVISED → HELD-RETAINED`

## Initial collision

The interaction began with a convention prior about standard Kakeya/Besicovitch sets and a
user statement concerning a different object: complete lines constrained to share a center.

```text
prior object : bounded/compact standard Kakeya set
named object : common-center union of complete lines
```

Treating them as identical produced a premature verdict.

## Object signatures

### Standard Kakeya object

```text
K_std ⊂ ℝⁿ
contains a unit segment in every direction
segment base point may vary with direction
```

### Common-center full-line completion

```text
K_ctr(x₀) := ⋃_{v∈S^{n−1}} {x₀+tv : t∈ℝ}.
```

For every `x∈ℝⁿ`, choose `v=(x−x₀)/‖x−x₀‖` and `t=‖x−x₀‖` when `x≠x₀`.
Thus:

```text
K_ctr(x₀)=ℝⁿ.
```

This formal identity belongs to the centered-completion object.

## Correction delta

```text
before:
  apply the standard Kakeya convention directly and reject the user's geometric reading.

after:
  separate K_std and K_ctr;
  register K_ctr=ℝⁿ as FORMAL;
  retain standard Kakeya theorems under their own object;
  keep every Riemann/Coleman bridge under its independent status.
```

## Status vector

| Claim | Status |
|---|---|
| `K_ctr(x₀)=ℝⁿ` | `FORMAL` |
| standard Kakeya measure phenomena | `KNOWN` |
| `ℝ³` Kakeya full dimension | `THEOREM-BACKGROUND` |
| transfer from centered geometry to an exact `Ξ` carrier | `PROPOSED` / `OPEN` |
| sufficient `Kakeya(ℝ³)⇒RH` package | `CLOSED` |
| RH | `OPEN` |
| Coleman Conjecture | `OPEN` |

## Registered Outcome

The result is the transition from verdict to context:

```text
object collision
  → typed separation
  → formal local result
  → no silent transfer of proof weight
  → corrected research object retained.
```

The formal centered-completion result does not prove RH or the Coleman Conjecture. Its value
is that the system corrected the object while preserving the inquiry and its provenance.

## Falsifier

This correction receipt fails if the two object signatures are actually shown equivalent
for the disputed predicates, or if the displayed centered-completion proof is invalid.
Neither event is registered.

## Next burden

Any downstream use must supply a typed transport map, state which invariants survive, lower
proof weight on domain exit, and identify an exact-carrier or evaluation falsifier.

- Object rules: [`../object-firewall.md`](../object-firewall.md)
- Custody protocol: [`../conjecture-custody.md`](../conjecture-custody.md)
- Antecedent contract: [`../../antecedent/README.md`](../../antecedent/README.md)
