"""
Given a sorted list of integers, square the elements and give the output in
sorted order.

```
[-9, -2, 0, 2, 3] -> [0, 4, 4, 9, 81]
```

"""

from typing import List
from collections import namedtuple


def square_sort(x: List[int]) -> List[int]:
    """We know that the list is already sorted, and we can take advantage of
    the fact that we know that all of the negative numbers will be cancelled.
    All of the numbers retain their ordering, so we just need to weave the
    negative numbers and positive numbers together.

    This allows us to take advantage of the fact that the array is already
    sorted, and doesn't make us repeat work that's already been done.
    This is O(n) space and O(n) time.
    """
    # Find the boundary for the negative numbers in this array
    negative_boundary = 0

    while x[negative_boundary] < 0:
        negative_boundary += 1

    res = [0 for _ in x]

    # n_it is the iterator for the negative half of the list. We know that
    # the absolute values of the negative list are what matter, so we traverse
    # the negative list backwards since we want the sorted order of the absolute
    # values of the list.
    n_it = max(negative_boundary, 0)

    # p_it is the iterator for the positive half of the list. We simply traverse
    # up the list with this one
    p_it = negative_boundary + 1

    # res_it is the iterator for the resultant array
    res_it = 0

    # Do a merge between the negative and positive arrays, comparing absolute
    # value since a negative value is positive when it's squared.
    # Squaring is monotonic so a higher number will still be higher when it's
    # squared
    while n_it >= 0 and p_it < len(x):
        if abs(x[n_it]) < x[p_it]:
            res[res_it] = x[n_it] ** 2
            n_it -= 1
        else:
            res[res_it] = x[p_it] ** 2
            p_it += 1
        res_it += 1

    # Take care of any of the remaining elements, since the above loop will
    # run until one list is exhausted
    while n_it >= 0:
        res[res_it] = x[n_it] ** 2
        res_it += 1
        n_it -= 1

    while p_it < len(x):
        res[res_it] = x[p_it] ** 2
        res_it += 1
        p_it += 1
    return res


def test_square_sort():
    TestCase = namedtuple("TestCase", ["input", "expected"])

    test_cases = [
        TestCase([-9, -2, 0, 2, 3], [0, 4, 4, 9, 81]),
        TestCase([1, 1, 2, 3], [1, 1, 4, 9]),
    ]

    for test_case in test_cases:
        assert square_sort(test_case.input) == test_case.expected
