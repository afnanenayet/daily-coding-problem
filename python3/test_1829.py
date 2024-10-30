from solution_1829 import optimal_start_letters

import pytest


@pytest.mark.parametrize(
    ("dictionary", "expected"),
    [
        (
            ["cat", "calf", "dog", "bear"],
            {"b", "cal"},
        ),
        (
            ["bear", "moir", "moire", "muse", "must", "more"],
            {"b", "mu", "mor"},
        ),
    ],
)
def test_optimal_start_letters(dictionary: list[str], expected: set[str]) -> None:
    actual = optimal_start_letters(dictionary)
    assert actual == expected
