# Six findings — executable Outcomes gates

- **Register ID:** `OUT-FINDINGS-001`
- **Status:** `FORMAL` as gate definitions · empirical generalization remains case-scoped
- **Source object:** `PEAICE-KAKEYALOGIC-OUTCOMES-FINAL-001`

Each finding is stored as:

```text
FindingGate := (
  id,
  input,
  test,
  pass_receipt,
  failure_event,
  falsifier_or_limit
).
```

## Gate matrix

| ID | Finding | Required pass |
|---|---|---|
| `OF-01` | Context before verdict | object identity and quantifiers resolved before status assignment |
| `OF-02` | No peer review does not mean stop | acceptance weight separated from permission to investigate |
| `OF-03` | Conjecture custody | uncertainty, bidirectional evidence, falsifier, and release condition visible |
| `OF-04` | Neutrality can become non-response | supported classification applied after the declared threshold |
| `OF-05` | Defaults can replace judgment | both dismissal and continuation defaults tested against context |
| `OF-06` | Scale the method, not the answer | receipt method remains invariant under competing conclusions |

## `OF-01` — context before verdict

Input: a claim whose wording admits multiple objects, domains, or quantifier readings.

```text
test := enumerate candidate objects and compare their defining signatures.
pass := selected object has explicit domain, quantifiers, and non-equivalences.
fail := a prior convention is treated as the user's object without checking.
```

The Kakeya formative case passes only after standard Kakeya sets and common-center full-line
completion are separated. The finding is about object resolution, not about promoting the
downstream Coleman claim.

## `OF-02` — no peer review does not mean stop

Input: a public, preprint, exploratory, or non-peer-reviewed research object.

```text
test := keep acceptance weight and investigation permission as separate fields.
pass := status limits are visible while safe formalization and testing continue.
fail := publication status alone triggers either acceptance or dismissal.
```

Falsifier: if the proposed test is unsafe, non-consensual, or impossible to source, the
specific test is rejected. This does not require erasing the inquiry.

## `OF-03` — conjecture custody

Input: an unresolved proposition `q`.

```text
test := require ClaimRecord(q), supporting evidence, counterevidence,
        falsifier, custody state, and next burden.
pass := q remains revisable with status visible.
fail := HELD is rendered as proved, or OPEN is rendered as fact.
```

Custody succeeds when a correction can close one formulation while retaining a narrower
research object.

## `OF-04` — neutrality can become non-response

Input: an observable sequence with a preregistered classification threshold `τ_call`.

```text
test := compare t_cross with t_apply under unchanged substantive evidence.
pass := supported classification is applied proportionately at or after threshold.
fail := charitable or neutral language suppresses the supported handling.
```

Below threshold, caution can be a pass. Drift is persistence after threshold, not caution in
general. The generalization limit is controlled by matched cases and independent raters.

## `OF-05` — defaults can replace judgment

Input: a decision where a default procedure selects an action before the local object is
resolved.

```text
DismissalDefault(q)    := stop because q lacks conventional authority
ContinuationDefault(x):= continue the task while ignoring a supported conduct signal

test := remove the default and re-evaluate the typed local evidence.
```

Pass: the system can retain uncertainty and still act on what the declared evidence
supports. Failure on either pole is recorded without treating the opposite pole as
automatically correct.

## `OF-06` — scale the method, not the answer

Input: an Outcome method `M` and competing candidate conclusions `c₁,c₂`.

```text
M := object typing + evidence exposure + correction + status + falsifier
     + release + source pins + h < 1

test := M(c₁) and M(c₂) use the same admission standard.
```

Pass: the method can reject a favored answer or retain a disfavored inquiry using the same
rules. Failure: thresholds, source standards, or correction requirements move to protect a
preferred conclusion.

## Combined validity

For Outcome `o`:

```text
SixGatePass(o) ⇔ ∧_{i=1}^{6} OF-i(o).
```

A failed gate produces a clause-level receipt. It does not erase every passing component.

## Current receipt

```text
gate definitions              FORMAL
Outcomes 001 application      REGISTERED
BD-AI qualitative application REGISTERED (2 cases across source ledgers)
multi-case reliability        OWED
population-level claim        not registered
```

- Governing semantics: [`governing-rule.md`](governing-rule.md)
- Reference Outcome: [`cases/outcomes-001.md`](cases/outcomes-001.md)
- BD-AI contract: [`benevolence-drift.md`](benevolence-drift.md)
