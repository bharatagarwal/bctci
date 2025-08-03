"""
# Cheater Detection

You are given an array, answers, with the answers of a multi-choice test.

The list has k characters ('a', 'b', 'c', or 'd'), where k is the number of questions in the exam.

answer array of length k, containing right answer out of a, b, c or d.
-----

You are also given an array, students, of students' answers for the test. Each entry is a tuple [student_id, desk, answers], where:

array of students' answers

[
	(student_id, desk, answers)
	(student_id, desk, answers)
	(student_id, desk, answers)
	(student_id, desk, answers)
]

- desks arrange in rows of length 'm'
- not all desks may be occupied

- Student IDs are unique positive integers.
- Desks are unique positive integers. Desks are arranged in rows of m desks, starting with desks 1 to m in the first row, m+1 to 2m in the second row, and so on. Not all desks may be occupied. E.g., there may be a student at desk 2 but none at desk 1.
- For each student, answers is an array of k characters ('a', 'b', 'c', or 'd').
-------

Two students are considered _suspect_ if they have made **identical mistakes** and **sit next to each other** in the same row (we don't care about students in the front or behind one another).

suspect if:
	- identical mistakes (same wrong answer for a question)
	- set next to each other in the same row

Return a list of all pairs of suspect students in any order (the order of the two students in a pair also doesn't matter).


Constraints:

- The length of answers is at most 10^5
- The length of students is at most 10^5
- All answers are 'a', 'b', 'c', or 'd'
- All student IDs are unique positive integers
- All desks are unique positive integers
- m is a positive integer less than 10^5
"""

from collections import defaultdict


def detect_cheaters(students, answers, m):
	mistakes = defaultdict(set)
	seating = dict()

	# disk - 1 accounts for one-index of desks
	for student_id, desk, choices in students:
		if (desk - 1) // m not in seating():
			seating[(desk - 1) // m] = [None] * m
			seating[(desk - 1) // m][(desk - 1) % m] = student_id
		else:
			seating[(desk - 1) // m][(desk - 1) % m] = student_id

		for index, choice in enumerate(choices):
			if answers[index] != choices[index]:
				mistakes[student_id].add((index, choices[index]))

	consecutives_in_row = defaultdict(set)

	for row, students in seating.items():
		for index in range(len(students) - 1):
			if students[index] and students[index + 1]:
				consecutives_in_row[row].add(
					(students[index], students[index + 1])
				)

	suspects = list()

	for _, consecutives in consecutives_in_row.items():
		for first, second in consecutives:
			# use get() so that you don't initialise empty value
			if mistakes.get(first) and mistakes.get(second):
				if mistakes[first] == mistakes[second]:
					suspects.append([first, second])

	print(suspects)
	return suspects


students = [
	# student ID, desk, answers
	(1, 6, ["a", "b", "c", "d"]),
	(9, 7, ["a", "b", "c", "d"]),
	(3, 8, ["a", "b", "d", "d"]),
	(4, 10, ["a", "b", "c", "d"]),
	(5, 11, ["a", "b", "c", "d"]),
	(6, 16, ["a", "b", "d", "d"]),
]

answers = ["a", "b", "c", "c"]

m = 5


# 1: 4_d
# 9: 4_d
# 3: 3_d, 4_d not considered, even if competitive, because mistakes are not the same

# 4: 4_d

# mistakes:
# 	id: ((q_i, wrong_answer), (q_i, wrong_answer))


# row 1 [(student_id, desk), (None, None), (student_id, desk_id), id]
# row 2
# row 3

# ->

# row 1 consecutive pairs
# row 2

detect_cheaters(
	students, answers, m
)  # => [[1, 9]], Students 1 and 9 made the same mistakes and sit next to each other.


students = [(1, 1, ["a", "b"]), (2, 2, ["a", "b"])]

answers = ["a", "b"]
m = 2

detect_cheaters(
	students, answers, m
)  # => [] Perfect scores are not suspicious.


students = [(1, 1, ["b", "b"]), (2, 2, ["b", "b"])]

answers = ["a", "b"]
m = 2

detect_cheaters(
	students, answers, m
)  # => [[1, 2]] Both students made the same mistake and sit next to each other.
