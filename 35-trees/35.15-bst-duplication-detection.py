import math

from binarytree import Node

example = Node(
    5, Node(2, None, Node(4)), Node(9, Node(9, None, Node(9)), Node(11))
)

""" 
# BST Duplication detection

Given the root of a binary search tree, determine if it contains any duplicate values.

Type of tree: le and re in respective subtrees


      __5____
     /       \
    2       __9
     \     /   \
      4   9     11
           \
            9

Makes sense to do inorder traversal
Keep track of previous, if same, return true

Constraints:

The number of nodes is at most 10^5
The height of the tree is at most 500
The value at each node is between 0 and 10^9

"""


def has_duplicate(root):
    if not root:
        return False

    previous = -math.inf
    dup = bool()

    def inorder(node):
        nonlocal previous, dup

        if not node:
            return

        if dup:
            return

        inorder(node.left)

        if node.val == previous:
            dup = True

        previous = node.val

        inorder(node.right)

    inorder(root)
    return dup


# Example 1 - BST with duplicates
"""
  __5____
 /       \
2       __9
 \     /   \
  4   9     11
       \
        9

"""
root1 = Node(
    5, Node(2, None, Node(4)), Node(9, Node(9, None, Node(9)), Node(11))
)

# Example 2 - empty tree
root2 = None

# Example 3 - single node
root3 = Node(1)

# Example 4 - BST without duplicates
"""
    __5__
   /     \
  2       8
 / \     / \
1   4   6   9
"""
root4 = Node(5, Node(2, Node(1), Node(4)), Node(8, Node(6), Node(9)))

tests = [
    (root1, True),  # Has duplicates (9s)
    (root2, False),  # Empty tree has no duplicates
    (root3, False),  # Single node has no duplicates
    (root4, False),  # No duplicates
]

for i, (root, want) in enumerate(tests):
    got = has_duplicate(root)
    print(f"has_duplicate(root{i + 1}): got: {got}, want: {want}")
    assert got == want
