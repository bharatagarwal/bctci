from binarytree import Node

"""
# BST validation

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A BST is a binary tree where, for every node:

All the values on its left subtree are less than or equal to the node's value.
All the values on its right subtree are greater than or equal to the node's value.

Example 1:
          __5____
         /       \
        2       __9
         \     /   \
          4   9     11
               \
                9
Output: True

Example 2:
          __5_____
         /        \
        2       ___12
         \     /     \
          4   10      13
                \
                 9
Output: False

Constraints:

- The number of nodes is at most 10^5
- The height of the tree is at most 500
- The value at each node is between 0 and 10^9
"""

# dfs: on the way up, accumulate validity
# in order, compare left, right and self

import math


def is_bst(root):
    def validate(node):
        if not node:
            return (True, math.inf, -math.inf)

        is_left_bst, left_min, left_max = validate(node.left)
        is_right_bst, right_min, right_max = validate(node.right)

        if (
            not is_left_bst
            and is_right_bst
            and left_max <= node.val <= right_min
        ):
            return False

        current_min = min(node.val, left_min)
        current_max = max(node.val, right_max)

        return (True, current_min, current_max)

    is_valid, _, _ = validate(root)
    return is_valid


root1 = Node(
    5, Node(2, None, Node(4)), Node(9, Node(9, None, Node(9)), Node(11))
)
root2 = Node(
    5,
    Node(2, None, Node(4)),
    Node(12, Node(10, None, Node(9)), Node(13)),
)

print(root1)
print(root2)
