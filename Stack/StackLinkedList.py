class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def __iter__(self):
		curr = self.head
		while curr:
			yield curr
			curr = curr.next

class Stack:
	def __init__(self):
		self.linkedList = LinkedList()

	def isEmpty(self):
		return not self.linkedList.head

	def push(self, value):
		new_node = Node(value)
		new_node.next = self.linkedList.head
		self.linkedList.head = new_node

	def pop(self):
		if not self.isEmpty():
			poped_node_value = self.linkedList.head.value
			self.linkedList.head = self.linkedList.head.next
			print(f"poped out {poped_node_value}")
		else:
			print("Stack is empty!")

	def peek(self):
		if not self.isEmpty():
			print(self.linkedList.head.value)
		else:
			print("Stack is empty!")

	def delete(self):
		self.linkedList.head = None


	def __str__(self):
		lst = [x.value for x in self.linkedList]
		return "\n".join(map(str, lst))



customStack = Stack()
print(customStack.isEmpty())
customStack.push(10)
customStack.push(20)
customStack.push(30)
# print(customStack)
customStack.pop()
print(customStack)