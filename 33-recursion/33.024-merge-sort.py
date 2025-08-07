def merge_sort(array):
	# ---- BASE CASE

	if len(array) <= 1:
		return array[:]

	# ---- DIVIDE

	mid = len(array) // 2
	left_half = array[:mid]
	right_half = array[mid:]

	left_sorted = merge_sort(left_half)
	right_sorted = merge_sort(right_half)

	# ----- CONQUER

	result = []
	i = 0
	j = 0

	while i < len(left_sorted) and j < len(right_sorted):
		if left_sorted[i] <= right_sorted[j]:
			result.append(left_sorted[i])
			i += 1
		else:
			result.append(right_sorted[j])
			j += 1

	while i < len(left_sorted):
		result.append(left_sorted[i])
		i += 1

	while j < len(right_sorted):
		result.append(right_sorted[j])
		j += 1

	return result


test = [64, 34, 25, 12, 22, 11, 90]
sorted = merge_sort(test)

print(sorted)
