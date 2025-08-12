class Node:
    """Node for a binary tree, with val and optional left/right"""

    def __init__(
        self,
        text,
        left=None,
        right=None,
    ):
        self.text = text
        self.left = left
        self.right = right


"""
# Hidden Message

The self-proclaimed 'cryptography expert' in your friend group has devised their own schema to hide messages in binary trees. 

Each node has a text field with exactly two characters. 

The first character is either 'b', 'i', or 'a'. 

The second character is part of the hidden message. To decode the message, you have to read the hidden-message characters in the following order:

If the first character in a node is 'b', the node goes before its left subtree, and the left subtree goes before the right subtree.


b: preorder
- node
- left
- right

a: postorder
- left
- right
- node

i: inorder
- left
- node
- right

If it is 'a', the node goes after its right subtree, and the right subtree goes after the left subtree.

If it is 'i', the node goes after its left subtree and before its right subtree.

Given the root of the binary tree, return the hidden message as a string.

Example:

                 bn
               /    \
             i_      a!
            /  \     /
          ae    it  br
         /  \         \
       bi    bc        ay

Output: "nice_try!"

Constraints:

- Assume we have a binary tree node class with a left and right fields, and a text field.
- The number of nodes is at most 10^5
- The height of the tree is at most 500
- The text field is a string of length 2. The first character is either 'b', 'i', or 'a'. The second character is a letter or number.
"""


def hidden_message(node):
    result = []

    def process(node):
        if not node:
            return

        order, payload = node.text[0], node.text[1]

        if order == "b":
            result.append(payload)
            process(node.left)
            process(node.right)
        elif order == "a":
            process(node.left)
            process(node.right)
            result.append(payload)
        elif order == "i":
            process(node.left)
            result.append(payload)
            process(node.right)

    process(node)

    return "".join(result)


n3 = Node("ae", Node("bi"), Node("bc"))
n4 = Node("i_", n3, Node("it"))

n6 = Node("br", None, Node("ay"))
n7 = Node("a!", n6, None)

n8 = Node("bn", n4, n7)

print(hidden_message(n8))
