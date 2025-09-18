"""
# Reconstruct Longest Common Subsequence

Given two strings, `s1` and `s2`,
return the longest subsequence that is common to both `s1` and `s2`.

A _subsequence_ of a string `s` is a sequence of characters that appears in `s` in the same relative order but not necessarily consecutively.

In case of a tie, return any common subsequence of maximum length. The two strings consist of uppercase English letters only.

Constraints:

-   The length of each string is at most `1000`.
-   The two strings consist of uppercase English letters only.
"""


def count_calls(fn):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return fn(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def lcs_optimal(s1, s2):
    S1, S2 = len(s1), len(s2)
    memo = dict()

    @count_calls
    def lcs_rec(i1, i2):
        if i1 == S1 or i2 == S2:
            return 0

        if (i1, i2) in memo:
            return memo[(i1, i2)]

        if s1[i1] == s2[i2]:
            memo[(i1, i2)] = 1 + lcs_rec(i1 + 1, i2 + 1)
            return memo[(i1, i2)]

        first = lcs_rec(i1 + 1, i2)
        second = lcs_rec(i1, i2 + 1)

        memo[(i1, i2)] = max(first, second)

        return memo[(i1, i2)]

    i1, i2 = 0, 0
    res = list()

    while i1 < S1 and i2 < S2:
        if s1[i1] == s2[i2]:
            res.append(s1[i1])
            i1 += 1
            i2 += 1
        elif lcs_rec(i1 + 1, i2) > lcs_rec(i1, i2 + 1):
            i1 += 1
        else:
            i2 += 1

    print("recursive calls:", lcs_rec.calls)
    return "".join(res)


s1 = "HAHAH"
s2 = "AAAAHH"
print(lcs_optimal(s1, s2))
# recursive calls: 42
# AHH


s1 = ""
s2 = "AA"
print(lcs_optimal(s1, s2))
# recursive calls: 0
# ""

s1 = "ABCD"
s2 = "ACBAD"
print(lcs_optimal(s1, s2))
# recursive calls: 17
# ABD
