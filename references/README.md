# Paper references

This surface registers the seven supplied EEV4 papers and chapters as evidence with typed
roles. It distinguishes an external result from the use EEV4 makes of that result.

The machine-readable source is
[`registry/paper-references.json`](../registry/paper-references.json). Each record carries the
provided PDF name, page count, and SHA-256 fingerprint. The PDFs are not vendored; the
primary arXiv, DOI, or ChaosBook locator remains the public access path.

## Role map

| Key | Domain | EEV4 role | Status |
|---|---|---|---|
| P1 | Restriction / decoupling | Bound-producing dependency tower | `THEOREM-BACKGROUND` |
| P2 | Hilbert-Schmidt determinant moments | Bounded comparative operator example | `STRUCTURAL-ANALOGY` |
| P3 | Kakeya in `R^3` | Full-dimension theorem background | `THEOREM-BACKGROUND` |
| P4 | Inertial proximal optimization | Controlled inertial-dynamics background | `KNOWN` |
| P5 | Krein spectral shift | Rank-one perturbation background | `KNOWN` |
| P6 | Kakeya in `R^3` | Streamlined theorem-background presentation | `THEOREM-BACKGROUND` |
| P7 | Spectral determinants | Trace / determinant / evolution-operator background | `KNOWN` |

No entry changes the program seals: RH is `OPEN`, the Coleman Conjecture is `OPEN`, and the
faithful exact bridge is `OPEN`. All seven records have `bridge_effect = does-not-close`.

## Citations and use boundaries

### P1 — Wang–Wu: restriction via decoupling

Hong Wang and Shukun Wu, “Restriction estimates using decoupling theorems and two-ends
Furstenberg inequalities,” arXiv:2411.08871v3 (2024).
[Primary record](https://arxiv.org/abs/2411.08871)

EEV4 use: theorem background for the geometric-to-analytic part of the dependency tower.
The paper proves a restriction estimate in `R^3`; it does not provide exact Riemann zero
placement or a Kakeya-to-Riemann carrier.

### P2 — Slater: Hilbert-Schmidt determinant moments

Paul B. Slater, “Hilbert-Schmidt Orthogonality of det(ρ) and det(ρPT) over the Two-Rebit
Systems ρ and Further Determinantal Moment Analyses,” arXiv:1007.4805v4 (2010).
[Primary record](https://arxiv.org/abs/1007.4805)

EEV4 use: a domain-bounded comparative example. It is not a general Hilbert-Schmidt theorem,
a Kakeya result, or evidence for an exact Xi-realizing operator.

### P3 — Wang–Zahl: Kakeya in three dimensions

Hong Wang and Joshua Zahl, “Volume estimates for unions of convex sets, and the Kakeya set
conjecture in three dimensions,” arXiv:2502.17655v1 (2025).
[Primary record](https://arxiv.org/abs/2502.17655)

EEV4 use: primary theorem background for full Minkowski and Hausdorff dimension of Kakeya
sets in `R^3`. The result does not by itself prove RH.

### P4 — Ochs–Chen–Brox–Pock: iPiano

Peter Ochs, Yunjin Chen, Thomas Brox, and Thomas Pock, “iPiano: Inertial Proximal Algorithm
for Nonconvex Optimization,” *SIAM Journal on Imaging Sciences* 7(2) (2014), 1388–1419.
[DOI record](https://epubs.siam.org/doi/10.1137/130942954)

EEV4 use: external grounding for controlled inertial dynamics. EEV4 `beta_continuity` is a
governance quantity, not iPiano’s momentum parameter; the citation does not validate EEV4
factors or bridge claims.

### P5 — Poltoratski: Krein spectral shift

Alexei G. Poltoratski, “The Krein spectral shift and rank one perturbations of spectra,”
arXiv:math/9601206v1 (1996).
[Primary record](https://arxiv.org/abs/math/9601206)

EEV4 use: operator-theoretic background for spectral shift and self-adjoint rank-one
perturbations. The paper does not supply the prime weights, Gamma-factor density, or exact
Xi-realizing carrier required by the live route.

### P6 — Guth–Wang–Zahl: streamlined Kakeya proof

Larry Guth, Hong Wang, and Joshua Zahl, “A streamlined proof of the Kakeya set conjecture in
`R^3`,” arXiv:2601.14411v1 (2026).
[Primary record](https://arxiv.org/abs/2601.14411)

EEV4 use: a streamlined theorem-background presentation. It does not close RH, the Coleman
Conjecture, or the faithful kappa bridge.

### P7 — ChaosBook: spectral determinants

Predrag Cvitanović, Roberto Artuso, Ronnie Mainieri, Gregor Tanner, Gábor Vattay, Niall
Whelan, and Andreas Wirzba, “Spectral determinants,” Chapter 19 in *Chaos: Classical and
Quantum*, version 14 (2012).
[Primary chapter](https://chaosbook.org/version14/chapters/det.pdf) ·
[Version 14 contents and credits](https://chaosbook.org/version14/paper.shtml)

EEV4 use: background for trace formulas, spectral determinants, dynamical zeta functions,
and evolution-operator spectra. It supplies vocabulary and examples, not an EEV4 operator
realization or a proof that a proposed determinant equals Xi.

## Evidence rule

When a reference is cited in an EEV4 claim:

1. cite the stable P-key and primary locator;
2. preserve its `reference_status`;
3. state the EEV4 use separately from the paper’s result;
4. carry the `claim_boundary` into any bridge-facing discussion;
5. never convert paper presence, citation count, or model agreement into closure.
