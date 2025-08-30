"""
# Jumping Numbers

A jumping number is a positive integer where every two consecutive digits differ by one, such as 2343. Given a positive integer, n, return all jumping numbers smaller than n, ordered from smallest to largest.

Example 1: n = 34
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21, 23, 32]

Example 2: n = 1
Output: []


Constraints:
n is a positive integer less than 10^5.
"""

from ucb import trace


def jumping_numbers(n):
    res = list()

    @trace
    def visit(num):
        if num >= n:
            return

        res.append(num)
        last_digit = num % 10

        if last_digit > 0:
            visit(num * 10 + (last_digit - 1))
        if last_digit < 9:
            visit(num * 10 + (last_digit + 1))

    for num in range(1, 10):
        visit(num)

    return sorted(res)


print(jumping_numbers(359))
