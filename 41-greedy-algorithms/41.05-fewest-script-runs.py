"""
# Fewest Script Runs

There are n meetings scheduled,
each with a start time and an end time.

We have a script that, when run, captures some information about all ongoing meetings.

Given an array, meetings,
where each element is a tuple [l, r] with l < r,
what's the minimum number of times we need to run the script
to capture information from all meetings?

If the script runs at the same time that a meeting starts or ends, it captures the information for that meeting.

Constraints:

- 0 <= n <= 10^5
- 0 <= meetings[i][0] < meetings[i][1] <= 10^9
"""

from itertools import pairwise


def fewest_script_runs(meetings):
    meetings.sort(key=lambda x: x[1])
    count = 1

    for first, second in pairwise(meetings):
        if second[0] > first[1]:
            count += 1

    return count


print(fewest_script_runs([[2, 3], [2, 3], [1, 4], [3, 6], [8, 10]]))
# => 2
# We can run the script at t = 3 and t = 9.

print(fewest_script_runs([[1, 3], [2, 5], [3, 6], [4, 7], [5, 8], [7, 9]]))
# =>  2, Counterexample

print(fewest_script_runs([]))
# =>  0, No meetings

print(fewest_script_runs([[1, 5], [2, 6], [3, 7]]))
# =>  1, All meetings overlap

print(fewest_script_runs([[1, 2], [3, 4], [5, 6]]))
# =>  3, Non-overlapping meetings

print(fewest_script_runs([[1, 2]]))
# =>  1, Single meeting

print(fewest_script_runs([[i, i + 1] for i in range(100)]))
# => 50, Large number of meetings
