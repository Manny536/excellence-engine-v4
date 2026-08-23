# Multiscale topology and formalization sources

This surface records topology and Mathlib sources for
`PEAICE-EEV4-MULTISCALE-COMPACTNESS-GATE-001`. These references provide background and formal
interfaces. Their presence does not establish the proposed KakeyaLogic instantiation.

## MAT327 topology sources

- [Official MAT327 course index](https://www.math.toronto.edu/ivan/mat327/)
- [Nets and filters](https://www.math.toronto.edu/ivan/mat327/docs/other/nets.pdf)
- [Finite products](https://www.math.toronto.edu/ivan/mat327/docs/notes/08-products.pdf)
- [Compactness](https://www.math.toronto.edu/ivan/mat327/docs/notes/16-compact.pdf)
- [Tychonoff and compactness](https://www.math.toronto.edu/ivan/mat327/docs/notes/17-tychonoff.pdf)

EEV4 use: `KNOWN` background for directed sets, product-directed indexing, nets, subnets, and
compactness. The sources do not define the EEV4 configuration carrier or prove preservation of
Kakeya observables.

## Mathlib interfaces

- [Compactness API](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Compactness/Compact.html)
- [Filter and topology definitions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Defs/Filter.html)
- [`atTop` and `atBot`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/Filter/AtTopBot/Basic.html)

EEV4 use: formalization targets for `Filter.atTop`, cluster points, compactness, and product
carriers. Exact declarations remain `PLANNED / NOT COMPILED` until checked against the active
Mathlib revision.

## Claim boundary

These sources support the abstract mathematical vocabulary only. They do not establish:

- compactness of the proposed measure-valued KakeyaLogic carrier;
- survival of direction coverage, shading density, incidence, union measure, or dimension;
- an analytic interpretation of framework `L²_C`;
- an interpretability improvement;
- RH, Coleman, or a faithful κ bridge.
