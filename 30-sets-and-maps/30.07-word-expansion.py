"""
Word Expansion Class

Implement a class, Checker, that receives a string s upon initialization.

The class must support a method, expands_into(s2), which takes another string and checks if s2 can be formed by adding exactly one letter to s1 and reordering the letters.

All letters in both strings are lowercase alphabetical characters.


Constraints:
- The length of s and s2 is at most 10^5
- All characters are lowercase English letters

"""

from collections import defaultdict


class Checker:
	def __init__(self, word):
		self.length = len(word)
		self.membership = defaultdict(int)

		for char in word:
			self.membership[char] += 1

		# order of expanded words does not matter
		# store membership and count in a dict

	def expands_into(self, expanded_word):
		if len(expanded_word) != self.length + 1:
			return False

		expanded_membership = defaultdict(int)

		for char in expanded_word:
			expanded_membership[char] += 1

		extra_count = 0

		for char, count in self.membership.items():
			if expanded_membership[char] == self.membership[char]:
				continue

			if (
				expanded_membership[char] == self.membership[char] + 1
				and extra_count == 0
			):
				extra_count += 1
				continue

			return False

		return True

		# iterate through dict keys, and allow one word to exceed count
		# if character not found or more than one word exceeds count, then return False


checker = Checker("tea")
print(checker.expands_into("tea"))  # returns False
print(checker.expands_into("team"))  # returns True
print(checker.expands_into("seam"))  # returns False

print()

checker = Checker("on")
print(checker.expands_into("nooo"))  # returns False
print(checker.expands_into("not"))  # returns True
print(checker.expands_into("now"))  # returns True

print()


checker = Checker("")
print(checker.expands_into("a"))  # returns True
print(checker.expands_into(""))  # returns False
print(checker.expands_into("ab"))  # returns False
