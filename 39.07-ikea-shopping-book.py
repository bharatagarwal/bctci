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


def max_style(budget, prices, ratings):
    max_rating_sum = 0
    best_items = []
    n = len(prices)
    items = []

    def visit(i, cur_cost, cur_rating_sum):
        nonlocal best_items, max_rating_sum

        if i == n:
            if cur_rating_sum > max_rating_sum:
                max_rating_sum = cur_rating_sum
                best_items = items.copy()
            return

        if cur_cost + prices[i] <= budget:
            items.append(i)
            visit(
                i + 1, cur_cost + prices[i], cur_rating_sum + ratings[i]
            )
            items.pop()

        visit(i + 1, cur_cost, cur_rating_sum)

    visit(0, 0, 0)
    print(best_items)
    return best_items


# budget = 10
# prices = [2, 3, 4, 5]
# ratings = [1.0, 2.0, 3.5, 4.0]

budget = 20
prices = [10, 5, 15, 8, 3]
ratings = [7.0, 3.5, 9.0, 6.0, 2.0]

max_style(budget, prices, ratings)  # => [2, 3]
