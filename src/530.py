"""
#530, Google, Easy

The edit distance between two strings refers to the minimum number of character
insertions, deletions, and substitutions required to change one string to the
other. For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""


def edit_distance(s1: str, s2: str) -> int:
    """I think this problem is very well known as a dynamic programming problem.
    I'm going to go straight for the optimal solution. The edit distance between
    two strings is something that we can solve with dynamic programming, as I
    just said. In order to do that, we need to break the string down into
    subproblems. Given a string s1, and another string, s2, we can determine the
    edit distance between the two strings as the minimum edit distance between
    s1[:-1] and s2[:-1] + the edit distance between s1[-1] and s2[-1]. The key
    insight is that you can calculate the edit distance for each part of the
    substring once.

    This solution is O(mn) and O(mn) space
    """
    # dp[a][b] is the edit distance between s1[:a] and s2[:b]
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            dp[i][j] = 0

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            # The two base cases: the empty string compared to another string
            # alway has the edit distance of the length of the other string,
            # because you just insert all of the characters from the other
            # string
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            # If the characters are equal, we don't add anything to the edit
            # distance
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # We have 3 cases when the characters aren't equal: we have an
            # insertion, a deletion, or a substitution.
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                               dp[i - 1][j - 1]) + 1
    print(dp)
    return dp[-1][-1]


def test_edit_distance():
    assert edit_distance("kitten", "sitting") == 3
