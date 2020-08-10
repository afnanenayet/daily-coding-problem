"""
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""

from typing import NamedTuple


def mapping_exists(a: str, b: str) -> bool:
    """Determine whether it's possible to create a bijection between the characters in a to the
    characters in b.

    We do this by first checking to see if a and b have the same length, if they don't, we know a
    bijection is impossible. We iterate through a and b, keeping track of a character that a
    corresponds to with b. If we don't already have a mapping established, set it, otherwise ensure
    that the given character always matches up with what we have mapped.

    param a: An input string
    param b: An input string
    returns: Whether it is possible to create a 1-1 character mapping between the two strings
    """
    # We know that there can't be a mapping if there's different length strings
    if len(a) != len(b):
        return False

    # mappings[x] gives us which character from b the character `x` from a corresponds to
    mappings = {}

    for a_char, b_char in zip(a, b):
        if a_char not in mappings:
            mappings[a_char] = b_char
        elif b_char != mappings[a_char]:
            return False
    return True


def test_mapping_exists():
    class TestCase(NamedTuple):
        a: str
        b: str
        expected: bool

    test_cases = [
        TestCase("abc", "bcd", True),
        TestCase("foo", "bar", False),
    ]

    for test_case in test_cases:
        assert mapping_exists(test_case.a, test_case.b) == test_case.expected
