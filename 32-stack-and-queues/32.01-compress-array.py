"""
Compress Array

Given an array of integers, arr, a compress operation finds the first pair of consecutive equal numbers and combines them into their sum. If there are no consecutive equal numbers, the array is considered fully compressed. Your goal is to repeatedly compress the array until it is fully compressed.

Example 1: arr = [8, 4, 2, 2, 2, 4]
Output: [16, 2, 4].

The steps are [8, 4, 2, 2, 2, 4] -> [8, 4, 4, 2, 4] -> [8, 8, 2, 4] -> [16, 2,
4]

start building a stack

8, 4
check top two, if they are equal, consolidate
keep consolidating until top two are different
add to stack

Example 2: arr = [4, 4, 4, 4]
Output: [16]
The steps are [4, 4, 4, 4] -> [8, 4, 4] -> [8, 8] -> [16]

Example 3: arr = [1, 2, 3, 4]
Output: [1, 2, 3, 4]
Constraints:
The length of arr is at most 10^5
Each element in arr is a non-negative integer less than 10^3
"""

# Given an array of integers, arr, a compress operation finds the first pair of consecutive equal numbers and combines them into their sum.

# If there are no consecutive equal numbers, the array is considered fully compressed.

# Your goal is to repeatedly compress the array until it is fully compressed.


def compressed(array):
	for index in range(len(array) - 1):
		if array[index] == array[index + 1]:
			print("not compressed:", array)
			return False

	print("compressed:", array)
	return True


def compress(array):
	new_array = list()

	index = 0
	while True:
		if index >= len(array):
			break

		if index < len(array) - 1:
			if array[index] == array[index + 1]:
				array[index] *= 2
				new_array.append(array[index])
				index += 2
				continue

		new_array.append(array[index])
		index += 1

	print(new_array)
	return new_array


def compress_array(array):
	while True:
		if compressed(array):
			return array

		array = compress(array)


arr = [1, 2, 2, 4]
print(compress_array(arr))  # => [1, 8]


arr = [8, 4, 2, 2, 2, 4]
print(compress_array(arr))  # => [16, 2, 4]

arr = [4, 4, 4, 4]
print(compress_array(arr))  # => [16]

arr = [1, 2, 3, 4]
print(compress_array(arr))  # => [1, 2, 3, 4]
