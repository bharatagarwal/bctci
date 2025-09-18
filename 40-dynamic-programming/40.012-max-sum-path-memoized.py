"""
# Max-sum path

Given a non-empty RxC grid of positive integers, grid, find the path from top-left corner to the bottom-right corner with the largest sum. You can only go down or to the right, ie not diagonal.


signature:
max_path(r,c): the maximum path sum starting from grid [r][c]

base case:
    bottom-right corner: R-1, C-1
        max_path(r,c) = grid[r][c]

edge cases:
    last-row: r == R - 1 and c in range(C)
        max_path(r,c) = grid[r][c] + max_path(r, c+1)
    last-column: c == C - 1 and r in range(R)
        max_path(r,c) = grid[r][c] + max_path(r+1, c)

general case:
    choices: max_path(r, c+1) or max_path(r+1, c)
    aggregation: max

    max_path(r,c) = grid[r][c] + max(max_path(r+1, c), max_path(r, c+1))

original_problem:
    max_path(0, 0)
"""


def max_path(grid):
    R, C = len(grid), len(grid[0])
    memo = dict()

    def max_path_rec(r, c):
        # base case
        if r == R - 1 and c == C - 1:
            return grid[r][c]

        if (r, c) in memo:
            return memo[(r, c)]
        elif r == R - 1:
            memo[(r, c)] = grid[r][c] + max_path_rec(r, c + 1)
        elif c == C - 1:
            memo[(r, c)] = grid[r][c] + max_path_rec(r + 1, c)
        else:
            memo[(r, c)] = grid[r][c] + max(
                max_path_rec(r + 1, c),
                max_path_rec(r, c + 1),
            )

        return memo[(r, c)]

    return max_path_rec(0, 0)


grid = [
    [1, 5, 1],
    [2, 3, 2],
    [20, 1, 1],
]  # => 25

print(max_path(grid))
