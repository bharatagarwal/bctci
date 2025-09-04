"""
# Escape with All Clues

We are building an escape room puzzle where a player has to collect all the clues in a room to unlock the way out.

The room is represented by a non-empty grid, `room`, consisting of walkable spaces (`0`), obstacles (`1`), and clues (`2`).

The player starts on the top-left cell of the grid, which is guaranteed to be an open space, and can move to adjacent cells (diagonals not allowed).

If it is possible to collect all the clues **without repeating any cell**, return an array with the list of cells in the shortest path to collect them, starting with `[0, 0]`.

Otherwise, return an empty array. If there are multiple shortest paths, return any of them. It is guaranteed that there is at least one clue.

Example 1: room = [[0, 1, 0],
                   [0, 2, 0],
                   [0, 0, 2]]

Output: [[0,0], [1,0], [1,1], [1,2], [2,2]]. The other valid output is [[0,0],
[1,0], [1,1], [2,1], [2,2]].

Example 2: room = [[0, 0, 0],
                   [2, 1, 2]]
Output: []. It is not possible to get both clues without revisiting a cell.

Example 3: room = [[0, 0, 1, 2],
                   [0, 1, 0, 0]]
Output: []. It is not possible to reach the clue.

Constraints:

- room is a 2D grid of 0s, 1s, and 2s.
- room has at least one 2.
- room[0][0] is 0.
- room has at least 1 to 6 rows and 1 to 6 columns.
"""

import math

from ucb import log, trace


def find_clues(room):
    row_len, col_len = len(room), len(room[0])
    total_clues = sum(row.count(2) for row in room)

    best_pathlen = math.inf
    best_path = list()

    path = list()
    seen = {(0, 0)}

    def valid(row, col):
        return (
            (row, col) not in seen
            and row in range(row_len)
            and col in range(col_len)
            and room[row][col] != 1
        )

    @trace
    def visit(path, clue_count):
        nonlocal best_path, best_pathlen

        # stop further recursion
        if len(path) >= best_pathlen:
            return

        if clue_count == total_clues:
            if len(path) < best_pathlen:
                best_pathlen = len(path)
                best_path = path.copy()
            return

        row, col = path[-1]

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

                clue_diff = 1 if room[new_row][new_col] == 2 else 0

                visit(path, clue_count + clue_diff)

                path.pop()
                seen.remove((new_row, new_col))

    start = [0, 0]
    visit([start], 0)
    return best_path


room = [
    [0, 1, 0],
    [0, 2, 0],
    [0, 0, 2],
]

print(find_clues(room))
