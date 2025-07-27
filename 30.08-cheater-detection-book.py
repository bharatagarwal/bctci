"""
# Cheater Detection

You are given an array, answers, with the answers of a multi-choice test. The list has k characters ('a', 'b', 'c', or 'd'), where k is the number of questions in the exam.

You are also given an array, students, of students' answers for the test. Each entry is a tuple [student_id, desk, answers], where:

Student IDs are unique positive integers.

Desks are unique positive integers. Desks are arranged in rows of m desks, starting with desks 1 to m in the first row, m+1 to 2m in the second row, and so on. Not all desks may be occupied. E.g., there may be a student at desk 2 but none at desk 1.

For each student, answers is an array of k characters ('a', 'b', 'c', or 'd').

Two students are considered suspect if they have made identical mistakes and sit next to each other in the same row (we don't care about students in the front or behind one another).

Return a list of all pairs of suspect students in any order (the order of the two students in a pair also doesn't matter).

Example 1: answers = ['a', 'b', 'c', 'c'], m = 5, students = [
    # student ID, desk, answers
    (4, 10, ['a', 'b', 'c', 'd']),
    (1, 6,  ['a', 'b', 'c', 'd']),
    (3, 8,  ['a', 'b', 'd', 'd']),
    (5, 11, ['a', 'b', 'c', 'd']),
    (9, 7,  ['a', 'b', 'c', 'd']),
    (6, 16, ['a', 'b', 'd', 'd'])
]
Output: [[1, 9]]. Students 1 and 9 made the same mistakes and sit next to each
other.

Example 2: answers = ['a', 'b'], m = 2, students = [
    (1, 1, ['a', 'b']),
    (2, 2, ['a', 'b'])
]
Output: []. Perfect scores are not suspicious.

Example 3: answers = ['a', 'b'], m = 2, students = [
    (1, 1, ['b', 'b']),
    (2, 2, ['b', 'b'])
]
Output: [[1, 2]]. Both students made the same mistake and sit next to each
other.

Constraints:

- The length of answers is at most 10^5
- The length of students is at most 10^5
- All answers are 'a', 'b', 'c', or 'd'
- All student IDs are unique positive integers
- All desks are unique positive integers
- m is a positive integer less than 10^5
"""


def same_row(desk1, desk2, width):
	return (desk1 - 1) // width == (desk2 - 1) // width


def suspect_students(students, answers, m):
	desk_to_index = {}

	for index, [student_id, desk, student_answers] in enumerate(
		students
	):
		if student_answers != answers:
			desk_to_index[desk] = index

	sus_pairs = []

	for student_id, desk, answers in students:
		other_desk = desk + 1
		if (
			same_row(desk, other_desk, m)
			and other_desk in desk_to_index
		):
			other_student = students[desk_to_index[other_desk]]
			if answers == other_student[2]:
				sus_pairs.append([student_id, other_student[0]])

	print(sus_pairs)
	return sus_pairs


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

suspect_students(
	students, answers, m
)  # => [[1, 9]], Students 1 and 9 made the same mistakes and sit next to each other.


students = [(1, 1, ["a", "b"]), (2, 2, ["a", "b"])]

answers = ["a", "b"]
m = 2

suspect_students(
	students, answers, m
)  # => [] Perfect scores are not suspicious.


students = [(1, 1, ["b", "b"]), (2, 2, ["b", "b"])]

answers = ["a", "b"]
m = 2

suspect_students(
	students, answers, m
)  # => [[1, 2]] Both students made the same mistake and sit next to each other.
