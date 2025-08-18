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


def distance(first, second):
    return abs(first - second)


def find_nearest(root, key):
    nearest: "Node"
    closest = root
    dist: int

    cur = root

    while cur:
        if cur.val == key:
            return cur.val

        if cur.val < closest.val:
            closest = cur

        if cur.left:
            dist = distance(cur.left.val, key)
            nearest = cur.left

        if cur.right:
            ldist = distance(cur.right.val, key)
            if ldist < dist:
                dist = ldist
                nearest = cur.right

        cur = nearest


# - look at current, see diff
#     - bw left and right, go to side which is closer
