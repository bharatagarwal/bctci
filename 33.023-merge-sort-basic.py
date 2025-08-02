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


def merge_sort_basic(array, depth=0):
	indent = "  " * depth
	print(f"{indent}Calling merge_sort with array: {array}")

	if len(array) <= 1:
		print(f"{indent}Base case reached, returning: {array}")
		return array

	mid = len(array) // 2
	left_half = array[:mid]
	right_half = array[mid:]

	print(
		f"{indent}Splitting into left: {left_half}, right: {right_half}"
	)

	print(f"{indent}Recursively sorting left half:")
	left_sorted = merge_sort_basic(left_half, depth + 1)

	print(f"{indent}Recursively sorting right half:")
	right_sorted = merge_sort_basic(right_half, depth + 1)

	print(f"{indent}Merging {left_sorted} and {right_sorted}")
	result = merge_two_sorted_arrays(left_sorted, right_sorted)
	print(f"{indent}Merged result: {result}")

	return result


test = [64, 34, 25, 12, 22, 11, 90]
sorted = merge_sort_basic(test)

print(sorted)
