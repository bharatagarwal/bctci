"""
# Subset Enumeration

Given a set of elements, S,
a subset of S is another set obtained by removing any number of elements from S (including none or all of them).

As usual with sets, order does not matter.

Given an array of unique characters, S, return all possible subsets in any order.


Example: S = ['x', 'y', 'z']

Constraints:

The elements in S are unique.
The length of S is at most 12.
"""


def subset(elements):
    res = list()
    length = len(elements)

    def visit(string):
        if len(string) == length:
            # check for membership here
            if set(string) not in res:
                res.append(set(string))
            return
        else:
            if set(string) not in res:
                res.append(set(string))

            for el in elements:
                # or check for membership here
                visit(string + el)

    visit("")
    return [list(s) for s in res]


S = ["x", "y", "z"]
print(subset(S))
