from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    q = deque()
    q.append((root, 0))

    while len(q) != 0:
        node, depth = q.popleft()

        if not node:
            continue

        print("val:", node.val, "depth", depth)

        q.append((node.left, depth + 1))
        q.append((node.right, depth + 1))


# Build the tree
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
node_6 = Node(6)
node_7 = Node(7)
node_8 = Node(8)
node_9 = Node(9)

node_1.left = node_2
node_1.right = node_3
node_2.left = node_4
node_2.right = node_5
node_3.left = node_6
node_4.left = node_7
node_4.right = node_8
node_6.right = node_9

root = node_1

"""
Level order traversal:

            1
       /         \
      2           3
    /   \       /
   4     5     6
 /  \           \
7    8           9
"""

level_order(root)
