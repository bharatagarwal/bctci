def merge_two_sorted_arrays(left, right):
	result = []
	i = 0
	j = 0

	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1

	while i < len(left):
		result.append(left[i])
		i += 1

	while j < len(right):
		result.append(right[j])
		j += 1

	return result


left = [1, 4, 7, 9]
right = [2, 3, 6, 8, 10]
merged = merge_two_sorted_arrays(left, right)

print(merged)
