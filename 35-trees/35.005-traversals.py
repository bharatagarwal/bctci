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


pre = []


# pre refers to root, not children
def preorder(node):
    if not node:
        return

    pre.append(node.val)
    preorder(node.left)
    preorder(node.right)


_in = []


def inorder(node):
    if not node:
        return

    inorder(node.left)
    _in.append(node.val)
    inorder(node.right)


post = []


# post refers to root, not children
def postorder(node):
    if not node:
        return

    postorder(node.left)
    postorder(node.right)
    post.append(node.val)


tree = """
                1
        2               3
    4       5       6       7
"""

root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))


preorder(root)
print(tree)
print("preorder: ", pre)

inorder(root)
print("inorder:  ", _in)

postorder(root)
print("postorder:", post)
