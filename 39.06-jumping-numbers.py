from ucb import log, trace
import logging

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

DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def process(num):
    digits = 1

    while num > 10:
        num = num // 10
        digits += 1

    return num, digits


def jumping_numbers(num):
    res = list()
    cur = []

    @trace
    def process(index):
        log(f"cur: {cur}")

        cur_string = "".join(map(str, cur))
        val = int(cur_string) if cur_string.isdigit() else 0

        if val >= num:
            return
        elif val != 0:
            res.append(val)

        cur.append(DIGITS[index])

        if DIGITS[(index + 1) % 10] == DIGITS[index] + 1:
            process(index + 1)
            cur.pop()
        if DIGITS[(index - 1) % 10] == DIGITS[index] - 1:
            process(index - 1)
            cur.pop()

        process(index + 1)
        cur.pop()

    process(0)
    return res


jumping_numbers(5)
