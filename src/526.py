"""
You are given a string of length `N` and a parameter `k`. The string can be
manipulated by taking one of the first `k` letters and moving it to the end,
with an unlimited number of moves.

For example, if we are given the string `daily` and `k = 1`, then the best we
can do is `ailyd`, since you can only move the first letter to the end.
"""


from collections import namedtuple


def smallest_string(s: str, k: int) -> str:
    """The lexicographical ordering of a string is marked by the cumulative
    "score" of all of its letters. For example, aaa < aab and aab < bba, and so
    on.

    We are given the first k elements of a string to play with, which means that
    we have the option of taking any of those letters and moving them to the end
    in any order we please. We don't have to move any or all of the letters if
    the shift wouldn't yield a smaller string.

    If `k == 1`, then our best bet is to place the character with the smallest
    lexicographical ordering at the front. This is a simple case: just find the
    minimum character and rotate the string until the min character is at the
    front of the string. If k > 1, then the best posslbe ordering for the 
    string is the sorted string.
    """
    if k == 0:
        return s
    elif k > 1:
        return "".join(sorted(s))
    min_char = min(s)
    min_idx = s.find(min_char)
    return s[min_idx] + s[min_idx + 1 :] + s[:min_idx]


def test_smallest_string():
    TestCase = namedtuple("TestCase", ["input", "expected"])
    test_cases = [
        TestCase(("daily", 1), "ailyd"),
        TestCase(("daily", 2), "adily"),
    ]

    for test_case in test_cases:
        assert (
            smallest_string(test_case.input[0], test_case.input[1])
            == test_case.expected
        )
