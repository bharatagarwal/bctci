"""
# To Be or Not to Be

Inspired by Shakespeare's iconic line, you decide to write a function, `shakespearify()`, which takes in a string, `sentence`, consisting of lowercase letters and spaces.

For each word in the string, the function chooses if it should "be" or "not be" included in the sentence, returning all possible outcomes.

The order of the output strings does not matter.

Example 1: sentence = "I love dogs"
Output: [
         "",
         "I",
         "love",
         "dogs",
         "I love",
         "I dogs",
         "love dogs",
         "I love dogs"
        ]

Example 2: sentence = "hello"
Output: ["", "hello"]

Example 3: sentence = ""
Output: [""]


Constraints:

- The sentence consists of lowercase letters and spaces.
- The sentence has at most 12 words and at most 100 characters.
"""


def shakespearify(sentence):
    words = sentence.split()
    res = list()
    cur = list()

    def visit(index):
        nonlocal cur, res
        if index == len(words):
            res.append((" ".join(cur)))
            return

        cur.append(words[index])
        visit(index + 1)

        cur.pop()
        visit(index + 1)

    visit(0)
    return res


sentence = "I love dogs"
print(shakespearify(sentence))
"""
[
    "",
    "I",
    "love",
    "dogs",
    "I love",
    "I dogs",
    "love dogs",
    "I love dogs"
]
"""
