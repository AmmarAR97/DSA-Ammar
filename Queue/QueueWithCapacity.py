class Queue:
	def __init__(self, maxSize):
		self.list = maxSize*[None]
		self.maxSize = maxSize
		self.start = -1
		self.top = -1


	def isFull(self):
		if self.top + 1 == self.start:
			return True
		elif self.start == 0 and self.top + 1 == self.maxSize:
			return True
		else:
			return False 


	def isEmpty(self):
		return self.top == -1


	def enqueue(self, value):
		if self.isFull():
			print("The queue is full")
		else:
			if self.top + 1 == self.maxSize:
				self.top = 0
			else:
				self.top += 1
				if self.start == -1:
					self.start = 0

			self.list[self.top] = value


	def dequeue(self):
		if self.isEmpty():
			print("The queue is empty!")
		else:
			self.list[self.start] = None 
			if self.start == self.top:
				self.start = -1
				self.top = -1
			elif self.start + 1 == self.maxSize:
				self.start = 0
			else:
				self.start += 1


	def __str__(self):
		return " ".join(map(str, self.list))

customQueue = Queue(3)
print(customQueue.isFull())
print(customQueue.isEmpty())
customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)
customQueue.enqueue(40)
print(customQueue)
customQueue.dequeue()
print(customQueue)
customQueue.dequeue()
print(customQueue)
customQueue.dequeue()
print(customQueue)
customQueue.dequeue()
print(customQueue)
customQueue.enqueue(10)
customQueue.enqueue(20)
print(customQueue)
