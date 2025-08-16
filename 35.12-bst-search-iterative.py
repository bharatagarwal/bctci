"""
# BST Search

A binary search tree (BST) is a binary tree if, for every node:

- All the values on its left subtree are less than or equal to the node's value.
- All the values on its right subtree are greater than or equal to the node's value.
- Given the root of a binary search tree and a value, target, return true if the tree contains the target value, and false otherwise.

Example 1:
              5
            /    \
           2      9
            \    / \
             4  9   11
                 \
                  9
target = 4
Output: true

Example 2:
Same tree, target = 3
Output: false
The value 3 does not exist in the tree.

Constraints:

- The number of nodes is at most 10^5
- The value at each node is between 0 and 10^9
"""


# risks hitting stack height limit of 1000
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find(root, target):
    cur_node = root

    while cur_node:
        if cur_node.val == target:
            return True
        elif cur_node.val > target:
            cur_node = cur_node.left
        else:
            cur_node = cur_node.right

    return False


def run_tests():
    root1 = Node(
        5,
        Node(2, None, Node(4)),
        Node(9, Node(9, None, Node(9)), Node(11)),
    )

    root2 = None

    root3 = Node(1)

    root4 = Node(
        4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7))
    )

    root5 = Node(5, Node(3, Node(2, Node(1), None), Node(4)), None)

    tests = [
        (root1, 6, False),
        (root1, 9, True),
        (root1, 3, False),
        (root1, 4, True),
        (root2, 1, False),  # Empty tree
        (root3, 1, True),  # Single node, target exists
        (root3, 2, False),  # Single node, target doesn't exist
        (root4, 5, True),  # Perfect BST, target exists
        (root4, 8, False),  # Perfect BST, target doesn't exist
        (root5, 1, True),  # Unbalanced BST, target exists at leaf
        (root5, 5, True),  # Unbalanced BST, target exists at root
        (root5, 6, False),  # Unbalanced BST, target doesn't exist
    ]

    for i, (root, target, want) in enumerate(tests):
        got = find(root, target)
        print(f"{target}): got: {got}, want: {want}")
        assert got == want


run_tests()
