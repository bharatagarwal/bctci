"""
# String matching

Implement an index_of(s, t) method, which returns the first index where string t appears in string s,
or -1 if s does not contain t.
"""

LARGE_PRIME = 10**9 + 7


def str_to_num(string):
    res = 0

    for c in string:
        res = (res * 128 + ord(c)) % LARGE_PRIME

    return res


def power(x):
    """128 raised to the power, but avoiding overflow"""
    res = 1

    for i in range(x):
        res = (res * 128) % LARGE_PRIME

    return res


def next_hash(string, t_len, index, current_hash, first_power):
    """this is like bit shifting, for base 128"""
    res = current_hash
    res = (res - (ord(string[index]) * first_power)) % LARGE_PRIME
    res = (res * 128) % LARGE_PRIME

    return (res + ord(string[index + t_len])) % LARGE_PRIME


def index_of(string, target):
    s_len, t_len = len(string), len(target)

    if t_len > s_len:
        return -1

    hash_t = str_to_num(target)

    current_hash = str_to_num(string[:t_len])

    # compare hash and check for collision
    if hash_t == current_hash and target == string[:t_len]:
        return 0

    # last_power will be 0
    first_power = power(t_len - 1)

    for index in range(s_len - t_len):
        current_hash = next_hash(
            string, t_len, index, current_hash, first_power
        )

        next_index = index + 1

        if (
            hash_t == current_hash
            and target == string[next_index : next_index + t_len]
        ):
            return next_index

    return -1


tests = [
    # Basic test cases from book
    ("hello world", "world", 6),
    ("hello world", "hello", 0),
    ("needle in a haystack", "needle", 0),
    ("needle in a haystack", "haystack", 12),
    ("needle in a haystack", "not", -1),
    # Edge case - empty strings
    ("", "", 0),
    ("", "x", -1),
    ("x", "", 0),
    ("abc", "", 0),
    # Edge case - single character
    ("x", "x", 0),
    ("abc", "a", 0),
    ("abc", "b", 1),
    ("abc", "c", 2),
    ("abc", "d", -1),
    # Edge case - pattern longer than string
    ("x", "xx", -1),
    ("abc", "abcd", -1),
    # multiple occurrences
    ("banana", "ana", 1),  # Should return first occurrence
    ("banana", "an", 1),  # Should return first occurrence
    ("banana", "a", 1),  # Should return first occurrence
    # overlapping patterns
    ("aaaaa", "aa", 0),
    ("aaaaa", "aaa", 0),
    ("aabaabaa", "aaba", 0),
    # pattern at start/end
    ("startend", "start", 0),
    ("startend", "end", 5),
    # special characters
    ("\n\n\n", "\n", 0),
    ("\n\n\n", "\n\n", 0),
    ("tab\tseparated", "\t", 3),
    # repeated characters
    ("mississippi", "issi", 1),
    ("mississippi", "ssi", 2),
    ("mississippi", "sip", 6),
    # case sensitivity
    ("Hello World", "hello", -1),
    ("Hello World", "Hello", 0),
    # whitespace
    ("   spaces   ", " ", 0),
    ("   spaces   ", "   ", 0),
    ("   spaces   ", "spaces", 3),
    # numbers and special chars
    ("123123", "123", 0),
    ("!@#$%", "@#", 1),
    # long strings and patterns
    ("very very very long string to search in", "very long string", 10),
    ("aaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaa", 0),  # Many matches
]

for s, t, want in tests:
    got = index_of(s, t)
    got = index_of(s, t)
assert got == want, (
    f"\nindex_of_using_rolling_hash({s}, {t}): got: {got}, want: {want}\n"
)
