# Faithful κ bridge — exact-location invariant specification

- **Claim ID:** `ANT-KAPPA-001`
- **Status:** existence `OPEN` · candidate class `PROPOSED`
- **Purpose:** define the minimum invariant surplus required beyond bound exponents

## Configuration space

Let an admissible configuration be

```text
a := (G_a, B_a, Z_a, M_a, P_a, A_a),
```

where:

- `G_a ∈ 𝔊_K` is the declared geometric/incidence object;
- `B_a ∈ 𝔅_Ξ` is a candidate carrier constructed without a zero oracle;
- `Z_a ∈ 𝔃` is the zero multiset produced by the carrier identity;
- `M_a` records multiplicities;
- `P_a` is the prime-power trace data;
- `A_a` is the archimedean/Gamma contribution.

Define the truncated and total off-line defects

```text
Off_T(a) := Σ_{z ∈ Z_a, |Re(z)|≤T, Im(z)≠0} mult_a(z),
Off(a)   := sup_{T>0} Off_T(a) ∈ ℕ₀ ∪ {∞}
```

under the `Ξ(z)=ξ(1/2+iz)` coordinate. Thus `Off(a)=0` is the exact critical-line
condition for the represented multiset.

## Primary invariant burden

A candidate invariant is a map

```text
κ : 𝔄_adm → 𝒴
```

with a distinguished value `κ* ∈ 𝒴`. The Coleman invariant form asks for

```text
κ(a)=κ* ⇔ Off(a)=0.
```

This equivalence is the target, not an available theorem. A faithful `κ` must satisfy every
axiom below before the reverse direction can enter proof status.

## Faithfulness axioms

### `Fκ-1` — location separation

For admissible configurations with identical aggregate bounds but different critical-line
truth values, faithfulness requires

```text
Off(a₁)=0 ∧ Off(a₂)>0
  ⇒ κ(a₁)=κ* ∧ κ(a₂)≠κ*.
```

### `Fκ-2` — multiplicity sensitivity

If `Z_{a₁}` and `Z_{a₂}` have the same support but different multiplicity functions in a
way relevant to the target identity, `κ` must retain or explicitly account for that
difference. A set-valued invariant that discards multiplicity is insufficient for a
determinant identity.

### `Fκ-3` — counting compatibility

The carrier coupled to `κ` must reproduce

```text
N_ζ(T) = (T/2π) log(T/2π) − T/2π + O(log T),
```

where `N_ζ(T)` counts nontrivial zeros `ρ` with `0<Im(ρ)≤T`, with multiplicity. An
invariant attached to a power-law or `Λ^{1/4}` counting class cannot be declared
faithful without a proved transformation to the `T log T` class.

### `Fκ-4` — arithmetic and archimedean compatibility

`κ` must be compatible with both sides of the explicit-formula architecture:

```text
prime-power data : log(p^k), Λ(p^k)p^{-k/2}
smooth data      : the Gamma-factor / archimedean term.
```

Purely geometric scale data or purely spectral-shift vocabulary does not satisfy this
axiom by itself.

### `Fκ-5` — non-circular computability

There must be an algorithmic or analytic definition

```text
κ(a) = Compute(G_a, B_a, declared source data)
```

that does not insert `Z_Ξ`, the truth value of RH, or a list of zero ordinates as hidden
input. Defining `κ(a):=κ*` exactly when RH holds is extensionally correct and scientifically
empty; it fails this axiom.

### `Fκ-6` — geometric contact

The Kakeya side must enter through a named map or essential module:

```text
G_a --T_K--> B_a --T_Ξ--> Z_a.
```

The map `T_K` must expose which incidence quantity is transported and support a deletion
test. Shared words such as direction, spectrum, overlap, or determinant do not establish
geometric contact.

## Bound-factorization rejection test

Let `π_bound(a)` retain only restriction, Lindelöf, or zero-density summary data. If

```text
κ = κ_bound ∘ π_bound,
```

then `κ` is faithful only if one also proves that the bound summary is exact-location
complete:

```text
π_bound(a₁)=π_bound(a₂)
  ⇒ [Off(a₁)=0 ⇔ Off(a₂)=0].
```

No such completeness theorem is registered. Therefore a naive Kakeya/restriction/density
exponent remains below the admission threshold. This is the **faithfulness obstruction**:
the bridge must carry more information than the bound-producing dependency tower currently
retains.

## Candidate record

Every proposed `κ` must publish

```text
KappaCandidate := (
  domain,
  codomain,
  normalization κ*,
  independent computation rule,
  location theorem owed,
  multiplicity rule,
  counting rule,
  prime/archimedean interface,
  Kakeya transport map,
  deletion test,
  falsifier
).
```

A scalar formula without this record is an untyped placeholder.

## Falsification and release

The candidate `κ` is falsified if an admissible configuration satisfies

```text
κ(a)=κ* ∧ Off(a)>0.
```

The Kakeya-specific invariant program is released or revised if an exact, non-circular
invariant meeting `Fκ-1` through `Fκ-5` has no essential Kakeya transport map and survives
the deletion test.

## Current state

```text
faithfulness axioms specified         FORMAL (EEV4 admission contract)
existence of an admitted κ            OPEN
κ(a)=κ* ⇒ Off(a)=0                    OPEN / RH-hard
bound exponent as faithful κ          not admitted
Kakeya essentiality of a faithful κ   PROPOSED / OPEN
```

- Carrier clauses: [`exact-zero-location-burden.md`](exact-zero-location-burden.md)
- Dependency ceiling: [`dependency-tower.md`](dependency-tower.md)
- Controlling claim types: [`antecedent/README.md`](README.md)
