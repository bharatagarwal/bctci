# still weak because anagrams will collide
def str_to_num(string):
    return sum([ord(ch) for ch in list(string)])


def hsh(string, size):
    num = str_to_num(string)
    return num % size


print(hsh("bharat", 1000))
