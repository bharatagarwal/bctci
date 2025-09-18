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


def lcs(s1, s2):
    S1, S2 = len(s1), len(s2)
    memo = dict()

    @count_calls
    def lcs_rec(i1, i2):
        if i1 == S1 or i2 == S2:
            return ""

        if (i1, i2) in memo:
            return memo[(i1, i2)]

        if s1[i1] == s2[i2]:
            memo[(i1, i2)] = s1[i1] + lcs_rec(i1 + 1, i2 + 1)
        else:
            first = lcs_rec(i1 + 1, i2)
            second = lcs_rec(i1, i2 + 1)

            if len(first) >= len(second):
                memo[(i1, i2)] = first
            else:
                memo[(i1, i2)] = second

        return memo[(i1, i2)]

    res = lcs_rec(0, 0)
    print("recursive calls:", lcs_rec.calls)
    return res


s1 = "HAHAH"
s2 = "AAAAHH"
print(lcs(s1, s2))
# recursive calls: 35
# AAH


s1 = ""
s2 = "AA"
print(lcs(s1, s2))
# recursive calls: 1
# ""

s1 = "ABCD"
s2 = "ACBAD"
print(lcs(s1, s2))
# recursive calls: 15
# ABD
