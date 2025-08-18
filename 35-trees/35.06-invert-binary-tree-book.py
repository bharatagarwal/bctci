"""
# Invert binary tree

Given a binary tree, invert it by modifying the left and right pointers (do not modify the values in the nodes or create new nodes).

The left subtree of the root should become the right subtree inverted, and the right subtree of the root should become the left subtree inverted.

Return the root of the tree after modifying it.

Example:
     1
   /   \
  6     7
 / \   /
4  11 2
 \     \
  5     9

Output:
     1
   /   \
  7     6
   \   / \
    2 11  4
   /     /
  9     5

Constraints:

- The number of nodes is at most 10^5
- The height of the tree is at most 500
- Each node has a value between 0 and 10^9
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def reverse(node):
    if not node:
        return

    node.left = reverse(node.right)
    node.right = reverse(node.left)

    return node


n1 = Node(4, None, Node(5))
n2 = Node(6, n1, Node(11))

n3 = Node(2, None, Node(9))
n4 = Node(7, n3)

root = Node(1, n2, n4)

inverted = reverse(root)
breakpoint()
