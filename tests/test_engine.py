"""Test suite for Excellence Engine v4.

Covers the FORMAL spine: equation values, the h < 1 ceiling and its consequence
(R strictly < 1), the three firewall guards, overclaim detection, factor-bound
rejection, and stamp determinism.
"""
import math

import pytest

from excellence_engine_v4 import (
    ExcellenceEngine,
    EngineInput,
    Claim,
    ClaimLedger,
    Status,
    Quantity,
    Metric,
    Analogy,
    NP_ANALOGY,
    bind_domain_coordinate,
    require_h_below_one,
    FirewallError,
    UndefinedMetricError,
    NonSovereigntyError,
    factors as F,
)


# ---- equation values -------------------------------------------------------

def test_excellence_is_product_of_factors():
    assert F.excellence(0.5, 0.5, 0.5, 0.5) == pytest.approx(0.0625)


def test_excellence_is_conjunctive_any_zero_zeroes_it():
    assert F.excellence(0.0, 1.0, 1.0, 1.0) == 0.0
    assert F.excellence(1.0, 1.0, 1.0, 0.0) == 0.0


def test_L2_squares_mean_agreement():
    # mean agreement 0.8 -> 0.64
    assert F.L2([0.8, 0.8, 0.8]) == pytest.approx(0.64)


def test_L2_empty_is_zero():
    assert F.L2([]) == 0.0


def test_C_is_one_minus_contradiction():
    assert F.C(0.25) == pytest.approx(0.75)


# ---- h < 1 ceiling and the R < 1 consequence -------------------------------

def test_require_h_below_one_accepts_below_one():
    assert require_h_below_one(0.999) == pytest.approx(0.999)


@pytest.mark.parametrize("bad_h", [1.0, 1.0001, 2.0, -0.1])
def test_require_h_below_one_rejects_out_of_range(bad_h):
    with pytest.raises(NonSovereigntyError):
        require_h_below_one(bad_h)


def test_integrity_is_strictly_below_one_even_at_the_extreme():
    # d=c=e=1 and h just under 1 -> R just under 1, never 1.
    R = F.integrity(1.0, 1.0, 1.0, 0.999999)
    assert R < 1.0


@pytest.mark.parametrize("d,c,e,h", [
    (1.0, 1.0, 1.0, 0.99),
    (0.9, 0.8, 0.95, 0.5),
    (1.0, 1.0, 1.0, 0.0),
])
def test_R_below_one_property(d, c, e, h):
    assert F.integrity(d, c, e, h) < 1.0


# ---- factor bounds are enforced, not clamped -------------------------------

@pytest.mark.parametrize("bad", [-0.01, 1.01, 5.0])
def test_out_of_range_agreement_raises(bad):
    with pytest.raises(ValueError):
        F.L2([bad])


def test_out_of_range_integrity_factor_raises():
    with pytest.raises(ValueError):
        F.integrity(1.2, 1.0, 1.0, 0.5)


# ---- firewall: zeta(0) transport -------------------------------------------

def test_zeta0_transport_is_blocked():
    zeta0 = Quantity(value=-0.5, role="codomain_value", label="zeta(0)")
    with pytest.raises(FirewallError):
        bind_domain_coordinate(zeta0)


def test_a_real_domain_coordinate_binds_fine():
    coord = Quantity(value=0.5, role="domain_coordinate", label="Re(s)")
    assert bind_domain_coordinate(coord) == pytest.approx(0.5)


# ---- firewall: undefined headline metric -----------------------------------

def test_undefined_headline_metric_raises():
    with pytest.raises(UndefinedMetricError):
        Metric(value=0.94, counted="", population="runs", source="log")


def test_defined_headline_metric_ok():
    m = Metric(value=0.94, counted="passing probes",
               population="all CUP probes in run", source="cup_probe_log v4")
    assert m.value == pytest.approx(0.94)


# ---- firewall: NP framing is analogy only ----------------------------------

def test_np_framing_cannot_be_used_as_mechanism():
    with pytest.raises(FirewallError):
        NP_ANALOGY.as_mechanism()


def test_analogy_status_is_pinned():
    a = Analogy(name="white blood cell", maps_to="L^2_C (illustrative)")
    assert a.status is Status.ANALOGY


# ---- beta: overclaiming is penalised ---------------------------------------

def test_beta_is_one_when_nothing_overclaimed():
    led = ClaimLedger()
    led.add(Claim("k1", "completion identity", Status.FORMAL))
    led.add(Claim("k2", "RH", Status.OPEN))
    assert F.beta(led) == pytest.approx(1.0)


def test_beta_drops_when_a_claim_is_overclaimed():
    led = ClaimLedger()
    led.add(Claim("k1", "completion identity", Status.FORMAL, weight=1.0))
    led.add(Claim("k2", "RH", Status.OPEN, weight=1.0))
    # RH asserted as FORMAL though it is OPEN -> overclaim, weight 1 of 3 removed
    led.add(Claim("k3", "RH-asserted", Status.OPEN, weight=1.0,
                  asserted_as=Status.FORMAL))
    assert F.beta(led) == pytest.approx(2.0 / 3.0)


# ---- end-to-end score + stamp determinism ----------------------------------

def _sample_input(h=0.99):
    led = ClaimLedger()
    led.add(Claim("k1", "completion identity", Status.FORMAL))
    led.add(Claim("k2", "C_2 rate", Status.FORMAL))
    led.add(Claim("k3", "RH", Status.OPEN))
    return EngineInput(
        agreements=[0.9, 0.85, 0.95],
        ledger=led,
        contradiction_rate=0.0,
        cup_pass_rate=0.9,
        d=0.9, c=0.95, e=0.8, h=h,
    )


def test_score_runs_and_reports_R_below_one():
    rep = ExcellenceEngine().score(_sample_input())
    assert 0.0 <= rep.E <= 1.0
    assert rep.R < 1.0
    assert rep.R_below_one is True


def test_stamp_is_deterministic_for_identical_content():
    eng = ExcellenceEngine()
    a = eng.score(_sample_input())
    b = eng.score(_sample_input())
    assert a.stamp_sha256 == b.stamp_sha256


def test_stamp_changes_when_content_changes():
    eng = ExcellenceEngine()
    a = eng.score(_sample_input(h=0.99))
    b = eng.score(_sample_input(h=0.50))
    assert a.stamp_sha256 != b.stamp_sha256


def test_engine_rejects_h_at_one_end_to_end():
    with pytest.raises(NonSovereigntyError):
        ExcellenceEngine().score(_sample_input(h=1.0))


def test_program_state_keeps_rh_and_coleman_open():
    rep = ExcellenceEngine().score(_sample_input())
    assert rep.program_state["RH"]["status"] == "OPEN"
    assert rep.program_state["Coleman"]["status"] == "OPEN"
    assert rep.program_state["zeta(0) transport"]["status"] == "CLOSED-NEGATIVE"
