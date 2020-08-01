"""
Given a stack of N elements, interleave the first half of the stack with the 
second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from 
a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3].
If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.
"""

from typing import List, NamedTuple, Deque
from collections import deque


def reverse_interweave(stack: List[int]) -> List[int]:
    q: Deque[int] = deque()

    # first, we reverse the list
    while stack:
        q.append(stack.pop())

    # We want to keep the first half of the queue in the queue, and the second half of the queue
    # back to the stack (which was originally the first half, but now reversed)
    old_len = len(q)

    for i in range(old_len):
        if i < old_len // 2:
            q.append(q.popleft())
        else:
            stack.append(q.popleft())

    # Start pushing items back into the queue, weaving elements together
    for i in range(old_len // 2):
        q.append(stack.pop())
        q.append(q.popleft())

    # If there's an odd number of elements, the stack will have an extra element that we need to add
    # to the end of the queue. There is nothing to weave with here so we just add the last element
    # to the end of the queue.
    if stack:
        q.append(stack.pop())

    # Push everything from the queue back onto the stack since the problem says we have to use the
    # stack
    while q:
        stack.append(q.popleft())
    return stack


def test_reverse_interweave():
    class TestCase(NamedTuple):
        input: List[int]
        expected: List[int]

    test_cases = [
        TestCase([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        TestCase([1, 2, 3, 4], [1, 4, 2, 3]),
    ]

    for test_case in test_cases:
        assert reverse_interweave(test_case.input) == test_case.expected
