"""
# Restaurant Ratings

We are doing a road trip and trying to plan where to stop to eat. There are n restaurants along the route.

We are given an array, ratings, with the ratings of all the restaurants maximizing the sum of ratings of the places where we stop.

The only constraint is that we don't want to stop at 2 consecutive restaurants, as we would be too full.

Return the optimal sum of ratings.


signature:
    best_ratings(index):
        best path from this rating onwards
    n is the number of restaurants

base case:
    n - 1: have to stop here
    i >= n: 0

general case:
    at the current restaurant,
    ratings[index] + max(best_ratings(index + 2), best_ratings(index + 3)

original_case:
    max(best_ratings(0), best_ratings(1))
"""


def count_calls(fn):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return fn(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def tastiest_route(ratings):
    N = len(ratings)
    memo = dict()

    if N == 0:
        return 0

    @count_calls
    def best_ratings(i):
        if i in memo:
            return memo[i]

        if i == N - 1:
            memo[i] = ratings[i]
            return memo[i]
        elif i >= N:
            return 0

        memo[i] = ratings[i] + max(
            best_ratings(i + 2), best_ratings(i + 3)
        )

        return memo[i]

    res = max(best_ratings(0), best_ratings(1))

    print("recursive calls:", best_ratings.calls)
    return res


ratings = [8, 1, 3, 9, 5, 2, 1]
"""
           .  S  S  .  S  .  S
           S  .  S  .  S  .  S
           .  S  .  S  .  S  .
           .  S  S  .  S  .
"""
print(tastiest_route(ratings))
# => 19 [*8*, 1, 3, *9*, 5, *2*, 1]

ratings = [8, 1, 3, 7, 5, 2, 4]

#          .     .     .     .
print(tastiest_route(ratings))
# => 20 [*8*, 1, *3*, 7, *5*, 2, *4*].

ratings = []
print(tastiest_route(ratings))
# => 0
