"""
# 4-Directional Max-Sum Path

Given an `RxC` grid of integers (which can be negative), `grid`, return the path from the top-left corner to the bottom-right corner with the largest sum. You can go in all four directions (diagonals not allowed), but you **can't visit a cell more than once**


Example: grid = [[ 1, -4,  3],
                 [-2,  7, -6],
                 [ 5, -4,  9]]

Output: [[0, 0], [0, 1], [1, 1], [1, 0], [2, 0], [2, 1], [2, 2]]

The maximum path is 1 -> -4 -> 7 -> -2 -> 5 -> -4 -> 9, which has sum 12.

Constraints:
- grid has at least 1 to 5 rows and 1 to 5 columns.
- grid[i][j] is an integer between -100 and 100.
"""

import math

from ucb import log, space, trace


def max_sum_path(grid):
    row_len = len(grid)
    col_len = len(grid[0])
    max_sum = -math.inf

    res = list()
    cur = list()
    cur_sum = int()
    seen = set()

    def valid(row, col):
        return row in range(row_len) and col in range(col_len)

    def visit(row, col):
        nonlocal max_sum, cur_sum, res

        cur_sum += grid[row][col]
        cur.append(grid[row][col])
        seen.add((row, col))

        if row == row_len - 1 and col == col_len - 1:
            if cur_sum > max_sum:
                max_sum = cur_sum
                res = cur.copy()
        else:
            down = row + 1, col
            up = row - 1, col
            right = row, col + 1
            left = row, col - 1

            directions = [down, right, up, left]

            for direction in directions:
                if valid(*direction) and direction not in seen:
                    visit(*direction)

        cur.pop()
        cur_sum -= grid[row][col]
        seen.remove((row, col))

    visit(0, 0)
    return res, max_sum


grid = [
    [1, -4, 3],
    [-2, 7, -6],
    [5, -4, 9],
]

print(max_sum_path(grid))
