"""
# Count Unique Submultisets with Sum Zero

A multiset is a set that allows repeated elements.

A submultiset of a multiset `S` is another multiset obtained by removing any number of elements from `S`.

We are given an array with `n` integers representing a multiset (it can have duplicates).

Return the number of unique submultisets of `S` with sum `0`, ignoring which position in `S` the values came from.

Example 1: S = [1, 1, -1, -1]
Output: 3. The unique submultisets with sum 0 are [], [1, 1, -1, -1] and [1,
-1]. The last one can be obtained in more than one way.

Example 2: S = []
Output: 1. [] is a submultiset of [] with sum 0.

Example 3: S = [-1, 2, 1, 0, 3]
Output: 4. The unique submultiset with sum 0 are [-1, 1], [-1, 1, 0], [0], and
[].

Constraints:

- The length of S is at most 20.
- The elements in S are integers.
"""

from collections import Counter


def unique(array):
    res = set()
    cur = Counter()
    length = len(array)

    def visit(index):
        if index == length:
            total = sum(
                [k * v for k, v in cur.items()],
            )

            if total == 0:
                immutable_cur = tuple(
                    sorted(
                        item[0] for item in cur.items() if item[1] > 0
                    )
                )

                res.add(immutable_cur)
            return

        cur.update([array[index]])
        visit(index + 1)
        cur.subtract([array[index]])
        visit(index + 1)

    visit(0)
    return res


print(unique([1, 1, -1, -1]))
print(unique([-1, 2, 1, 0, 3]))
