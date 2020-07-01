"""
Given an array of integers, return a new array such that each element at index
`i` of the new array is the product of all the numbers in the original array 
except the one at `i`.
"""

from typing import List
from functools import reduce


def exclude_product(a: List[int]) -> List[int]:
    """Return the product of every element besides the index at `i` in a list
    `a`.

    We can do this in-place by keeping track of the right-to-left product in a
    variable and the left-to-right product in the original array
    """
    # We use the result array to also store the information for the products
    # from left to right. Before we start the second loop, res[i] is the product
    # of the elements in `a[:i]` (up to, but not including index i).
    res = [0 for _ in a]
    res[0] = 1
    rtl_product = 1

    for i in range(1, len(a)):
        res[i] = a[i - 1] * res[i - 1]

    # We then go through the second loop, using a variable to keep track of the
    # right to left product as we traverse the array, multiplying that with the
    # left to right product, so the result is the product of every element in
    # `a` excluding the index `i`.
    for i in reversed(range(len(a))):
        res[i] *= rtl_product
        rtl_product *= i
    return res


def all_but_i(a: List[int], i: int) -> int:
    """A utility function that takes the product of all elements in an array
    except for the element at index `i`.

    param a: The input list
    param i: The index of the element to exclude
    returns: The product of all of the elements in `a` except for `a[i]`
    """
    res = 1

    for j in range(len(a)):
        if j != i:
            res *= a[j]
    return res


def test_exclude_product():
    test_cases = [[0, 1, 2]]

    for test_case in test_cases:
        expected = [all_but_i(test_case, i) for i in range(len(test_case))]
        assert expected == exclude_product(test_case)
