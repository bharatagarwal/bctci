"""
a value we're looking for, or the current node's depth:
    - down the tree
    - parameters of recursive function

information about the subtree, like size or height or sum
    - up the tree
    - return value of recursive function

storing node values
    - global state
    - variable visible in every recursive call
"""


def visit(node, info_passed_down):
    if base_case:
        return info_to_pass_up

    ... = visit(node.left, info_passed_down)
    ... = visit(node.right, info_passed_down)

    global_state = info_stored_globally

    return info_to_pass_up
