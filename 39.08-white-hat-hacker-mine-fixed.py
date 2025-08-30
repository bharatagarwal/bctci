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

ALPHABET = [c for c in "abcdefghijklmnopqrstuvwxyz"]


def check_password(s):
    return s == "cde"


def hack(maxlen):
    cur = list()

    def visit():
        if len(cur) > maxlen:
            return None

        pwd = "".join(cur.copy())
        if len(pwd) > 0 and check_password(pwd):
            return pwd

        for c in ALPHABET:
            if c not in cur:
                cur.append(c)
                result = visit()

                if result:
                    return result

                cur.pop()

        return None

    return visit()


print(hack(5))
