import pytest


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


# Given a pointer to a specific node in a tree, node, that # - might be null
# - might be root


# a. return whether it is a leaf


def if_leaf(node):
    if not node:
        return False

    if node.left or node.right:
        return False

    return True


# b. return the values of its children as an array of at-most 2


def children(node):
    if not node:
        return []

    values = []

    # if node.left:
    #     values.append(node.left.val)

    # if node.right:
    #     values.append(node.right.val)

    for child in [node.left, node.right]:
        if child:
            values.append(child.val)

    return values


# c. return the values of its grandchildren as an array of length at most 4.
def grandchildren(node):
    if not node:
        return []

    values = []

    # if node.left:
    #     if node.left.left:
    #         values.append(node.left.left.val)

    #     if node.left.right:
    #         values.append(node.left.right.val)

    # if node.right:
    #     if node.right.left:
    #         values.append(node.right.left.val)

    #     if node.right.right:
    #         values.append(node.right.right.val)

    for child in [node.left, node.right]:
        if child:
            for grandchild in [child.left, child.right]:
                if grandchild:
                    values.append(grandchild.val)

    return values


# d. return the size of the node's subtree.
# A node's subtree includes itself and all of its descendants.
# The size of a tree is the number of nodes present in the tree.
def size(node):
    if not node:
        return 0

    return 1 + size(node.left) + size(node.right)


partial = Node(
    1,
    Node(
        2,
        Node(4, Node(5)),
        None,
    ),
    Node(3, None, Node(7)),
)

print(size(partial))


# e. Return the height of its subtree.
def height(node):
    if not node:
        return 0

    return max(
        height(node.left) + 1,
        height(node.right) + 1,
    )


print(height(partial))
