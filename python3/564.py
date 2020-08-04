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
from collections import namedtuple, deque


def non_adj_max_sum(A: List[int]) -> int:
    """We are going to divide this problem into subproblems. Let us iterate
    through the array. Let us define the maximum non-adjacent sum of the
    subarray `A[0..i]` as `max[i]`. The maximum for any subarray `A[0..i]` is
    `max(max[i - 2], A[i], A[i] + max[i - 2])`.

    This is O(n) time and O(1) space.
    """
    if not A:
        raise ValueError("The input array must not be empty")

    # Base case: the maximum sum for the array at the beginning is 0. The
    # `maxes` deque holds the maximum for A[0..i - 1] and A[0..i] at any given
    # iteration of the loop, which makes this constant space. The key insight
    # here is that we only need to record the max of A[0..i-2] and A[0..i-1] at
    # any given iteration.
    maxes = deque([0, 0])

    # Iterate through the array, recording the current max as the maximum of:
    # - the maximum value of A[0..i - 1]
    # - the maximum value of A[0..i - 2] + A[i]
    # - A[i]
    for elem in A:
        current_max = max(maxes[0] + elem, maxes[1], elem)

        # Popping and appending is O(1) since `deque` is implemented as a linked
        # list under the hood
        maxes.popleft()
        maxes.append(current_max)

    # At the very end, maxes is [max[0..n - 1], max[0..n]], so we return the
    # last element in the deque to get our answer.
    return maxes[-1]


def test_non_adj_max_sum():
    TestCase = namedtuple("TestCase", ["array", "expected"])

    test_cases = [
        TestCase([2, 4, 6, 2, 5], 13),
        TestCase([5, 1, 1, 5], 10),
        TestCase([-1, -2, -3, -4], 0),
    ]

    for test_case in test_cases:
        assert non_adj_max_sum(test_case.array) == test_case.expected
