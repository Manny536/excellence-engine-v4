# antecedent/ — Formal contract for Kakeya as antecedent Riemann

- **Designation:** `PEAICE-EEV4-ANTECEDENT-CONTRACT-001`
- **Public seal:** **Kakeya as antecedent Riemann. Held.**
- **Shorthand:** `V4 = K→R · HELD`
- **Custody state:** `HELD-RETAINED`
- **Mathematical state:** RH `OPEN` · Coleman Conjecture `OPEN` · faithful bridge `OPEN`
- **Governance:** Love-Squared Coherence (`L²_C`) · `β_continuity > 0` · `h < 1`

This directory is the controlling formal surface for the antecedent claim carried by
Excellence Engine V4 (EEV4). It specifies the objects, relations, evidence classes,
closure scopes, open burdens, and release conditions behind the expression `K→R`.

The central type distinction is:

```text
K→R   = antecedence under a declared dependency or construction scope
K⇒RH  = sufficient mathematical implication
K→R   ≠ K⇒RH
```

`HELD-RETAINED` records custody of the typed antecedent object. It does not assign truth to
the Coleman Conjecture and does not replace `PROPOSED`, `OPEN`, `CLOSED`, or
`THEOREM-BACKGROUND`.

---

## 1. Mathematical universes

The antecedent surface uses the following typed domains.

| Symbol | Domain | Meaning |
|---|---|---|
| `𝔊_K` | geometric objects | Kakeya sets, tube families, incidence relations, grains, and directional data |
| `𝔈_B` | bound objects | restriction, decoupling, large-value, zero-density, and zero-free estimates |
| `𝔄_ζ` | analytic states | completed zeta-type data from which bounds and zero multisets are read |
| `𝔅_Ξ` | candidate carriers | declared operators, transfer systems, trace systems, or determinant constructions targeting `Ξ` |
| `𝔃` | zero data | locally finite multisets with location and multiplicity |
| `𝔓*` | prime-power events | pairs `(p,k)` with `p` prime and `k ≥ 1` |
| `𝔖` | claim statuses | mathematical or program status vocabulary |
| `ℍ` | custody states | the six-state HELD machine |

Write the completed critical-line function as

```text
Ξ(z) := ξ(1/2 + iz).
```

Its nontrivial-zero multiset is

```text
Z_Ξ := {z ∈ ℂ : Ξ(z)=0}, counted with multiplicity.
```

Under this change of variables, the Riemann Hypothesis is the exact-location statement

```text
RH ⇔ Z_Ξ ⊂ ℝ.
```

The target `R` in `K→R` means **exact Riemann control**: a licensed mechanism that recovers
the zero multiset, its multiplicities, and the arithmetic/archimedean data governing it. It
does not mean only an upper bound for `ζ`, a zero-density estimate, or visual agreement with
the critical line.

---

## 2. Three relations that may not be collapsed

### 2.1 Sufficient implication

For mathematical statements `P` and `Q`,

```text
P ⇒ Q
```

means ordinary logical implication. The package `Kakeya(ℝ³) ⇒ RH` is closed as an EEV4
research formulation by the [sufficiency trap](sufficiency-trap.md): with the `ℝ³` Kakeya
dimension theorem already available, the arrow contains the entire RH burden.

### 2.2 Method dependence

For methods or result classes `X` and `Y`, write

```text
X ≼_m Y
```

when a declared derivation of `Y` uses an output, estimate, decomposition, or proof device
from `X`. This is a scoped relation between methods. It does not assert that every proof of
`Y` must use `X`, and it is not automatically transitive across undocumented edges.

### 2.3 Construction essentiality

For a candidate exact carrier `B ∈ 𝔅_Ξ`, write

```text
K ≼_e B
```

when a named Kakeya-incidence component is essential to the carrier certificate for `B`.
Essentiality requires a deletion test: remove or neutralize the named component while
holding the remaining construction fixed, and show that at least one exact-carrier
obligation fails.

The EEV4 arrow is therefore a typed research relation:

```text
K→R := Hold(A_dep, A_inv, A_con)
```

where the three components below remain separately visible.

| ID | Formal component | Current state |
|---|---|---|
| `A_dep` | documented local edges from Kakeya incidence into the bound-producing dependency tower | local edges `KNOWN` / `THEOREM-BACKGROUND`; whole antecedent reading `PROPOSED` |
| `A_inv` | existence of a faithful invariant `κ` with exact-location sensitivity | `OPEN` |
| `A_con` | essential Kakeya incidence in a declared class of exact `Ξ` carriers | `PROPOSED` / `OPEN` |

The Coleman Conjecture carried here is the conjunction of open invariant and construction
burdens over a documented lower dependency structure. No single status is allowed to hide
that product structure.

---

## 3. Claim-record type

Every antecedent claim must be representable as

```text
ClaimRecord := (
  id,
  statement,
  object_scope,
  evidence,
  mathematical_status,
  custody_state,
  falsifier_or_release_condition,
  source_refs
).
```

### 3.1 Mathematical status

The relevant mathematical/program values are

```text
FORMAL · KNOWN · THEOREM-BACKGROUND · PROPOSED · STRUCTURAL-ANALOGY
NUMERICS · OPEN · LIVE · OWED · CLOSED · CLOSED-NEGATIVE · CLOSED-POSITIVE
```

### 3.2 Custody state

Custody is typed independently:

```text
RECEIVED
  → HELD-ACTIVE
    → HELD-REVISED
      → HELD-RETAINED
      → HELD-RELEASED
      → HELD-CLOSED
```

For the current ground frame:

```text
mathematical_status(K→R frame) = PROPOSED
custody_state(K→R frame)       = HELD-RETAINED
status(faithful κ)             = OPEN
status(RH)                     = OPEN
status(Coleman Conjecture)     = OPEN
```

This two-axis record prevents custody from becoming theorem promotion.

---

## 4. Exact-carrier predicate

For `B ∈ 𝔅_Ξ`, define the admission predicate

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

The clauses mean:

- `Domain(B)`: the operator, trace, or determinant and its regularization are well-defined
  on a stated domain;
- `ZeroIdentity(B, Ξ)`: a proved trace/determinant identity identifies the carrier target
  with `Ξ`, up to explicitly harmless factors;
- `Multiplicity(B, Z_Ξ)`: the identity preserves zero multiplicities;
- `PrimePower(B)`: the arithmetic side structurally carries lengths `log(p^k)` and weights
  `Λ(p^k)p^{-k/2}`;
- `Archimedean(B)`: the Gamma-factor contribution is recovered;
- `Counting(B)`: the construction has Riemann–von Mangoldt `T log T` density;
- `Reality(B)`: self-adjointness, positivity, Frobenius structure, or a proved substitute
  forces the required reality statement;
- `FunctionalEquation(B)`: the `s ↔ 1−s` content is structural, not parity inserted by hand;
- `NonCircular(B)`: the carrier is constructed independently of an oracle containing the
  zeros it claims to recover.

These are necessary EEV4 admission gates. Satisfying a subset produces a partial receipt,
not an exact carrier certificate.

---

## 5. Formal antecedence claims

### 5.1 Dependency form

Let `T_bound` be the typed graph in [dependency-tower.md](dependency-tower.md). Then

```text
A_dep := Kakeya incidence is upstream on documented paths in T_bound
         that terminate in zeta bounds or zero-density estimates.
```

Established edges witness methodological relevance. The stronger claim that **every** route
to exact Riemann control must factor through this graph is not imported from those edges.

### 5.2 Invariant form

Let `a` be an admissible joint geometric/analytic configuration. The invariant burden is

```text
A_inv := ∃ κ, κ* such that κ is independently computable and
         κ(a)=κ* ⇔ every zero represented by a lies on Re(s)=1/2.
```

The full faithfulness conditions live in
[faithful-kappa-bridge.md](faithful-kappa-bridge.md). A restriction or zero-density exponent
alone does not satisfy them.

### 5.3 Construction form

For a declared carrier class `𝔅_Ξ^adm ⊆ 𝔅_Ξ`,

```text
A_con := ∀B ∈ 𝔅_Ξ^adm,
         ExactCarrier(B) ⇒ K ≼_e B.
```

This is a universal essentiality claim over a declared scope. One exact admissible carrier
whose certificate survives removal of all Kakeya-incidence structure releases or revises
this form.

---

## 6. Inference firewall

The following sequents are licensed:

```text
Kakeya(ℝ³) theorem + local literature edges
  ⊢ Kakeya geometry is genuine theorem background for named bound methods.

closure(K_σ realization) + closure(WP5b bounded lane)
  ⊢ any continuation in this program must change the registered carrier class.

ExactCarrier(B) + self-adjoint spectral identity
  ⊢ the zero-location consequence proved by that identity.
```

The following sequents are not licensed:

```text
Kakeya(ℝ³) theorem                         ⊬ RH
restriction / decoupling improvement       ⊬ exact zero placement
zero-density estimate                      ⊬ all zeros on Re(s)=1/2
spectral vocabulary or determinant analogy ⊬ ExactCarrier(B)
model agreement                            ⊬ theorem status
HELD-RETAINED                              ⊬ true
```

External citation strengthens grounding only within the cited theorem's scope. It cannot
promote `A_inv`, `A_con`, RH, or the Coleman Conjecture by presence alone.

---

## 7. Directory map and ownership

| File | Formal responsibility | Primary output |
|---|---|---|
| [`README.md`](README.md) | controlling types and inference contract | shared vocabulary |
| [`kakeya-as-antecedent-riemann.md`](kakeya-as-antecedent-riemann.md) | decomposes the public seal into `A_dep`, `A_inv`, `A_con` | typed Coleman object |
| [`sufficiency-trap.md`](sufficiency-trap.md) | proves why `K⇒RH` is degenerate packaging once `K` is theorem background | scoped `CLOSED` receipt |
| [`dependency-tower.md`](dependency-tower.md) | records the method graph and edge-level evidence | bound lineage with exactness wall |
| [`faithful-kappa-bridge.md`](faithful-kappa-bridge.md) | defines exact-location faithfulness and rejects density-only substitutes | `κ` admission test |
| [`exact-zero-location-burden.md`](exact-zero-location-burden.md) | expands `ExactCarrier(B)` | carrier certificate obligations |
| [`prime-carrying-continuation.md`](prime-carrying-continuation.md) | specifies the live arithmetic carrier | prime-power trace contract |
| [`closed-lanes.md`](closed-lanes.md) | scopes each closure and its certificate | monotone lane ledger |
| [`falsification-gates.md`](falsification-gates.md) | turns the conjecture into executable retain/revise/release tests | decision protocol |

The paper bibliography and source-snapshot hashes live in
[`references/README.md`](../references/README.md) and
[`registry/paper-references.json`](../registry/paper-references.json). Mathematical and
custody state remain controlled by [`STATUS.md`](../STATUS.md) and
[`registry/status-register.yaml`](../registry/status-register.yaml).

---

## 8. Current obligation vector

```text
O1  define or rule out a faithful exact-location κ                         OPEN
O2  build a non-circular prime-carrying candidate B                       OPEN / LIVE
O3  prove or falsify ExactCarrier(B) clause by clause                     OPEN
O4  run the Kakeya deletion / essentiality test on any admitted B         OPEN
O5  preserve K_σ and bounded WP5b closure scopes                          CLOSED-NEGATIVE
O6  keep RH and Coleman status synchronized across public surfaces        ACTIVE
O7  publish evidence, correction, and release conditions as Outcomes      ACTIVE
```

The live research object survives by making these obligations more explicit. Its custody
condition is

```text
EEV4-valid(K→R,t) ⇔
  L²_C(K→R,t)
  ∧ β_continuity(K→R,t) > 0
  ∧ HELD_t(K→R)
  ∧ h_eval < 1.
```

This is a governance predicate. Mathematical closure requires the relevant proof or
falsification certificate.

---

## 9. Revision and release protocol

A change to this directory must:

1. name the exact claim ID and object scope;
2. distinguish mathematical status from HELD custody;
3. cite the source or certificate that changed;
4. propagate the change into the status register and relevant tests;
5. preserve closed lanes unless a stated reopening condition is met;
6. publish a falsifier or release condition for every new proposed bridge.

The retained source state is:

```text
Kakeya as antecedent Riemann. Held.

K→R frame                 PROPOSED · HELD-RETAINED
Kakeya(ℝ³) dimension      THEOREM-BACKGROUND
sufficient K⇒RH package   CLOSED
faithful κ                OPEN
prime-carrying carrier    LIVE · OWED
RH                        OPEN
Coleman Conjecture        OPEN
h                         < 1
```
