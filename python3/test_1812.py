from contextlib import AbstractContextManager, nullcontext as does_not_raise
from typing import cast

import pytest

from solution_1812 import Graph, divide_teams


@pytest.mark.parametrize(
    ("input_graph", "expected", "raises"),
    [
        (
            {0: [3], 1: [2], 2: [1, 4], 3: [0, 4, 5], 4: [2, 3], 5: [3]},
            ({0, 1, 4, 5}, {2, 3}),
            cast(AbstractContextManager[None], does_not_raise()),
        ),
        (
            {0: [3], 1: [2], 2: [1, 3, 4], 3: [0, 2, 4, 5], 4: [2, 3], 5: [3]},
            (set(), set()),
            cast(AbstractContextManager[None], pytest.raises(ValueError)),
        ),
    ],
)
def test_divide_teams(
    input_graph: Graph,
    expected: tuple[set[int], set[int]],
    raises: AbstractContextManager[None],
) -> None:
    with raises:
        actual = divide_teams(input_graph)
        assert actual == expected
