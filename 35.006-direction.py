"""
down the tree
    - looking for a value, of current node depth
    - parameter of recursive function

up the tree
    - information about the subtree, like size or height or sum
    - return value of recursive function

global state
    - storing node values
    - variable visible for every recursive call
"""


def visit(node, info_passed_down):
    if base_case:
        return info_to_pass_up

    ... = visit(node.left, info_passed_down)
    ... = visit(node.right, info_passed_down)

    global_state = info_stored_globally

    return info_to_pass_up
