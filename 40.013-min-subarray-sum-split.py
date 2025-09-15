"""
# Min-of-max-subarray-sum split

Given a non-empty array with n positive integers, arr
a number k with 1 ≤ k ≤ n,

the goal is to split arr into k non-empty subarrays so that the largest sum across all subarrays is minimized.

arr = [10, 5, 8, 9, 11]
k = 3


n = 5
k = 3

[10], [5], [8,9,11]
[10], [5,8], [9,11]

signature
------

min_split(i, x): minimum possible largest subarray-sum after splitting elements between i and n.
    i -> index of rest of elements
    x -> subarrays left

base cases
------

if x elements left, and subarray count is also x, each will be a single element. max of subarray sum will be max of elements left.

if subarray left, remaining elements will go into the subarray and max of subarray sum will be sum of remaining array.

general case
-------
    - make sure next iteration has 1 or more subarray counts left
    - ranging from size 1 to p, the subarrays will have a sum, and we need the min of those choices

original problem
-------
min_split(0, k)


Constraints:

- 1 ≤ n ≤ 10^6
- 1 ≤ arr[i] ≤ 10^4
- 1 ≤ k ≤ n
"""

import math

import snoop

# Configure snoop to not show timestamps or elapsed times
snoop.install(columns=[])

def min_split(array, k):
    n = len(array)

    @snoop
    def min_split_rec(i, x):
        if x == 1:
            return sum(array[i:])

        # n - 1 - (i - 1) == x
        elif n - i == x:
            return max(array[i:])

        current_sum = 0
        res = math.inf

        for p in range(i, n - (x - 1)):
            current_sum += array[p]

            recursive_result = min_split_rec(p + 1, x - 1)
            option_result = max(current_sum, recursive_result)

            if option_result < res:
                res = option_result

        return res

    return min_split_rec(0, k)


print(min_split([10, 5, 8, 9, 11], 3))
# => 17, [10, 5], [8, 9], and [11]
