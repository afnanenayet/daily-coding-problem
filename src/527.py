"""Determine how many distinct ways there are to create a max heap from a list of
`N` given integers.

For example, if N = 3, and our integers are [1, 2, 3], there are two ways, shown below.

  3      3
 / \    / \
1   2  2   1
"""


from typing import List, Tuple
import math


# A cache for the results of the `choose` method
CHOOSE_CACHE: List[List[int]] = []

# A cache for the results of the `num_max_heaps_helper` method
NUM_HEAPS_CACHE: List[int] = []


def num_max_heaps(n: int) -> int:
    """We can solve this problem recursively by selecting different values for
    each node as we traverse the array. For example, for the first node in the
    array [1, 2, 3], we know we have to pick the max element. The second and
    third nodes, however, are interchangeable.

    Note that this problem doesn't specify that the heap has to be balanced,
    which makes the problem significantly easier to work with.

    First, we know that the top-level element has to be the maximum element for
    the heap. The left and right subtrees are defined recursively, it's just a
    matter of choosing which elements go into the left subtree and which
    elements go into the right subtree and recursively solving for those values.
    The solution to this problem is T(n) = (n - 1 choose l) * T(l) * T(r), where
    l + r = n - 1 (are are the number of elements in the left subtree and right
    subtree, respectively, and we lose one node to the root).

    You need to calculate the number of elements that can be in the left side and
    right subtrees of the root of a max-heap.
    """

    def child_element_count(n: int) -> Tuple[int, int]:
        """Calculate the number of elements on the left side of the heap. We
        know that the maximum height of the heap is log_2(n), with it being a
        binary tree and all. A heap doesn't necessarily have to be a full
        binary tree -- the last level might not be fully formed.

        This method returns the number of elements in the left and right
        subtrees as a tuple, (left, right)

        param n: The number of elements in the subtree
        """
        height = math.floor(math.log2(n))
        # Theoretical maximum number of nodes that can be in the left subtree
        max_nodes = 2 ** height

        # The number of nodes in the last level of the left subtree is n - (2^h
        # - 1)
        nodes_last_left = n - 1 - max_nodes

        # If the last level of the heap is more than half-full
        if nodes_last_left >= max_nodes // 2:
            l = max_nodes - 1
            r = n - l - 1
            return (l, r)

        # Otherwise the last level of the heap is less than half-full
        l = max_nodes - 1 - ((max_nodes // 2) - nodes_last_left)
        r = n - l - 1
        return (l, r)

    def choose(n: int, k: int) -> int:
        """An implementation of n choose k, calculated recursively with
        memoization.
        """
        # Base cases
        if k > n:
            return 0

        if n <= 1 or k == 0:
            return 1

        if CHOOSE_CACHE[n][k]:
            return CHOOSE_CACHE[n][k]

        res = choose(n - 1, k - 1) + choose(n - 1, k)
        CHOOSE_CACHE[n][k] = res
        return res

    def num_max_heaps_helper(n: int) -> int:
        """Get the number of heaps for a particular value of n using the
        recursive formula described in the docstring of the outer function.
        """
        if n <= 1:
            return 1

        if NUM_HEAPS_CACHE[n]:
            return NUM_HEAPS_CACHE[n]

        num_left, num_right = child_element_count(n)
        res = (
            choose(n - 1, num_left)
            * num_max_heaps_helper(num_left)
            * num_max_heaps_helper(num_right)
        )
        NUM_HEAPS_CACHE[n] = res
        return res

    # Init routine
    CHOOSE_CACHE = [[None for _ in range(n)] for _ in range(n)]
    NUM_HEAPS_CACHE = [None for _ in range(n + 1)]
    return num_max_heaps_helper(n)


def test_max_heaps():
    assert num_max_heaps(3) == 2
