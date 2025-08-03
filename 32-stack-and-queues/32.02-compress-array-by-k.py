"""
# Compress Array By K

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


def check_last_are_same(stack, times, num):
	if len(stack) < times:
		return False

	for i in range(1, times + 1):
		if num != stack[-i]:  element
			return False

	return True


def compress_array(array, k):
	stack = []

	for num in array:
		while stack and check_last_are_same(stack, k - 1, num):

			for _ in range(k - 1):
				num += stack.pop()

		stack.append(num)
		
	return stack

print(compress_array([1, 9, 9, 3, 3, 3, 4], 3))
print()

print(compress_array([8, 4, 2, 2], 2))
print()

print(compress_array([4, 4, 4, 4], 5))