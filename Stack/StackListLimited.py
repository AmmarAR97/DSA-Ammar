class Stack:
	def __init__(self, maxSize):
		self.maxSize = maxSize
		self.list = []

	# IsEmpty
	def isEmpty(self):
		return not self.list

	# Is full
	def isFull(self):
		return True if len(self.list) >= self.maxSize else False


	# Push
	def push(self, value):
		if not self.isFull():
			self.list.append(value)
		else:
			print("Failed to push item: Stack is full")


	# Pop
	def pop(self):
		if self.isEmpty():
			print("Stack is empty")
		else:
			return self.list.pop()


	# Peek
	def peek(self):
		if self.isEmpty():
			print("Stack is empty")
		else:
			return self.list[-1]

	# Delete
	def delete(self):
		self.list = None


	def __str__(self):
		return "\n".join(map(str, self.list[-1::-1]))


customStack = Stack(5)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)
customStack.push(6)
print(customStack.pop())
print(customStack.peek())