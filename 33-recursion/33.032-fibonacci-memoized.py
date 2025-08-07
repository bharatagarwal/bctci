def fib(n):
	memo = {}
	stack_depth = 0
	print(f"Computing fibonacci({n})")

	def fib_rec(i):
		nonlocal stack_depth
		stack_depth += 1
		indent = "  " * stack_depth
		print(f"{indent}ENTER fib_rec({i}) - Stack depth: {stack_depth}")
		
		if i <= 1:
			print(f"{indent}  Base case: fib_rec({i}) = 1")
			result = 1
		elif i in memo:
			print(f"{indent}  Found in memo: fib_rec({i}) = {memo[i]}")
			result = memo[i]
		else:
			print(f"{indent}  Computing fib_rec({i}) = fib_rec({i-1}) + fib_rec({i-2})")
			result = fib_rec(i - 1) + fib_rec(i - 2)
			memo[i] = result
			print(f"{indent}  Storing in memo: fib_rec({i}) = {result}")

		print(f"{indent}EXIT fib_rec({i}) = {result} - Stack depth: {stack_depth}")
		stack_depth -= 1
		return result

	return fib_rec(n)


print(fib(5))
