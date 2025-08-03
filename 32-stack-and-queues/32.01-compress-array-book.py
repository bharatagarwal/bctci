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


def compress_array(arr):
	stack = []  # going with a naive stack
	print(f"Starting with array: {arr}")

	for num in arr:
		print(f"Processing number: {num}")
		print(f"Current stack: {stack}")

		while stack and stack[-1] == num:
			popped = stack.pop()
			num += popped
			print(
				f"Found consecutive equal: {popped} + {num - popped} = {num}"
			)
			print(f"Stack after pop: {stack}")

		stack.append(num)
		print(f"Added {num} to stack: {stack}")
		print()

	print(f"Final compressed array: {stack}")
	return stack


# arr = [8, 4, 2, 2, 2, 4]
# print(compress_array(arr))  # => [16, 2, 4]

arr = [4, 4, 4, 4]
print(compress_array(arr))  # => [16]

# arr = [1, 2, 3, 4]
# print(compress_array(arr))  # => [1, 2, 3, 4]
