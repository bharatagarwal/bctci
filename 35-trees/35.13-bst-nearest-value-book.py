"""
# BST Nearest Value

Given the root of a non-empty binary search tree and a value, target, find the closest value to target in the tree. In case of a tie, return the smaller value.

Example 1:
              5
            /    \
           2      9
            \    / \
             4  9   11
                 \
                  9
target = 4
Output: 4

Example 2:
Same tree, target = 3
Output: 2

Constraints:

- 1 <= number of nodes <= 10^4
- -10^9 <= node.val <= 10^9
- -10^9 <= target <= 10^9
- The tree is a valid binary search tree
"""

from collections import deque
from math import inf

from binarytree import Node

root = Node(
    8,
    Node(6, Node(5, Node(2), Node(6)), Node(8, Node(8), Node(8))),
    Node(12, Node(10, Node(9))),
)

"""
        ______8_____
       /            \
    __6__           _12
   /     \         /
  5       8       10
 / \     / \     /
2   6   8   8   9
"""


def find_closest(root, target):
    """
    >>> root = Node(8, Node(6, Node(5, Node(2), Node(6)), Node(8, Node(8), Node(8))), Node(12, Node(10, Node(9))))
    >>> find_closest(root, 7)
    6
    """
    current = root
    next_above, next_below = inf, -inf

    while current:
        if current.val == target:
            return current.val
        elif current.val > target:
            next_above = current.val
            current = current.left
        else:
            next_below = current.val
            current = current.right

    diff_above = abs(next_above - target)
    diff_below = abs(next_below - target)

    if diff_below <= diff_above:
        return next_below
    else:
        return next_above

    return next_below


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
    5,
    Node(2, None, Node(4)),
    Node(9, Node(9, None, Node(9)), Node(11)),
)

# Test 2: Empty tree
root2 = None

# Test 3: Single node
root3 = Node(1)

# Test 4: Perfect BST
"""
    __4__
   /     \
  2       6
 / \     / \
1   3   5   7

"""
root4 = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))

"""
# Test 5: Unbalanced BST

      __5
     /
    3
   / \
  2   4
 /
1
"""
root5 = Node(5, Node(3, Node(2, Node(1), None), Node(4)), None)


# Example from the book
"""
        ______8_____
       /            \
    __6__           _12
   /     \         /
  5       8       10
 / \     / \     /
2   6   8   8   9

"""

root6 = Node(
    8,
    Node(6, Node(5, Node(2), Node(6)), Node(8, Node(8), Node(8))),
    Node(12, Node(10, Node(9), None), None),
)

tests = [
    (root1, 6, 5),  # Closest to 6 is 5
    (root1, 9, 9),  # Exact match
    (root1, 3, 2),  # Closest to 3 is 2
    (root1, 4, 4),  # Exact match
    (root2, 1, -inf),  # Empty tree
    (root3, 1, 1),  # Single node, exact match
    (root3, 2, 1),  # Single node, closest is 1
    (root4, 5, 5),  # Perfect BST, exact match
    (root4, 8, 7),  # Perfect BST, closest is 7
    (root5, 1, 1),  # Unbalanced BST, exact match at leaf
    (root5, 5, 5),  # Unbalanced BST, exact match at root
    (root5, 6, 5),  # Unbalanced BST, closest is 5
    (root6, 9, 9),
    (root6, 13, 12),
    (root6, 1, 2),
    (root6, 8, 8),
    (root6, 6, 6),
    (root6, 7, 6),
    (root6, 11, 10),
    (root6, 4, 5),
]

for i, (root, target, want) in enumerate(tests):
    got = find_closest(root, target)
    assert got == want, (
        f"\nfind_closest(root{i + 1}, {target}): got: {got}, want: {want}\n"
    )
