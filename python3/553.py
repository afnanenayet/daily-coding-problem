"""
Google, medium

You are given an N by M 2D matrix of lowercase letters. Determine the minimum
number of columns that can be removed to ensure that each row is ordered from
top to bottom lexicographically. That is, the letter at each column is
lexicographically later as you go down each row. It does not matter whether
each row itself is ordered lexicographically.

For example, given the following table:

```
cba
daf
ghi
```

This is not ordered because of the a in the center. We can remove the second column to make it
ordered:

```
ca
df
gi
```

So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

```
abcdef
```

Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

```
zyx
wvu
tsr
```

Your function should return 3, since we would need to remove all the columns to order it.
"""

from typing import List
from collections import namedtuple


def lex_ordering(matrix: List[List[str]]) -> int:
    """We can easily check if a column is ordered by iterating through each row
    to see if the element in the previous row is ordered properly. If not, we can
    mark that a column needs to be deleted by setting the topmost element to the
    max element, so we don't even have to use any extra space to note which
    columns need to be deleted.

    I'm making the assumption that the matrix is row-indexed.
    """
    if not matrix:
        return 0

    m = len(matrix)
    n = len(matrix[0])

    for row_idx in range(m):
        for col_idx in range(n):
            # If a column breaks the lexical ordering property, mark it for
            # deletion
            if (
                row_idx > 0
                and matrix[row_idx - 1][col_idx] > matrix[row_idx][col_idx]
            ):
                matrix[0][col_idx] = None
    # Count the number of null elements in the top row
    count = 0

    for elem in matrix[0]:
        if not elem:
            count += 1
    return count


def test_lex_ordering():
    TestCase = namedtuple("TestCase", ["matrix", "expected"])
    test_cases = [
        TestCase(["a", "b", "c", "d"], 0),
        TestCase([["c", "b", "a"], ["d", "a", "f"], ["g", "h", "i"],], 1),
    ]

    for test_case in test_cases:
        assert lex_ordering(test_case.matrix) == test_case.expected
