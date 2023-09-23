class Stack:
	def __init__(self):
		self.list = []

	# IsEmpty
	def isEmpty(self):
		return not self.list

	# Push Method
	def push(self, value):
		self.list.append(value)
		return f"{value} inserted to the stack succesfully"

	# Pop method
	def pop(self):
		if self.isEmpty():
			return "Stack is empty"
		else:
			return self.list.pop()

	def peek(self):
		if self.isEmpty():
			return "Stack is empty"
		else:
			return self.list[-1]

	def delete(self):
		self.list = None

	def __str__(self):
		return "\n".join(map(str, self.list[-1::-1]))


customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)
print(customStack.pop())
print(customStack.peek())