"""
From: LinkedIn

You are given a binary tree in a peculiar string representation. Each node is
written in the form "(lr)" where "l" corresponds to the left child and "r" 
corresponds to the right child. If either l or r is null, it will be
represented as 0. Otherwise, it will be represented by a new (lr) pair.
"""


def depth(s: str) -> int:
    """This method ascertains the depth of a binary tree by tracking the max 
    depth using a stack to track the parenthesis. When we encounter a "(", we
    add to the depth. When we encounter a ")", we pop from the stack. At any
    given moment, the tree depth is len(stack) - 1 (since the dummy leaf node is
    syntactically the same).
    """
    # A running counter keeping track of the depth as we go along
    depth = 0
    # Keep track of the maximum depth we encounter as we go along
    max_depth = 0

    for char in s:
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
        max_depth = max(max_depth, depth)
    # We subtract one because we need to subtract the depth of the root node
    return max_depth - 1


def test_root_no_children():
    s = "(00)"
    assert depth(s) == 0


def test_root_two_children():
    s = "((00)(00))"
    assert depth(s) == 1


def test_root_three_children():
    s = "((((00)0)0)0)"
    assert depth(s) == 3
