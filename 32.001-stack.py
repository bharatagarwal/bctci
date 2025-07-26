class Stack:
	def __init__(self):
		self.array = list()

	def push(self, value):
		self.array.append(value)

	def pop(self):
		if not self.array:
			raise IndexError("Stack is empty")

		value = self.array[-1]
		self.array.pop()

		return value

	def peek(self):
		if not self.array:
			raise IndexError("Stack is empty")

		return self.array[-1]

	def size(self):
		return len(self.array)

	def __len__(self):
		return len(self.array)
