"""
Given a string split it into as few strings as possible such that each string is
a palindrome.

Examples:

"racecarannakayak" -> ["racecar", "anna", "kayak"]

"abc" -> ["a", "b", "c"]

The naive method would be to try every possible split of the string and check if
those split strings are palindromes. This is obviously not very efficient.
"""

from typing import List


def is_palindrome(s: str) -> bool:
    """Return whether a string is a palindrome

    This is as efficient as you can get when computing whether a string is a
    palindrome. It runs in O(n) time and O(1) space.
    """
    if len(s) <= 1:
        return True

    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False

        i += 1
        j -= 1

    return True


def naive_split(s: str) -> List[str]:
    """In the naive case, you simply check every possible split to see if
    there's a palindrome created, and you recursively add to the result.
    """
    res = []

    def helper(s: str, path: List[str]):
        """A helper function for the recursive search. We are essentially
        running a DFS from each letter, which will expand, trying to shift the
        splits as it finds larger palindromes. Because the iterator iterates up
        (from 1 to the length of the string), the largest palindromes (aka the
        fewest splits) will be appended to the string last. This method is
        O(n^3). It's O(n^2) to traverse the strings with the search, and then
        another multiplied O(n) to check if a string is a palindrome.

        param s: The search space for the helper to examine
        param path: The path that has been searched so far
        """
        # There is nothing left to search, append the given path to the result
        if not s or len(s) == 0:
            # This is a workaround because python has an identical operator for
            # both assignment and initialization. If we do res = path, it will
            # define a new variable named "res" in this scope, but we don't
            # need the intermediate paths we take to get to the end, so this
            # makes sure we don't hold unneeded information in memory.
            if len(res) > 0:
                res.pop()
            res.append(path)
            return

        for i in range(1, len(s) + 1):
            if is_palindrome(s[:i]):
                helper(s[i:], path + [s[:i]])
    helper(s, [])

    # Uncomment these lines if you want to see the steps the search takes
    # print("\nsteps:")
    # for line in res:
    # print(line)
    # print("")
    return res[-1]


# TODO there's an error in this implementation, not sure what's causing the
# answer to be off
def memoized_split(s: str) -> List[str]:
    """This approach is identical to the naive method, except that it caches
    some results. You might have noticed that we are scanning the same multiple
    times to check if they're palindromes. We can precompute all of the
    palindromes in the string first, and then run the search.
    """
    # palindrome[i][j] returns whether s[i:j] is a palindrome
    palindromes = [[False for _ in range(len(s))] for _ in range(len(s))]

    for i in range(len(s)):
        for j in range(len(s)):
            palindromes[i][j] = False

    res = []

    # Build the cache for which substrings are palindromes
    for i in range(len(s)):
        for j in range(i + 1):
            if s[i] == s[j] and (i - j < 1 or palindromes[j + 1][i - 1]):
                palindromes[j][i] = True

    def helper(start: int, path: List[str]):
        """A helper function for the recursive search. We are essentially
        running a DFS from each letter, which will expand, trying to shift the
        splits as it finds larger palindromes. Because the iterator iterates up
        (from 1 to the length of the string), the largest palindromes (aka the
        fewest splits) will be appended to the string last. This method is
        O(n^3). It's O(n^2) to traverse the strings with the search, and then
        another multiplied O(n) to check if a string is a palindrome.

        param s: The search space for the helper to examine
        param start: The start index of the palindrome
        param end: The end index 
        param path: The path that has been searched so far
        """
        # There is nothing left to search, append the given path to the result
        if start == len(s):
            res.append(path)
            return

        for i in range(start, len(s)):
            if palindromes[start][i]:
                helper(i + 1, path[:] + [s[start:i + 1]])

    helper(0, [])
    return res[-1]


def test_is_palindrome():
    assert is_palindrome("a")
    assert not is_palindrome("ab")
    assert is_palindrome("aba")
    assert is_palindrome("abba")


def test_naive_split():
    assert naive_split("abc") == ["a", "b", "c"]
    assert naive_split("racecarannakayak") == ["racecar", "anna", "kayak"]
    assert naive_split("aba") == ["aba"]
    assert naive_split("aaaa") == ["aaaa"]


def test_memoized_split():
    assert memoized_split("abc") == ["a", "b", "c"]
    assert memoized_split("racecarannakayak") == ["racecar", "anna", "kayak"]
    assert memoized_split("aba") == ["aba"]
    assert memoized_split("aaaa") == ["aaaa"]
