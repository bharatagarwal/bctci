"""
# Time Traveler

You are a time traveler who is stuck in the past and trying to reach a future point.

Fortunately, in addition to just letting time pass naturally, you can use an emergency system to jump forward in time -- but there are constraints:

- Jumping Points: The emergency system can only jump to the next year specified in a sorted list called jumping_points.

- Jumps: You have a limited number of jumps k, which lets you instantly move forward to the next jumping point of your choice.

Once you're out of jumps, you must live through the years naturally to reach your target year.

Maximum Aging: You want to avoid aging more than a certain limit, max_aging, which is the total number of years you live naturally during your journey.

Your starting point is the first year in jumping_points and your goal is to reach the last year in the list. To achieve this, you can use any mix of:

- Jumping to the next jumping point instantaneously (up to a limit of k jumps).
- Let time pass naturally.

Return whether you can reach the final jumping point without exceeding the max_aging limit.

Constraints:
- 0 ≤ k ≤ n-1
- 0 < max_aging ≤ 10^9
- 2 ≤ jumping_points.length ≤ 10^5
- 0 ≤ jumping_points[i] ≤ 10^9
- The list of jumping points is sorted in ascending order (no duplicates).
"""

from itertools import pairwise


def can_reach(points, jumps, max_aging):
    gaps = sorted([pair[1] - pair[0] for pair in pairwise(jumping_points)])

    stop_index = len(gaps) - jumps

    # for list[start:end], end is exclusive
    return sum(gaps[:stop_index]) <= max_aging


jumping_points = [2020, 2024]
k = 0
max_aging = 3
print(can_reach(jumping_points, k, max_aging))
# => False.
# We don't have jumps, and aging naturally from 2020 to 2024 would take 4 years.


jumping_points = [2020, 2024]
k = 1
max_aging = 1
print(can_reach(jumping_points, k, max_aging))
# => True.
# We can use the jump to go from 2020 to 2024, so we get to 2024 in 0 years.


jumping_points = [
    1803,
    1861,
    1863,
    1865,
    1920,
    1929,
    1941,
    1964,
    2001,
    2021,
]
k = 4
max_aging = 45
print(can_reach(jumping_points, k, max_aging))
# => True
"""
We start at 1803. 
- We use our first jump to get to 1861. 
- We let time flow naturally for four years, 
    carrying us to 1865. 
- We use our second jump to fast forward to 1920. 
    We bide our time until 1941. 
- The third jump takes us to 1964,
    and we jump again immediately to 2001. 

- Out of jumps, we endure the final stretch of 20 long years. 

In total, we have aged 4 + 9 + 12 + 20 = 45 years, the maximum we could afford.
"""
