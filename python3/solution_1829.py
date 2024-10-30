"""
# Question

From 2sig.

Ghost is a two-person word game where players alternate appending letters to a word. The first 
person who spells out a word, or creates a prefix for which there is no possible continuation, 
loses. Here is a sample game:

Player 1: g
Player 2: h
Player 1: o
Player 2: s
Player 1: t [loses]
Given a dictionary of words, determine the letters the first player should start with, such that 
with optimal play they cannot lose.

For example, if the dictionary is `["cat", "calf", "dog", "bear"]`, the only winning start letter 
would be b.

The prompt is not specific enough, so I decided to interpret this question so that the solution
should contain the minimal prefixes that guarantee a win (otherwise I don't see how this question
could be considered a "hard").

Example:
Words: `["bear", "more", "moire", "muse", "must"]`
Solution: `{"b", "mu"}`

# Solution

## Approach

Build a trie with all of the words we are given. In this trie each node keeps track of
whether that node is "poisoned". We consider a node poisoned if any of its children
leads to a word that would cause player 1 to lose the game.

We trivially know that any word with an even number of letters is a winnable word.
Any word with an odd number of letters will lead to a loss. When building the trie,
we use this property to set whether the nodes for the given word should be marked
as poisoned. This means we don't have to compute this after constructing the tree,
which would be an expensive bottom-up traversal.

After we build the trie, we can find the winning prefix sequences by traversing the trie
and building up the prefixes as we go along. If we run into a node that's not poisoned, (i.e.
none of the children of that node can lead to a losing word), we have found a minimal sequence
of letters that will lead to a win. We can add this prefix to a set. 

We also take care not to add the sequences from any terminal nodes, which are also full words.
If a player plays every letter in a word, then they lose.

## Complexity

Suppose the longest word has $m$ characters. The time and space complexity is $O(mn)$.

We traverse every letter for each word once to build the trie. Every letter gets a node,
so that's the space complexity. We then traverse again to find the optimal winning sequences.
This is also a linear traversal.
"""

from collections.abc import Sequence
from dataclasses import dataclass
from typing import TypeVar


T = TypeVar("T")


RecursiveDict = dict[T, "RecursiveDict[T] | None"]


@dataclass
class Node[T]:
    """A node for our prefix trie."""

    value: T
    """The character in this level of the sequence."""

    poisoned: bool = False
    """Whether any of the children in this node lead to strings that have odd letters."""

    children: dict[T, "Node[T]"] | None = None
    """
    The children of this node.

    If the node is terminal, or sentinel node, this will be `None`
    """

    @property
    def terminal(self) -> bool:
        return self.children is None or len(self.children) == 0

    def add_child(self, child: "Node[T]") -> None:
        """
        Add a child to this node.

        This will also set the poisoned flag based on the incoming node's value.
        """
        if self.children is None:
            self.children = dict()
        self.children[child.value] = child
        if child.poisoned:
            self.poisoned = True


class Trie[T]:
    """A character trie."""

    def __init__(self, sentinel: T) -> None:
        self._root: Node[T] = Node(sentinel)

    def insert(self, /, x: Sequence[T]) -> None:
        """Insert an element into the trie."""
        if len(x) == 0:
            return
        curr = self._root

        # If there is an odd number of letters than player 1 will lose
        poisoned = len(x) % 2 == 1

        # Expand the trie with the given sequence. The trie might terminate earlier than
        # our sequence, so we need to expand them for all of the elements. Treat the last
        # element as a special case because we might terminate the trie with a `None`.
        for elem in x:
            # Just to satisfy the type checker
            assert isinstance(curr, Node)
            if curr.terminal:
                curr.children = dict()
            assert curr.children is not None
            # Don't want to overwrite the existing flag for poisoning, only add to it.
            curr.poisoned |= poisoned
            if elem not in curr.children:
                curr.children[elem] = Node(elem, poisoned=poisoned)
            curr = curr.children[elem]

    @property
    def root(self) -> Node[T]:
        return self._root


def optimal_start_letters(dictionary: list[str]) -> set[str]:
    """
    Args:
        dictionary: A list of words that define valid prefixes and losing words. Every string in this
          list must have a length of at least 1.

    Returns:
        A list of starting sequences that will not lose with optimal playing.
    """
    trie = Trie(sentinel="")
    for word in dictionary:
        trie.insert(word)

    # Perform a DFS, building a sequence of elements until we find the
    # first node that has no poisoned children. That is a minimal sequence
    # that's guaranteed to win.
    optimal_prefixes: set[str] = set()

    def dfs_helper(node: Node[str], prefix: str) -> None:
        # If we have a terminal node, the sequence is the whole string.
        # We can't play a whole string because that would cause the player to lose the game.
        if node.terminal:
            return
        assert node.children is not None

        new_prefix = prefix + node.value

        if node.poisoned:
            assert node.children is not None
            for child in node.children.values():
                dfs_helper(child, new_prefix)
        else:
            optimal_prefixes.add(new_prefix)

    assert trie.root.children is not None
    for child in trie.root.children.values():
        dfs_helper(child, "")
    return optimal_prefixes
