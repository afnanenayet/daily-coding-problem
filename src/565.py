"""
Givena n integer list where each number represents the number of hops you can
make, determine whether you can reach the last index starting at index 0.

Example:

```
[2, 0, 1, 0] -> True
[1, 1, 0, 1] -> False
```
"""

from typing import List
from collections import namedtuple


def valid_hops(A: List[int]) -> bool:
    """We can solve this in O(n) time and O(1) space by simply traversing the
    array and accumulating hops as we see them. We also have to remove a hop for
    every traversal we do. We keep moving until we run out of hops or we reach
    the end.
    """
    # The base case is that you have an empty list, which means you don't have
    # to traverse to any location, which means you've already reached the last
    # index. Same applies if the length of the array is 1.
    if not A or len(A) == 1:
        return True

    hops_remaining = A[0]
    idx = 1

    # Keep accumulating hops for as long as possible, until we reach the end
    while hops_remaining > 0 and idx < len(A):
        # Remove one to account for the hop we just consumed
        hops_remaining += A[idx] - 1
        idx += 1

    # If we reached the end, then this was a success. Otherwise it is not
    # possible to reach the end.
    return idx == len(A)


def test_valid_hops():
    TestCase = namedtuple("TestCase", ["array", "expected"])

    test_cases = [
        TestCase([2, 0, 1, 0], True),
        TestCase([1, 1, 0, 1], False),
        TestCase([], True),
        TestCase([0], True),
    ]

    for test_case in test_cases:
        assert valid_hops(test_case.array) == test_case.expected
