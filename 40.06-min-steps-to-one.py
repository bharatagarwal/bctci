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
    def steps_to_one(val):
        if val == 1:
            return 1
        elif val < 1:
            return 0

        total = 0
        options = list()

        if val % 3 == 0:
            total_3 = total + steps_to_one(val // 3)

        if val % 2 == 0:
            options.append(steps_to_one(val // 2))

        options.append(steps_to_one(val - 1))

        return

    return steps_to_one(n)


n = 10
print(min_steps(n))  # => 3. We can do 10 -> 9 -> 3 -> 1.

n = 1
print(min_steps(n))  # => 0

n = 15
print(min_steps(n))  # => 4
