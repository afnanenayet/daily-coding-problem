from collections import namedtuple

"""
Apple, medium

Suppose you have a multiplication table that is N by N. That is, a 2D array
where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if
0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X
appears as a value in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the
multiplication table looks like this:

```
| 0 | 1  | 2  | 3  | 4  | 5  |
------------------------------
| 1 | 2  | 3  | 4  | 5  | 6  |
| 2 | 4  | 6  | 8  | 10 | 12 |
| 3 | 6  | 9  | 12 | 15 | 18 |
| 4 | 8  | 12 | 16 | 20 | 24 |
| 5 | 10 | 15 | 20 | 25 | 30 |
| 6 | 12 | 18 | 24 | 30 | 36 |
```

And there are 4 12's in the table.
"""


def mult_table(x: int, n: int) -> int:
    """The naive way to address this would be to simply run through the table
    and iterate over ever value, counting the number of times we see `x`. We
    can utilize math, however, to cut down on the number of iterations we do.

    We can do this in O(n) by keeping a list of the numbers from [1..n] and
    seeing which numbers are valid factors of x.

    This solution has a better runtime than the naive solution, which is to 
    build up the table, which takes O(n^2) time. This method is O(n) time and 
    O(1) space.
    """
    # Factors we have computed so far
    # factors = set()
    counter = 0

    for i in range(1, n + 1):
        # Checking if i divides evenly into x
        if x % i == 0:
            a = x // i

            # Need to make sure that the other factor is actually in the table
            if a <= n:
                counter += 1
    return counter


def test_mult_table():
    TestCase = namedtuple("TestCase", ["n", "x"])

    test_cases = [
        TestCase(6, 12),
        TestCase(6, 13),
        TestCase(7, 13),
        TestCase(9, 13),
        TestCase(9, 169),
        TestCase(169, 9),
    ]

    for test_case in test_cases:
        assert mult_table(test_case.x, test_case.n) == generate_solution(
            test_case.x, test_case.n
        )


def generate_solution(x: int, n: int) -> int:
    """This is the "naive" way to compute the solution, for testing purposes.
    In this one, we actually run through each element.
    """
    counter = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j == x:
                counter += 1
    return counter
