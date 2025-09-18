"""
# Minivan Road Trip


We are driving down a road with n rest stops between us and our destination.

For each rest stop, our mapping software tells us how long of a detour it would be to stop there.

We start before the first rest stop and our destination is past the last one.

We are given an array of n positive integers, times, indicating the delay incurred to stop at each rest stop.

We are also given a positive integer k, indicating the number of consecutive rest areas we can skip.

If we don't want to go more than k rest stops without taking a break, what's the least amount of time we have to spend on detours?

Constraints:

- n is at least 0 and at most 1000.
- times[i] is at least 1 and at most 1000.
- k is at least 1 and at most 1000.
"""

import math


def minivan_road_trip(times, k):
    n = len(times)
    memo = dict()

    def delay(i):
        if i >= n:
            return 0
        elif i >= n - k - 1:
            return times[i]
        elif i in memo:
            return memo[i]

        memo[i] = times[i] + min(delay(i + p) for p in range(1, k + 2))

        return memo[i]

    min_delay = math.inf

    for p in range(k + 1):
        min_delay = min(min_delay, delay(p))
    return min_delay


times = [8, 1, 2, 3, 9, 6, 2, 4]  # => len: 8
k = 2
print(minivan_road_trip(times, k))
# => 6, [8, *1*, 2, *3*, 9, 6, *2*, 4]

times = [8, 1, 2, 3, 9, 6, 2, 4]
k = 3
print(minivan_road_trip(times, k))
# => 4, [8, 1, *2*, 3, 9, 6, *2*, 4]

times = [10, 10]
k = 2
print(minivan_road_trip(times, k))  # => 0
