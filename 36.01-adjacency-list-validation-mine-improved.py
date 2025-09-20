"""
# Adjacency List Validation

Given an adjacency list, graph, write a function that returns whether graph is a valid undirected graph, meaning that:
- Every node is between 0 and V-1.
- There are no self-loops: edges connecting a node to itself.
- There are no parallel edges: two edges connecting the same two nodes.
- If node1 appears in graph[node2], then node2 also appears in graph[node1].

Constraints:
graph.length ≤ 1000
graph[i].length ≤ 1000
"""


def valid_adjacency_list(graph):
    V = len(graph)

    sets = list()

    for node, neighbors in enumerate(graph):
        seen = set()

        for nbr in neighbors:
            # invalid node
            if nbr < 0 or nbr >= V:
                return False
            # self membership
            elif nbr == node:
                return False

            seen.add(nbr)

        # duplicate check (parallel edge check)
        if len(seen) != len(neighbors):
            return False

        sets.append(seen)

    # symmetry check
    for node in range(V):
        for val in sets[node]:
            if node not in sets[val]:
                return False

    return True


graph = [[1], [0]]
print(valid_adjacency_list(graph))

# => True
# This is a simple valid graph with two nodes connected by an edge.

# ------

graph = [[2], [0]]
print(valid_adjacency_list(graph))

# => False
# Node index 2 is invalid since there are only 2 nodes.

# ------

graph = [[0], []]
print(valid_adjacency_list(graph))

# => False
# Self-loop in node 0.

# ------

graph = [[1, 1], [0, 0]]
print(valid_adjacency_list(graph))

# => False
# Parallel edges between nodes 0 and 1.

# ------

graph = [[1], []]
print(valid_adjacency_list(graph))

# => False
# Node 0 has node 1 as a neighbor but not vice versa.


def run_tests():
    tests = [
        # Valid cases
        [[[1], [0]], True],  # Simple valid graph
        [[[1, 2], [0, 2], [0, 1]], True],  # Triangle graph
        [[], True],  # Empty graph
        [[[]], True],  # Single isolated node
        # Invalid node index cases
        [[[2], [0]], False],  # Node index too large
        [[[-1], []], False],  # Negative node index
        # Self-loop cases
        [[[0], []], False],  # Self loop
        [[[1], [1]], False],  # Self loop in second node
        # Parallel edge cases
        [[[1, 1], [0, 0]], False],  # Same edge twice from first node
        [[[1], [0, 2, 0], [1]], False],  # Same edge twice from second node
        # Unmatched edge cases
        [[[1], []], False],  # Edge only in one direction
        [[[1, 2], [0], []], False],  # Some edges missing their pairs
        [[[1], [2], [0]], False],  # Cycle with unmatched edges
    ]
    for graph, want in tests:
        got = valid_adjacency_list(graph)
        assert got == want, f"\nvalidate({graph}): got: {got}, want: {want}\n"


run_tests()
