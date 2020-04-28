"""
Given a string and a pattern, find the starting indices of all occurrences of 
the pattern in the string. For example, given "abracadabra" and the pattern 
"abr", you should return `[0, 7]`.
"""

from typing import List


def indices(s: str, pattern: str) -> List[int]:
    """I think that the given example makes this problem look deceptively easy.
    What should we do, for example, if the pattern is "aaa" and the string is
    "aaaaaaaaaa"? We need the KMP string matching algorithm to properly solve
    this problem. KMP is O(n + m), which is the best you can do given that you 
    will need to look at every character in the string.

    The idea behind KMP is that you don't need to re-check every character in a
    pattern if there's a mismatch in the string.
    """
    prefix_indices = []
    T = build_lps_table(pattern)
    k = 0

    for j in range(len(s)):
        if s[j] == pattern[k]:
            j += 1
            k += 1

            if k == len(pattern):
                prefix_indices.append(j - k)
                k = T[k - 1]
        else:
            k = T[k]

            if k < 0:
                j += 1
                k += 1
    return prefix_indices


def build_lps_table(prefix: str) -> List[int]:
    """Build the LPS table for the KMP algorithm. This table specifies whether
    the current character is part of an earlier prefix, so we know the latest
    character to check for when we are scanning the string. The table
    preprocesses the pattern and looks for the longest prefix that is also a
    suffix, which means that we can use this table rather than backtrack when
    scanning the string to see if it contains the pattern.

    Note that this function takes the pattern rather than the input string.

    This function is O(n) time and space, where n is `len(prefix)`.
    """
    if len(prefix) == 0:
        return []
    table = [0] * len(prefix)

    # The current index in the preprocessing table
    i = 1

    # The next character of the candidate substring
    cand = 0

    # Base case
    table[0] = -1

    for i in range(1, len(prefix)):
        if prefix[i] == prefix[cand]:
            table[i] = table[cand]
        else:
            table[i] = cand
            cand = table[cand]

            while cand >= 0 and prefix[i] != prefix[cand]:
                cand = table[cand]
        cand += 1
    return table


def test_preprocess():
    test_cases = [
        ("abcdabd ", [-1, 0, 0, 0, -1, 0, 2, 0]),
        ("abacababa ", [-1, 0, -1, 1, -1, 0, -1, 3, -1, 3]),
    ]

    for test_case in test_cases:
        assert build_lps_table(test_case[0]) == test_case[1]


def test_search():
    s = "abracadabra"
    pattern = "abr"
    expected = [0, 7]
    result = indices(s, pattern)
    assert expected == result
