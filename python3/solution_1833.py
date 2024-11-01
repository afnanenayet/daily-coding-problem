"""
# Problem

Difficulty: medium
Company: Pinterest

The sequence `[0, 1, ..., N]` has been jumbled, and the only clue you have for its order is an array 
representing whether each number is larger or smaller than the last. Given this information, 
reconstruct an array that is consistent with it. For example, given `[None, +, +, -, +]`, you could 
return `[1, 2, 3, 0, 4]`.

# Solution

One of the key facts to note about this problem is that each element in the ordering array
is *only* dependent on the element before. For something like `[None, -, +]`, the following
solutions are valid: `[0, 2, 1], [1, 2, 0]`. This makes our solution less constrained.

We can solve this in a greedy way by iterating through the array backwards. We keep two counters:
a lower counter starting at 0, and an upper counter starting at `len(ordering) - 1`. This is the
same as having two pointers to the ordered array, but we don't actually need to allocate that
array since it's just an array of numbers from 0 to N - 1.

We traverse the ordering array in reverse. Every time we see a "+": assign the corresponding
index in the solution to the upper value and then decrement the upper value. For "-": assign
lower value and increment lower value. For the first number, which can't have a constraint,
arbitrarily assign the lower value.

Every "+" element in the array will always be increasing, and they will always be greater
than any "-" value, since we assign each of these elements from opposite ends of our
ordered array.

## Complexity

$O(n)$ time because we linearly traverse the array. $O(n)$ space for the result array.
This could be reduced to $O(1)$ since we could just assign the result into the constraint
array instead of the results array (since we don't need to see any elements after the fact when in 
reverse order).
"""


def solve_array(constraints: list[str | None]) -> list[int]:
    """
    Returns an array that satisfies the constraints by some input problem.

    Args:
        constraints: A list of constraints, either "+", "-", or `None`.
          - "+" means that the element must be greater than the last number
          - "-" means that the element must be less than the last number
          - `None` means no constraint has been applied.

          The first element must be `None`.

    Returns:
        Some array that satisfies the constraints.
    """
    res = [0 for _ in range(len(constraints))]
    lower_idx = 0
    upper_idx = len(constraints) - 1

    for i, c in reversed(list(enumerate(constraints))):
        if c == "+":
            res[i] = upper_idx
            upper_idx -= 1
        elif c == "-":
            res[i] = lower_idx
            lower_idx += 1
        elif c is None:
            res[i] = lower_idx
        else:
            raise ValueError(f"Unexpected element {c} in constraint array")
    return res


def verify_array_constraints(array: list[int], constraints: list[str | None]) -> None:
    """
    Check if an array passes the given constraints.

    Will raise an exception or assertion error if anything fails.
    """
    assert len(array) == len(constraints)
    assert sorted(array) == [i for i in range(len(array))]
    for i in range(1, len(array)):
        c = constraints[i]
        if c == "-":
            assert array[i] < array[i - 1], f"index {i}, {array=}"
        elif c == "+":
            assert array[i] > array[i - 1], f"index {i}, {array=}"
        elif c is None:
            pass
        else:
            raise ValueError("Unexpected value in constraint array")
