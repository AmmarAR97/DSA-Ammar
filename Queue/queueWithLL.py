class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None 
		self.tail = None

	def __iter__(self):
		curr = self.head
		while curr:
			yield curr.value
			curr = curr.next

class Queue:
	def __init__(self):
		self.linkedList = LinkedList()

	def isEmpty(self):
		return self.linkedList.head == None

	def enqueue(self, value):
		new_node = Node(value)
		if self.linkedList.head == None:
			self.linkedList.head = new_node
			self.linkedList.tail = new_node
		else:
			self.linkedList.tail.next = new_node 
			self.linkedList.tail = new_node

	def dequeue(self):
		if self.isEmpty():
			print("The queue is empty!")
		elif self.linkedList.head == self.linkedList.tail:
			self.linkedList.head = None 
			self.linkedList.tail = None 
		else:
			self.linkedList.head = self.linkedList.head.next

	def peek(self):
		if self.isEmpty():
			print("The queue is empty!")
		else:
			print(self.linkedList.head.value)

	def delete(self):
		self.linkedList.head = None 
		self.linkedList.tail = None 

	def __str__(self):		
		return " -> ".join(map(str, self.linkedList))

customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)
customQueue.enqueue(40)
customQueue.enqueue(50)
print(customQueue)
print(customQueue.isEmpty())
customQueue.dequeue()
print(customQueue)
customQueue.peek()
customQueue.delete()
print(customQueue)
