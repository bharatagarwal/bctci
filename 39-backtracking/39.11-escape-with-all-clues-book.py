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


def find_clues(room):
    all_clues = []

    for i in range(len(room)):
        for j in range(len(room[0])):
            if room[i][j] == 2:
                all_clues.append((i, j))

    shortest_path = list()

    def valid_moves(pos):
        i, j = pos
        moves = []

        for dir_i, dir_j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nbr_i, nbr_j = i + dir_i, j + dir_j
            if (
                0 <= nbr_i < len(room)
                and 0 <= nbr_j < len(room[0])
                and room[nbr_i][nbr_j] != 1
            ):
                moves.append((nbr_i, nbr_j))

        return moves

    def visit(path, clues_left):
        nonlocal shortest_path

        if shortest_path and len(path) >= len(shortest_path):
            return

        if not clues_left:
            if not shortest_path or len(path) < len(shortest_path):
                shortest_path = path[:]
            return

        cur = path[-1]

        for next_pos in valid_moves(cur):
            if next_pos not in path:
                path.append(next_pos)
                remaining = set(clues_left)

                if next_pos in remaining:
                    remaining.remove(next_pos)

                visit(path, remaining)
                path.pop()

    visit([(0, 0)], set(all_clues))

    return [list(point) for point in shortest_path]


room = [
    [0, 1, 0],
    [0, 2, 0],
    [0, 0, 2],
]

print(find_clues(room))
