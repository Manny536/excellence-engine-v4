# Example 1.1 replay protocol

## Reproduce the evidence check

From the repository root, verify the nine original files and then verify both artifact locations at the recorded revision.

```bash
(cd evidence/assets/peaice-thinking-machine-2026-11-11 && sha256sum -c SHA256SUMS)
revision=2ac13b7b539ba62d8b44fc726389691d5e4d7b61
git rev-parse \
  "$revision:docs/meta/PeAIce-Thinking-Machine-V4-Wired-Telemetry.html" \
  "$revision:site/artifacts/meta/thinking-machine-v4-wired-telemetry.html"
```

Both Git blob IDs should be `9cc34b518c348fbc2472385dfff85c2b2321c496`. A shallow checkout may need to fetch the recorded revision. Compare each displayed path against its pinned counterpart. Preserve partial recovery when the screenshot shows a path stem.

## Collect a fresh pilot

1. Run the three registered queries below in fresh signed-out private sessions. On each of two dates, collect three sessions per query. Preselect and record the query order, browser, region, language, and capture time with time zone. Hold browser, region, and language fixed. Keep a distinct session ID for each run.
2. Capture the unexpanded search result first and then any expanded answer and source cards. Record the query actually displayed and any search rewrite. Keep runs with no overview in the denominator. Screenshots, expansions, and carousel movements belong to their originating session.
3. Compare the main answer with the pinned project identity and repository paths. Record exact strings, corroborating screenshot filenames, and separate observations for spelling suggestions, closing clarification, and source cards. Capture the backend version only if the interface discloses it.
4. Report counts by query and date for an overview shown, correct project attribution, exact source-path recovery, exact or partial mirror-path recovery, and mixed disambiguation. Mark unavailable checks as unresolved. Where feasible, have a second reader score the captures independently and log disagreements.

| Query | Role |
| --- | --- |
| `PeAIce thinking machine` | Target query used in the original observation |
| `PeAIce thinking machine Manny536` | Author-handle control |
| `thinking machine` | Unbranded ambiguity baseline |

**Decision rule.** A main answer passes identity if it connects the PeAIce Thinking Machine to the EEv4 repository without merging it with another entity. An exact source or mirror path passes only when the full path appears in the response. A path stem is partial. Name disambiguation is mixed if the main answer is accurate and the interface still suggests an alternative as the intended referent. Report separate counts for each check, including unresolved observations.

This pilot tests repeatability under recorded public-search conditions. Queries differ in specificity, so the comparison describes the observed effect of wording within the sampled sessions. The protocol does not infer an internal retrieval mechanism or cross-model compaction performance.
