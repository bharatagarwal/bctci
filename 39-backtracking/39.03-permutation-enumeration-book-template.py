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


def generate_permutations(array):
    res = list()
    current = array.copy()

    def backtrack(i):
        if i == len(current):
            res.append(current.copy())
            return

        for j in range(i, len(current)):
            current[i], current[j] = current[j], current[i]
            backtrack(i + 1)
            current[j], current[i] = current[i], current[j]

    backtrack(0)
    return res


arr = ["🟢", "🟡", "⚪", "🔴"]
generate_permutations(arr)
