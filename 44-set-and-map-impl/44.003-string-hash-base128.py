LARGE_PRIME = 10**9 + 7


def str_to_num(string):
    res = 0

    # base 128 grows very quickly
    # for c in string:
    #     res = res * 128 + ord(c)

    for c in string:
        res = (res * 128 + ord(c)) % LARGE_PRIME

    return res


def hsh(string, size):
    num = str_to_num(string)
    return num % size


print(hsh("bharat", 1000))
