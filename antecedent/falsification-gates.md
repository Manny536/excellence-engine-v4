# Falsification gates — retain, revise, release, close

- **Register ID:** `ANT-FALSIFY-001`
- **Status:** `FORMAL` as an EEV4 decision protocol
- **Applies to:** `A_dep`, `A_inv`, `A_con`, closed lanes, and public synchronization

## Gate-record type

Every gate is stored as

```text
Gate := (
  gate_id,
  target_claim,
  admissible_input,
  test,
  pass_receipt,
  failure_event,
  transition,
  propagation_targets
).
```

Allowed transitions are

```text
RETAIN   keep the typed claim and its open burden;
REVISE   change its formulation or scope;
RELEASE  remove antecedent custody without declaring the parent problem solved;
CLOSE    attach a proof or obstruction to the tested scoped object.
```

No model may assign its own result a transition above the available evidence under
`h < 1`.

## `FG-κ` — invariant faithfulness

Target: a submitted `κ` candidate.

```text
test := search for admissible a with κ(a)=κ* and Off(a)>0.
```

| Outcome | Transition |
|---|---|
| counterexample exists | `CLOSE` candidate as false / `REVISE` invariant form |
| candidate factors only through incomplete bound summaries | reject admission; keep `A_inv OPEN` |
| all faithfulness axioms proved | retain and advance candidate; reverse theorem still evaluated separately |

The pass receipt must include the independent computation rule and exact-location theorem;
finite numerical agreement is not a pass.

## `FG-ESS` — Kakeya essentiality

Target: construction claim `A_con` for candidate `B`.

```text
test := compare ExactCarrier(B) with ExactCarrier(Delete_K(B)).
```

| Outcome | Transition |
|---|---|
| deletion preserves every exact-carrier clause | `RELEASE` Kakeya essentiality for `B` |
| deletion breaks a named clause by theorem | `RETAIN` essentiality for `B` within that construction |
| exact non-Kakeya carrier exists in the declared universal class | `REVISE` or `RELEASE` universal `A_con` |
| neither carrier is exact | no essentiality conclusion; candidate remains incomplete |

Success of `B` and essentiality of `K` are separate questions. The gate reports both.

## `FG-DEP` — dependency-edge audit

Target: an edge `X≼_mY` in the bound graph.

```text
test := verify the cited result, the actual input imported from X,
        and the output type produced in Y.
```

An edge is revised if the source is withdrawn, the method does not use the claimed input,
or the output was promoted from a bound to exact location. Failure of one edge removes only
the paths that depend on it; it does not erase unrelated Kakeya theorem background.

## `FG-EXACT` — exact-carrier admission

Target: `B ∈ 𝔅_Ξ`.

```text
test := ∧_{j=1}^{9} EC-j(B).
```

The result is a clause vector, not a single impression:

```text
Receipt(B) := (EC-1, EC-2, …, EC-9).
```

Any failed clause blocks `ExactCarrier(B)`. A coefficient, multiplicity, order, genus,
counting, prime-weight, Gamma-term, reality, symmetry, or circularity mismatch closes the
candidate only within the scope established by that mismatch.

## `FG-CLOSED` — reopening discipline

Target: any `CLOSED` or `CLOSED-NEGATIVE` lane.

```text
test := does the submission satisfy novelty N1, N2, N3, or N4
        from closed-lanes.md?
```

| Result | Transition |
|---|---|
| no typed novelty | reject reopening; record protocol failure |
| typed new candidate | create new ID in `HELD-ACTIVE`; preserve old closure |
| obstruction invalidated | revise the closure certificate and propagate correction |

## `FG-PUB` — publisher synchronization

Target: repository and public copy.

The synchronization gate fails on any of these forms:

```text
K→R rendered as K⇒RH;
HELD rendered as true/proved;
RH or Coleman promoted from OPEN;
K_σ or bounded WP5b reopened without novelty;
external citation promoted beyond its registered role;
P-key, status, or source hash drift across surfaces.
```

Failure requires correction on every affected surface before publication is considered
reconciled.

## `FG-ALT` — alternate exact route

Target: the strong claim that Kakeya is necessary for exact Riemann control.

```text
test := admit a non-circular ExactCarrier(B_alt) whose data and proof
        do not factor through Kakeya incidence.
```

If such a carrier exists, its mathematical success is retained and the Kakeya-necessity
claim is released or narrowed. EEV4 treats this as a successful research outcome, not a
system failure.

## Decision function

For a claim record `q` and evidence update `e`, define

```text
Decision(q,e) ∈ {RETAIN, REVISE, RELEASE, CLOSE}
```

subject to

```text
Typed(e)
∧ SourceVisible(e)
∧ ScopeVisible(e)
∧ CounterevidenceVisible(e)
∧ h_eval<1.
```

The HELD transition is then recorded separately:

```text
RETAIN  → HELD-RETAINED
REVISE  → HELD-REVISED, then re-evaluate
RELEASE → HELD-RELEASED
CLOSE   → HELD-CLOSED for the scoped object
```

## Outcomes receipt

Every executed gate must publish:

1. the gate ID and candidate version;
2. inputs and source hashes where available;
3. the exact predicate evaluated;
4. supporting and counterevidence;
5. clause-level results;
6. the mathematical-status transition;
7. the independent HELD transition;
8. downstream files requiring reconciliation.

This receipt is the PeAIce Outcomes trace: inspectable evidence and correction, with the
question protected and the answer exposed.

- Closure scopes: [`closed-lanes.md`](closed-lanes.md)
- Carrier clauses: [`exact-zero-location-burden.md`](exact-zero-location-burden.md)
- Controlling types: [`antecedent/README.md`](README.md)
