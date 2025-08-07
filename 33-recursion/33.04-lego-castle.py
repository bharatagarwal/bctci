"""
You're building an n-story 2D Lego castle following these instructions:

A 1-story castle is just a 1x1 block.

x

blocks(1) = 1
blocks(2) = blocks(1) + blocks(1) + 2*(n+1)
blocks(3) = blocks(2) + blocks(2) + 2*n+1

An n-story castle is made with two (n-1)-story castles, side by side, one unit apart, with a row of blocks above them connecting them.

0
.
x

xxx
x.x
n=2, 3
2^n -1

xxxxxxx
xxx xxx
x.x x.x
n=3, 3+3+1 = 7
2^n -1

xxxxxxxxxxxxxxx
xxxxxxx xxxxxxx
xxx xxx xxx xxx
x.x x.x x.x x.x
n=4, 15
2^n -1


2^(n-1) + 1

Given n > 0, return the number of 1x1 blocks in an n-story castle.


Example 1: n = 1
Output: 1

Example 2: n = 2
Output: 5

Example 3: n = 3
Output: 17

Example 4: n = 4
Output: 49

Example 5: n = 5
Output: 129
Constraints:

1 ≤ n ≤ 1000
"""

from collections import defaultdict

memo = defaultdict(int)


def blocks(stories):
	if stories == 1:
		return 1

	if stories not in memo:
		memo[stories] = 2 * blocks(stories - 1) + (2**stories - 1)

	return memo[stories]


def run_tests():
	tests = [(1, 1), (2, 5), (3, 17), (4, 49), (5, 129)]

	for n, want in tests:
		got = blocks(n)

		print(f"blocks({n}): got: {got}, want: {want}")


run_tests()
