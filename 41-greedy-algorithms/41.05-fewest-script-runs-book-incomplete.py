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

import math


def fewest_script_runs(meetings):
    meetings.sort(key=lambda x: x[1])
    count = 0

    prev_end = -math.inf

    for l, r in meetings:
        if l > prev_end:
            count += 1
            prev_end = r

    return count


meetings = [[2, 3], [1, 4], [2, 3], [3, 6], [8, 10]]

print(fewest_script_runs(meetings))  # => 2
# We can run the script at t = 3 and t = 9.


def run_tests():
    # Example test cases
    tests = [
        # Example 1
        ([[2, 3], [1, 4], [2, 3], [3, 6], [8, 10]], 2),
        # Example 2 - Counterexample from solution
        ([[1, 3], [2, 5], [3, 6], [4, 7], [5, 8], [7, 9]], 2),
        # Additional test cases
        # Edge case: No meetings
        ([], 0),
        # Edge case: All meetings overlap
        ([[1, 5], [2, 6], [3, 7]], 1),
        # Edge case: Non-overlapping meetings
        ([[1, 2], [3, 4], [5, 6]], 3),
        # Edge case: Single meeting
        ([[1, 2]], 1),
        # Edge case: Large number of meetings
        ([[i, i + 1] for i in range(100)], 50),
    ]

    for meetings, want in tests:
        got = fewest_script_runs(meetings)
        assert got == want, (
            f"\nminimum_script_runs({meetings}): got: {got}, want: {want}\n"
        )


run_tests()
