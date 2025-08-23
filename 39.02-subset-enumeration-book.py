"""
# Subset Enumeration

Given a set of elements, S,
a subset of S is another set obtained by removing any number of elements from S (including none or all of them).

As usual with sets, order does not matter.

Given an array of unique characters, S, return all possible subsets in any order.


Example: S = ['x', 'y', 'z']
"""

from ucb import log, space


def all_subsets(elements):
    res = list()
    subset = list()
    stack = list()

    @space
    def visit(i):
        log(f"stack i: {i}, {subset.copy()}")

        if i == len(elements):
            log("base case")
            res.append(subset.copy())
            return

        subset.append(elements[i])
        visit(i + 1)

        subset.pop()
        visit(i + 1)

    visit(0)
    return res


S = ["x", "y", "z"]
print("Starting subset enumeration demo")
result = all_subsets(S)
print(f"Final result: {result}")
print(f"Total subsets found: {len(result)}")
