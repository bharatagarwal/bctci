"""
# Center Assignment

- A list of points on a 2D plane, points, where each point is represented as [x, y] (floating-point coordinates). The list always contains an even number of points.

- Two additional points, center1 and center2, each also represented as [x, y].

Your task is to divide the points in points into two groups of equal size:

- Assign half of the points to center1.
- Assign the other half to center2.

The goal is to minimize the sum of the (Euclidean) distance from each point to its assigned center. Return the sum of distances for an optimal assignment.

Constraints:

- points.length is even.
- 0 <= points.length <= 10^5.
- All coordinates are between -10^4 and 10^4.
- The answer should be a real-point within 10^-3 of the correct answer.
"""

import math


def minimize_distance(points, center1, center2):
    n = len(points)
    assignment = [0] * n
    baseline = 0
    c1_count = 0

    for i, p in enumerate(points):
        if math.dist(p, center1) <= math.dist(p, center2):
            assignment[i] = 1
            baseline += math.dist(p, center1)
            c1_count += 1
        else:
            assignment[i] = 2
            baseline += math.dist(p, center2)

    if c1_count == n // 2:
        return baseline

    switch_costs = []

    for i, p in enumerate(points):
        if assignment[i] == 1 and c1_count > n // 2:
            switch_costs.append(math.dist(p, center2) - math.dist(p, center1))
        elif assignment[i] == 2 and c1_count < n // 2:
            switch_costs.append(math.dist(p, center1) - math.dist(p, center2))

    res = baseline

    switch_costs.sort()

    for cost in switch_costs[: abs(c1_count - n // 2)]:
        res += cost

    return res


points = [[0, 1], [1, 0], [-1, 0], [0, -1]]
center1 = [0, 0]
center2 = [1, 1]

print(minimize_distance(points, center1, center2))  # => 4

# We can assign [-1, 0] and [0, -1] to center1 and [0, 1] and [1, 0] to center2.

# -----

points = [[0, 0], [0, 0]]
center1 = [0, 0]
center2 = [1, 1]

print(minimize_distance(points, center1, center2))  # => 1.414
# One of the points has to be assigned to center2, which is at distance sqrt(2) from [0, 0].

# -----

points = [[0, 0.5], [1, 0.5]]
center1 = [0, 0]
center2 = [1, 1]

print(minimize_distance(points, center1, center2))  # => 1

# -----

points = []
center1 = [0.3, -3.3]
center2 = [-1.6, 4.6]

print(minimize_distance(points, center1, center2))  # => 0
