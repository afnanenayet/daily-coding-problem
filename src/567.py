"""
`cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the
first and last element of that pair. For example, `car(cons(3, 4))` returns 3,
and `cdr(cons(3, 4))` returns 4.

Given an implementation of `cons`, implement `car` and `cdr`
"""

from typing import Tuple


def cons(a, b):
    """Create a pair from the elements a and b

    param a: The first element in the tuple
    param b: The second element in the tuple
    returns: A pair created from a and b
    """

    def pair(f):
        return f(a, b)

    return pair


def car(pair):
    """Return the first element of a pair created with `cons`

    param pair: A pair that was created with `cons`
    returns: The first element of the pair
    """

    def fst(x, _):
        return x

    return pair(fst)


def cdr(pair):
    """Return the last element of a pair created with `cons`

    param pair: A pair that was created with `cons`
    returns: The second element of the pair
    """

    def snd(_, y):
        return y

    return pair(snd)
