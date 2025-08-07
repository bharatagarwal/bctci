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


def find_sum_eager(nested_array):
	result = 0

	for element in nested_array:
		if isinstance(element, int):
			result += element
		else:
			result += find_sum_eager(element)

	return result


def find_sum_lazy(nested_array):
	if isinstance(nested_array, int):
		return nested_array

	result = 0

	for element in nested_array:
		result += find_sum_lazy(nested_array)

	return result


def find_sum(nested_array):
	return find_sum_eager(nested_array)
	return find_sum_lazy(nested_array)
	pass


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
