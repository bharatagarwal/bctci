# """
# # Max-Sum Path

# Given a non-empty grid of positive integers, grid,
# find the path from the top-left corner to the bottom-right corner with the largest sum.

# You can only go down or to the right (not diagonal).

# Example 1: grid = [
#                     [1, 4, 3],
#                     [2, 7, 6],
#                     [5, 8, 9]
#                 ]

# """

# # 0, 1, 2

# # 1, 4, 3  0
# # 2, 7, 6  1
# # 5, 8, 9  2


import math

from ucb import trace


# DP is better.
# But this demonstrates backtracking.
def max_sum_path(grid):
    max_sum = -math.inf

    R, C = len(grid), len(grid[0])

    @trace
    def visit(r, c, cur_sum):
        nonlocal max_sum

        # at last node
        if r == R - 1 and c == C - 1:
            max_sum = max(max_sum, cur_sum)
            return

        if r + 1 < R:  # can only go on till right edge
            # move right, carrying sum
            next_el = grid[r + 1][c]
            visit(r + 1, c, cur_sum + next_el)
        if c + 1 < C:  # can only go on till bottom edge
            # move down, carrying sum
            next_el = grid[r][c + 1]
            visit(r, c + 1, cur_sum + next_el)

    first_el = grid[0][0]
    visit(0, 0, first_el)

    return max_sum


grid = [[1, 4, 3], [2, 7, 6], [5, 8, 9]]
