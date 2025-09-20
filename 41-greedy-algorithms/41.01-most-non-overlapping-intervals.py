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

# move through the elements
#     - create a list of overlapping intervals
#     - at each interval, compare against list of intervals, update if necessary


def distinct_count(intervals):
    res = list()

    for start, end in intervals:
        if not res:
            res.append(range(start, end + 1))
        else:
            for i in len(res):
                if start in res[i]:
                    pass
                    # update res[i]
                elif end in res[i]:
                    pass
                    # update res[i]
                else:
                    res.append(range(start, end))


intervals = [[2, 3], [1, 4], [2, 3], [3, 6], [8, 9]]
print(distinct_count(intervals))
# =>  2, [2, 3] and [8, 9]

intervals = [[1, 2], [2, 3], [3, 4]]
print(distinct_count(intervals))
# =>  2, [1, 2] and [3, 4]

intervals = [[1, 10], [8, 9], [2, 3]]
print(distinct_count(intervals))
# =>  2, [2, 3] and [8, 9]
