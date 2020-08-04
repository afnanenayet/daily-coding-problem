"""
Google, easy


Given an array of numbers `A` and a number `k`, return whether there are two
numbers in the array `A` that add up to `k`.
"""


from typing import List


def add_to_k(A: List[int], k: int) -> bool:
    """We scan the array and add each element to the set. As we traverse the
    array, we record each element and check to see if the element's complement
    has already been seen (k - element). If it has been seen, then we know that
    there are two elements in the array that add up to `k`. If we have traversed
    the entire array without finding two elements that add to `k` then we return
    `False`.
    """
    s = set()

    for elem in A:
        if k - elem in s:
            return True
        s.add(elem)
    return False


def test_add_to_k():
    A = [1, 2, 3, 4, 5]
    k = 6
    assert add_to_k(A, k)
    A = [1, 2, 3, 4, 5]
    k = 70
    assert not add_to_k(A, k)
