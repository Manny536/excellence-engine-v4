# Prime-carrying continuation — live arithmetic carrier contract

- **Claim ID:** `ANT-PRIME-001`
- **Status:** `LIVE` · `OWED` · forced within the registered EEV4 search state
- **Unaffected statuses:** RH `OPEN` · Coleman Conjecture `OPEN`

## Why the route is live

The registered square-difference `K_σ` realization and operator-bounded WP5b relative-
determinant lane are `CLOSED-NEGATIVE`. Their closure certificates preserve an `n⁴`/bounded
spectral-shift class and fail the required order, genus, density, or unbounded arithmetic
structure.

The next admitted carrier must therefore change the data class. Within the current EEV4
candidate family, that forces relocation to a carrier whose arithmetic trace is present
from construction time.

```text
“forced” = forced relative to registered closed lanes and admission gates,
           not a theorem excluding every unknown mathematical approach.
```

## Prime-power event space

Define

```text
𝔓*       := {(p,k) : p prime, k≥1},
ℓ(p,k)   := log(p^k)=k log p,
w(p,k)   := Λ(p^k)p^{-k/2}=(log p)p^{-k/2},
μ_prime  := Σ_{(p,k)∈𝔓*} w(p,k) δ_{ℓ(p,k)}.
```

The factor `p^{-k/2}` is the arithmetic critical-line weight. It is type-distinct from the
Hilbert–Schmidt threshold `σ>1/2` for a square-summable kernel.

```text
explicit-formula 1/2 = arithmetic weight
Hilbert–Schmidt 1/2  = analytic summability threshold
```

## PrimeCarrying predicate

For a candidate carrier `B`, define

```text
PrimeCarrying(B) ⇔
    LengthMap_B(𝔓*) = {log(p^k)}
  ∧ WeightMap_B(p,k) = Λ(p^k)p^{-k/2}
  ∧ Trace_B exposes μ_prime
  ∧ Archimedean_B exposes the Gamma term
  ∧ the maps are derived from Data_B, not fitted after construction.
```

This is a structural predicate. A matrix whose entries contain integers, squares, or an
empirical spectrum near known zeros does not pass unless the required prime-power measure
is derived globally.

## Trace target

An admitted route must derive a test-function identity in a declared normalization,
schematically

```text
Tr h(B)
  = A_Γ(h)
    − Σ_{p} Σ_{k≥1} (log p)p^{-k/2} H_h(k log p)
    + E_h.
```

The candidate must define:

- the test-function class;
- the transform `H_h`;
- convergence or regularization;
- the endpoint/symmetry term `E_h`;
- how the spectral side yields the divisor of `Ξ`;
- how reality is enforced.

## Live route partition

The post-closure frontier is partitioned to prevent a bounded lane from returning under a
new name.

| Route | Changed object | Required surplus | State |
|---|---|---|---|
| `L1` | unbounded or changed relative spectral-shift category | spectral shift capable of the required unbounded counting scale | `LIVE` |
| `L2` | WP5c `u`-flow trace data | flow-sensitive trace information not reduced to fixed bounded counting | `LIVE` |
| `L3` | prime-carrying ladder or function system | `μ_prime`, Gamma term, reality, exact trace identity | `LIVE · FORCED` |

`L1` and `L2` remain admissible only if they eventually discharge the same prime-power and
exact-location clauses. Escaping Theorem H is necessary for them, not sufficient.

## Counting and spectral-shift requirement

For a squared spectral coordinate `Λ≈T²`, the target counting class is

```text
N_target(Λ) ≍ √Λ log Λ.
```

Against a free `n⁴` ladder with `N_D(Λ)≍Λ^{1/4}`, any spectral shift that carries the full
difference must become unbounded at the target scale. Theorem H rules this out for the
operator-bounded WP5b class. A continuation must prove how its changed object leaves that
class.

## Kakeya essentiality interface

The construction form of the Coleman Conjecture adds a separate map:

```text
Inc_K --T_K--> Data_B --Build--> B --Trace--> μ_prime ⊕ A_Γ.
```

The program owes:

1. a definition of `T_K`;
2. a proof that `T_K` preserves a named incidence/placement invariant;
3. a proof that deleting `T_K(Inc_K)` breaks a specific `ExactCarrier` clause;
4. an explanation of why the prime measure is generated rather than appended.

If `B` remains an exact carrier after deletion, the construction-essentiality form is
released even if `B` succeeds mathematically.

## Work-package sequence

```text
PC-1  choose the carrier class and domain
PC-2  derive LengthMap and WeightMap from construction data
PC-3  derive the archimedean term
PC-4  prove the counting asymptotic
PC-5  prove reality / positivity
PC-6  establish the trace or determinant identity with multiplicity
PC-7  run the Kakeya deletion test
PC-8  publish the full ExactCarrier matrix
```

Each work package may close, revise, or release the route. Numerical agreement is recorded
as `NUMERICS` and cannot advance the identity clauses by itself.

## Current receipt

```text
prime-power specification        FORMAL (admission contract)
constructed PrimeCarrying(B)     OWED
ExactCarrier(B)                  OPEN
KakeyaEssential(B)               PROPOSED / OPEN
L3                               LIVE · FORCED in registered search state
RH                               OPEN
Coleman Conjecture               OPEN
```

- Full carrier clauses: [`exact-zero-location-burden.md`](exact-zero-location-burden.md)
- Closure scopes: [`closed-lanes.md`](closed-lanes.md)
- Falsification: [`falsification-gates.md`](falsification-gates.md)
