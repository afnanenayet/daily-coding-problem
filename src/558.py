"""
Google, medium

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using 
a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.
"""

from random import random
from math import sqrt


def monte_carlo_pi(num_decimal_places: int) -> float:
    """This isn't really a traditional leetcode problem, we just do a Monte 
    Carlo simulation. To get three digits of decimal places, we need to take
    1000 samples. Why? consider that we get some value as a result of simulating
    a bunch of darts and summing them up. If that is an integer, and we divide it
    by 1000, it will have three decimal places. In general, to get n decimal
    places, you take 10^n samples.
    """
    if num_decimal_places < 0:
        raise ValueError("num_decimal_places must be a positive integer")
    r = 1
    n = 10 ** num_decimal_places
    # The accumulated value
    acc = 0

    for _ in range(n):
        x = random()
        y = random()

        if (x ** 2 + y ** 2) <= 1.0:
            acc += 1
    # Multiply by four since we're sampling a circle with a radius of 1, so 
    # we're actually sampling a quarter of the value we're looking for. We
    # can compensate for this by multiplying by 4 again at the end.
    return 4 * acc / n


def test_monte_carlo_pi():
    # pi to three decimal places
    expected = 3.142

    # Since this is a stochastic process
    margin_of_error = 0.1 * expected
    assert abs(monte_carlo_pi(3) - expected) < margin_of_error
