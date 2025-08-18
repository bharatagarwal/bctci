"""
# Zig-zag order

Given a binary tree, return the values of all its nodes in zig-zag order. 

This is similar to a level-order traversal but alternating the direction of the nodes at each level. 

Nodes at even depth are ordered left to right, and nodes at odd depth are ordered right to left.

Example:

Input:
    1
   / \
  2   3
 / \   \
4   5   6

Output: [1, 3, 2, 4, 5, 6]
"""

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zig_zag(root):
    res = list()
    q = deque()

    q.append((root, 0))
    current_level = []
    current_depth = 0

    while q:
        current, depth = q.popleft()

        if not current:
            continue

        if depth > current_depth:
            if current_depth % 2 == 0:
                res.extend(current_level)
            else:
                res.extend(current_level[::-1])

            current_level = list()
            current_depth = depth

        current_level.append(current.val)
        q.append((current.left, depth + 1))
        q.append((current.right, depth + 1))

    if current_depth % 2 == 0:
        res.extend(current_level)
    else:
        res.extend(current_level[::-1])

    return res


root = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(6)))

print(zig_zag(root))
