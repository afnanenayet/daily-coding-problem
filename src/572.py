"""
Given a number represented by a list of digits, find the next greater 
permutation of a number, in terms of lexicographic ordering. If there is not 
greater permutation possible, return the permutation with the lowest 
value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should 
return [2,1,3]. The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding 
the input memory)?
"""

from typing import List, NamedTuple


def next_permutation(nums: List[int]) -> List[int]:
    """Return the next greater permutation of a given number

    We can figure out which digit we want to switch by finding the first index where the ith element
    is less than the i + 1th element.

    Ex: in [1, 2, 3], 2 < 3, so we want to switch 2. In [1, 3, 2], 1 < 3 so we want to switch 1.

    Once we know which digit we want to switch, we swap it with the smallest element that's greater
    than it on the right side of the array. In both of the aforementioned examples, that element is
    2.
    """
    min_idx = len(nums) - 1
    curr_min = float("inf")
    digit_to_switch = -1

    # Figure out which digit we need to switch by finding the first number such that perm[i] <
    # perm[i + 1]
    for i in reversed(range(len(nums) - 1)):
        if nums[i] < nums[i + 1]:
            digit_to_switch = i
            break

    # Corner case: digits are in descending order, which means it's at the lexicographical max,
    # return the sorted list.
    if digit_to_switch == -1:
        return sorted(nums)

    # Find the smallest number greater than the digit to switch on the rigth side
    for i in reversed(range(digit_to_switch + 1, len(nums))):
        if nums[i] > nums[digit_to_switch] and nums[i] < curr_min:
            curr_min = nums[i]
            min_idx = i

    nums[digit_to_switch], nums[min_idx] = (
        nums[min_idx],
        nums[digit_to_switch],
    )

    # Because the digit we switch is the first element we found that is less than the elemnt fo the
    # right, we know that every element to the right of that is sorted in descending order. To get
    # the next permutation, we simply need to reverse all of the elements to the right of
    # `digit_to_switch` so we can get the smallest permutation given the prefix
    # permutation[0..digit_to_switch] (we want the next permutation, not just any permutation that's
    # higher than the given one).
    low = digit_to_switch + 1
    high = len(nums) - 1

    # We can easily reverse the list in-place using two pointers
    while low < high:
        nums[low], nums[high] = nums[high], nums[low]
        low += 1
        high -= 1
    return nums


def test_next_permutation():
    class TestCase(NamedTuple):
        permutation: List[int]
        expected: List[int]

    test_cases: List[TestCase] = [
        TestCase([1, 2, 3], [1, 3, 2]),
        TestCase([1, 3, 2], [2, 1, 3]),
        TestCase([3, 2, 1], [1, 2, 3]),
        TestCase([2, 3, 1], [3, 1, 2]),
        TestCase([2, 30, 1, 5], [2, 30, 5, 1]),
    ]

    for test_case in test_cases:
        assert next_permutation(test_case.permutation) == test_case.expected
