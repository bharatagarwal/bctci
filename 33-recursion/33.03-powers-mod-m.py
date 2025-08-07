"""
# Powers Mod M

a > 1
p >= 0
m > 1

(a^p) % m

avoiding storing intermediate values much larger than m.


a^0 = 1
a^p = a*a^(p-1)



When it comes to the modulo operation, we can apply it at each step without affecting the result:

a^0 % m = 1
For p > 0, a^p % m = (a * (a^(p-1) % m)) % m

Constraints:

- 1 < a <= 10^9
- 0 <= p <= 10^9
- 1 < m <= 10^9
"""


def calculate(base, exponent, modulo):
	if exponent == 0:
		return 1

	return base * calculate(base, exponent - 1, modulo) % modulo


a = 2
p = 5
m = 100
print(calculate(a, p, m))  # => 32

a = 2
p = 5
m = 30
print(calculate(a, p, m))  # => 2

a = 3
p = 1
m = 5
print(calculate(a, p, m))  # => 3

a = 5
p = 3
m = 7
print(calculate(a, p, m))  # => 6


a = 123456789
p = 987654321
m = 1000000007
print(calculate(a, p, m))  # => 652541198
