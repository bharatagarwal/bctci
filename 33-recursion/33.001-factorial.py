def factorial(n):
	if n == 1:
		return 1

	return n * factorial(n - 1)


factorial(998)  # => if I go to 999, I get a recursionError
