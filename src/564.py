"""
Given a list of integers, write a function that returns the largest sum of
non-adjacent numbers. Numbers can be 0 or negative.

Example:

```
[2, 4, 6, 2, 5] -> 13

[5, 1, 1, 5] -> 10
```
"""

from typing import List
from collections import namedtuple


def non_adj_max_sum(A: List[int]) -> int:
    """We are going to divide this problem into subproblems. Let us iterate
    through the array. Let us define the maximum non-adjacent sum of the
    subarray `A[0..i]` as `max[i]`. The maximum for any subarray `A[0..i]` is
    `max(max[i - 2], A[i], A[i] + max[i - 2])`.
    """
    if not A:
        raise ValueError("The input array must not be empty")

    maxes = [0 for _ in A]

    # Base case: the maximum sum for an array with one element is just the value
    # of that element or 0, whichever is higher
    maxes[0] = max(A[0], 0)

    # Iterate through the array, recording the current max as the maximum of:
    # - the maximum value of A[0..i - 1]
    # - the maximum value of A[0..i - 2] + A[i]
    # - A[i]
    for i in range(1, len(A)):
        elem = A[i]

        if i < 2:
            maxes[i] = max(maxes[i - 1], elem)
        else:
            maxes[i] = max(maxes[i - 2] + elem, elem, maxes[i - 1])
    return maxes[-1]


def test_non_adj_max_sum():
    TestCase = namedtuple("TestCase", ["array", "expected"])

    test_cases = [
        TestCase([2, 4, 6, 2, 5], 13),
        TestCase([5, 1, 1, 5], 10),
    ]

    for test_case in test_cases:
        assert non_adj_max_sum(test_case.array) == test_case.expected
