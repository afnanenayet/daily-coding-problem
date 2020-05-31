"""
Amazon, medium

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than
linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4
(the index of 8 in the array).

You can assume all the integers in the array are unique.
"""

from typing import List
from collections import namedtuple


def rotated_array(A: List[int], x: int) -> int:
    """We can use a binary search to get the time less than O(n). Instead of
    looking for a particular element, we are going search for an index `i` such
    that A[i - 1] > A[i] to find the actual starting index of the array.

    Once we have the actual starting point of the array, we can break it into
    two halves. Each half of the array is ascending within some range, and we
    can use a simple comparison to check which half to search for `x`. We then
    perform another binary search in that range.

    If we don't find anything, that means the array was rotated 0 times.

    param A: The array to search
    param x: The element to find
    returns: The index of the element in the array
    """
    left = 0
    right = len(A) - 1

    def find_start_idx() -> int:
        """Find the starting index of the array given that there's some 
        arbitrary rotation.
        """
        left = 0
        right = len(A) - 1

        # Find the starting index of the array
        while left < right:
            mid = (left + right) // 2

            if A[mid - 1] > A[mid]:
                return mid
            elif A[mid] > A[-1]:
                left = mid
            else:
                right = mid
        return 0

    def binary_search(left: int, right: int) -> int:
        while left < right:
            mid = (left + right) // 2

            if A[mid] == x:
                return mid
            elif A[mid] < x:
                left = mid
            else:
                right = mid
        return -1

    start_idx = find_start_idx()

    # Check which half `x` is in, then set the left and right bounds for the
    # search
    if A[start_idx] <= x <= A[-1]:
        left = start_idx
        right = len(A) - 1
    else:
        left = 0
        right = start_idx
    return binary_search(left, right)


def test_rotated_array():
    TestCase = namedtuple("TestCase", ["array", "x", "expected"])
    test_cases = [
        TestCase([13, 18, 25, 2, 8, 10], 8, 4),
        TestCase([0, 1, 2, 3, 4, 5], 2, 2),
    ]

    for test_case in test_cases:
        assert rotated_array(test_case.array, test_case.x) == test_case.expected
