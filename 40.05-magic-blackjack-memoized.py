"""
# Magic Blackjack

You're given a magic deck of cards.

- When one card is removed, an identical card spawns as a replacement. - - Each card is a number between `1` and `10` (suits do not matter).
- When a card is drawn, each value from `1` to `10` has a `10%` chance of appearing.

A dealer repeatedly draws cards until one of two things happen:
- The sum of the cards is between `16` and `21`.
- The sum of the cards exceeds `21`. When this happens, we say the dealer busts.

Return the number of different ways the dealer can bust.

For instance, if the dealer draws `10`, `2`, `10`, they bust. If they draw `2`, `10`, `10`, that counts as a different way to bust. If the dealer draws `10`, `1`, `10`, they don't bust.

Constraints:

- No input parameters (the problem has fixed parameters)

draw(card, sum)
    check card and against sum, and keep playing, blackjack or bust

base case:
    sum is bust -> return 1
    sum is blackjack -> return 0

general case:
    draw each of 10 options and count busts

general case:
    (0, 0)
"""


def count_calls(fn):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return fn(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def ways_to_bust():
    memo = dict()

    @count_calls
    def draw(card, total):
        total += card

        if (card, total) in memo:
            return memo[(card, total)]

        if 21 < total:
            memo[(card, total)] = 1
            return memo[(card, total)]
        elif 21 >= total >= 16:
            memo[(card, total)] = 0
            return memo[(card, total)]

        count = 0

        for i in range(1, 10 + 1):
            count += draw(i, total)

        memo[(card, total)] = count

        return memo[(card, total)]

    res = draw(0, 0)
    print("recursive calls:", draw.calls)
    return res


print(ways_to_bust())

# 10, 2, 10 -> bust
# 2, 10, 10 -> bust
# 10, 1, 10 -> no bust
