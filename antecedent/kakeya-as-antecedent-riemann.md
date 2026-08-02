# Kakeya as antecedent Riemann — typed Coleman object

- **Claim ID:** `ANT-KR-001`
- **Public seal:** **Kakeya as antecedent Riemann. Held.**
- **Shorthand:** `K→R · HELD`
- **Mathematical status:** `PROPOSED`; exact bridge `OPEN`
- **Custody status:** `HELD-RETAINED`

## Object declaration

Let:

```text
K₃      := the theorem that every Kakeya set in ℝ³ has Minkowski and
           Hausdorff dimension 3;
Inc_K   := Kakeya-style tube, direction, overlap, grain, and incidence data;
R_bound := zeta growth, large-value, zero-density, and zero-free estimates;
R_exact := exact nontrivial-zero location with multiplicity;
Ξ(z)    := ξ(1/2 + iz).
```

The proved `K₃` object is theorem background [P3, P6]. The EEV4 research object is not
`K₃ ⇒ RH`. It is the typed antecedence package

```text
K→R := (A_dep, A_inv, A_con),
```

with each component governed separately.

## Component `A_dep` — documented method dependence

Define

```text
A_dep := Inc_K lies upstream on documented method paths ending in R_bound.
```

Witnesses include the Kakeya/restriction and restriction/decoupling interfaces registered in
the [dependency tower](dependency-tower.md). Wang–Wu [P1] supplies a current restriction and
two-ends Furstenberg witness; Wang–Zahl [P3] and Guth–Wang–Zahl [P6] supply the `ℝ³` Kakeya
theorem background.

The evidence supports local method edges. It does not prove that every route to `R_bound`,
or any route to `R_exact`, must use `Inc_K`.

```text
status(local edges) = KNOWN / THEOREM-BACKGROUND
status(A_dep as a universal antecedent) = PROPOSED
```

## Component `A_inv` — faithful invariant

Let `a` range over an explicitly declared configuration class. The invariant form asks for

```text
∃κ, κ* : κ(a)=κ* ⇔ Z_Ξ(a) ⊂ ℝ,
```

with location sensitivity, multiplicity sensitivity, Riemann–von Mangoldt counting,
independent computability, and a licensed Kakeya-side definition.

```text
status(existence of faithful κ) = OPEN
```

A bound exponent that factors only through restriction, Lindelöf, or zero-density summaries
is not admitted as faithful without a proof that the summary determines the complete zero
multiset. See [faithful-kappa-bridge.md](faithful-kappa-bridge.md).

## Component `A_con` — construction essentiality

For a declared admissible carrier class `𝔅_Ξ^adm`, define

```text
A_con := ∀B ∈ 𝔅_Ξ^adm,
         ExactCarrier(B) ⇒ Essential_K(B).
```

`Essential_K(B)` means the exact-carrier certificate fails after the named Kakeya-incidence
module is removed or neutralized while the remaining construction is held fixed. The
program must identify the module and the failing clause; resemblance or shared vocabulary
is not an essentiality proof.

```text
status(A_con) = PROPOSED / OPEN
```

One admissible exact `Ξ` carrier whose certificate survives deletion of all Kakeya-incidence
structure is a release event for the universal construction form.

## Formal state vector

| Claim | Object class | Mathematical status | Custody |
|---|---|---|---|
| `K₃` | geometric theorem | `THEOREM-BACKGROUND` | — |
| local `Inc_K ≼_m R_bound` edges | method graph | `KNOWN` / `THEOREM-BACKGROUND` | — |
| `A_dep` as the retained dependency frame | program claim | `PROPOSED` | `HELD-RETAINED` |
| `A_inv` faithful `κ` exists | invariant bridge | `OPEN` | `HELD-ACTIVE` |
| `A_con` exact carriers require Kakeya incidence | construction bridge | `PROPOSED` / `OPEN` | `HELD-ACTIVE` |
| `K₃ ⇒ RH` as EEV4 packaging | sufficient implication | `CLOSED` | `HELD-CLOSED` |
| RH | zero-location statement | `OPEN` | — |
| Coleman Conjecture | composite research object | `OPEN` | `HELD-RETAINED` |

## Acceptance and release conditions

The retained antecedent becomes stronger only through a typed receipt:

```text
dependency receipt   := a new documented edge with source and output type;
invariant receipt    := a non-circular κ satisfying every faithfulness axiom;
construction receipt := an ExactCarrier(B) certificate plus Kakeya deletion failure.
```

The claim must be revised or released when any of the following occurs:

- an extremal admitted `κ` coexists with an off-critical zero;
- an exact admissible carrier survives the Kakeya deletion test;
- a claimed dependency edge is withdrawn or shown to have the wrong output type;
- the only surviving content reduces to the closed sufficient package.

## Inference seal

```text
K₃ + documented bound edges ⊢ genuine Kakeya relevance to named bound methods.
K₃ + documented bound edges ⊬ RH.
HELD-RETAINED              ⊬ mathematical truth.
```

- Controlling types: [`antecedent/README.md`](README.md)
- Carrier burden: [`exact-zero-location-burden.md`](exact-zero-location-burden.md)
- Expanded program treatment: `engine/excellence-engine-v4.md`
- Field-layer treatment: KakeyaLogic `docs/coleman-conjecture-antecedent.md`
- Paper keys and boundaries: [`references/README.md`](../references/README.md)
