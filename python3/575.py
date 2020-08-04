"""
Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement
the following methods:

next(): returns the next element in the array of arrays. If there are no more elements, raise an
exception.

has_next(): returns whether or not the iterator still has elements left.

For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output
1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
"""

from typing import List


class ArrayArrayIterator:
    """An iterator for doubly nested arrays

    This will allow you to iterate as if you had flattened the iterators
    """

    def __init__(self, arrays: List[List]):
        """Initialize the double array iterator

        We store the index of the current array and the index in that array
        """
        self._arrays = arrays
        self._curr_array = 0  # which array
        self._curr_elem = 0  # which index in the current array

    def next(self):
        """Return the next element in the array

        If there isn't another element then this element will raise an exception
        """
        # If the current index is out of bounds, move onto the next array
        while self._curr_elem >= len(
            self._arrays[self._curr_array]
        ) and self._curr_array < len(self._arrays):
            self._curr_array += 1
            self._curr_elem = 0

        # If we've exhausted the list, raise an error
        if self._curr_array >= len(self._arrays) and self._curr_elem >= len(
            self._arrays[self._curr_elem]
        ):
            raise IndexError()

        elem = self._arrays[self._curr_array][self._curr_elem]
        self._curr_elem += 1

        # When we advance the iterator we want to make sure that we skip any empty arrays
        while self._curr_array < len(self._arrays) and self._curr_elem >= len(
            self._arrays[self._curr_array]
        ):
            self._curr_elem = 0
            self._curr_array += 1
        return elem

    def has_next(self) -> bool:
        """Returns whether the iterator has any remaining elements
        """
        return self._curr_array < len(self._arrays) and self._curr_elem < len(
            self._arrays[self._curr_array]
        )


def test_array_array_it():
    test_case = [
        [1, 2],
        [3],
        [],
        [4, 5, 6],
    ]
    it = ArrayArrayIterator(test_case)
    result = []
    expected = [x for l in test_case for x in l]

    while True:
        elem = None
        has_next = it.has_next()
        try:
            elem = it.next()
        except:
            assert not has_next
            break
        assert has_next
        result.append(elem)

    assert result == [1, 2, 3, 4, 5, 6]
