"""
# Most Non-Overlapping Intervals

Given a list, intervals,
where each element is a pair of integers [l, r],
with l ≤ r,
representing an interval
(with both endpoints included).

Return the largest number of
non-overlapping intervals.

Constraints:
- 0 ≤ intervals.length ≤ 10^5
- intervals[i].length = 2
- 0 ≤ intervals[i][j] ≤ 10^9
"""

import math


def most_non_overlapping_intervals(intervals):
    intervals.sort(key=lambda x: x[1])
    breakpoint()
    count = 0
    prev_end = -math.inf

    for l, r in intervals:
        if l > prev_end:
            count += 1
            prev_end = r

    return count


intervals = [[2, 3], [1, 4], [2, 3], [3, 6], [8, 9]]
print(most_non_overlapping_intervals(intervals))
# =>  2, [2, 3] and [8, 9]

# intervals = [[1, 2], [2, 3], [3, 4]]
# print(most_non_overlapping_intervals(intervals))
# =>  2, [1, 2] and [3, 4]

# intervals = [[1, 10], [8, 9], [2, 3]]
# print(most_non_overlapping_intervals(intervals))
# =>  2, [2, 3] and [8, 9]
