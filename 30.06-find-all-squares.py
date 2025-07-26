"""
# Find All Squares

Given an array of unique integers, arr, return a list with all pairs of indices, [i, j], such that arr[i]^2 == arr[j]. You can return the pairs in any order.

list of all pairs of indices such that the value of square of the ith value equals value of jth value.

Example 1: arr = [4, 10, 3, 100, 5, 2, 10000]

Output: [[5, 0], [1, 3], [3, 6]].

The 3 pairs of values that satisfy the constraint are (2, 4), (10, 100), and (100, 10000).
We return [5, 0] because arr[5] is 2 and arr[0] is 4, and similarly for the other two pairs. Other
orders like [[1, 3], [0, 5], [3, 6]] would also be valid.

Example 2: arr = [1]
Output: [[0, 0]]. Since 1 is its own square, a 1 forms a pair with itself.

Constraints:
- The length of arr is at most 10^6
- 1 ≤ arr[i] ≤ 10^9
- All elements in arr are unique
"""


def find_squares(array):
	record = dict()
	pairs = list()

	for index, num in enumerate(array):
		record[num] = index

	for index, num in enumerate(array):
		if num * num in record:
			pairs.append([index, record[num * num]])

	return pairs


arr = [4, 10, 3, 100, 5, 2, 10000]

print(find_squares(arr))

# => [[5, 0], [1, 3], [3, 6]]

arr = [1]
print(find_squares(arr))
# => [[0, 0]]
