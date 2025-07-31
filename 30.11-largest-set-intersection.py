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


def largest(sets):
	if not sets:
		return -1

	if len(sets) == 1:
		return 0

	resulting_index = 0
	max_length_without = 0

	for i in range(len(sets)):
		# Valiant, but can be replace by having a None placeholder
		# union_without = set()

		# for j in range(len(sets)):
		# 	if j != i:
		# 		union_without = union_without.union(sets[j])

		intersection_without = None

		for j in range(len(sets)):
			if j != i:
				if not intersection_without:
					intersection_without = set(sets[j])
					continue

				intersection_without = (
					intersection_without.intersection(sets[j])
				)

		if len(intersection_without) > max_length_without:
			resulting_index = i
			max_length_without = len(intersection_without)

	return resulting_index


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
