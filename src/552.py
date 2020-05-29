"""
Easy, Wayfair

You are given a 2 x N board, and instructed to completely cover the board with
the following shapes:

* Dominoes, or 2 x 1 rectangles.
* Trominoes, or L-shapes.

For example, if N = 4, here is one possible configuration, where A is a domino,
and B and C are trominoes.

```
A B B C
A B C C
```

Given an integer N, determine in how many ways this task is possible.
"""


def num_configs(n: int) -> int:
    """We are given a 2 x N board. This problem is mostly about figuring out
    the possible cases for laying out the shapes. Here are the possible cases:

    * Place a domino vertically
    * Place two dominos horizontal on top of each other
    * two trominos interlocking

    We can solve this problem by handling state transitions as we iterate from
    0 to `n`. We just record the state of the last column, noting which bits
    were filled.

    The last column can have several states, which can lead to the following
    situations:

    * no rows filled (0, 0b11)
        * nothing
        * both rows filled + vertical domino
    * top row filled (1, 0b01)
        * 0 rows filled and a tromino
        * bottom row filled and a horizontal domino
    * bottom row filled (2, 0b10)
        * 0 rows filled and a tromino
        * top row filled and a horizontal domino
    * both rows filled (3, 0b11)
        * two trominos
        * 0 rows filled and two dominos

    param n: The length of the 2 x n board
    returns: The number of possible configurations for the triominos
    """
    # The base case
    if n <= 0:
        return 0

    # There's only one way to get the the starting state, which is 0 rows
    # filled. We record the number of ways to get to each scenario, defined
    # out in the comments, in this array.
    last_state = [1, 0, 0, 0]

    for _ in range(n):
        next_state = [0, 0, 0, 0]
        next_state[0b00] = last_state[0b00] + last_state[0b11]
        next_state[0b01] = last_state[0b00] + last_state[0b10]
        next_state[0b10] = last_state[0b00] + last_state[0b01]
        next_state[0b11] = (
            last_state[0b00] + last_state[0b01] + last_state[0b10]
        )
        last_state = next_state
    return last_state[0]


def test_num_configs():
    assert num_configs(3) == 5
