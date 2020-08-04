"""
Given a list of words, determine whether the words can be chained to form a circle. A word X can
be placed in front of another word Y in a circle if the last character of X is same as the first
character of Y.

For example, the words ['chair', 'height', 'racket', touch', 'tunic'] can form the following
circle: chair --> racket --> touch --> height --> tunic --> chair
"""

from typing import List, Deque, Tuple, Dict
from collections import defaultdict, deque
from enum import Enum


class DFSState(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2


def word_circle(words: List[str]) -> bool:
    """We can resolve this by doing a breath-first-search
    """
    # A dictionary of all letters that begin with a particular letter
    first_letters: Dict[str, List[str]] = defaultdict(list)

    # Initialize the first and last letter lookup tables
    for word in words:
        first_letters[word[0]].append(word)

    seen: Dict[str, DFSState] = dict()

    for word in words:
        seen[word] = DFSState.WHITE

    def has_cycle(node: str) -> bool:
        """Use a DFS to detect a cycle

        param init: The node to start the search from
        returns: Whether there is a cycle in the graph
        """
        if seen[node] != DFSState.WHITE:
            return True
        seen[node] = DFSState.GREY
        last_letter = node[-1]

        for neighbor in first_letters[last_letter]:
            if seen[neighbor] != DFSState.BLACK and has_cycle(neighbor):
                return True
        seen[node] = DFSState.BLACK
        return False

    for word in words:
        if seen[word] == DFSState.WHITE and has_cycle(word):
            return True
    return False


def test_word_circle():
    test_case = ["chair", "height", "racket", "touch", "tunic"]
    assert word_circle(test_case)

    test_case = ["chair", "height"]
    assert not word_circle(test_case)
