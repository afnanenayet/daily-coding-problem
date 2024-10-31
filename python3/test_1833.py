import pytest

from solution_1833 import solve_array, verify_array_constraints


@pytest.mark.parametrize("constraints", [[None, "+", "+", "-", "+"]])
def test_solve_array(constraints: list[str | None]) -> None:
    res = solve_array(constraints)
    verify_array_constraints(res, constraints)
