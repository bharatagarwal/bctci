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


def test_if_leaf():
    # Test null node
    result = if_leaf(None)
    expected = False
    print(f"if_leaf(None) = {result}, expected = {expected}")
    assert result == expected

    # Test leaf node
    leaf = Node(1)
    result = if_leaf(leaf)
    expected = True
    print(f"if_leaf(leaf node) = {result}, expected = {expected}")
    assert result == expected

    # Test node with only left child
    node_left = Node(2, Node(3))
    result = if_leaf(node_left)
    expected = False
    print(
        f"if_leaf(node with left child) = {result}, expected = {expected}"
    )
    assert result == expected

    # Test node with only right child
    node_right = Node(4, None, Node(5))
    result = if_leaf(node_right)
    expected = False
    print(
        f"if_leaf(node with right child) = {result}, expected = {expected}"
    )
    assert result == expected

    # Test node with both children
    node_both = Node(6, Node(7), Node(8))
    result = if_leaf(node_both)
    expected = False
    print(
        f"if_leaf(node with both children) = {result}, expected = {expected}"
    )
    assert result == expected


def test_children():
    # Test null node
    result = children(None)
    expected = []
    print(f"children(None) = {result}, expected = {expected}")
    assert result == expected

    # Test leaf node
    leaf = Node(1)
    result = children(leaf)
    expected = []
    print(f"children(leaf node) = {result}, expected = {expected}")
    assert result == expected

    # Test node with only left child
    node_left = Node(2, Node(3))
    result = children(node_left)
    expected = [3]
    print(
        f"children(node with left child) = {result}, expected = {expected}"
    )
    assert result == expected

    # Test node with only right child
    node_right = Node(4, None, Node(5))
    result = children(node_right)
    expected = [5]
    print(
        f"children(node with right child) = {result}, expected = {expected}"
    )
    assert result == expected

    # Test node with both children
    node_both = Node(6, Node(7), Node(8))
    result = children(node_both)
    expected = [7, 8]
    print(
        f"children(node with both children) = {result}, expected = {expected}"
    )
    assert result == expected


def test_grandchildren():
    # Test null node
    result = grandchildren(None)
    expected = []
    print(f"grandchildren(None) = {result}, expected = {expected}")
    assert result == expected

    # Test leaf node
    leaf = Node(1)
    result = grandchildren(leaf)
    expected = []
    print(f"grandchildren(leaf node) = {result}, expected = {expected}")
    assert result == expected

    # Test node with children but no grandchildren
    node_no_grandchildren = Node(1, Node(2), Node(3))
    result = grandchildren(node_no_grandchildren)
    expected = []
    print(
        f"grandchildren(node with children but no grandchildren) = {result}, expected = {expected}"
    )
    assert result == expected

    # Test node with left child having children
    node_left_grandchildren = Node(1, Node(2, Node(4), Node(5)))
    result = grandchildren(node_left_grandchildren)
    expected = [4, 5]
    print(
        f"grandchildren(node with left child having children) = {result}, expected = {expected}"
    )
    assert result == expected

    # Test node with right child having children
    node_right_grandchildren = Node(1, None, Node(3, Node(6), Node(7)))
    result = grandchildren(node_right_grandchildren)
    expected = [6, 7]
    print(
        f"grandchildren(node with right child having children) = {result}, expected = {expected}"
    )
    assert result == expected

    # Test node with both children having children
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    result = grandchildren(root)
    expected = [4, 5, 6, 7]
    print(
        f"grandchildren(node with both children having children) = {result}, expected = {expected}"
    )
    assert result == expected

    # Test node with partial grandchildren
    partial = Node(1, Node(2, Node(4), None), Node(3, None, Node(7)))
    result = grandchildren(partial)
    expected = [4, 7]
    print(
        f"grandchildren(node with partial grandchildren) = {result}, expected = {expected}"
    )
    assert result == expected


if __name__ == "__main__":
    test_if_leaf()
    test_children()
    test_grandchildren()
    print("All tests passed!")
