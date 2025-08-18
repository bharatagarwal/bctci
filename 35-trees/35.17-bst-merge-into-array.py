from binarytree import Node

root1 = Node(5, Node(2, None, Node(4)), Node(9, Node(9), Node(11)))

root2 = Node(3, Node(2, Node(1)), Node(7, Node(6), Node(8)))

print(root1)
print(root2)
"""
# BST Merge Into Array

Given the roots of two binary search trees, return an array containing all elements from both trees in sorted order. The trees may contain duplicate values.

Example:
root1 =
              5
            /    \
           2      9
            \    / \
             4  9   11
root2 =
              3
            /    \
           2      7
          /      / \
         1      6   8

Output: [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 9, 11]

Example 2:
root1 =
              2
            /    \
           2      2

root2 =
              2
            /    \
           2      2

Output: [2, 2, 2, 2, 2, 2]


Constraints:

- The number of nodes of each tree is at most 10^5
- The height of each tree is at most 500
- The value at each node is between 0 and 10^9

"""


def merge(root1, root2):
    res1 = list()
    res2 = list()

    def traverse(node, res):
        if not (node):
            return

        traverse(node.left, res)
        res.append(node.val)
        traverse(node.right, res)

    traverse(root1, res1)
    traverse(root2, res2)

    merged = []
    i = j = 0

    while i < len(res1) and j < len(res2):
        if res1[i] <= res2[j]:
            merged.append(res1[i])
            i += 1
        else:
            merged.append(res2[j])
            j += 1

    merged.extend(res1[i:])
    merged.extend(res2[j:])

    return merged


print(merge(root1, root2))  # => [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 9, 11]
