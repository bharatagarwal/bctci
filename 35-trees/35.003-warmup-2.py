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


def ancestors(node):
    result = []

    def recursive(node):
        if not node.parent:
            return []
        else:
            result.append(node.parent.id)
            recursive(node.parent)

            return result

    return recursive(node)


# c. Return the depth of the node


def depth(node):
    return len(ancestors(node))


"""
 d. 
 Given two non-null nodes from the same tree, 
    node1 and node2, 

return the ID of their lowest common ancestor. 

The deepest node in the tree which is a non-strict ancestor of both.

'Non-strict' means that a node is considered its own ancestor. For instance, in Figure 4, LCA(j, f) = f.

"""


def lowest_common_ancestor(node_1, node_2):
    n1_ancestors = []
    n2_ancestors = []

    while node_1:
        n1_ancestors.append(node_1.id)
        node_1 = node_1.parent

    while node_2:
        n2_ancestors.append(node_2.id)
        node_2 = node_2.parent

    n1_ancestors.reverse()
    n2_ancestors.reverse()

    ancestor = None
    for index in range(min(len(n1_ancestors), len(n2_ancestors))):
        if n1_ancestors[index] == n2_ancestors[index]:
            ancestor = n1_ancestors[index]

    return ancestor


"""
Given two non-null nodes from the same tree, return the distance between them. 

The sequence of edges between two nodes is called a path, and the number of edges in the path is the distance between the two nodes. 

Note that, in a binary tree, the path between any two nodes is unique.
"""


def distance_between_nodes(node1, node2):
    lca = lowest_common_ancestor(node1, node2)
    # path: node1 -> lca -> node2

    distance = 0

    while node1.id != lca:
        node1 = node1.parent
        distance += 1

    while node2.id != lca:
        node2 = node2.parent
        distance += 1

    return distance


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

print(ancestors(node_6))
print(ancestors(node_4))
print(depth(node_2))
print(depth(node_4))
print(depth(root))


print(lowest_common_ancestor(node_5, node_3))  # => 3
print(lowest_common_ancestor(node_6, node_4))  # => 1
print(distance_between_nodes(node_4, node_6))
