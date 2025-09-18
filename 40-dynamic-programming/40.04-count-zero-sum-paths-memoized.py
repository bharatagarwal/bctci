"""
# Count 0-Sum Paths

Given a non-empty RxC binary grid, grid, return the number of paths from the top-left corner to the bottom-right corner with a sum of 0. You can only go down, to the right, or diagonally down and to the right.

Example 2:
grid = [
  [1]
]
Output: 0

Example 3:
grid = [
  [0, 0],
  [0, 0]
]
Output: 3


Constraints:

- R is at least 1 and at most 1000.
- C is at least 1 and at most 1000.
- Each element in the grid is either 0 or 1.
"""

"""
signature:
    zero_sum_paths_left(r, c, sum)

base case:
    r == R - 1, c == C - 1:
        if current is zero, 1
    current is 1:
        return 0

general case:
    if right == 0, go right
    if left == 0, go left
    if diagonal == 0, go left

zero_sum_paths_left(0, 0, 0)
"""


def count_calls(fn):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return fn(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def paths(grid):
    R, C = len(grid), len(grid[0])
    memo = dict()

    @count_calls
    def paths_left(r, c):
        if r >= R or c >= C or grid[r][c] == 1:
            return 0

        if r == R - 1 and c == C - 1:
            return 1

        if (r, c) in memo:
            return memo[(r, c)]

        memo[(r, c)] = (
            paths_left(r + 1, c)
            + paths_left(r, c + 1)
            + paths_left(r + 1, c + 1)
        )
        return memo[(r, c)]

    res = paths_left(0, 0)

    print("recursive calls:", paths_left.calls)
    return res


grid = [
    [0, 1, 1],
    [0, 0, 0],
    [1, 0, 0],
]

print(paths(grid))  # => 7

grid = [[1]]

print(paths(grid))  # => 0

grid = [[0, 0], [0, 0]]
print(paths(grid))  # => 3
