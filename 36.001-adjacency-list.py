graph = [
    [1],
    [0, 2, 5, 4],
    [1, 4, 5],
    [],
    [5, 2, 1],
    [1, 2, 4],
]


def num_nodes(graph):
    print("nodes:")
    return len(graph)


def num_edges(graph):
    count = 0

    for node in graph:
        count += len(node)

    print("edges:")
    return count // 2


def degree(graph, node):
    print("degree:")
    return len(graph[node])


def print_neighbours(graph, node):
    print("neighbours:")

    for nbr in graph[node]:
        print(nbr)


print(num_nodes(graph))
print(num_edges(graph))
print(degree(graph, 1))
print_neighbours(graph, 1)
