"""
# Largest Set Intersection

You are given a non-empty array, sets, where each element is an array of unique integers representing a set.

The intersection of a list of sets is the set of elements that appears in every set.

Return the index of the set that should be excluded to maximize the size of the intersection of the remaining sets. In case of a tie, return the smallest index.

Constraints:
- 1 ≤ sets.length ≤ 10^5
- 0 ≤ sets[i].length ≤ 10^5
- The total number of elements across all sets is at most 10^5
- All integers in each set are unique
- -10^9 ≤ sets[i][j] ≤ 10^9
"""

from collections import defaultdict


def set_intersection(list_of_sets):
	result = list_of_sets[0]

	for i in range(1, len(list_of_sets)):
		result = result.intersection(list_of_sets[i])


def largest(list_of_sets):
	if len(list_of_sets) == 1:
		return 0

	freq = defaultdict(int)

	for candidate in list_of_sets:
		for val in candidate:
			freq[val] += 1

	number_of_sets = len(list_of_sets)

	best_index = 0
	min_count = float("inf")

	for index, candidate in enumerate(list_of_sets):
		count = 0

		for val in candidate:
			# how many intersection elements do you have that are candidates for intersection without
			# you
			if freq[val] == number_of_sets - 1:
				count += 1

		# the fewer such candidates you have, the less likelihood you'll contribute to intersection.
		if count < min_count:
			min_count = count
			best_index = index

	return best_index


sets = [[1, 2, 3], [3, 2, 1], [1, 4, 5], [1, 2]]

print(largest(sets))  # => 2

# Explanation: Excluding the third set (index 2)
# yields a set intersection of size 2: {1, 2}.

sets = [[1, 2], [3, 4], [5, 6]]

print(largest(sets))  # => 0

# Explanation: The sets don't have any elements in common,
# so the intersection will be empty regardless of which set you exclude.

sets = [[1, 2, 3], [4, 5]]

print(largest(sets))  # => 1

# Explanation: After excluding a set, there will be only one set left,
# so the intersection is the remaining set.

sets = [[1, 2, 3]]

print(largest(sets))  # => 0

# Explanation: There is only one set, so after excluding it,
# the intersection is empty.
