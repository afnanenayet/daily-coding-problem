"""
The Tower of Hanoi is a puzzle game with three rods and n disks, each a
different size.

All the disks start off on the first rod in a stack. They are ordered by size,
with the largest disk on the bottom and the smallest one at the top.

The goal of this puzzle is to move all the disks from the first rod to the last
rod while following these rules:

You can only move one disk at a time.
A move consists of taking the uppermost disk from one of the stacks and placing
it on top of another stack.
You cannot place a larger disk on top of a smaller disk.
Write a function that prints out all the steps necessary to complete the Tower
of Hanoi. You should assume that the rods are numbered, with the first rod
being 1, the second (auxiliary) rod being 2, and the last (goal) rod being 3.

For example, with n = 3, we can do this in 7 moves:

Move 1 to 3
Move 1 to 2
Move 3 to 2
Move 1 to 3
Move 2 to 1
Move 2 to 3
Move 1 to 3
"""

from typing import List, NamedTuple


class Move(NamedTuple):
    """Represents a move in the towers of hanoi game
    """

    src: int  # The source rod
    dest: int  # The destination rod


def towers_of_hanoi(n: int) -> List[Move]:
    """This is a classic CS problem that's often used as an introduction to
    recursion.
    """
    return towers_helper(n, 1, 3, 2)


def towers_helper(n: int, src: int, dest: int, using: int) -> List[Move]:
    """A recursive helper method for the towers of hanoi problem

    The general template for the ToH problem is to move the largest piece to the
    destination rod using the other tower as the intermediary.
    """
    res: List[Move] = []

    if n == 0:
        return res
    res.extend(towers_helper(n - 1, src, using, dest))
    res.append(Move(src, dest))
    res.extend(towers_helper(n - 1, using, dest, src))
    return res


def test_towers_of_hanoi():
    expected = [
        Move(1, 3),
        Move(1, 2),
        Move(3, 2),
        Move(1, 3),
        Move(2, 1),
        Move(2, 3),
        Move(1, 3),
    ]
    assert towers_of_hanoi(3) == expected
