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


def distance(p1, p2):
    return math.sqrt(
        math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2),
    )


def min_euclidian_sum(points, c1, c2):
    L = len(points)
    S = set(points)

    from_c1 = [(point, distance(point, c1)) for point in points]
    from_c2 = [(point, distance(point, c2)) for point in points]

    from_c1.sort(key=lambda x: x[1])
    from_c2.sort(key=lambda x: x[1])

    c1, c2 = len(from_c1) - 1, len(from_c2) - 1
    sum1 = list()
    sum2 = list()

    while S:
        if from_c2[c2][1] >= from_c1[c1][1] and len(sum2) <= L // 2:
            sum2.append(from_c2[c2][1])


points = [[0, 1], [1, 0], [-1, 0], [0, -1]]
center1 = [0, 0]
center2 = [1, 1]

print(min_euclidian_sum(points, center1, center2))  # => 4

# We can assign [-1, 0] and [0, -1] to center1 and [0, 1] and [1, 0] to center2.

points = [[0, 0], [0, 0]]
center1 = [0, 0]
center2 = [1, 1]

# => 1.414
# One of the points has to be assigned to center2, which is at distance sqrt(2) from [0, 0].

points = [[0, 0.5], [1, 0.5]]
center1 = [0, 0]
center2 = [1, 1]

# => 1

points = []
center1 = [0.3, -3.3]
center2 = [-1.6, 4.6]

# => 0
