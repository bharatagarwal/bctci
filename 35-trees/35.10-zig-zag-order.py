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

    current_row = []
    current_level = 0

    while q:
        current, level = q.popleft()

        if not current:
            continue

        if level > current_level:
            if current_level % 2 == 0:
                res.extend(current_row)
            else:
                res.extend(reversed(current_row))

            # add first row to current level
            current_row = []
            current_level = level
        else:
            current_row.append(current.val)

        # This is bad, it's repetition
        # res.append(current.val)

        q.append((current.left, level + 1))
        q.append((current.right, level + 1))

    # haven't flushed the last level
    # did, but removed

    return res


root = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(6)))

print(zig_zag(root))
