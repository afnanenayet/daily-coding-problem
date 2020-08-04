"""
Given two non-empty binary trees s and t, check whether tree t has exactly the
same structure and node values with a subtree of s. A subtree of s is a tree
consists of a node in s and all of this node's descendants. The tree s could
also be considered as a subtree of itself.
"""


from typing import Optional


class BinaryTree:
    def __init__(
        self,
        value,
        left: Optional["BinaryTree"] = None,
        right: Optional["BinaryTree"] = None,
    ):
        self.value = value
        self.left: Optional["BinaryTree"] = left
        self.right: Optional["BinaryTree"] = right


def subtree_helper(a: Optional[BinaryTree], b: Optional[BinaryTree]) -> bool:
    if a is None and b is None:
        return True

    # If we reach this branch, that means either a xor b is None, which is an
    # equality
    if a is None or b is None:
        return True

    if a.value != b.value:
        return False
    return subtree_helper(a.left, b.left) and subtree_helper(a.right, b.right)


def is_subtree(s: BinaryTree, t: BinaryTree) -> bool:
    """We traverse the tree, checking for potential matches
    """
    # Traverse tree until we get a match
    return (
        subtree_helper(s, t)
        or subtree_helper(s.left, t)
        or subtree_helper(s.right, t)
    )
