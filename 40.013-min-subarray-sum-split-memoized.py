import math


def min_split(array, k):
    print(array, ":", k)
    n = len(array)
    memo = {}

    def min_split_rec(i, x):
        if (i, x) in memo:
            return memo[(i, x)]

        if n - i == x:
            memo[(i, x)] = max(array[i:])
        elif x == 1:
            memo[(i, x)] = sum(array[i:])
        else:
            current_sum = 0
            res = math.inf

            for p in range(i, n - (x - 1)):
                current_sum += array[p]
                next_result = min_split_rec(p + 1, x - 1)
                candidate = max(current_sum, next_result)

                if candidate < res:
                    res = candidate

            memo[(i, x)] = res

        return memo[(i, x)]

    min_sum = min_split_rec(0, k)

    return min_sum


result = min_split([10, 5, 8, 9, 11], 3)


print(f"Min sum: {result}")
