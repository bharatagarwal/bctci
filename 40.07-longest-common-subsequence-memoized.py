"""
# Longest Common Subsequence

Given two strings, `s1` and `s2`,
return the length of the longest common subsequence that is common to `s1` and `s2`.

A _subsequence_ of a string `s` is a sequence of characters that appears in `s` in the same relative order but not necessarily consecutively.

Constraints:

- The length of each string is at least 0 and at most 1000.
- The two strings consist of uppercase English letters only.

Signature:
    lcs(i1, i2)
    i1: suffix of s1
    i2: suffix of s2

    longest common substring of the two suffixes

Base Cases:
    i1 >= S1 or i2 >= S2: returns 0

General Case:
    if s1[i1] == s2[i2], lcs(i1, i2) = 1 + lcs(i1+1,i2+2)
    lcs(i1, i2) = max(lcs(i1+1, i2), lcs(i1, i2 + 1)

Original problem:
    lcs(0,0)
"""


def count_calls(fn):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return fn(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def lcs(s1, s2):
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

        memo[(i1, i2)] = max(lcs_rec(i1 + 1, i2), lcs_rec(i1, i2 + 1))

        return memo[(i1, i2)]

    res = lcs_rec(0, 0)
    print("recursive calls:", lcs_rec.calls)
    return res


s1 = "HAHAH"
s2 = "AAAAHH"
print(lcs(s1, s2))
# AAH or AHH


s1 = ""
s2 = "AA"
print(lcs(s1, s2))
# ""


s1 = "ABC"
s2 = "BCA"
print(lcs(s1, s2))
# BC
