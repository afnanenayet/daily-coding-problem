"""
Check if a graph is minimally connected (that is, there is no edge that can be
removed while leaving the graph connected). This is an *undirected* graph.
"""

from typing import Dict, List, Set
from enum import Enum

class Colors(Enum):
    """Colors for the DFS
    """
    White = 0
    Grey = 1
    Black = 2


def is_minimally_connected(graph: Dict[int, List[int]]) -> bool:
    """We can check if a graph is minimally connected (or in other words, if the
    graph is a tree), by traversing the graph and checking for the presence of a
    cycle. If there are no cycles then the graph then the graph is minimally
    connected.

    param graph: The adjacency list matrix representation of the graph
    returns: Whether the graph is minimally connected
    """
    colors = {node: Colors.White for node in graph}

    def cycle(node, parent) -> bool:
        """Do a DFS and check if any of the nodes have been seen before. This
        ignores the parent node because that is a trivial cycle.

        param node: The node to initiate the search from
        param parent: The parent of the current node
        """
        # If we encounter a grey node during the traversal it means we've found
        # a back edge, which indicates a cycle
        if colors[node] == Colors.Grey:
            return True

        # Traverse each neighbor, except for the parent
        for neighbor in graph[node]:
            if neighbor == parent:
                continue

            if cycle(neighbor, node):
                return True
        colors[node] = Colors.Black
        return False

    # Traverse every node in the graph that hasn't been seen already (in case
    # the graph isn't fully connected)
    for node in graph:
        if colors[node] == Colors.White:
            has_cycle = cycle(node, None)

            if has_cycle:
                return False
    return True
