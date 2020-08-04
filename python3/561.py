"""
Etsy, hard

Given a sorted array, convert it into a height-balanced binary search tree


The fact that the tree is already sorted means we can pretty easily convert it
to a BST by making the node the midpoint of the array, and recursively repeating
the process for the left and right halves of the array, for the left and right
children of each node.
"""

from typing import Optional, List


class Node:
    """A node in a binary search tree
    """

    def __init__(self, val, left: Node = None, right: Node = None):
        self.val = val
        self.left = None
        self.right = None


def array_to_bst(A: List) -> Optional[Node]:
    """Do an "in-order" construction of the node by constructing the root and
    recursively constructing the left and right children. This is O(n) time and
    O(logn) space because of the depth of the call stack.
    """
    if not A:
        return None

    if len(A) == 1:
        return Node(A[0])

    midpoint = len(A) // 2
    left_half = A[:midpoint]
    right_half = A[midpoint + 1 :]
    return Node(A[midpoint], array_to_bst(left_half), array_to_bst(right_half))
