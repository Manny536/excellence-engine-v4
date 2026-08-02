# Dependency tower — typed bound graph

- **Claim ID:** `ANT-DEP-001`
- **Status:** local edges `KNOWN` / `THEOREM-BACKGROUND`; full `K→R` frame `PROPOSED`
- **Output class:** estimates and bounds
- **Exact-location bridge:** `OPEN`

## Typed graph

Let `T_bound = (V,E,τ)` be a directed graph whose vertices are method or result classes and
whose edge-type map `τ` records what an arrow means.

```text
G₀  incidence combinatorics
  ≼_m G₁  Kakeya / Besicovitch tube geometry
    ≼_m G₂  Fourier restriction / ℓ²-decoupling
      ≼_m G₃  exponential sums / Dirichlet-polynomial large values
        ≼_m G₄  zeta growth and zero-density N(σ,T)
          ≼_m G₅  zero-free regions and related bounds
```

The symbol `≼_m` means **documented method dependence**. Each edge must be read locally. The
display is not a theorem asserting that every result in `G_{i+1}` follows from every result
in `G_i`, and it does not make the composed path a sufficient proof of RH.

## Vertex contracts

| Vertex | Input type | Output type | Exact information retained? |
|---|---|---|---|
| `G₀` | point, line, tube, direction, incidence data | multiplicity and incidence estimates | geometric placement only |
| `G₁` | tube families and scale parameters | union, overlap, maximal, or dimension bounds | no zeta-zero object |
| `G₂` | wave packets, caps, oscillatory integrals | restriction/decoupling norm estimates | norm-level information |
| `G₃` | coefficient sequences and frequency structure | large-value or mean-value estimates | aggregate arithmetic control |
| `G₄` | Dirichlet-polynomial/zeta estimates | `ζ` growth and `N(σ,T)` upper bounds | density, not the complete zero multiset |
| `G₅` | growth and density inputs | zero-free regions or exceptional-set bounds | regional exclusion, not all-zero placement |

## Edge ledger

| Edge | Witness class | Registered use | Status |
|---|---|---|---|
| `G₀ → G₁` | Kakeya incidence and grain/tube geometry | geometric control of overlap and direction | `THEOREM-BACKGROUND` |
| `G₁ → G₂` | Kakeya–restriction interfaces; two-ends Furstenberg geometry | geometric input to restriction arguments | `KNOWN` / `THEOREM-BACKGROUND` |
| `G₂ → G₃` | decoupling and mean-value machinery | analytic control of exponential sums | `KNOWN` at named results |
| `G₃ → G₄` | large-value estimates for Dirichlet polynomials | zeta-growth and zero-density bounds | `KNOWN` at named results |
| `G₄ → G₅` | density/growth arguments | scoped zero-free information | `KNOWN` at named results |

Wang–Wu [P1] witnesses a current `G₁/G₂` interface: restriction in `ℝ³` for `p>22/7`
through refined decoupling and two-ends Furstenberg inequalities. Wang–Zahl [P3] and
Guth–Wang–Zahl [P6] ground the full-dimension Kakeya theorem in `ℝ³`. Guth–Maynard
([arXiv:2405.20552](https://arxiv.org/abs/2405.20552)) witnesses a current `G₃/G₄`
large-values and zero-density advance.

These sources license the named edges within their scopes. They do not establish the entire
display as one implication.

## Bound projection and exactness deficit

Let `𝔄_ζ` be a declared class of analytic states containing both the completed-function data
and its zero multiset. Define

```text
π_bound : 𝔄_ζ → 𝔈_B
```

to retain the collection `B` of growth, density, and zero-free bounds produced by a chosen
method. Let `Z(a)` denote the zero multiset of state `a`, and define the compatibility fibre

```text
Fib(B) := {a ∈ 𝔄_ζ : π_bound(a)=B}.
```

An estimate package is exact-location complete only if its admissible fibre determines the
critical-line property:

```text
∀a₁,a₂ ∈ Fib(B),
[Z(a₁) ⊂ ℝ ⇔ Z(a₂) ⊂ ℝ].
```

Current dependency-tower outputs are registered as bounds; no proof in this surface shows
that their fibres have this exactness property. The stronger meta-claim that no possible
bound-type method can ever imply RH is itself `OPEN` and is not promoted here.

## Lindelöf ceiling

The standard implication direction is

```text
RH ⇒ Lindelöf Hypothesis ⇒ Density Hypothesis.
```

Reverse implications remain `OPEN`. Consequently, saturation of a restriction, Lindelöf,
or density exponent cannot be substituted for exact zero location without an additional
faithfulness theorem.

## Interface to the exact route

The missing typed edge is

```text
G₅  - - - owed - - ->  ExactCarrier(B)  ->  Z_Ξ ⊂ ℝ.
```

An admissible edge must specify how bound/placement data becomes a prime-carrying,
archimedean, multiplicity-preserving trace or determinant identity. The obligations are in
[`exact-zero-location-burden.md`](exact-zero-location-burden.md).

## Status conclusion

```text
documented local method relevance      KNOWN / THEOREM-BACKGROUND
whole tower as necessary for R_exact   PROPOSED
tower as sufficient for RH             not licensed
exact-location completion              OPEN
```

- Reference keys and boundaries: [`references/README.md`](../references/README.md)
- Controlling relation types: [`antecedent/README.md`](README.md)
