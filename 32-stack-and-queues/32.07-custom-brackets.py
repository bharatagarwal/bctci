"""
# Custom Brackets

Given a string and an array of strings where each element consists of two characters, representing matching opening and closing brackets,

return whether s is balanced according to those brackets:

Characters not in brackets do not affect whether s is balanced.

A pair of matching brackets of one type cannot surround only half of a matching pair of another type of brackets.

Assume that brackets does not contain any repeated characters

Constraints:

- The length of s is at most 10^5
- The length of brackets is at most 10
"""


def is_balanced(string, brackets):
	corresponding_opening = dict()
	opening_set = set()
	closing_set = set()
	stack = list()

	for bracket_pair in brackets:
		opening, closing = bracket_pair[0], bracket_pair[1]
		opening_set.add(opening)
		closing_set.add(closing)

		corresponding_opening[closing] = opening

	for char in string:
		if char not in opening_set and char not in closing_set:
			continue

		if char in opening_set:
			stack.append(char)
			continue

		if char in closing_set:
			if not stack:
				return False

			if stack[-1] != corresponding_opening[char]:
				return False

			stack.pop()

	return len(stack) == 0


s = "((a+b)*[c-d]-{e/f})"
brackets = ["()", "[]", "{}"]

print(is_balanced(s, brackets))  # => True

s = "()[}"
brackets = ["()", "[]", "{}"]

print(is_balanced(s, brackets))  # => False

s = "([)]"
brackets = ["()", "[]", "{}"]

print(is_balanced(s, brackets))  # => False

s = "<div> hello :) </div>"
brackets = ["<>", "()"]

print(is_balanced(s, brackets))  # => False

s = ")))(()(("
brackets = [")("]

print(is_balanced(s, brackets))  # => True
