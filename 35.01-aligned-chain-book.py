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
# Aligned Chain

Given a binary tree, we say a node is aligned if its value is the same as its depth. Return the length of the longest descendent chain of aligned nodes. The chain need not start at the root.

               7         :0
          1         3    :1
       2     8    2      :2
     4  3        3  3    :3
.
"""

            7
        3
    2
  4   3


"""
     1    : 1
  2    8  : 2
 4 3      : 3
"""

longest_chain = []
current_chain = []
"""
start at root node
     if aligned, add to current chain
          check longest chain, if longer, replace
     if not aligned

look at left node
     going down uses parameter
     if aligned, add to current chain
          check longest chain, if longer, replace
     if not aligned, move on

look at right node,
     going down uses parameter
     if aligned, add to current chain
          check longest chain, if longer, replace
     if not aligned, move on

if both left and right are not aligned, break chain
 -- going up uses return value
"""


def longest_aligned_chain(root):
    result = 0
    
    def visit(node, depth):
        nonlocal result

        if not node:
            # zero base case as opposed to just 'return' to # account for return value of outer method
            return 0 

        # postorder traversal
        # post in context of root

        left_chain = visit(node.left, depth + 1)
        right_chain = visit(node.right, depth + 1)

        # building up, starting from leaf node
        current_chain = 0

        # start incrementing
        # if neither has node.val, then chain remains 0
        if node.val == depth:
            current_chain = 1 + max(left_chain, right_chain)
            result = max(result, current_chain)

        return current_chain

    visit(root, 0)
    return result


# Level 4 (bottom-most)
node_4_left = Node(4)
node_3_left = Node(3)
node_3_right_left = Node(3)
node_3_right_right = Node(3)

# Level 3
node_2_left = Node(2, node_4_left, node_3_left)
node_8 = Node(8)
node_2_right = Node(2, node_3_right_left, node_3_right_right)

# Level 2
node_1 = Node(1, node_2_left, node_8)
node_3 = Node(3, node_2_right, None)

# Level 1 (root)
root = Node(7, node_1, node_3)

print(longest_aligned_chain(root))
