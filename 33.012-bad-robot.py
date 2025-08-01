def moves(sequence):
	results = []

	def move_recursively(position):
		if position == len(sequence):
			return

		if sequence[position] == "2":
			move_recursively(position + 1)
			move_recursively(position + 2)

		if sequence[position] in "LR":
			results.append(sequence[position])
			move_recursively(position + 1)

	# return move_recursively(sequence[0])
	return "".join(results)
