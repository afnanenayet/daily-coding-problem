"""
Facebook, medium

Given an array of integers, write a function to determine whether the array
could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can
modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any
one element to get a non-decreasing array.
"""

from typing import List, Optional
from collections import namedtuple


def non_decreasing(A: List[int]) -> bool:
    """We can solve this linearly by checking the ordering of the array. In 
    order for this method to return true, at any given moment, we can have at
    most one instance where A[i - 1] > A[i], so we check for that condition.
    We set a flag when this condition is tripped, so if it happens again,
    we can bail and return false.
    """
    # Base case: an empty array or an array of length 1 is non-decreasing and
    # doesn't need any changes
    if not A or len(A) <= 1:
        return True

    # Indicates if the ordering has been broken sof ar
    ordering_broken = False

    for i in range(1, len(A)):
        # Check if ordering has been broken
        if A[i - 1] > A[i]:
            # If `skip_idx` was already set, that means that ordering was
            # broken before, which breaks the condition, so we return false.
            if ordering_broken:
                return False
            # Otherwise, we note that we need to skip the element that breaks
            # the ordering
            ordering_broken = True
    return True


def test_non_decreasing():
    TestCase = namedtuple("TestCase", ["array", "expected"])
    test_cases = [
        TestCase([1, 2, 3], True),
        TestCase([10, 5, 7, 8, 9], True),
        TestCase([5, 7, 99, 8, 9], True),
        TestCase([10, 5, 1], False),
    ]

    for test_case in test_cases:
        assert non_decreasing(test_case.array) == test_case.expected
