from typing import Any

import pytest

from solution_1754 import all_strobo_nums, combinations_with_replacement


@pytest.mark.parametrize(
    ("xs", "size", "expected"),
    [
        (
            [1, 2],
            1,
            [
                (1,),
                (2,),
            ],
        ),
        (
            [1, 2, 3],
            2,
            [
                (1, 1),
                (1, 2),
                (1, 3),
                (2, 1),
                (2, 2),
                (2, 3),
                (3, 1),
                (3, 2),
                (3, 3),
            ],
        ),
    ],
)
def test_combinations_with_replacement(
    xs: list[Any], size: int, expected: list[list[Any]]
) -> None:
    combos = combinations_with_replacement(xs, size)
    actual = set([tuple(x) for x in combos])
    assert actual == set(expected)


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (
            1,
            [(1,), (6,), (8,), (9,)],
        ),
        (
            2,
            [
                (
                    1,
                    1,
                ),
                (8, 8),
                (6, 9),
                (9, 6),
            ],
        ),
    ],
)
def test_another_way(n: int, expected: list[tuple[int]]) -> None:
    actual = set([tuple(x) for x in all_strobo_nums(n)])
    expected_ = set(expected)
    assert actual == expected_
