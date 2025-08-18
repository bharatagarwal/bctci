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
