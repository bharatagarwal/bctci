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


def max_sum_path(grid):
    row_len, col_len = len(grid), len(grid[0])

    best_path = list()
    best_sum = -math.inf

    seen = set()
    seen.add((0, 0))

    def valid(row, col):
        return (
            row in range(row_len)
            and col in range(col_len)
            and (row, col) not in seen
        )

    def visit(path, path_sum):
        nonlocal best_path, best_sum
        row, col = path[-1]

        if row == row_len - 1 and col == col_len - 1:
            if path_sum > best_sum:
                best_sum = path_sum
                best_path = path.copy()
            return

        for diff_row, diff_col in [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]:
            new_row = row + diff_row
            new_col = col + diff_col

            if valid(new_row, new_col):
                path.append([new_row, new_col])
                seen.add((new_row, new_col))

                visit(
                    path,
                    path_sum + grid[new_row][new_col],
                )

                path.pop()
                seen.remove((new_row, new_col))

    start = [0, 0]
    visit([start], grid[0][0])

    return best_path


grid = [
    [1, -4, 3],
    [-2, 7, -6],
    [5, -4, 9],
]

print(max_sum_path(grid))
