"""
# Problem

A teacher must divide a class of students into two teams to play dodgeball. Unfortunately, not all the kids get along, and several refuse to be put on the same team as that of their enemies.

Given an adjacency list of students and their enemies, write an algorithm that finds a satisfactory pair of teams, or returns False if none exists.

# Notes

This is a bipartite graph problem. We can use the standard bipartition algorithm to try to solve this.

## Bipartite graph algorithm

1. Pick some arbitrary node, assign it to a side
2. For each of the node's neighbors, assign them to the other side. Repeat.

If at any point we find that nodes have already been assigned, check to see if they're
on the correct side. If not, a bipartition isn't possible.
"""

from collections import deque


type Graph = dict[int, list[int]]
"""The adjacency list representation used to show who dislikes who."""


def divide_teams(dislikes: Graph) -> tuple[set[int], set[int]]:
    """
    Divides students into two teams, constrained by the dislikes graph.

    Returns:
        A tuple of sets that have the IDs of the students on that team.
    """
    # The queue of vertices and their associated team to visit next.
    # Each element is a tuple of (id, team index)
    q: deque[tuple[int, int]] = deque()

    # The running sets of each team. We keep both of them in a list so it's easy
    # to flip back and forth between the team that we are constructing as we traverse
    # the graph.
    teams: list[set[int]] = [set(), set()]

    # Keeps track of the nodes already seen
    seen: set[int] = set()

    # start it off by adding the first node
    all_keys = list(dislikes.keys())
    all_keys_s = set(all_keys)
    assert len(all_keys) > 0
    q.append((all_keys[0], 0))

    # Keep going until everyone has been assigned to a team.
    while (len(teams[0]) + len(teams[1])) < len(dislikes):
        # The graph might have unconnected components, which means we could drain the queue without
        # seeing every node. If that happens, just pick a node we haven't seen
        if len(q) == 0:
            candidate_nodes = list(all_keys_s - seen)
            q.append((candidate_nodes[0], 0))

        next_node, current_team = q.popleft()
        seen.add(next_node)
        # Add current node to some team
        teams[current_team].add(next_node)

        # Each neighbor is added to the team opposite the side of the current node.
        opposite_team = int(not current_team)

        for neighbor in dislikes[next_node]:
            # If one of the neighboring nodes has already been added to the current team,
            # then the bipartition is impossible.
            if neighbor in teams[current_team]:
                raise ValueError(
                    f"Impossible bipartition at node {neighbor}, current node is {next_node}"
                )
            teams[opposite_team].add(neighbor)
            if neighbor not in seen:
                q.append((neighbor, opposite_team))

    return (teams[0], teams[1])
