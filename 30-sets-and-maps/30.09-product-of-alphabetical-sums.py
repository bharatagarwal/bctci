"""
# Product of Alphabetical Sums

Given a list of lowercase strings, words, where each string has between 1 and 3 letters

"1", "12", "123""

Determine if there exist three strings such that the product of their alphabetical sums is a given target value, target.

The alphabetical sum of a string is the sum of the positions of its letters in the alphabet (e.g., the alphabetical sum of "abz" is 1 + 2 + 26 = 29).

Return true if such a triplet exists. The same string can be used more than once.


Constraints:
- 0 ≤ words.length ≤ 10^5
- Each string in words has length between 1 and 3
- All strings contain only lowercase English letters
- 1 ≤ target ≤ 10^6
"""


def product_alphabet_sums(words, target):
	scores = []

	for word in words:
		scores.append(sum([ord(char) - 96 for char in word]))

	for i in range(len(words)):
		for j in range(len(words)):
			for k in range(len(words)):
				if scores[i] * scores[j] * scores[k] == target:
					print((words[i], words[j], words[k]))
					return True

	return False


words = ["abc", "fg", "hij", "klm", "nop", "qrs", "vwx"]
target = 1620


product_alphabet_sums(words, target)

# => true
# Explanation: The triplet is "abc", "abc", "nop": 6 * 6 * 45 = 1620.

words = ["a", "b"]
target = 2

product_alphabet_sums(words, target)


# => true
# Explanation: The triplet is "a", "a", "b": 1 * 1 * 2 = 2.

words = ["a", "b", "c"]
target = 7
product_alphabet_sums(words, target)


# => false
# Explanation: No triplet of strings has a product of alphabetical sums equal to 7
