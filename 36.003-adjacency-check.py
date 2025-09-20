graph = [
    [1],
    [0, 2, 5, 4],
    [1, 4, 5],
    [],
    [5, 2, 1],
    [1, 2, 4],
]


def adjacent(graph, node1, node2):
    # for nbr in graph[node1]:
    #     if nbr == node2:
    #         return True
    # return False

    return node2 in graph[node1]


graph_alt = [set(nodes) for nodes in graph]


def adjacent_faster(graph, node1, node2):
    return node2 in graph[node1]
