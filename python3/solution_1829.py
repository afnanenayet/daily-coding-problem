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
"""


def optimal_start_letters(dictionary: list[str]) -> set[str]:
    """
    Args:
        dictionary: A list of words that define valid prefixes and losing words.

    Returns:
        A list of starting letters that will not lose with optimal playing.
    """
    return set()
