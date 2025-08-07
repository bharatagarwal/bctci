def blocks(n):
	if n == 1:
		return 1

	return blocks(n - 1) * 2 + roof(n)


def roof(n):
	if n == 1:
		return 1

	return roof(n - 1) * 2 + 1


def run_tests():
	tests = [(1, 1), (2, 5), (3, 17), (4, 49), (5, 129)]

	for n, want in tests:
		got = blocks(n)

		print(f"blocks({n}): got: {got}, want: {want}")


run_tests()
