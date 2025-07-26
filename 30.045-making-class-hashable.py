class Point:
	def __init__(self, name, x, y):
		self.x = x
		self.y = y
		self.name = name

	def __str__(self):
		return f"{self.name}: {self.x},{self.y}"

	def __hash__(self):
		return hash((self.name, self.x, self.y))


p = Point("Origin", 0, 0)
print(p)

record = {}

record[p] = 11

print(record[p])
