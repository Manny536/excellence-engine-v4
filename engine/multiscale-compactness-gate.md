# Multiscale configuration net and compactness gate

**Designation:** `PEAICE-EEV4-MULTISCALE-COMPACTNESS-GATE-001`
**Claim status:** `PROPOSED`
**Current terminal state:** `BLOCKED-COMPACTNESS`
**Scope:** EEV4 finite-to-limit custody. This is not a Kakeya theorem or a compiled Lean receipt.

## Purpose

This gate prevents a family of finite multiscale configurations from being promoted to a
continuous or all-scale conclusion merely because the finite cases are numerous, nested, or
numerically stable.

```text
finite configurations
  -> product-directed net
  -> compact containment
  -> cluster point / convergent subnet
  -> closed admissibility
  -> continuous or semicontinuous observable transfer
  -> scoped limit conclusion
```

Each arrow is an independently typed obligation.

## 1. Product-directed refinement

Let the scale index be

```text
D_scale := (0,1]
δ <=_scale ε  iff  ε <= δ in the usual real order.
```

Later indices are finer scales. A common later scale for `δ₁` and `δ₂` is
`min(δ₁,δ₂)`.

Fix a compact observation window `Q ⊂ R^n`, the compact unoriented direction space
`Ω := RP^(n-1)`, and the bounded tube-parameter carrier `P := Q × Ω`.

A refinement index is a pair

```text
r := (S, Π)
```

where `S` is a finite subset of `P` and `Π` is a finite measurable partition used to record
shadings. Define `(S,Π) <=_ref (S',Π')` when `S ⊆ S'` and `Π'` refines `Π`. The declared
common refinement is

```text
(S₁ ∪ S₂, Π₁ ∨ Π₂),
```

where `Π₁ ∨ Π₂` contains the nonempty intersections of cells. A richer refinement model must
supply its own checkable join certificate; the word “refinement” alone is insufficient.

The full index is

```text
D := D_scale × D_refinement
```

with coordinatewise order. The abstract directedness claim is `KNOWN` topology. The concrete
Lean instance and join proof are `PLANNED / NOT COMPILED`.

## 2. Common configuration carrier

Variable-length tube arrays do not automatically inhabit one compact space. Embed each finite
configuration into fixed measure-valued coordinates.

At `d = (δ,S,Π)`, let:

- `μ_d` be a probability measure on `P`, retaining the joint position-direction law;
- `ν_d` be a nonnegative, uniformly mass-bounded measure on `P × Q`, retaining shaded
  incidence;
- `pos_d` and `dir_d` be the position and direction marginals of `μ_d`.

The configuration packet is

```text
K(d) := (pos_d, dir_d, (μ_d, ν_d))
      ∈ X_position × X_direction × X_shading,

X_position  := Prob(Q)
X_direction := Prob(Ω)
X_shading   := Prob(P) × Measure_<=M(P × Q).
```

The `P` coordinate in the shading packet prevents the product presentation from erasing the
position-direction-incidence coupling. The model must also specify the consistency relation
between `μ_d` and the `P`-marginal of `ν_d`.

At scale `δ`, require

```text
supp(ν_d) ⊆ I_δ,
I_δ := {(p,x) : x lies in the δ-tube represented by p}.
```

The exact normalization, mass bound, tightness condition, measurable structure, and
quantitative shading density remain owed. Empty shading cannot support a positive union,
volume, or dimension conclusion.

## 3. Gate contract

| Gate | Required evidence | Failure boundary |
|---|---|---|
| `G0 CARRIER` | One named topological carrier contains every configuration. | Convergence is not well typed. |
| `G1 DIRECTED` | Both factors are directed and a common-refinement join is certified. | The claimed refinement net is invalid. |
| `G2 COMPACT` | The configurations lie, or eventually lie, in a proved compact subset. | No convergent subnet may be claimed. |
| `G3 EXTRACT` | Compactness yields a cluster point or convergent subnet. | No limit candidate exists. |
| `G4 CLOSED` | The intended admissibility property is closed under the selected convergence. | The limit may leave the Kakeya or coherence class. |
| `G5 TRANSFER` | Every promoted observable is continuous or semicontinuous in the needed direction. | The finite estimate cannot pass to the limit. |

Allowed terminal states:

- `PASS-LIMIT`: `G0` through `G5` pass for one named property and observable;
- `LIMIT-CANDIDATE`: `G0` through `G3` pass while closure or transfer remains open;
- `BLOCKED-COMPACTNESS`: `G2` is missing or fails;
- `BLOCKED-CLOSURE`: extraction succeeds but `G4` is missing or fails;
- `BLOCKED-TRANSFER`: admissibility survives but `G5` is missing or fails.

The current machine-readable receipt is
[`benchmarks/cases/multiscale-compactness-gate-001.json`](../benchmarks/cases/multiscale-compactness-gate-001.json).

## 4. L²_C application

In EEV4, `L²_C` remains **coherence as continuation, not closure**. The symbol supplies no
standard norm, inner product, completeness, reflexivity, weak topology, or compactness theorem.

The framework interface is

```text
ψ : D -> H
Continue(d,e,ψ_d,ψ_e)  whenever d <= e.
```

The gate may custody a candidate `ψ_∞` only after a compact carrier is proved. Coherence of the
candidate then requires a separately proved closed continuation/admissibility condition.

A distinct conditional analytic lane is available when `H` is an actual `L²(Z,μ)` Hilbert
space, the net is uniformly norm-bounded, and the coherence class is weakly closed. Standard
weak compactness may then supply a weakly convergent subnet with limit in the class. Applying
that lane to framework `L²_C` is `OPEN` until all of those structures and hypotheses are
supplied.

## 5. KakeyaLogic application

KakeyaLogic owns the concrete finite tube family, shading `Y(T) ⊆ T`, multiplicity, union,
density, and dimension observables. EEV4 owns this non-promoting gate and its receipt.

Passing `G0` through `G3` produces only a limit candidate for position, direction, and shaded
incidence. A Kakeya conclusion additionally owes:

1. limiting direction saturation;
2. closed incidence support as `δ -> 0`;
3. nontrivial quantitative shading density;
4. multiplicity or union control in the required semicontinuity direction;
5. a separate dimension or volume transfer theorem.

Compactness, connectedness, or cross-repository agreement cannot substitute for these items.
No Kakeya admissibility or observable-transfer theorem is established.

## 6. Lean and EEV4 receipts

| Receipt | Directly validates | Does not validate |
|---|---|---|
| Lean kernel | A theorem follows from exact formal definitions, hypotheses, imports, and axioms. | Adequacy of an unproved Kakeya model. |
| EEV4 schema and probe | Gate structure, dependency ordering, negative controls, and non-promotion. | Compactness or a Kakeya theorem. |
| Deterministic finite fixture | The named implementation produced the recorded scoped output. | An all-scale or continuous theorem. |

Mathlib normally represents a net `K : D -> X` using `Filter.atTop` and represents compactness
through filters and cluster points. Exact declarations must be checked in the active Mathlib
revision and compiled before a Lean receipt is registered.

**Lean status:** `PLANNED / NOT COMPILED`.

## 7. Claim ledger

| Claim | Status | Promotion threshold or falsifier |
|---|---|---|
| The stated multiscale configuration interface is useful. | `PROPOSED` | Reject if it cannot preserve incidence coupling or expose a usable transfer lemma. |
| The concrete refinement order is directed. | `PLANNED / NOT COMPILED` | Compile the common-upper-bound proof in Lean. |
| The proposed measure carrier is compact for the actual family. | `OWED` | Prove compact containment with normalization, mass bounds, and closed constraints. |
| Every configuration net has a convergent subnet. | `OPEN` in this instantiation | Establish `G2` before invoking extraction. |
| A limit remains Kakeya-admissible. | `OPEN` | Prove direction, incidence, and shading closure. |
| The intended Kakeya observable transfers. | `OPEN` | Prove continuity or semicontinuity in the needed direction. |
| The gate improves interpretability. | `OPEN` | Run an independent, prespecified failure-localization evaluation. |
| Passing EEV4 probes proves the mathematical limit theorem. | `CLOSED-NEGATIVE` | Category error: operational validation is not kernel proof. |

## 8. Current receipt and stop rule

```text
G0_CARRIER: PASS-SPEC
G1_DIRECTED: PASS-SPEC / LEAN NOT COMPILED
G2_COMPACT: OWED
G3_EXTRACT: BLOCKED BY G2
G4_CLOSED: OWED
G5_TRANSFER: OWED
terminal_status: BLOCKED-COMPACTNESS
claim_status: PROPOSED
```

**Pass condition:** a named receipt satisfies the gate dependencies and preserves all OPEN
boundaries.
**Failure condition:** extraction or promotion is asserted before its prerequisite passes.
**Kill criterion:** abandon this carrier if it loses incidence coupling or supplies no useful
continuity/semicontinuity statement.
**Next smallest action:** compile the directed-order skeleton in Lean, then prove compactness
for one bounded finite carrier before attempting a Kakeya limit.
