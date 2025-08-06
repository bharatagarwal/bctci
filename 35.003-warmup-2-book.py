class Node:
    def __init__(
        self,
        id,
        parent,
        left=None,
        right=None,
    ):
        self.id = id
        self.parent = parent
        self.left = left
        self.right = right


# Given a non-null node in the tree, node, which might or might not be the root, implement the following functions:

# a. return whether it is the root


def is_root(node):
    return not node.parent


# b. return the id of its ancestors as an array


def ancestors_iterative(node):
    ids = []

    while node.parent:
        node = node.parent
        ids.append(node.id)

    return ids


# c. Return the depth of the node


def depth_iterative(node):
    result = 0

    while node.parent:
        node = node.parent
        result += 1

    return result


"""
 d. 
 Given two non-null nodes from the same tree, 
    node1 and node2, 

return the ID of their lowest common ancestor. 

The deepest node in the tree which is a non-strict ancestor of both.

'Non-strict' means that a node is considered its own ancestor. For instance, in Figure 4, LCA(j, f) = f.

"""


def LCA(node1, node2):
    depth1 = depth_iterative(node1)
    depth2 = depth_iterative(node2)

    while depth1 > depth2:
        node1 = node1.parent
        depth1 -= 1

    while depth2 > depth1:
        node2 = node2.parent
        depth2 -= 1

    while node1.id != node2.id:
        node1 = node1.parent
        node2 = node2.parent

    return node1.id


"""
Given two non-null nodes from the same tree, return the distance between them. 

The sequence of edges between two nodes is called a path, and the number of edges in the path is the distance between the two nodes. 

Note that, in a binary tree, the path between any two nodes is unique.
"""


def distance(node1, node2):
    lca_id = LCA(node1, node2)

    steps = 0

    while node1.id != lca_id:
        node1 = node1.parent
        steps += 1

    while node2.id != lca_id:
        node2 = node2.parent
        steps += 1

    return steps


# Set up test tree structure:
#         1 (root)
#        / \
#       2   3
#      /   / \
#     4   5   6

root = Node(1, None)
node_2 = Node(2, root)
node_3 = Node(3, root)
node_4 = Node(4, node_2)
node_5 = Node(5, node_3)
node_6 = Node(6, node_3)

# Set up the tree connections
root.left = node_2
root.right = node_3
node_2.left = node_4
node_3.left = node_5
node_3.right = node_6

print(is_root(root))
print(is_root(node_2))

print(ancestors_iterative(node_6))
print(ancestors_iterative(node_4))
print(depth_iterative(node_2))
print(depth_iterative(node_4))
print(depth_iterative(root))
print(LCA(node_5, node_3))
print(LCA(node_5, node_6))
print(LCA(node_4, node_6))
print(distance(node_4, node_6))
