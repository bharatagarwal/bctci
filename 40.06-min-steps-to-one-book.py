"""
# Minimum Steps to One

Write a function that accepts a positive integer, `n`, and returns the minimum number of operations to get to `1`, assuming we can choose between the following operations:

-   Subtract `1`.
-   Divide by `2`. We can only do this if the number is divisible by `2`.
-   Divide by `3`. We can only do this if the number is divisible by `3`.

Constraints:
- n is at least 1 and at most 10^6.


steps_to_one(val):
    min number of steps from val to 1

base case:
    val == 1:
        return 1
    val < 1:
        return 0

general case:
    res + min(steps_to_one(div_by_3), steps_to_one(div_by_2), steps_to_one(subtract_one)

original problem:
    steps_to_one(val)
"""


def min_steps(n):
    def num_steps(i):
        if i == 1:
            return 0

        steps = num_steps(i - 1)

        # pattern of casewise min
        # relevant when cases are optional
        if i % 2 == 0:
            steps = min(steps, num_steps(i // 2))

        if i % 3 == 0:
            steps = min(steps, num_steps(i // 3))

        return 1 + steps  # add this to memo

    return num_steps(n)


n = 10
print(min_steps(n))  # => 3. We can do 10 -> 9 -> 3 -> 1.

n = 1
print(min_steps(n))  # => 0

n = 15
print(min_steps(n))  # => 4
