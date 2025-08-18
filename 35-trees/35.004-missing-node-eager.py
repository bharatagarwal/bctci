# eager check
# check inside main logic
def size_eager(node):
    result = 0

    if node.left:
        result += size_eager(node.left)

    if node.right:
        result += size_eager(node.left)

    return result + 1


# lazy check
# checked at beginning of method
def size_lazy(node):
    if not node:
        return 0

    return size_lazy(node.left) + size_lazy(node.right) + 1


"""

                2 # 4 tabs for 3 depth
        5               8 # 2 tabs
    3       9       10      12 # 1 tab
                                1 # 2 spaces
"""
