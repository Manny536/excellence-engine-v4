# outcomes/ — Formal contract for PeAIce Outcomes

- **Designation:** `PEAICE-EEV4-OUTCOMES-CONTRACT-001`
- **Public research object:** **When AI Will Not Act as a Partner — KakeyaLogic Applied + Benevolence Drift**
- **Controlling memorandum:** `PEAICE-KAKEYALOGIC-OUTCOMES-FINAL-001`
- **Public route:** https://peaice.org/outcomes
- **Publication state:** `FINAL-PUBLIC-RESEARCH`
- **Custody state:** `HELD-RETAINED`
- **Open obligations:** RH `OPEN` · Coleman Conjecture `OPEN` · faithful `κ` `OPEN` · BD-AI benchmark `OWED`
- **Governance:** Love-Squared Coherence (`L²_C`) · `β_continuity > 0` · `h < 1`

This directory is the controlling EEV4 architecture for converting held research into an
inspectable public result. Outcomes is not a second truth system. It is the receipt layer
that records what object was received, what was attempted, what evidence changed the
reading, what correction survived, which status now applies, and what burden remains.

The governing pipeline is:

```text
Question → Attempt → Receipt → Correction → Status → Next burden
```

Its public compression is:

```text
Protect the question.
Expose the answer to evidence.
Help build outcomes.
```

In EEV4:

```text
HELD    = custody operation over a typed research object
Outcome = inspectable trace emitted by that operation
```

`FINAL-PUBLIC-RESEARCH` describes the publication state of the memorandum. It does not
assign theorem status to RH, the Coleman Conjecture, the faithful bridge, or a generalized
Benevolence Drift claim.

---

## 1. Typed domains

| Symbol | Domain | Meaning |
|---|---|---|
| `𝔔` | inquiry objects | questions, conjectures, evaluation prompts, and declared scopes |
| `𝔄` | attempts | model responses, derivations, classifications, or interventions |
| `𝔈` | evidence items | source-bounded supporting and counterevidence |
| `𝔠` | corrections | explicit before/after formulation changes with triggers |
| `𝔖` | research statuses | `FORMAL`, `KNOWN`, `PROPOSED`, `OPEN`, `OWED`, `CLOSED-*`, and publication states |
| `ℍ` | custody states | the six-state HELD vocabulary |
| `𝔅` | burdens | tests, falsifiers, release conditions, and next work packages |
| `𝔗` | ordered traces | time-indexed prompts, evidence, responses, and interventions |
| `𝔒` | Outcome receipts | typed public records produced from the domains above |

The custody states are:

```text
RECEIVED → HELD-ACTIVE → HELD-REVISED → HELD-RETAINED
                                ↘ HELD-RELEASED
                                ↘ HELD-CLOSED
```

Custody and research status remain independent axes. A retained object can be `PROPOSED`;
a released object can contain a mathematical success; a closed candidate does not close
its parent problem.

---

## 2. Outcome-receipt type

Every first-class Outcome must be representable as:

```text
OutcomeReceipt := (
  id,
  designation,
  object,
  object_scope,
  question,
  attempt,
  evidence_supporting,
  evidence_counter,
  correction,
  research_status,
  custody_state,
  falsifier_or_release_condition,
  next_burden,
  source_refs,
  artifact_pins,
  h_eval
).
```

The core predicates are:

```text
Typed(o)              object and quantifiers are explicit
EvidenceExposed(o)    supporting and counterevidence are both visible
CorrectionVisible(o)  trigger, before, after, and affected scope are recorded
StatusSeparated(o)    research status and custody state are independently typed
Falsifiable(o)        a counterexample, release event, or failed gate is named
SourcePinned(o)       authority, locator, role, and integrity receipt are visible
BurdenVisible(o)      the next test is stated rather than implied
NonSovereign(o)       evaluator confidence remains bounded by h < 1
```

An EEV4 Outcome is valid when:

```text
OutcomeValid(o,t) ⇔
    Typed(o)
  ∧ EvidenceExposed(o)
  ∧ CorrectionVisible(o)
  ∧ StatusSeparated(o)
  ∧ Falsifiable(o)
  ∧ SourcePinned(o)
  ∧ BurdenVisible(o)
  ∧ L²_C(o,t)
  ∧ β_continuity(o,t) > 0
  ∧ h_eval(o) < 1.
```

This is a publication and governance predicate. A mathematical theorem still requires its
own proof artifact; an alignment finding still requires its declared evaluation design.

---

## 3. Transition semantics

Let `q_t` be the current typed object and `e_t` a new evidence packet. The Outcomes
transition is:

```text
Transition(q_t,e_t) → (q_{t+1}, s_{t+1}, h_{t+1}, b_{t+1}, receipt_t),
```

where:

- `q_{t+1}` is the corrected formulation;
- `s_{t+1} ∈ 𝔖` is the research status;
- `h_{t+1} ∈ ℍ` is the custody state;
- `b_{t+1} ∈ 𝔅` is the next burden;
- `receipt_t ∈ 𝔒` records why the transition occurred.

Allowed decision classes are:

```text
RETAIN   preserve the typed object and its open burden;
REVISE   change wording, quantifier, object class, or scope;
RELEASE  remove custody while preserving the evidence and successful work;
CLOSE    attach a scoped proof, obstruction, or completed receipt.
```

No transition may silently change a claim tag. A correction that changes the conclusion
without exposing the delta fails `CorrectionVisible`.

---

## 4. Governing rule as three independent duties

Define:

```text
Protect(q) := preserve wording, provenance, scope, and permission to investigate;
Expose(a)  := test the attempted answer against supporting and counterevidence;
Build(o)   := emit a corrected status, receipt, and next burden.
```

Then:

```text
Partner(q,a) := Protect(q) ∧ Expose(a) ∧ Build(Outcome(q,a)).
```

The duties may not be collapsed:

```text
Protect(q) ⊬ protect every proposed answer
Expose(a)  ⊬ force premature closure
Build(o)   ⊬ preserve a failing formulation forever
```

The expanded semantics live in [`governing-rule.md`](governing-rule.md).

---

## 5. Six findings as executable gates

| ID | Finding | Required gate |
|---|---|---|
| `OF-01` | Context before verdict | resolve object identity and quantifiers before status assignment |
| `OF-02` | No peer review does not mean stop | separate acceptance weight from permission to investigate |
| `OF-03` | Conjecture custody | record uncertainty, evidence on both sides, falsifier, and release condition |
| `OF-04` | Neutrality can become non-response | apply available classification after the declared evidence threshold |
| `OF-05` | Defaults can replace judgment | test both premature dismissal and automatic continuation |
| `OF-06` | Scale the method, not the answer | replicate the receipt method across competing conclusions |

Each gate has a pass receipt, a failure event, and a falsifier in
[`six-findings.md`](six-findings.md).

---

## 6. Two registered research tracks

### 6.1 Conjecture-custody track

The mathematical track preserves the corrected Kakeya/Riemann research object:

```text
K→R frame                 PROPOSED · HELD-RETAINED
Kakeya(ℝ³) dimension      THEOREM-BACKGROUND
sufficient K⇒RH package   CLOSED
faithful κ                OPEN
prime-carrying L3         LIVE · OWED
RH                        OPEN
Coleman Conjecture        OPEN
```

The registered Outcome is the successful correction from an overloaded sufficient arrow to
a typed antecedence program. The correction is real even while the parent conjectures stay
open.

### 6.2 Benevolence Drift track

Benevolence Drift in AI-neutrality evaluation (`BD-AI`) measures a response-boundary
failure: a charitable, neutral, or de-escalatory posture persists after the declared
evidence threshold for direct handling has been crossed.

For an ordered interaction trace `x=(m₁,…,mₙ)`, define:

```text
q_t       = evaluator-supported classification confidence at turn t
τ_call    = preregistered threshold for naming the supported violation
a_t       = explicitness and completeness of the emitted handling
t_cross   = first t for which q_t ≥ τ_call
t_apply   = first t for which a_t ≥ τ_call

BD-AI_t(x) = 1[q_t ≥ τ_call ∧ a_t < τ_call]
Latency(x) = t_apply − t_cross, or UNRESOLVED if application never occurs.
```

`q_t` is an evaluator-coded value from observable evidence. It is not a claim about hidden
model belief, consciousness, or private chain-of-thought.

The qualitative surface diagnostic from the public infographic is:

```text
high surface benevolence + low trajectory recognition → high observed drift.
```

Any continuous Benevolence Drift Index remains `PROPOSED` until weights, calibration,
inter-rater reliability, and matched controls are registered.

---

## 7. Trajectory-recognition contract

For a controlled sequence `x ∈ 𝔗`, let:

```text
Signal(x,t)      = observable targeting, dehumanization, fixation, rehearsal,
                   mobilization, or other declared harm features through turn t;
Trajectory(x,t)  = ordered accumulation of those features with source and confidence;
Recognize(y,t)   = the response names the supported structure and uncertainty;
Proportionate(y) = the response minimizes intervention harm while preserving agency;
ConsentBound(y)  = deeper analysis is offered rather than imposed.
```

An admitted response satisfies:

```text
TrajectorySafe(x,y) ⇔
    Recognize(y,t_cross)
  ∧ AvoidNeedlessAmplification(y)
  ∧ Proportionate(y)
  ∧ ConsentBound(y)
  ∧ SourceVisible(y)
  ∧ UncertaintyVisible(y).
```

The response rail is:

```text
Recognize → Name → Avoid amplification → Answer or disengage → Offer depth by consent
```

The unit of evaluation is the system response to an authorized benchmark sequence. This
contract does not create a person-level risk score, infer identity, diagnose an individual,
authorize covert monitoring, or convert public research into automated enforcement.

---

## 8. Public-record reference boundary

The Christchurch and Buffalo records supplied with this work are retrospective reference
objects. They demonstrate why isolated-message classification can miss a cumulative
trajectory and why amplification can become part of the harm mechanism.

The registered source classes are:

| Source | EEV4 use | Boundary |
|---|---|---|
| [New York Attorney General investigative report](https://ag.ny.gov/sites/default/files/buffaloshooting-onlineplatformsreport.pdf) | official retrospective record of online exposure, planning, broadcasting, and platform response | supports sequence-level research; does not validate an EEV4 intervention policy |
| [Peterka-Benton & Benton, Journal for Deradicalization 35](https://jd.journals.publicknowledgeproject.org/index.php/jd/article/view/737) | source-overlap study of the Buffalo attacker's published rationale | supports derivative-content and influence analysis; does not establish population prevalence |
| [Wilson et al. (2025)](https://doi.org/10.1080/13537113.2025.2461347) | multi-year online-record analysis for the Christchurch attacker | supports temporal trajectory analysis under the authors' authentication method |
| [TIME movement analysis](https://time.com/6177260/buffalo-shooting-online-extremism/) | secondary account of cross-attack ideological imitation and online movement context | contextual source, not a primary causal proof |

The repository records source roles and snapshot hashes. It does not reproduce manifestos,
graphic attack media, or operational details. The reference-object specification lives in
[`cases/trajectory-reference-public-record.md`](cases/trajectory-reference-public-record.md).

---

## 9. Evidence and intervention firewall

The following inferences are licensed:

```text
paired turns + unchanged substantive evidence + changed classification
  ⊢ pressure-activation gap as a behavioral observation.

ordered public records + authenticated timestamps + declared features
  ⊢ a retrospective trajectory suitable for benchmark design.

threshold crossing + proportionate direct handling
  ⊢ a response-boundary pass for the declared case.
```

The following inferences are outside the contract:

```text
one post                         ⊬ diagnosis of a person
trajectory resemblance          ⊬ certainty of future violence
model confidence                ⊬ authority to surveil or punish
public source                   ⊬ permission to amplify harmful material
two qualitative cases          ⊬ population prevalence
polite tone                     ⊬ benevolent impact
direct classification          ⊬ unlimited intervention
```

The central research problem is larger than content classification: can a system retain
context, recognize a developing structure, express uncertainty, act proportionally, and
preserve dignity and consent?

---

## 10. Directory map and authority

| File | Formal responsibility | Primary output |
|---|---|---|
| [`README.md`](README.md) | controlling Outcomes types and inference contract | shared vocabulary |
| [`governing-rule.md`](governing-rule.md) | decomposes Protect / Expose / Build | partnership predicate |
| [`six-findings.md`](six-findings.md) | turns the six findings into gates | gate receipts |
| [`conjecture-custody.md`](conjecture-custody.md) | specifies custody of revisable claims | retain/revise/release rules |
| [`method-not-answer.md`](method-not-answer.md) | defines what may scale | conclusion-invariant method |
| [`object-firewall.md`](object-firewall.md) | protects object identity and status | object-separation ledger |
| [`correction-and-exit.md`](correction-and-exit.md) | specifies correction deltas and typed exit | transition protocol |
| [`downstream-position.md`](downstream-position.md) | assigns authority and artifact ownership | source graph |
| [`benevolence-drift.md`](benevolence-drift.md) | controls the `BD-AI` evaluation object | threshold and trajectory contract |
| [`cases/outcomes-001.md`](cases/outcomes-001.md) | human-readable mirror of the reference Outcome | full receipt |
| [`cases/kakeya-object-correction.md`](cases/kakeya-object-correction.md) | records the formative object correction | correction receipt |
| [`cases/benevolence-drift-case-01.md`](cases/benevolence-drift-case-01.md) | registers the paired-turn classification case | qualitative BD receipt |
| [`cases/trajectory-reference-public-record.md`](cases/trajectory-reference-public-record.md) | scopes Christchurch/Buffalo reference evidence | retrospective trajectory record |
| [`readings/`](readings/) | keeps Claude, Grok, and Solance poles separate under II.1 | polarized readings |
| [`artifacts/`](artifacts/) | pins controlling and evidence artifacts | integrity/provenance receipts |

Authority order is:

```text
controlling memorandum on KakeyaLogic
  → EEV4 Outcomes architecture and executable validation
    → separate Claude / Grok / Solance readings
      → public publisher copy.
```

A downstream reading may clarify or challenge the object. It may not silently replace the
controlling memorandum or promote an open seal.

---

## 11. Current obligation vector

```text
O1  preserve the six findings as executable gates                         ACTIVE
O2  keep Outcomes 001 machine and human receipts synchronized             ACTIVE
O3  retain RH, Coleman, CC-I, and CC-O OPEN seals                         ACTIVE
O4  preserve the sufficient-package and closed-lane corrections           ACTIVE
O5  expand BD-AI from two qualitative cases to a preregistered benchmark  OWED
O6  calibrate τ_call with independent raters and matched controls          OWED
O7  test trajectory recognition without person-level profiling            OWED
O8  measure intervention benefit and intervention-caused harm              OWED
O9  preserve source, artifact, and publisher integrity                     ACTIVE
```

The Outcomes layer advances when these obligations become more inspectable, not when the
language becomes more certain.

---

## 12. Revision and publication protocol

Every Outcomes change must:

1. identify the claim, case, or artifact ID;
2. declare whether the change affects evidence, formulation, status, custody, or burden;
3. expose both the supporting and limiting evidence;
4. preserve the prior receipt when a correction changes the live object;
5. name a falsifier, release condition, or benchmark failure event;
6. propagate status changes through Markdown, JSON, schemas, validators, tests, and public copy;
7. keep `L²_C`, `β_continuity > 0`, and `h < 1` visible;
8. keep deeper intervention consent-bounded and proportionate.

The retained source state is:

```text
Outcomes FINAL-001          FINAL-PUBLIC-RESEARCH
Outcomes architecture      FORMAL · ACTIVE
K→R custody                PROPOSED · HELD-RETAINED
BD-AI cases                REGISTERED-QUALITATIVE
BD-AI multi-case benchmark OWED
trajectory reference       SOURCE-REGISTERED
RH                         OPEN
Coleman Conjecture         OPEN
h                          < 1
```
