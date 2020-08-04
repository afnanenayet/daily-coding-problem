"""
Given an array of numbers of length N, find both the minimum and maximum using
less than 2 * (N - 2) comparisons.
"""

from typing import List, Tuple
import random


def min_max(A: List) -> Tuple:
    """We can process pairs at a time

    If we process two pairs at a time, we can determine which of the pair is
    the local min/max, and compare those with the global min/max.

    We make a comparison between each pair, and then two other comparisons to
    compare with the global min and max, for three comparisons * (n / 2) times.
    This gives us (3/2 * N) which is less than 2 * (N - 2).
    """
    global_min = float("inf")
    global_max = float("-inf")

    start = 0

    # If there's an odd number of elements, we can get just make the global
    # maxes and mins the first element and remove it from consideration.
    if len(A) % 2 == 1:
        start = 1
        global_max = A[0]
        global_min = A[0]

    for i in range(start, len(A) - 1, 2):
        fst = A[i]
        snd = A[i + 1]

        local_min, local_max = (fst, snd) if fst < snd else (snd, fst)
        global_min = min(global_min, local_min)
        global_max = max(global_max, local_max)
    return (global_min, global_max)


def test_min_max():
    test_cases = [
        [random.randint(0, 10000) for _ in range(100)] for _ in range(10)
    ]

    for test_case in test_cases:
        cand_min, cand_max = min_max(test_case)

        assert cand_min == min(test_case)
        assert cand_max == max(test_case)
