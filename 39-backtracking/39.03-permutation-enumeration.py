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
    # used = set()

    def backtrack(partial):
        if len(partial) == len(array):
            res.append(partial.copy())

        for choice in array:
            if choice not in partial:
                partial.append(choice)
                backtrack(partial)
                partial.pop()

    backtrack([])
    return res


arr = ["a", "b", "c"]

print(possible(arr))
