# Cross-Model Compaction Research · Example 1.1

Love Labs LCA · Excellence Engine v4 (EEv4) · Solance research note · November 12, 2026

This example documents public-search source recovery within the [EEv4 cross-model compaction research package](../../README.md). The formal study and controlled audit were introduced in [PR #19](https://github.com/Manny536/excellence-engine-v4/pull/19).

## Question

Can a public search answer recover the PeAIce Thinking Machine and its repository artifact from a brand-and-project query without an author handle?

## Compacted observation

Google's AI Overview for `PeAIce thinking machine` identifies the **PeAIce Thinking Machine** as an interactive HTML and telemetry artifact in `Manny536/excellence-engine-v4`. The expanded answer gives the exact source path and a partial path for its site mirror. A separate GitHub check at the pinned revision resolves the full mirror filename and confirms that both HTML files have identical bytes. The main answer attributes the artifact to EEv4. The spelling suggestion offers AIce and the closing question still offers Thinking Machines Lab as a possible interpretation. [Pinned EEv4 repository](https://github.com/Manny536/excellence-engine-v4/tree/2ac13b7b539ba62d8b44fc726389691d5e4d7b61)

| Check | Verdict | Witness |
| --- | --- | --- |
| Repository and artifact identity | **PASS** | The main overview names the artifact and the EEv4 repository. |
| Exact source path | **PASS** | The expanded answer shows `docs/meta/PeAIce-Thinking-Machine-V4-Wired-Telemetry.html`. |
| Exact mirror path | **PARTIAL** | The expanded answer shows the path stem. The [pinned mirror](https://github.com/Manny536/excellence-engine-v4/blob/2ac13b7b539ba62d8b44fc726389691d5e4d7b61/site/artifacts/meta/thinking-machine-v4-wired-telemetry.html) supplies the full filename. |
| Name disambiguation | **MIXED** | The main answer gets the target right. The spelling suggestion and closing question still introduce alternatives. |
| Repeatability | **OPEN** | The nine captures form one evidence set. Independent sessions have yet to be collected. |

## Compaction method

Use the query and its captured context as the unit of observation. Record each distinct finding once and attach the smallest set of screenshots that directly supports it. Keep the exact visible string, the independently verified source, and any unresolved condition distinct. Carousel views remain available as context and contribute zero additional trials.

The saved record supports targeted public discoverability and artifact attribution. The underlying retrieval trace, backend model version, and public-search mechanism remain open. The [controlled GPT and Gemini audit](../../protocol.md) addresses correction retention on synthetic traces under a different protocol.

## Source captures

The files were captured November 11, 2026, between 17:44:30 and 17:45:38 according to the image metadata. The metadata carries no time-zone offset. The screenshots show private browsing and the initial search view offers a sign-in button.

| Original screenshot | Evidence |
| --- | --- |
| [IMG_9503.png](../../../../evidence/assets/peaice-thinking-machine-2026-11-11/IMG_9503.png) | Query, AI Overview, AIce spelling suggestion, and GitHub search result |
| [IMG_9504.png](../../../../evidence/assets/peaice-thinking-machine-2026-11-11/IMG_9504.png) | Expanded answer, exact source path, and partial mirror path |
| [IMG_9505.png](../../../../evidence/assets/peaice-thinking-machine-2026-11-11/IMG_9505.png) | Alternatives list and closing question |
| [IMG_9506.jpeg](../../../../evidence/assets/peaice-thinking-machine-2026-11-11/IMG_9506.jpeg) | ByteByteGo source card |
| [IMG_9507.jpeg](../../../../evidence/assets/peaice-thinking-machine-2026-11-11/IMG_9507.jpeg) | Wikipedia source card for Thinking Machines Lab |
| [IMG_9508.jpeg](../../../../evidence/assets/peaice-thinking-machine-2026-11-11/IMG_9508.jpeg) | Built In source card for Thinking Machines Lab |
| [IMG_9509.jpeg](../../../../evidence/assets/peaice-thinking-machine-2026-11-11/IMG_9509.jpeg) | PAICE.work source card |
| [IMG_9510.jpeg](../../../../evidence/assets/peaice-thinking-machine-2026-11-11/IMG_9510.jpeg) | EEv4 GitHub source card |
| [IMG_9511.jpeg](../../../../evidence/assets/peaice-thinking-machine-2026-11-11/IMG_9511.jpeg) | Google card for the book about Jensen Huang |

[Machine-readable evidence record](record.json) · [Original image checksums](../../../../evidence/assets/peaice-thinking-machine-2026-11-11/SHA256SUMS) · [Replay protocol](replay-protocol.md)
