"""
# Most Protected Node

Given the root of a non-empty binary tree, return the highest protection level of any node.

The protection level of a node is the minimum of four values:
- number of ancestors: dfs, on the way down 
- length of longest chain of descendants: dfs, on the way up
- number of nodes on same level to its left: bfs, along the queue
- number of nodes on the same level to its right: bfs, along the queue

Example:
            O
         /     \
        O       O
       / \     / \
      O   O   O   O
     / \   \   \   \
    O   O   O   O   O
   / \   \   \   \   \
  O   O   O   O   O   O
 /   / \     / \   \   \
O   O   O   O   O   O   O

Output: 2.
The protection level of each node is:
            0
         /     \
        0       0
       / \     / \
      0   1   1   0
     / \   \   \   \
    0   1   2   1   0
   / \   \   \   \   \
  0   1   0   1   1   0
 /   / \     / \   \   \
0   0   0   0   0   0   0

Constraints:

- The number of nodes is at most 10^5
- The height of the tree is at most 500
- The value at each node doesn't matter.
"""

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def most_protected_node(root):
    state = dict()

    def longest_chain(node, level):
        if not node:
            return -1

        state[node] = {"ancestors": level}

        d_left = longest_chain(node.left, level + 1)
        d_right = longest_chain(node.right, level + 1)

        state[node]["descendants"] = max(d_left, d_right) + 1
        return max(d_left, d_right) + 1

    def store_left_right(nodes):
        length = len(nodes)
        for i, node in enumerate(nodes):
            state[node]["left"] = i
            state[node]["right"] = (length - 1) - i

    def bfs(root):
        q = deque()
        q.append((root, 0))

        cur_level = 0
        cur_row = list()

        while q:
            node, level = q.popleft()

            if not node:
                continue

            if level > cur_level:
                store_left_right(cur_row)
                cur_row = []
                cur_level = level

            cur_row.append(node)

            q.append((node.left, level + 1))
            q.append((node.right, level + 1))

        store_left_right(cur_row)

    longest_chain(root, 0)
    bfs(root)
    return max(
        [min(node_state.values()) for node_state in state.values()]
    )


# Bottom level (level 5) - 7 nodes
n29 = Node(0)  # leftmost
n30 = Node(0)
n31 = Node(0)
n32 = Node(0)
n33 = Node(0)
n34 = Node(0)
n35 = Node(0)  # rightmost

# Level 4 - 6 nodes
n23 = Node(0, n29, None)  # has only left child
n24 = Node(0, n30, n31)  # has both children
n25 = Node(0, None, None)  # no children (leaf)
n26 = Node(0, n32, n33)  # has both children
n27 = Node(0, None, n34)  # has only right child
n28 = Node(0, None, n35)  # has only right child

# Level 3 - 5 nodes
n18 = Node(0, n23, n24)  # has both children
n19 = Node(0, None, n25)  # has only right child
n20 = Node(0, None, n26)  # has only right child
n21 = Node(0, None, n27)  # has only right child
n22 = Node(0, None, n28)  # has only right child

# Level 2 - 4 nodes
n14 = Node(0, n18, n19)  # has both children
n15 = Node(0, None, n20)  # has only right child
n16 = Node(0, None, n21)  # has only right child
n17 = Node(0, None, n22)  # has only right child

# Level 1 - 2 nodes
n12 = Node(0, n14, n15)  # has both children
n13 = Node(0, n16, n17)  # has both children

# Root (level 0)
root = Node(0, n12, n13)

print(most_protected_node(root))


def run_tests():
    # Example from the book
    root1 = Node(
        1,
        Node(
            2,
            Node(
                3,
                Node(4, Node(5, Node(6)), Node(7, Node(8), Node(9))),
                Node(10, Node(11)),
            ),
            Node(12, Node(13, Node(14, Node(15), Node(16)))),
        ),
        Node(
            17,
            Node(18, Node(19, Node(20, Node(21)))),
            Node(22, Node(23, Node(24, Node(25)))),
        ),
    )

    def perfect_tree(height):
        if height == 1:
            return Node(1)
        return Node(
            1, perfect_tree(height - 1), perfect_tree(height - 1)
        )

    tests = [
        (root1, 2),  # Book example (Example 1)
        (Node(1), 0),  # Single node (Example 2)
        # Linear tree (Example 3)
        (Node(1, Node(2, Node(3, Node(4)))), 0),
        (perfect_tree(1), 0),  # Perfect binary tree (Example 4)
        (perfect_tree(2), 0),  # Perfect binary tree (Example 5)
        (perfect_tree(3), 0),  # Perfect binary tree (Example 6)
        (perfect_tree(4), 1),  # Perfect binary tree (Example 7)
        (perfect_tree(5), 1),  # Perfect binary tree (Example 8)
        (perfect_tree(6), 2),  # Perfect binary tree (Example 9)
        (perfect_tree(7), 3),  # Perfect binary tree (Example 10)
        (perfect_tree(8), 3),  # Perfect binary tree (Example 11)
        (perfect_tree(9), 4),  # Perfect binary tree (Example 12)
    ]

    for i, (root, want) in enumerate(tests):
        got = most_protected_node(root)
        assert got == want, (
            f"\nExample {i + 1}: most_protected_node(): got: {got}, want: {want}\n"
        )
    print("ok")


run_tests()
