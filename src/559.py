"""
Google, medium

Given k sorted singly linked lists, write a function to merge all the lists
into one sorted singly linked list.
"""

import heapq
from typing import List, Tuple


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def merge_k_lists(lists: List[Node]) -> Node:
    """Merge k sorted lists by initializing a min-heap to the first element in
    each list. We put the first k elements into a min heap, using the element's
    value as the key and the index of the list as the value. Every time we
    extract the min value, we increment the pointer for the linked list it
    corresponds to, and add the next value to the cheap. Continue until the heap
    is empty.

    This method is O(nk) time and O(nlogk) space 
    """
    h: List[Tuple[int, int]] = []
    head = Node()
    it = head

    for i, l in enumerate(lists):
        heapq.heappush(h, (l.value, i))

    while h:
        (min_val, idx) = heapq.heappop(h)
        next_node = Node(min_val)
        it.next = next_node
        it = it.next
        list_node = lists[idx]
        list_node = list_node.next

        if list_node:
            heapq.heappush(h, (list_node.value, idx))
    return head.next
