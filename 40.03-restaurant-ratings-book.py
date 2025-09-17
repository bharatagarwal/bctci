"""
# Restaurant Ratings

We are doing a road trip and trying to plan where to stop to eat. There are n restaurants along the route.

We are given an array, ratings, with the ratings of all the restaurants maximizing the sum of ratings of the places where we stop.

The only constraint is that we don't want to stop at 2 consecutive restaurants, as we would be too full.

Return the optimal sum of ratings.
"""


def count_calls(fn):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return fn(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def restaurant_ratings(ratings):
    n = len(ratings)
    memo = {}

    @count_calls
    def rating_sum(i):
        if i >= n:
            return 0
        elif i in memo:
            return memo[i]

        memo[i] = max(ratings[i] + rating_sum(i + 2), rating_sum(i + 1))
        return memo[i]

    res = rating_sum(0)

    print("recursive calls:", rating_sum.calls)
    return res


ratings = [8, 1, 3, 9, 5, 2, 1]
"""
           .  S  S  .  S  .  S
           S  .  S  .  S  .  S
           .  S  .  S  .  S  .
           .  S  S  .  S  .
"""
print(restaurant_ratings(ratings))
# => 19 [*8*, 1, 3, *9*, 5, *2*, 1]

ratings = [8, 1, 3, 7, 5, 2, 4]

#          .     .     .     .
print(restaurant_ratings(ratings))
# => 20 [*8*, 1, *3*, 7, *5*, 2, *4*].

ratings = []
print(restaurant_ratings(ratings))
# => 0
