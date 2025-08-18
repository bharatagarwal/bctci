class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
# Aligned Chain

Given a binary tree, 
we say a node is aligned if its value is equal to its depth (distance from root). 

aligned - check if value is same as depth
need to track depth, something to pass down via parameter

A descendant chain is a sequence of nodes where each node is the parent of the next node.
pass up length of descendent chain, via return value

longest descendent chain - store a global variable for length
compare length and store the highest

Return the length of the longest descendant chain of aligned nodes. The chain does not need to start at the root.




Example:
                7
               / \
              1   3
             / \   \
            2   8   2
           / \     / \
          4   3   3   3

Output: 3
The aligned nodes are the circled ones:
Depth
  0             7
               / \
  1          (1)   3
             / \   \
  2        (2)  8  (2)
           / \     / \
  3       4  (3) (3) (3)

The longest descendant chain of aligned nodes is 1 -> 2 -> 3 on the left
subtree.

Constraints:

- The number of nodes is at most 10^5
- The height of the tree is at most 500
- Each node has a value between 0 and 10^9

"""


def is_aligned(node, depth):
    return node.val == depth


def longest_aligned_chain(node):
    # global variable reqd because longest chain
    # can exclude root node
    result = 0

    def longest_aligned_at(node, depth):
        # must be declared at the beginning of the function
        nonlocal result

        if not node:
            return 0

        left_chain = longest_aligned_at(node.left, depth + 1)
        right_chain = 1 + longest_aligned_at(node.right, depth + 1)

        # chain breaks if current is not aligned
        current_chain_len = 0

        if is_aligned(node, depth):
            current_chain_len = 1 + max(left_chain, right_chain)
            result = max(result, current_chain_len)

        return current_chain_len

    longest_aligned_at(node, 0)
    return result


n1 = Node(4)
n2 = Node(3)
n6 = Node(3)
n7 = Node(3)


n3 = Node(2, n1, n2)
n4 = Node(8)

n8 = Node(2, n6, n7)

n5 = Node(1, n3, n4)
n9 = Node(3, n8, None)

root = Node(7, n5, n9)

print(longest_aligned_chain(root))
