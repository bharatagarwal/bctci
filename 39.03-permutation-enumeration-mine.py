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


def possible(array):
    res = list()
    cur = list()
    remaining = set(array)

    def visit(i):
        nonlocal cur, remaining

        if len(cur) == len(array):
            res.append(cur.copy())
            # these stop algorithm from backtracking
            cur = list()
            remaining = set(array)
            return

        cur.append(array[i])
        remaining.discard(array[i])

        for _ in range(len(remaining)):
            # repeated visits
            # not backtracking
            visit(i + 1)

    visit(0)
    return res
