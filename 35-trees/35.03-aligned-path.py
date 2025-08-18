class Node:
    """Node for a binary tree, with val and optional left/right"""

    def __init__(
        self,
        val,
        left=None,
        right=None,
    ):
        self.val = val
        self.left = left
        self.right = right


"""
# Aligned path

Given a binary tree, we say a node is aligned if its value is equal to its depth (distance from root).

Return the length of the longest path of aligned nodes. A path can start and end at any node.

Example:
                7
               / \
              1   4
             / \   \
            2   8   2
           / \     / \
          4   3   3   3

Output: 3



                        7

                1               2

            3       4       1       3

The aligned nodes are the circled ones:
Depth
  0             7
               / \
  1          (1)   3
             / \   \
  2        (2)  8  (2)
           / \     / \
  3       4  (3) (3) (3)

There are two paths of aligned nodes with maximum length: 1 -> 2 -> 3 on the
left subtree, and 3 -> 2 -> 3 on the right subtree.
"""


def is_aligned(node, depth):
    return node.val == depth


def longest_path(node):
    result = 0
    left = 0
    right = 0

    def longest_path_at(node, depth):
        nonlocal result, left, right

        if not node:
            return 0

        current_longest = 0
        left = longest_path_at(node.left, depth + 1)

        if is_aligned(node, depth):
            current_longest = 1 + max(left, right)
            result = max(result, current_longest)

        right = longest_path_at(node.right, depth + 1)

        return current_longest

    longest_path_at(node, 0)
    return result


n1 = Node(2, Node(4), Node(3))
n2 = Node(1, n1, Node(8))

n3 = Node(2, Node(3), Node(3))
n4 = Node(3, None, n3)
n5 = Node(7, n2, n4)
print(longest_path(n5))
