"""
Given a singly linked list and an integer k, remove the kth last element from
the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""

from typing import Optional, List
from collections import namedtuple


class Node(object):
    """A node for a singly-linked list
    """

    def __init__(self, value, next=None):
        """Create a node with a value and a reference to it's successor
        """
        self.value = value
        self.next = next


def remove_k(ll: Node, k: int):
    """We can do this problem in one pass if we use two iterators
    simultaneously. We also luckily don't have to worry about input validation,
    as the problem states that k is guaranteed to be less than the length of the
    node.

    We will send an iterator up the list until it reaches the k - 1th element,
    and then delete the next node.

    While the input problem allows us to assume input safety, I made this safe
    anyways to appease mypy.
    """
    it = ll

    # Find the k - 1 element
    for _ in range(k - 1):
        if it.next:
            it = it.next

    # Delete the node that comes after it
    if it and it.next:
        it.next = it.next.next


def array_to_ll(xs: List) -> Optional[Node]:
    """Convert an array to a linked list

    This is a convenience method for testing.
    """
    if not xs:
        return None

    head = Node(xs[0])
    it = head

    for x in xs[1:]:
        node = Node(x)
        it.next = node
        it = it.next
    return head


def ll_to_array(ll: Node) -> List:
    """Convert a linked list to an array. A null linked list corresponds to an
    empty array.
    """
    res = []
    it = ll

    while it:
        res.append(it.value)
        it = it.next
    return res


def test_remove_k():
    TestCase = namedtuple("TestCase", ["start_list", "k", "expected"])
    test_cases = [
        TestCase([0, 1, 2], 1, [0, 2]),
    ]

    for test_case in test_cases:
        ll = array_to_ll(test_case.start_list)
        remove_k(ll, test_case.k)
        result = ll_to_array(ll)
        assert result == test_case.expected


def test_array_to_ll():
    assert array_to_ll([]) is None

    test_cases = [
        [0, 1, 2],
        [0],
        [0, 1, 2, 3, 4],
    ]

    for test_case in test_cases:
        ll = array_to_ll(test_case)
        array = ll_to_array(ll)
        assert array == test_case
