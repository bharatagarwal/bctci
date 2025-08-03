"""
# Balanced Partition

Given a balanced parentheses string, s,

a balanced partition is a partition of s into substrings, each of which is itself balanced.

Return the maximum possible number of substrings in a balanced partition.

Constraints:
- The length of s is at most 10^5
- s consists only of '(' and ')'
"""


def max_possible_substrings(string):
	stack = list()
	substrings = list()

	substring = ""

	for index in range(len(string)):
		if string[index] == "(":
			stack.append(string[index])
		elif string[index] == ")":
			stack.pop()

		substring += string[index]

		if not stack:
			substrings.append(substring)
			substring = ""

	print(substrings)
	return len(substrings)


s = "((()))(()())()(()(()))"

print(max_possible_substrings(s))  # => 4.

# The balanced partition with the most substrings is "((()))", "(()())", "()", "(()(()))".
