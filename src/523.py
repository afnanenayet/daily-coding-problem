"""
Easy, Jane Street

Given integers `M` and `N`, write a program that counts how many positive
integer pairs `(a, b)` satisfy the following conditions:

* a + b = M
* a XOR b = N
"""

from collections import namedtuple


def pairs(m: int, n: int) -> int:
    """Let's focus on solving the first constraint: if we have two integers and
    we know that they have to add up to M, we can iterate from 0 to M // 2 to
    get a, and subtract a from M to get b. We know, with basic arithmetic, that
    these numbers add up to M. We can then check that `a ^ b == N`.

    This algorithm is O(M / 2) in both space and time, because there are up to
    O(M / 2) pairs that add up to M. If they all somehow end up satisfying the
    second constraint, then the resultant array will have M / 2 elements. We can
    eliminate the constants to reduce this to O(M).
    """
    upper_bound = m // 2
    res = []

    for i in range(1, upper_bound + 1):
        a = i
        b = m - a

        if a ^ b == n:
            res.append((a, b))
    return res


def test_pairs():
    TestCase = namedtuple("TestCase", ["input", "expected"])
    test_cases = [
        TestCase((2, 0), [(1, 1)]),
    ]

    for test_case in test_cases:
        ans = pairs(test_case.input[0], test_case.input[1])
        ans_set = set(ans)
        expected_set = set(test_case.expected)
        assert ans_set == expected_set
