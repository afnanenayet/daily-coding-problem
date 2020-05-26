"""
Hard, Google

Given an array of integers where every integer occurs three times except for
one integer, which only occurs once, find and return the non-duplicated
integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13],
return 19.

Do this in O(N) time and O(1) space.
"""

from typing import List
from collections import namedtuple


def find_integer(A: List[int]) -> int:
    # The bits that appear for count % 3 == 0
    ones = 0

    # The bits that appear for (count % 3 == 0) + 1
    twos = 0

    for i in A:
        twos |= ones & i
        ones ^= i
        threes_mask = ~(ones & twos)
        ones &= threes_mask
        twos &= threes_mask
    return ones


def test_find_integer():
    TestCase = namedtuple("TestCase", ["input", "expected"])
    test_cases = [
        TestCase([6, 1, 3, 3, 3, 6, 6], 1),
        TestCase([13, 19, 13, 13], 19),
    ]

    for test_case in test_cases:
        assert find_integer(test_case.input) == test_case.expected
