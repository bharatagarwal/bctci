"""
Compress Array By K

Given an array of integers, arr, and an integer k >= 2, a k-compress operation finds the first block of k consecutive equal numbers and combines them into their sum.

If there are no k consecutive equal numbers, the array is considered fully k-compressed.

Your goal is to repeatedly apply k-compress operations until the array is fully k-compressed.

Example 1: arr = [1, 9, 9, 3, 3, 3, 4], k = 3
Output: [1, 27, 4]
The steps are [1, 9, 9, 3, 3, 3, 4] -> [1, 9, 9, 9, 4] -> [1, 27, 4]

Example 2: arr = [8, 4, 2, 2], k = 2
Output: [16]

Example 3: arr = [4, 4, 4, 4], k = 5
Output: [4, 4, 4, 4]
Constraints:
The length of arr is at most 10^5
Each element in arr is a non-negative integer less than 10^3
2 <= k <= len(arr)
"""


def merge(num, stack, k):
	if not stack or stack[-1][0] != num:
		stack.append([num, 1])

	elif stack[-1][1] < k - 1:
		stack[-1][1] += 1

	else:
		stack.pop()

		compressed_value = num * k

		merge(compressed_value, stack, k)


def compress_array(array, k):
	stack = []

	for i, num in enumerate(array):
		merge(num, stack, k)

	result = []

	for num, count in stack:
		for _ in range(count):
			result.append(num)

	return result


print(compress_array([1, 9, 9, 3, 3, 3, 4], 3))
print(compress_array([8, 4, 2, 2], 2))
print(compress_array([4, 4, 4, 4], 5))
