"""
Write a function, throw_dice(N, faces, total), that determines how many ways it is possible to
throw N dice with some number of faces each to get a specific total.

For example, throw_dice(3, 6, 7) should equal 15.
"""


def throw_dice(N: int, faces: int, total: int) -> int:
    """Determine how many ways you can throw N dice with some number of faces to get a specific
    total

    We can think of this in terms of subproblems: to get a total with N die, we can try rolling a
    die, and then solving how many ways there is to get the total - our roll for N - 1 die. We can
    use a dynamic programming table to save computations so we can refer back to them.

    This is O(m * n * k) time and O(m * n * k) space, where m is the number of die, n is the number
    of faces, and k is the total desired sum.
    """
    if total == 0:
        return 1

    # dp[i][j] returns the number of ways to get to the sum `i` using `j` dice
    dp = [[0 for _ in range(total + 1)] for _ in range(N)]

    # Initialize the array for the first die, which can only achieve the total for each face it
    # rolls
    for curr_roll in range(1, min(faces + 1, total + 1)):
        dp[0][curr_roll] = 1

    # For each die, iterate through each potential total and simulate a roll from the die. We can
    # add the number of ways to reach `current_total - current_roll` using n - 1 die (if we are
    # currently using n die).
    for die in range(1, N):
        for curr_total in range(1, total + 1):
            for curr_roll in range(1, min(curr_total, faces + 1)):
                dp[die][curr_total] += dp[die - 1][curr_total - curr_roll]
    return dp[-1][-1]


def test_throw_dice():
    assert throw_dice(3, 6, 7) == 15
