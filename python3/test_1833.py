from hypothesis import given
from hypothesis.strategies import text
import pytest

from solution_1833 import solve_array, verify_array_constraints


@pytest.mark.parametrize(
    "constraints",
    (
        [None, "+", "+", "-", "+"],
        [None, "-", "+"],
    ),
)
def test_solve_array(constraints: list[str | None]) -> None:
    res = solve_array(constraints)
    verify_array_constraints(res, constraints)


@given(text(alphabet=("+", "-")))
def test_solve_array_fuzzed(given_text: str) -> None:
    constraints: list[str | None] = [None]
    constraints.extend([x for x in given_text])
    res = solve_array(constraints)
    verify_array_constraints(res, constraints)
