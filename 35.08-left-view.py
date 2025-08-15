"""
# Left view

Given the root of a binary tree, return its left view.

The left view is an array with the value of the first node on each layer, ordered from top to bottom.


                5

        2               9
    .       6       9       8
  .   .                1
"""

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def left_view(root):
    res = []
    covered = set()

    q = deque()
    q.append((root, 0))

    while q:
        current, depth = q.popleft()

        if not current:
            continue

        if depth not in covered:
            covered.add(depth)
            res.append(current.val)

        q.append((current.left, depth + 1))
        q.append((current.right, depth + 1))

    return res


root = Node(
    5,
    Node(2, None, Node(6)),
    Node(9, Node(9, None, Node(1)), Node(8)),
)

print(left_view(root))
