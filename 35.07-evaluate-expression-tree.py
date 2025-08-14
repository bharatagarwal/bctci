"""
# Evaluate Expression Tree

We are given the root of a tree representing an arithmetic expression.

The node definition has three fields: kind, num, and children.

The kind field determines the node's type. There are 'Number' nodes, which have kind = "num", and 'Operation' nodes, where kind is one of "sum", "product", "max", or "min".
The num field is only valid for 'Number' nodes. It stores an integer value.
The children field is only valid for 'Operation' nodes. It stores a list of child nodes (there are no null children).
This is not a binary tree, as nodes can have more than two children. We call this an N-ary tree.

Implement an evaluate() function which evaluates the tree according to the following rules:

The value of a 'Number' node is its num field.
The value of an 'Operation' node depends on its kind: it is the sum, product, max, or min of the children's values (the product of a single value is itself).

Example:

Input:
     min
    /   \
 max     +
 /|\      \
4 6 +      *
   / \    / \
  5   7  6   8

Output: 12

The number of nodes is at most 10^5
The height of the tree is at most 500
'Number' nodes have values between -10^4 and 10^4
It is guaranteed that the evaluation at every node will be between -10^4 and 10^4
"""

from math import prod


class Node:
    def __init__(self, kind, num=None, children=[]):
        # "num", "sum", "product", "max", "min"
        self.kind = kind
        self.num = num
        self.children = children


def evaluate(node):
    if node.kind == "num":
        return node.num

    if node.kind == "max":
        return max([evaluate(child) for child in node.children])
    if node.kind == "min":
        return min([evaluate(child) for child in node.children])
    if node.kind == "sum":
        return sum([evaluate(child) for child in node.children])
    if node.kind == "product":
        return prod([evaluate(child) for child in node.children])


n1 = Node("product", None, [Node("num", 6), Node("num", 8)])
n2 = Node("sum", None, [n1])

n3 = Node("sum", None, [Node("num", 5), Node("num", 7)])
n4 = Node("max", None, [Node("num", 4), Node("num", 6), n3])

n5 = Node("min", None, [n4, n2])
print(evaluate(n5))
