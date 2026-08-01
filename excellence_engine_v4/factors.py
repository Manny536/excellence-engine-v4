"""Factor definitions for the Excellence and Integrity equations.

    E = L^2 * beta * C * P          (excellence)
    R = d * c * e * h               (integrity), with h < 1

STATUS OF THIS MODULE
---------------------
- The functional FORM of both equations is FORMAL (framework canon).
- The concrete operationalisation of each factor below is PROPOSED: a faithful,
  bounded, auditable *default*. Ratify, tune, or replace any of them. Slots
  whose canonical meaning is not on the record are flagged in-line with the tag
  "SLOT NOT ON RECORD".

Every factor returns a value in [0, 1] (h in [0, 1)). Out-of-range input raises,
rather than being silently clamped: garbage in is rejected, not absorbed.
"""
from __future__ import annotations

from statistics import mean
from typing import Sequence

from .status import ClaimLedger, Status
from .firewall import require_h_below_one

# The operationalisations in this module are, collectively, PROPOSED.
FACTOR_STATUS: Status = Status.PROPOSED


def _unit(x: float, name: str) -> float:
    if not (0.0 <= x <= 1.0):
        raise ValueError(f"{name} must lie in [0, 1]; got {x}")
    return float(x)


# ---- E-side ----------------------------------------------------------------

def L2(agreements: Sequence[float]) -> float:
    """L^2 - Love-Squared *Coherence* scoring factor.

    FENCE: this is the engine's bounded coherence *score*, NOT the L^2_C operator
    from the research layer. That object survives only as ANALOGY and is not
    imported here.

    PROPOSED operationalisation: the square of mean pairwise agreement across the
    signal / model stack. Perfect agreement -> 1; the square rewards concentrated
    agreement over merely-average agreement. Empty input -> 0.
    """
    if not agreements:
        return 0.0
    m = _unit(mean(_unit(a, "agreement") for a in agreements), "mean agreement")
    return m * m


def beta(ledger: ClaimLedger) -> float:
    """beta - beta-Protocol integrity factor.

    PROPOSED operationalisation: the share of ledger weight that is correctly
    typed and NOT overclaimed. Overclaiming (asserting a claim above its true
    status) removes that weight from the numerator. Empty ledger -> 0.
    """
    tw = ledger.total_weight
    if tw <= 0:
        return 0.0
    good = tw - ledger.overclaimed_weight
    return _unit(good / tw, "beta")


def C(contradiction_rate: float) -> float:
    """C - structural / logical Coherence of the claim set.

    SLOT DISAMBIGUATION: L^2 is Love-Squared Coherence; C is read here
    provisionally as *logical* coherence - freedom from holding A and not-A both
    FORMAL. Confirm the C-vs-L^2 split, or merge the two.

    PROPOSED operationalisation: C = 1 - contradiction_rate, with
    contradiction_rate in [0, 1] (the weighted fraction of the claim graph in
    direct contradiction).
    """
    return 1.0 - _unit(contradiction_rate, "contradiction_rate")


def P(cup_pass_rate: float) -> float:
    """P - pressure-robustness (Coherence-Under-Pressure factor).

    SLOT NOT ON RECORD: 'P' is read provisionally as pressure-robustness and tied
    to the CUP protocol. Confirm or replace.

    PROPOSED operationalisation: P = CUP pass-rate, the fraction of claims that
    survive adversarial probing under Coherence-Under-Pressure. Range [0, 1].
    """
    return _unit(cup_pass_rate, "cup_pass_rate")


def excellence(l2: float, b: float, c: float, p: float) -> float:
    """E = L^2 * beta * C * P.

    A product of four bounded factors, so E in [0, 1]. Any single factor at 0
    zeroes E - excellence is conjunctive, not additive.
    """
    return _unit(l2, "L2") * _unit(b, "beta") * _unit(c, "C") * _unit(p, "P")


# ---- R-side (integrity) ----------------------------------------------------

def integrity(d: float, c: float, e: float, h: float) -> float:
    """R = d * c * e * h, with h < 1 enforced (FLAG-001).

    Because 0 <= h < 1 and d, c, e in [0, 1], R is strictly < 1: integrity can
    approach but never certify to certainty. That strict ceiling is the FORMAL
    consequence of evaluator non-sovereignty - it is not an assumption, it falls
    out of h < 1.

    SLOT NOT ON RECORD: d, c, e are R-slots whose canonical expansions are not on
    the record here. Provisionally: derivation-validity (d), internal-consistency
    (c), evidential-support (e). PROPOSED - ratify or replace.
    """
    d = _unit(d, "d")
    c = _unit(c, "c")
    e = _unit(e, "e")
    h = require_h_below_one(h)
    return d * c * e * h
