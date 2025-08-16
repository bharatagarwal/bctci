"""
# Most Protected Node

Given the root of a non-empty binary tree, return the highest protection level of any node.

The protection level of a node is the minimum of four values:
- number of ancestors: dfs, on the way down 
- length of longest chain of descendants: dfs, on the way up
- number of nodes on same level to its left: bfs, along the queue
- number of nodes on the same level to its right: bfs, along the queue

Example:
            O
         /     \
        O       O
       / \     / \
      O   O   O   O
     / \   \   \   \
    O   O   O   O   O
   / \   \   \   \   \
  O   O   O   O   O   O
 /   / \     / \   \   \
O   O   O   O   O   O   O

Output: 2.
The protection level of each node is:
            0
         /     \
        0       0
       / \     / \
      0   1   1   0
     / \   \   \   \
    0   1   2   1   0
   / \   \   \   \   \
  0   1   0   1   1   0
 /   / \     / \   \   \
0   0   0   0   0   0   0

Constraints:

- The number of nodes is at most 10^5
- The height of the tree is at most 500
- The value at each node doesn't matter.
"""

from collections import defaultdict, deque
import math


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def most_protected_node(root):
    if not root:
        return 0

    # Map from node to its current minimum protection level
    protection = defaultdict(lambda: math.inf)
    nodes_per_level = defaultdict(int)
    node_to_index_in_level = {}

    # First pass: BFS to get depth and position in level
    Q = deque([(root, 0)])
    while Q:
        node, depth = Q.popleft()
        if not node:
            continue

        # Add node to its level
        nodes_per_level[depth] += 1
        # Store node's position in its level
        node_to_index_in_level[node] = nodes_per_level[depth] - 1

        # Update protection with ancestor count (depth)
        protection[node] = min(protection[node], depth)

        # Update protection with left counts
        protection[node] = min(
            protection[node], node_to_index_in_level[node]
        )

        Q.append((node.left, depth + 1))
        Q.append((node.right, depth + 1))

    # Second pass: DFS to get descendant heights
    # Passes current depth down the tree.
    # Passes subtree height up the tree.
    # Updates protection level of nodes in global map.
    def dfs(node, depth):
        if not node:
            return -1
        height = 1 + max(
            dfs(node.left, depth + 1), dfs(node.right, depth + 1)
        )

        protection[node] = min(protection[node], height)

        # Update protection with right counts
        protection[node] = min(
            protection[node],
            nodes_per_level[depth] - node_to_index_in_level[node] - 1,
        )

        return height

    dfs(root, 0)

    # Return highest protection level
    return max(protection.values())


def run_tests():
    # Example from the book
    root1 = Node(
        1,
        Node(
            2,
            Node(
                3,
                Node(4, Node(5, Node(6)), Node(7, Node(8), Node(9))),
                Node(10, Node(11)),
            ),
            Node(12, Node(13, Node(14, Node(15), Node(16)))),
        ),
        Node(
            17,
            Node(18, Node(19, Node(20, Node(21)))),
            Node(22, Node(23, Node(24, Node(25)))),
        ),
    )

    def perfect_tree(height):
        if height == 1:
            return Node(1)
        return Node(
            1, perfect_tree(height - 1), perfect_tree(height - 1)
        )

    tests = [
        (root1, 2),  # Book example (Example 1)
        (Node(1), 0),  # Single node (Example 2)
        # Linear tree (Example 3)
        (Node(1, Node(2, Node(3, Node(4)))), 0),
        (perfect_tree(1), 0),  # Perfect binary tree (Example 4)
        (perfect_tree(2), 0),  # Perfect binary tree (Example 5)
        (perfect_tree(3), 0),  # Perfect binary tree (Example 6)
        (perfect_tree(4), 1),  # Perfect binary tree (Example 7)
        (perfect_tree(5), 1),  # Perfect binary tree (Example 8)
        (perfect_tree(6), 2),  # Perfect binary tree (Example 9)
        (perfect_tree(7), 3),  # Perfect binary tree (Example 10)
        (perfect_tree(8), 3),  # Perfect binary tree (Example 11)
        (perfect_tree(9), 4),  # Perfect binary tree (Example 12)
    ]

    for i, (root, want) in enumerate(tests):
        got = most_protected_node(root)
        assert got == want, (
            f"\nExample {i + 1}: most_protected_node(): got: {got}, want: {want}\n"
        )
    print("ok")


run_tests()
