def fib(n, depth=0):
	indent = "  " * depth
	print(f"{indent}fib({n}) called")

	if n <= 1:
		print(f"{indent}fib({n}) = {n} (base case)")
		return n

	print(f"{indent}fib({n}) calculating fib({n - 1}) + fib({n - 2})")
	left = fib(n - 1, depth + 1)
	right = fib(n - 2, depth + 1)
	result = left + right
	print(f"{indent}fib({n}) = {left} + {right} = {result}")
	return result


# Test with a small number to see the call stack
print("Computing fib(5):")
print(f"Result: {fib(5)}")
