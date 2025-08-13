"""
# Triangle Count

Given the root of a binary tree, return the number of triangles. A triangle is a set of three distinct nodes, a, b, and c, where:

- a is the lowest common ancestor of b and c.
- b and c have the same depth.
- the path from a to b only consists of left children (the nodes in the path can have right children).
- the path from a to c only consists of right children (the nodes in the path can have left children).

Example 1:
         1                  : 0
     /       \              
    1         2             : 1
     \       / \
      3     4   5           : 2
     / \   /     \
    6   7 8       9         : 3


              1
      1               2
  .       3       4       5
.   .   6   7   8   .   .   9

Output: 4.
The triangles are: (0, 1, 2), (3, 6, 7), (2, 4, 5), (2, 8, 9).

Example 2:
      0
   /      \
  1        4
 /  \       \
2    3       5
Output: 3.
The triangles are: (0, 1, 4), (1, 2, 3), (0, 2, 5).

Constraints:

- The number of nodes is at most 10^5
- The height of the tree is at most 500
- The value at each node doesn't matter.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def print_triangles(root):
    if not (root.left or root.right):
        return

    def process_triangles(node, depth_left, depth_right):
        if not node:
            return

        if depth_left == depth_right:
            print((node.val, node.left.val, node.right.val))

        if node.left:
            process_triangles(node.left, depth_left + 1, depth_right)
        if node.right:
            process_triangles(node.left, depth_left + 1, depth_right)

    left, right = 0, 0

    if root.left:
        left += 1

    if root.right:
        right += 1

    process_triangles(root, left, right)


# fmt: off
root = Node(1,
      Node(1,
          None,
          Node(3,
              Node(6),
              Node(7)
          )
      ),
      Node(2,
          Node(4,
              Node(8),
              None
          ),
          Node(5,
              None,
              Node(9)
          )
      )
  )
# fmt:on
print_triangles(root)
