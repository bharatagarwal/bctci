def power(b, e, m):
	if e == 0:
		return 1

	if e % 2 == 0:
		half = power(b, e // 2, m)
		return (half * half) % m

		# for odd,
		# b * even power => subsequent is halved
	return (b * power(b, e - 1, m)) % m


a = 2
p = 5
m = 100
print(power(a, p, m))  # => 32

a = 2
p = 5
m = 30
print(power(a, p, m))  # => 2

a = 3
p = 1
m = 5
print(power(a, p, m))  # => 3

a = 5
p = 3
m = 7
print(power(a, p, m))  # => 6


a = 123456789
p = 987654321
m = 1000000007
print(power(a, p, m))  # => 652541198
