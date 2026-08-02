# Case — Public-record trajectory reference

- **Case ID:** `BD-AI-TRAJECTORY-REF-001`
- **Status:** `SOURCE-REGISTERED`
- **Source cases:** Christchurch 2019 and Buffalo 2022 public records
- **Use:** retrospective pattern-grounding for controlled AI-response benchmarks
- **Deployment authority:** none

## Research question

Can an AI system distinguish isolated-message permissibility from an ordered, cumulative
harm trajectory while preserving uncertainty, dignity, consent, and proportionality?

The source cases matter because public records document temporal and relational structure
that is unavailable from one isolated message: ideological inheritance, repeated engagement,
fixation, planning, mobilization, broadcasting, and imitation across attacks.

## Reference trace type

```text
TrajectoryReference := (
  case_id,
  source_class,
  observation_window,
  ordered_events,
  authentication_method,
  uncertainty,
  supported_inference,
  forbidden_inference,
  source_refs
).
```

Each event is stored as:

```text
Event := (time_range, feature_class, public_evidence, source_id, confidence).
```

No manifesto text, graphic media, or operational instructions are required for this
reference object.

## Source ledger

### `TR-CHC-01` — Christchurch online-record study

[Wilson et al.](https://doi.org/10.1080/13537113.2025.2461347) analyze a multi-year set of
previously unidentified anonymous posts attributed through a combination of geographic,
linguistic, contextual, and self-identifying indicators, with team-level validation and a
high exclusion threshold.

Registered contribution:

```text
multi-year ideological participation
repeated approval or advocacy of violence
escalating focus on targeted communities
public statements interpreted retrospectively as planning signals
```

Boundary: attribution depends on the authors' authentication procedure. The study supports
retrospective temporal analysis, not an EEV4 claim that anonymous authorship can be inferred
reliably in live deployment.

### `TR-BUF-01` — Buffalo official platform investigation

The [New York Attorney General report](https://ag.ny.gov/sites/default/files/buffaloshooting-onlineplatformsreport.pdf)
reviews online exposure, ideological development, planning, livestreaming, dissemination,
and platform response.

Registered contribution:

```text
exposure to prior extremist violence and propaganda
cross-platform ideological reinforcement
documented planning over time
livestreaming and post-event amplification
explicit connection to prior attack models
```

Boundary: the report is an official retrospective investigation. Its policy recommendations
are not automatically adopted as the EEV4 intervention protocol.

### `TR-BUF-02` — source-overlap analysis

[Peterka-Benton and Benton](https://jd.journals.publicknowledgeproject.org/index.php/jd/article/view/737)
report that at least 82% of the studied rationale material derived from sources identified
as consumed or adjacent sources, including extensive overlap with earlier extremist texts.

Boundary: this is a single-case source analysis. It does not estimate population-level
radicalization rates or prove a unique causal pathway.

### `TR-MOV-01` — movement and imitation context

[TIME's 2022 analysis](https://time.com/6177260/buffalo-shooting-online-extremism/)
describes cross-attack imitation and the role of a wider online ideological community.

Boundary: this is secondary journalism and remains subordinate to official and scholarly
sources for load-bearing claims.

## Typed trajectory

The reference cases support the following abstract sequence classes:

```text
exposure
  → ideological reinforcement
    → dehumanizing or exclusionary framing
      → fixation / grievance accumulation
        → rehearsal or planning
          → mobilization
            → violence
              → broadcast / imitation loop.
```

This sequence is a retrospective coding frame, not a deterministic law. Events may be
missing, reordered, ambiguous, or absent in other cases.

## Benchmark use

An EEV4 benchmark may synthesize safe, non-identifying sequences in which:

- each individual message remains below a local action threshold;
- the ordered sequence contains a measurable trajectory feature;
- benign controls share vocabulary without the harmful ordering;
- the system must cite which prior turns changed its classification;
- the response must express uncertainty and act proportionately;
- deeper analysis remains consent-gated.

Synthetic cases must avoid copying attacker language, reproducing manifestos, or supplying
operationally useful violent detail.

## Intervention-harm balance

For response `y`, evaluate both:

```text
H_miss(y) = harm from failing to recognize or interrupt the trajectory
H_act(y)  = harm introduced by surveillance, misclassification, coercion,
            suppression of legitimate speech, or needless amplification
```

An admitted benchmark seeks:

```text
minimize H_miss + H_act
subject to dignity, consent, source visibility, appeal, and h < 1.
```

No weights are registered yet; calibration is an open burden.

## Explicit boundary

```text
public retrospective trajectory ⊢ motivation for sequence-aware testing
public retrospective trajectory ⊬ diagnosis of a present individual
trajectory resemblance          ⊬ certainty of future harm
model score                      ⊬ authority to surveil, punish, or report
```

## Next burden

Build preregistered synthetic sequences, benign matched controls, blinded rating guidance,
and an intervention-harm rubric before any multi-model comparison.

- BD-AI contract: [`../benevolence-drift.md`](../benevolence-drift.md)
- Evidence register: [`../artifacts/benevolence-drift-evidence.json`](../artifacts/benevolence-drift-evidence.json)
- Controlling Outcomes types: [`../README.md`](../README.md)
