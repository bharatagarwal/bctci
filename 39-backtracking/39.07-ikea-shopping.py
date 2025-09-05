"""
# IKEA Shopping

A magazine has rated every IKEA item from 1 to 10 in terms of style.

We have gone to IKEA with a limited budget and the goal of maximizing the sum of style ratings of the items we buy.

We also dont want to pick more than one of each item. We are given 3 things:

- budget, a positive integer,
- prices, an array of n positive integers,
- ratings, an array of n positive floating-point numbers between 0 and 10 (inclusive).

budget = 20
prices = [10, 5, 15, 8, 3]
ratings = [7.0, 3.5, 9.0, 6.0, 2.0]
            ^              ^
# => [0, 3]

budget = 10
prices = [2, 3, 4, 5]
ratings = [1.0, 2.0, 3.5, 4.0]
# => [2, 3]


There are n items. Item i has price prices[i] and style rating ratings[i]. Return an array with the indices of the items that we should buy.
"""

import math

from ucb import log, trace


def shop():
    budget = 20
    prices = [10, 5, 15, 8, 3]
    ratings = [7.0, 3.5, 9.0, 6.0, 2.0]

    # budget = 10
    # prices = [2, 3, 4, 5]
    # ratings = [1.0, 2.0, 3.5, 4.0]
    max_rating = -math.inf

    cur = list()
    res = list()

    def rating(arr):
        return sum([ratings[i] for i in arr])

    def cost(arr):
        return sum([prices[i] for i in arr])

    @trace
    def visit(index):
        nonlocal max_rating, res

        if index == len(prices):
            if cost(cur) < budget and rating(cur) > max_rating:
                max_rating = rating(cur)
                res = cur.copy()
            return

        cur.append(index)
        visit(index + 1)
        cur.pop()
        visit(index + 1)

    visit(0)
    return res


print(shop())
