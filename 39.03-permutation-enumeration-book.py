"""
# Permutation Enumeration

A permutation of a list is a list with the same elements but in any order. Finding all permutations means finding all possible orderings of the input elements.

Given an array of unique characters, arr, return all possible permutations, in any order.

Example 1: arr = ['x', 'y', 'z']
Output: [['x', 'y', 'z'],
         ['x', 'z', 'y'],
         ['y', 'x', 'z'],
         ['y', 'z', 'x'],
         ['z', 'x', 'y'],
         ['z', 'y', 'x']]

Example 2: arr = ['x']
Output: [['x']]

Constraints:

- The elements in arr are unique.
- The length of arr is at most 10.
"""

from ucb import log, space, trace


def generate_permutations(array):
    res = []
    perm = array.copy()

    def visit(i):
        print(perm.copy())
        if i == len(perm) - 1:
            res.append(perm.copy())
            return

        # log(f"i: {i}")
        for j in range(i, len(perm)):
            # log(f"j: {j} swapping {perm[i], perm[j]}")
            perm[i], perm[j] = perm[j], perm[i]
            visit(i + 1)
            # log(f"j: {j} restoring {perm[j], perm[i]}")
            perm[i], perm[j] = perm[j], perm[i]

    visit(0)
    return res


arr = ["🟢", "🟡", "⚪", "🔴"]
generate_permutations(arr)
