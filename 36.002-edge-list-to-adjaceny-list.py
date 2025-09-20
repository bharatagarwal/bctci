from pprint import pprint

V = 6

edges = [
    [0, 1],
    [1, 2],
    [4, 5],
    [2, 4],
    [1, 5],
    [1, 4],
    [2, 5],
]

graph = [list() for _ in range(V)]

for node1, node2 in edges:
    graph[node1].append(node2)
    graph[node2].append(node1)

pprint(graph)
