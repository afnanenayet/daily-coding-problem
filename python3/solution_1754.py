"""
Daily Coding Problem #1754

Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees. 
For example, 16891 is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.
"""

from collections.abc import Generator, Sequence
from typing import Final, TypeGuard, TypeVar

FLIPPED_CHARS: Final[dict[int, int]] = {
    1: 1,
    6: 9,
    8: 8,
    9: 6,
}

T = TypeVar("T")


def combinations_with_replacement(
    xs: Sequence[T], size: int
) -> Generator[list[T], None, None]:
    """
    Return all permutations of the input list.

    Args:
        xs: An iterable of unique elements.
    """

    def helper(current: list[T], depth: int) -> Generator[list[T], None, None]:
        """
        Args:
            current: The combination prefix that's been built up so far.
            start: The index to start sampling from when adding another element to the prefix.
            depth: Current recursion depth for this invocation of the method.
        """
        if depth == size:
            yield current
        else:
            for i in range(0, len(xs)):
                next_prefix = current + [xs[i]]
                yield from helper(next_prefix, depth + 1)

    return helper([], 0)


def _check_list_has_no_optional(x: Sequence[T | None]) -> TypeGuard[Sequence[T]]:
    """
    This is a convenience method to help the type-checker.

    Checks that some sequence doesn't have any `None` elements
    """
    return not any(map(lambda element: element is None, x))


def all_strobo_nums(n_digits: int):
    """
    Generates all of the possible strobo numbers by generating all possible combinations of the 
    first half of the sequence recursively, then filling out the second half of the sequence
    since that's set by the first half (if we want to make a valid number that can be flipped).

    This solution first generates all permutations of the flipped chars recursively, which is O(5^N),
    we recurse for every flipped character N times. The space complexity is $O(n)$ since the maximum
    recursive depth is N.

    Filling out the second half of the sequence is O(n), so the time complexity is $O(5^n) + O(N)$ and space
    is $O(5^N) + O(N)$ (because of the recursion stack and the fact that we store every result).
    """
    helper_depth = n_digits // 2
    if n_digits % 2 != 0:
        helper_depth += 1

    def helper(
        current: Sequence[int | None], depth: int
    ) -> Generator[Sequence[int], None, None]:
        if depth == helper_depth:
            assert _check_list_has_no_optional(current)
            yield current
        else:
            # Need to make a copy so we're not referencing the exact same list with each invocation
            for digit, flipped in FLIPPED_CHARS.items():
                idx_digit = depth
                idx_flipped = n_digits - depth - 1
                current = [x for x in current]
                current[idx_digit] = digit
                # Handles the case of an odd number of digits
                if idx_digit < idx_flipped:
                    current[idx_flipped] = flipped
                yield from helper(current, depth + 1)

    return list(helper([None] * n_digits, 0))
