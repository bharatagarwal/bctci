"""
We are given an array, arr, whose length is a power of 2. We determine if an array is laminal as follows:

- The array arr is laminal.
- Each half of a laminal array is laminal.
- A subarray of arr with a single element is laminal.

Find the laminal subarray in arr with maximum sum and return its sum.

Example 1: arr = [3, -9, 2, 4, -1, 5, 5, -4]
Output: 6



The laminal arrays are:
[3, -9, 2, 4, -1, 5, 5, -4],
[3, -9, 2, 4], [-1, 5, 5, -4],
[3, -9], [2, 4], [-1, 5], [5, -4],
[3], [-9], [2], [4], [-1], [5], [5], [-4]
The one with the maximum sum is [2, 4].

Example 2: arr = [1]
Output: 1

Example 3: arr = [-1, -2]
Output: -1

Example 4: arr = [1, 2, 3, 4]
Output: 10

Example 5: arr = [-2, -1, -4, -3]
Output: -1

Constraints:

- The length of arr is a power of 2
- 1 ≤ len(arr) ≤ 10^5
- 10^9 ≤ arr[i] ≤ 10^9
"""


def max_sum(laminal):
	length = len(laminal)

	if length == 1:
		return laminal[0]

	left = laminal[: length // 2]
	right = laminal[length // 2 :]

	if max_sum(left) > max_sum(right):
		return sum(left)


arr = [3, -9, 2, 4, -1, 5, 5, -4]
print(max_sum(arr))
