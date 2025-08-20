c = 0.6180339887


def hash(num, size):
    num *= c
    num -= int(num)
    num *= size

    return num


print(hash(1, 1000))
print(hash(2, 1000))
print(hash(612, 1000))
print(hash(1000, 1000))
