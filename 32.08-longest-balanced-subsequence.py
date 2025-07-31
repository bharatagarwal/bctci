"""
# Longest Balanced Subsequence

Given a string of parentheses, s, return the longest balanced subsequence.

A subsequence of s (not a subarray) is a string obtained by removing some of the letters in s. In other words, you have to delete the smallest number of characters necessary to make s balanced and return the resulting string. There may be more than one valid answer.

Constraints:

- 0 <= s.length <= 10^5
- s consists only of '(' and ')'
"""

"""
- You want to keep the subsequence going
- You keep track of removal candidates
"""


def longest(string):
	removal_candidates = set()
	opening = "("
	closing = ")"
	stack = list()
	characters = list(string)

	# forward pass
	for index, char in enumerate(characters):
		if char == opening:
			stack.append(index)
			continue

		if char == closing:
			if not stack:
				removal_candidates.add(index)
			else:
				stack.pop()

	if stack:
		for index in stack:
			removal_candidates.add(index)

	# as string are immutable,
	# string concat in a loop is quadartic in python

	# for index, char in enumerate(characters):
	# 	if index not in removal_candidates:
	# 		subsequence += char
	result = list()

	for index, char in enumerate(characters):
		if index not in removal_candidates:
			result.append(char)

	return "".join(result)


s = "))(())(()"

"""

forward pass:

problems: 0, 1, 6

))(())(()
012345678
"""

print(repr(longest(s)))  # => "(())()".


s = "(()()"
print(repr(longest(s)))  # => "()()"

s = "())(()"

print(repr(longest(s)))  # => "()()".

s = "("

print(repr(longest(s)))  # => ""
