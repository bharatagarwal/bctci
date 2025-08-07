def binary_search(array, target, left, right):
	if left > right:
		return -1

	mid = (left + right) // 2

	if array[mid] == target:
		return mid

	if array[mid] > target:
		# don't forget return!
		return binary_search(array, target, left, mid - 1)

	if array[mid] < target:
		# don't forget return!
		return binary_search(array, target, mid + 1, right)
