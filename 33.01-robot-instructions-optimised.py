"""
# Robot instructions

We are given a string, seq, with a sequence of instructions for a robot.

The string consists of characters 'L', 'R', and '2'.

- The letters 'L' and 'R' instruct the robot to move left or right.
- The character '2'
	- never appears at the end of the string
	- "perform all the instructions after this '2' twice, but skip the instruction immediately following the '2' during the second repetition."
	- Output a string with the final list of left and right moves that the robot should do.


Constraints:
- The length of seq is at most 10^4 -> higher than linear ok?
- seq consists only of the characters 'L', 'R', and '2'
- '2' never appears at the end of seq
"""


def follow_instructions(sequence):
	result = []
	move_recursively(sequence, 0, result)
	return "".join(result)


def move_recursively(sequence, index, result):
	if index == len(sequence):
		return

	if sequence[index] == "2":
		move_recursively(sequence, index + 1, result)
		move_recursively(sequence, index + 2, result)

	if sequence[index] in "LR":
		result.append(sequence[index])
		move_recursively(sequence, index + 1, result)


seq = "LL"

print(follow_instructions(seq))
# => "LL"

seq = "2LR"
print(follow_instructions(seq))

# => "LRR".
# # The '2' indicates that we need to do "LR" first and then "R".

seq = "2L"

print(follow_instructions(seq))
# => "L".

# # The '2' indicates that we need to do "L" first and then "" (the empty string).

seq = "22LR"

print(follow_instructions(seq))

# # => "LRRLR". The first '2' indicates that we need to do "2LR" first and then "LR".

seq = "LL2R2L"
print(follow_instructions(seq))  # => "LLRLL"
