"""
Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

* init(size): initialize the array with size
* set(i, val): updates index at i with val where val is either 1 or 0.
* get(i): gets the value at index i.
"""

from enum import Enum


class BitArray:
    def __init__(self, size: int):
        self._int = 0
        self.size = size

    def set(self, i: int, val: int) -> None:
        """Set the value at index i

        param i: The index to set
        param val: The value to set at index i
        """
        if i > self.size:
            raise ValueError("i must be less than size")

        if val < 0 or val > 1:
            raise ValueError("The value must be 1 or 0")

        # Clear the value at i
        self._int = self._int & ~(val << i)

        # Set the new value at i
        self._int = self._int | (val << i)

    def get(self, i: int) -> int:
        """What should we do if `i` is greater than `size`?

        param i: The index to retrieve, this must be less than `size`
        returns: The value at BitArray[i]
        """
        if i >= self.size:
            raise ValueError("i must be less than size")

        return self._int >> i & 1
