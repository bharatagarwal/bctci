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

"""

S   .   .   .   .   .   .   .   .   E
    8   1   2   3   9   6   2   4
            1st
    .
        .
            .
                .       


signature:
    delay(i): minimum delay to reach destination from rest stop at i
    first stop at index 0
    last stop at index len(times) - 1

base cases:
    delay(n-1): at the last, skip 0 after this
    delay(n-2): at the second-last, skip 1 after this
        ....
    delay(n-k): k-1 ahead can be skipped
    delay(n - (k + 1)): k can ahead can be skipped
    i > N:
        return 0 -- facilitates easier later processing

general case:
    delay(i) = times[i] + min(delay(i+1), delay(i+2), ... delay(i+k+1))
                                skip 0     skip 1         skip k

original problem:
min(delay(0), ..... delay(k+1))
        skip 0.     skip k
"""


def optimal_stops(times, k):
    N = len(times)
    recursive_calls = 0

    if k >= N:
        print("recursive calls: ", recursive_calls)
        return 0

    def delay(i):
        nonlocal recursive_calls

        recursive_calls += 1

        if i in range(N - (k + 1), N):
            return times[i]
        elif i >= N:
            return 0

        options = [delay(j) for j in range(i + 1, (i + k + 1) + 1)]
        return times[i] + min(options)

    res = [delay(j) for j in range(0, (k) + 1)]
    print("recursive calls: ", recursive_calls)
    return min(res)


times = [8, 1, 2, 3, 9, 6, 2, 4]  # => len: 8
k = 2
print("solution:", optimal_stops(times, k))
# => 6, [8, *1*, 2, *3*, 9, 6, *2*, 4]

times = [8, 1, 2, 3, 9, 6, 2, 4]
k = 3
print("solution:", optimal_stops(times, k))
# => 4, [8, 1, *2*, 3, 9, 6, *2*, 4]

times = [10, 10]
k = 2
print("solution:", optimal_stops(times, k))  # => 0
