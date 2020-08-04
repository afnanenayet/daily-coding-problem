"""
Amazon, medium

Given an array of numbers, find the maximum sum of any contiguous subarray of
the array.

It is possible for the maximum sum in an array of negative elements to be zero,
since a subarray of size zero is a valid subarray.
"""

from typing import List
from collections import namedtuple


def max_subarray(a: List[int]) -> int:
    """The naive way to solve this problem would be to iterate over every 
    possible subset of of the array and take their sums, recording the running
    maximum and returning that. That method is horribly inefficient at O(2^n).

    There is a way to do this in linear time. First, we need to keep in mind
    that the subarray has to be contiguous. This means that we can keep a
    sliding window as we iterate through the array. We just want to keep track
    of points where the subarray is negative, and make sure we cut those
    subarrays out if they bring the sum of the array down. We can achieve this
    by keeping track of the rolling sum, and noting the minimum sum at any given
    point, and subtracting that if its less than 0, then keeping track of every
    potential maximum sum.

    Let's look at the example input:
    [34, -50, 42, 14, -5, 86]

    The rolling sums as an array are:
    [34, -16, 26, 40, 35, 121]
           ^ min           ^ max

    If we take the subarray from [min + 1 : max], we can find the maximum
    possible sum. Obviously removing the minimum element below zero will yield
    the highest sum, because that is equivalent to adding the absolute value of
    the minimum, which is the maximum negative value we could subtract.

    This is O(n) time and O(1) space
    """
    current_min = 0
    current_sum = 0
    max_sum = 0

    for elem in a:
        current_sum += elem
        current_min = min(current_min, current_sum)
        # We don't want to subtract if the current minimum is positive, since
        # that will lower the max sum. If the current minimum is negative, then
        # excluding that subarray will yield a higher max sum.
        max_sum = max(max_sum, current_sum - min(0, current_min))
    return max_sum


def test_max_subarray():
    TestCase = namedtuple("TestCase", ["input", "expected"])
    test_cases = [
        TestCase([34, -50, 42, 14, -5, 86], 137),
        TestCase([-5, -1, -8, -9], 0),
    ]

    for test_case in test_cases:
        assert max_subarray(test_case.input) == test_case.expected
