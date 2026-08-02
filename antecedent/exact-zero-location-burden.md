# Exact zero-location burden — carrier admission contract

- **Claim ID:** `ANT-EXACT-001`
- **Status:** specification `FORMAL`; construction and identity `OPEN`
- **Target:** an independently constructed carrier for `Ξ(z)=ξ(1/2+iz)`

## Carrier object

Let a candidate be

```text
B := (ℋ_B, Dom(B), Op_B, Reg_B, Tr_B, Det_B, Data_B),
```

where `ℋ_B` is a Hilbert or function space, `Op_B` is the operator or transfer system,
`Reg_B` is any required regularization, and `Data_B` is the geometric/arithmetic input.

The admission predicate is

```text
ExactCarrier(B) ⇔
    Domain(B)
  ∧ ZeroIdentity(B, Ξ)
  ∧ Multiplicity(B, Z_Ξ)
  ∧ PrimePower(B)
  ∧ Archimedean(B)
  ∧ Counting(B)
  ∧ Reality(B)
  ∧ FunctionalEquation(B)
  ∧ NonCircular(B).
```

Each conjunct is independently owed. Failure of one clause prevents exact-carrier
promotion even when other clauses pass.

## `EC-1` — domain and regularization

The construction must state:

```text
ℋ_B,
Dom(Op_B),
closedness / self-adjointness class,
trace ideal or distributional trace class,
regularization convention,
region of analytic continuation.
```

Changing determinant type—Fredholm, Carleman, relative, or zeta-regularized—changes the
admissible operator class and must be explicit.

## `EC-2` — zero identity

The target is a proved identity of the form

```text
D_B(z) = e^{g(z)} Ξ(z),
```

where `D_B` is the declared determinant or trace-generated entire function and `e^{g(z)}`
is proved zero-free on the target domain. The common special case `D_B(z)=C·Ξ(z)` has
constant `C≠0`.

Numerical eigenvalue agreement, fitted zeros, or parity alone does not establish this
identity.

## `EC-3` — multiplicity

The identity must preserve divisor data:

```text
ord_z D_B = ord_z Ξ
```

for every target zero. Matching only the support or a finite list of ordinates is a partial
receipt.

## `EC-4` — prime-power trace content

Let

```text
𝔓* := {(p,k) : p prime, k≥1},
ℓ(p,k) := log(p^k)=k log p,
w(p,k) := Λ(p^k)p^{-k/2}=(log p)p^{-k/2}.
```

The carrier must recover the prime contribution structurally through a trace formula or an
established equivalent. A schematic test-function form is

```text
Tr_B(h) = A_Γ(h)
          − Σ_{(p,k)∈𝔓*} w(p,k) · H_h(ℓ(p,k))
          + E_h,
```

with the transform `H_h`, endpoint term `E_h`, and normalization defined in the candidate
record. Prime weights appended after the spectrum is chosen do not satisfy structural
carriage.

## `EC-5` — archimedean term

`A_Γ(h)` must reproduce the smooth contribution arising from the completed zeta function's
Gamma factor. This clause carries information independent of the prime-power sum.

## `EC-6` — counting law

The carrier must reproduce the Riemann–von Mangoldt class

```text
N_ζ(T) = (T/2π) log(T/2π) − T/2π + O(log T),
```

where `N_ζ(T)` counts nontrivial zeros `ρ` with `0<Im(ρ)≤T`, with multiplicity. An `n⁴`
free ladder has `N(Λ)≈Λ^{1/4}`; after the relevant spectral-coordinate conversion,
bounded or relatively compact perturbations remain in the wrong Weyl class. Any proposed
escape must prove the changed counting mechanism.

## `EC-7` — reality mechanism

The route must prove the property that converts the carrier spectrum or divisor into real
`z`-coordinates. Accepted mechanism classes include:

- a self-adjoint operator with a proved zero/eigenvalue identity;
- a positivity theorem sufficient for the relevant Weil criterion;
- a Frobenius/cohomological mechanism with the required spectral bounds;
- another explicitly proved substitute.

Naming Hilbert–Pólya, self-adjointness, or positivity without constructing the relevant
object leaves this clause open.

## `EC-8` — functional-equation content

The identity must account for the completed function's `s↔1−s` symmetry. Writing the
spectral parameter as `z²` creates evenness syntactically; it does not by itself recover the
Gamma factor, prime side, or functional equation.

## `EC-9` — non-circularity

The construction data must be available independently of the zero multiset:

```text
Build(Data_B) → B → D_B → Z_Ξ.
```

The following reverse insertion is rejected:

```text
Z_Ξ → define B with spectrum Z_Ξ → recover Z_Ξ.
```

The candidate must state which inputs are permitted and show that no RH truth value or
zero-oracle is embedded in them.

## Kakeya contact burden

For the construction form of `K→R`, a further clause is required:

```text
KakeyaEssential(B) ⇔
  ExactCarrier(B)
  ∧ named Inc_K module enters Build(Data_B)
  ∧ ExactCarrier(Delete_K(B)) is false for a proved reason.
```

This is stronger than resemblance. The deletion must name which of `EC-1` through `EC-9`
fails.

## Candidate receipt

Every submitted carrier should include this matrix:

| Clause | Witness | Status | Falsifier |
|---|---|---|---|
| `EC-1` domain | theorem / construction | `OWED` | domain or trace failure |
| `EC-2` identity | analytic identity | `OWED` | coefficient or divisor mismatch |
| `EC-3` multiplicity | divisor theorem | `OWED` | multiplicity mismatch |
| `EC-4` prime powers | trace formula | `OWED` | absent/wrong length or weight |
| `EC-5` archimedean | Gamma-term derivation | `OWED` | smooth-term mismatch |
| `EC-6` counting | asymptotic theorem | `OWED` | wrong Weyl/order class |
| `EC-7` reality | self-adjointness/positivity theorem | `OWED` | nonreal admitted spectrum |
| `EC-8` symmetry | functional-equation derivation | `OWED` | cosmetic parity only |
| `EC-9` non-circularity | independent build audit | `OWED` | zero-oracle dependency |

## Source boundaries

Poltoratski [P5] grounds rank-one perturbation and Krein spectral-shift vocabulary.
ChaosBook Chapter 19 [P7] grounds trace/spectral-determinant relations and dynamical examples.
Slater [P2] remains a bounded Hilbert–Schmidt/determinant comparison. These references do
not discharge any `ExactCarrier` clause for EEV4.

- Prime continuation: [`prime-carrying-continuation.md`](prime-carrying-continuation.md)
- Closed realizations: [`closed-lanes.md`](closed-lanes.md)
- Reference keys: [`references/README.md`](../references/README.md)
