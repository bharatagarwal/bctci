"""
# White Hat Hacker

You are trying to hack into an account (for good reasons, I'm sure). You know that the password:

- has at least 1 and at most 10 letters,
- uses only lowercase English letters,
- does not repeat any letter.

You have a script that tries to log in with a given password and returns a boolean indicating if it was successful. Write a function to find the password. You can call check_password(s) to check if s is the password.

Example:
check_password("a")   # returns False
check_password("abc") # returns False
check_password("ac")  # returns False
check_password("ab")  # returns False
check_password("bc")  # returns True
Output: "bc"
"""

from time import sleep

from ucb import log, trace

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def check_password(s):
    return s == "abcdez"


def find_password(maxlen):
    count = 0

    def visit(password):
        nonlocal count
        count += 1

        if len(password) > maxlen:
            return None

        if check_password(password):
            print(count)  # => 39680027
            return password

        for char in ALPHABET:
            if char not in password:
                result = visit(password + char)

                if result:
                    return result

        return None

    return visit("")


find_password(10)
