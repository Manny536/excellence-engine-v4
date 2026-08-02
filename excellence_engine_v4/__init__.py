"""Excellence Engine v4 (PeAIce - KakeyaLogic - L^2_C).

Shorthand: V4 = K->R . HELD
State: RH OPEN . Coleman Conjecture OPEN . h < 1

Public API is re-exported here so callers can:

    from excellence_engine_v4 import ExcellenceEngine, EngineInput, Claim, Status
"""
from __future__ import annotations

from .status import HELD_STATES, Claim, ClaimLedger, HeldState, Status
from .firewall import (
    FIREWALL_CANON,
    FirewallError,
    UndefinedMetricError,
    NonSovereigntyError,
    Quantity,
    Metric,
    Analogy,
    bind_domain_coordinate,
    require_h_below_one,
)
from . import factors
from .engine import (
    VERSION,
    PROGRAM_STATE,
    NP_ANALOGY,
    EngineInput,
    EngineReport,
    ExcellenceEngine,
)

__version__ = VERSION

__all__ = [
    "Status", "HeldState", "HELD_STATES", "Claim", "ClaimLedger",
    "FIREWALL_CANON", "FirewallError", "UndefinedMetricError",
    "NonSovereigntyError", "Quantity", "Metric", "Analogy",
    "bind_domain_coordinate", "require_h_below_one",
    "factors",
    "VERSION", "PROGRAM_STATE", "NP_ANALOGY",
    "EngineInput", "EngineReport", "ExcellenceEngine",
]
