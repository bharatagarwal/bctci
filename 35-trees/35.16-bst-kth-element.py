import math

from binarytree import Node

example = Node(5, Node(2, None, Node(4)), Node(9, Node(9), Node(11)))

print(example)

"""
# BST k-th element

Given the root of a binary search tree with n nodes, find the k-th smallest element (0-indexed), where 0 ≤ k ≤ n-1.

  __5__
 /     \
2       9
 \     / \
  4   9   11

k = 4 => 9
k = 0 => 2

The number of nodes is at most 10^5
The height of the tree is at most 500
The value at each node is between 0 and 10^9
0 ≤ k ≤ n-1
"""


def kth_smallest(root, k):
    index = 0
    found = bool()
    res = -math.inf

    def traverse(node):
        nonlocal index, res, found

        if not node or found:
            return

        traverse(node.left)

        if index == k:
            found = True
            res = node.val

        index += 1

        traverse(node.right)

    traverse(root)

    if res == -math.inf:
        return "Not found"

    return res


print(kth_smallest(example, 4))  # = > 9
print(kth_smallest(example, 0))  # => 2
