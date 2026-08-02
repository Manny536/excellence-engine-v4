# Closed lanes — scoped obstruction ledger

- **Register ID:** `ANT-CLOSED-001`
- **Rule:** closure attaches to a typed candidate class and obstruction certificate
- **Open targets preserved:** RH `OPEN` · Coleman Conjecture `OPEN` · prime-carrying carrier `LIVE`

## Closure-certificate type

A lane may be marked closed only with a record

```text
ClosureCertificate := (
  lane_id,
  candidate_class,
  target_claim,
  obstruction_invariant,
  incompatibility_statement,
  proof_or_registered_receipt,
  closure_scope,
  reopening_condition
).
```

Two closure values are used:

```text
CLOSED          := a formulation is retired or a scoped route is completed;
CLOSED-NEGATIVE := the declared candidate class fails a required target gate.
```

Neither value propagates automatically to a changed operator, changed domain, unbounded
coupling, different trace formula, or the parent conjecture.

## Lane ledger

| Lane ID | Candidate class | Certificate | Status | Reopening condition |
|---|---|---|---|---|
| `CL-SUFF` | sufficient package `Kakeya(ℝ³)⇒RH` | logical degeneracy under proved premise | `CLOSED` | none as an intermediate package; any proof is evaluated directly as an RH proof |
| `CL-KSIGMA` | registered one-parameter square-difference determinant realization | order/genus/density pincer plus Weyl-class mismatch | `CLOSED-NEGATIVE` | a materially changed carrier or a demonstrated failure in the registered obstruction chain |
| `CL-WP5B` | operator-bounded WP5b relative-determinant class | bounded, thin-support Krein spectral shift (Theorem H / WP5-OBS-2) | `CLOSED-NEGATIVE` | leave operator-bounded class, change the free operator, or use independent flow data and discharge new gates |
| `CL-LIT` | claim that a reviewed Kakeya→`ζ` exact-zero bridge is already present in the registered literature audit | no qualifying source located in the declared audit | `CLOSED-NEGATIVE` as source-state claim | produce a qualifying reviewed source and update the audit |

## `CL-SUFF` — sufficient packaging

Candidate:

```text
CC-S := Kakeya(ℝ³) ⇒ RH.
```

Because the `ℝ³` Kakeya dimension statement is theorem background, `CC-S` is equivalent to
RH relative to that premise. The closure is a type correction: the package does not expose
an intermediate bridge. See [`sufficiency-trap.md`](sufficiency-trap.md).

```text
scope closed : CC-S as EEV4 research packaging
scope open   : RH, faithful κ, construction essentiality
```

## `CL-KSIGMA` — square-difference determinant realization

The registered kernel family is

```text
K_σ(m,n) = |m²−n²|^{-σ},  m≠n;
K_σ(n,n) = 0,
```

with the corresponding regulated/full-operator realization where declared downstream.
Its closure certificate combines three target incompatibilities:

```text
order   : the determinant growth class must match order-1 Ξ;
genus   : trace-class Fredholm products have the wrong genus for Ξ;
density : a power-law determinant spectrum and the n⁴ free ladder do not produce T log T.
```

For the full registered realization, relative compactness against the `n⁴` ladder preserves
`N(Λ)≈Λ^{1/4}`, while the squared `Ξ` target requires `≈√Λ log Λ`. The V6.4.3 downstream
ledger records the resulting `CLOSED-NEGATIVE` status.

EEV4 inherits that scoped downstream receipt. This file does not independently upgrade the
singular-value asymptotic beyond the status assigned in its theorem ledger; it records the
accepted lane state and the exact invariants on which that state depends.

The certificate is scope-correct:

- it closes the named square-difference determinant family;
- it does not prove that every global invariant built from integer-square data is
  prime-free;
- “missing primes in the entries” remains guidance, not the all-orders obstruction;
- it does not close a materially different prime-carrying carrier.

## `CL-WP5B` — operator-bounded relative determinant

Let

```text
D = diag(cn⁴),
A = D + V,
V=V*,  ‖V‖op<∞,
ξ(λ)=N_D(λ)−N_A(λ).
```

Theorem H's Weyl-window law gives

```text
sup_λ |ξ(λ)| < ∞,
|ξ(λ)|≤1 eventually,
supp ξ thin in bounded windows.
```

The WP5b functionals are transforms of this same bounded spectral shift:

```text
heat trace       = Laplace(ξ)
relative zeta    = Mellin(ξ)
perturbation det = Cauchy(ξ).
```

They cannot create the unbounded `√Λ log Λ` counting difference required against the `n⁴`
free ladder. This closes operator-bounded WP5b, including bounded kernel replacements in
the registered scope.

```text
scope closed : fixed n⁴ free ladder + operator-bounded self-adjoint coupling
scope open   : unbounded category L1, changed free operator, WP5c flow traces, L3
```

## `CL-LIT` — external exact-bridge audit

This lane is a source-state assertion, not a universal theorem of nonexistence. The audit
question is:

```text
Does a qualifying reviewed source prove a Kakeya-incidence → ζ exact-zero-location bridge?
```

No such source is present in the registered audit as of **2026-08-02**. Kakeya, restriction, decoupling,
large-value, spectral-shift, and spectral-determinant references retain their individual
roles; none is promoted into the missing bridge.

A qualifying source reopens this audit immediately. It must identify the exact theorem,
scope, carrier, and zero-location conclusion—not only topical proximity.

## Reopening rule

A closed-negative lane may be reconsidered only when at least one novelty condition holds:

```text
N1  candidate class changed materially;
N2  a load-bearing lemma in the closure certificate was invalidated;
N3  a new theorem supplies the previously incompatible invariant;
N4  a new source satisfies the declared literature criterion.
```

The reopening record must name `N1`–`N4`, assign a new lane/version ID, and preserve the old
receipt. Renaming the same object, changing notation, increasing truncation size, or citing
model agreement does not reopen a lane.

## Monotonic custody rule

```text
closed receipt + no novelty ⇒ status remains closed
closed receipt + typed novelty ⇒ new candidate enters HELD-ACTIVE
```

This monotonicity is ledger continuity, not attachment to a failed object. A valid changed
construction is welcomed as a new scoped candidate.

- Formal relation types: [`antecedent/README.md`](README.md)
- Live continuation: [`prime-carrying-continuation.md`](prime-carrying-continuation.md)
