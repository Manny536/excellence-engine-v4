# h notation and legacy score semantics

**ID:** EEV4-H-SEMANTICS-001 · **Status:** OPEN SEMANTIC OBLIGATION

[L2C-H-001](https://github.com/Manny536/love2-coherence-core/blob/research/gius-hf-2026/docs/evaluator-non-sovereignty.md) reserves h_eval for evaluator-sovereignty load. It is not Hamiltonian leakage ℓ_H, and no scalar calibration is validated.

The existing API computes `R = d*c*e*h`. For fixed positive d,c,e, increasing its legacy h input increases R. If that input were sovereignty load, higher load would increase a quantity called integrity. The semantics therefore cannot be identified without further work. `R < 1` is a bounded arithmetic result; it does not establish operational evaluator non-sovereignty.

Keep the legacy formula, input name and numeric behavior for compatibility. Treat its h as a legacy uncalibrated score factor, not a measurement of h_eval or a certificate. No `1-h` transformation is silently substituted. Legacy artifacts using h for leakage or plotting arbitrary h values do not provide calibrated authority evidence; see [KakeyaLogic migration](https://github.com/Manny536/kakeyalogic/blob/research/gius-hf-2026/docs/h-notation.md).

Resolution requires a versioned metric definition, direction/units, calibrated observations, monotonicity controls and independent review. Until then EEV4-SIUS-EVAL-001 uses explicit authority/correction evidence, not R, to test the non-sovereignty obligation. Operational validity remains OPEN.
