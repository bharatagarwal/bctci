"""
# Nested Array Sum

A nested array is an array where each element is either:

- An integer
- A nested array

The sum of a nested array is defined recursively as the sum of all its elements. Given a nested array, arr, return its sum.

Constraints:

- The array can be nested to any depth
- Each integer in the array is between -10^9 and 10^9
- The total number of integers in the array (counting nested ones) is at most 10^5
"""


def find_sum_with_helper(array):
	sum = 0

	def find_sum_recursively(array, sum):
		# is_instance respects inheritance
		# type checks exactly for that type

		# REDUNDANT BLOCK
		# if isinstance(array, int):
		# 	return array

		for val in array:
			if isinstance(val, int):
				sum += val
			elif isinstance(val, list):
				sum = find_sum_recursively(val, sum)

		return sum

	return find_sum_recursively(array, sum)


def find_sum(array):
	total = 0

	for val in array:
		if isinstance(val, int):
			total += val
		elif isinstance(val, list):
			total += find_sum(val)

	return total


def find_sum_elegant(array):
	if isinstance(array, int):
		return array

	total = 0

	for val in array:
		total += find_sum_elegant(val)

	return total


arr = [1, [2, 3], [4, [5]], 6]
print(find_sum(arr))  #  => 21

arr = [[[[1]], 2]]
print(find_sum(arr))  #  => 3

arr = []
print(find_sum(arr))  #  => 0

arr = [[], [1, 2], [], [3]]
print(find_sum(arr))  #  => 6

arr = [-1, [-2, 3], [4, [-5]], 6]
print(find_sum(arr))  #  => 5
