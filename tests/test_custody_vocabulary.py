from excellence_engine_v4 import HELD_STATES, PROGRAM_STATE, HeldState
from eev4.validation import HELD_STATES as VALIDATOR_HELD_STATES


EXPECTED_HELD_STATES = {
    "RECEIVED",
    "HELD-ACTIVE",
    "HELD-REVISED",
    "HELD-RETAINED",
    "HELD-RELEASED",
    "HELD-CLOSED",
}


def test_kernel_carries_complete_held_state_machine() -> None:
    assert set(HELD_STATES) == EXPECTED_HELD_STATES
    assert {state.value for state in HeldState} == EXPECTED_HELD_STATES


def test_validator_uses_kernel_custody_vocabulary() -> None:
    assert VALIDATOR_HELD_STATES is HELD_STATES


def test_program_state_uses_retained_substate() -> None:
    assert PROGRAM_STATE["K->R (frame)"]["status"] == HeldState.RETAINED.value
