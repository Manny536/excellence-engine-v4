"""beta-Protocol claim status typing for Excellence Engine v4.

Every claim the engine carries MUST be typed with one of the five admissible
statuses below. This is PeAIce canon: a claim's status is how honesty is
transported through the machinery, and elevating a claim above its true status
(overclaiming) is the thing the integrity factor is built to penalise.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Status(str, Enum):
    """The five beta-Protocol statuses."""

    FORMAL = "FORMAL"                     # proven to the framework's standard
    PROPOSED = "PROPOSED"                 # constructed; awaiting ratification / cross-derivation
    OPEN = "OPEN"                         # unsettled; a live question
    ANALOGY = "ANALOGY"                   # illustrative only; NOT a mechanism claim
    CLOSED_NEGATIVE = "CLOSED-NEGATIVE"   # ruled out (e.g. a type error)


# Strength ordering. Used only to detect overclaiming: asserting a claim at a
# rank above its true rank is an integrity penalty. Underclaiming is not.
_RANK: dict["Status", int] = {
    Status.CLOSED_NEGATIVE: -1,
    Status.ANALOGY: 0,
    Status.OPEN: 1,
    Status.PROPOSED: 2,
    Status.FORMAL: 3,
}


@dataclass(frozen=True)
class Claim:
    """A single typed claim.

    `asserted_as` records how the claim is *presented*. If that is stronger than
    the claim's true `status`, the claim is overclaimed and the gap is penalised
    by the beta factor.
    """

    id: str
    text: str
    status: Status
    weight: float = 1.0
    asserted_as: "Status | None" = None

    def __post_init__(self) -> None:
        if self.weight < 0:
            raise ValueError(f"claim {self.id!r}: weight must be >= 0, got {self.weight}")

    @property
    def is_overclaimed(self) -> bool:
        if self.asserted_as is None:
            return False
        return _RANK[self.asserted_as] > _RANK[self.status]


@dataclass
class ClaimLedger:
    """An ordered ledger of typed claims."""

    claims: list[Claim] = field(default_factory=list)

    def add(self, claim: Claim) -> "ClaimLedger":
        self.claims.append(claim)
        return self

    def by_status(self, status: Status) -> list[Claim]:
        return [c for c in self.claims if c.status is status]

    @property
    def total_weight(self) -> float:
        return sum(c.weight for c in self.claims)

    @property
    def overclaimed_weight(self) -> float:
        return sum(c.weight for c in self.claims if c.is_overclaimed)

    def counts(self) -> dict[str, int]:
        out: dict[str, int] = {s.value: 0 for s in Status}
        for c in self.claims:
            out[c.status.value] += 1
        return out
