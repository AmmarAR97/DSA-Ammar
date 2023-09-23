class Queue:
	def __init__(self):
		self.list = []


	def isEmpty(self):
		return not self.list


	def enqueue(self, value):
		self.list.append(value)


	def dequeue(self):
		if not self.isEmpty():
			return self.list.pop(0)
		else:
			print("The Queue is empty")

	def peek(self):
		if not self.isEmpty():
			return self.list[0]
		else:
			print("The Queue is empty")

	def delete(self):
		self.list = None

	def __str__(self):
		return " ".join(map(str, self.list))