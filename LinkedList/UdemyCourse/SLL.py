class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


class SinglyLinkedList:

	def __init__(self, value):
		new_node = Node(value)
		self.head = new_node
		self.tail = new_node
		self.length = 1

	def append(self, value):
		new_node = Node(value)
		if self.head:
			self.tail.next = new_node
			self.tail = new_node
		else:
			self.head = new_node
			self.tail = new_node
		self.length += 1


	def prepend(self, value):
		new_node = Node(value)
		if self.head:
			new_node.next = self.head
			self.head = new_node
		else:
			self.head = new_node
			self.tail = new_node
		self.length += 1


	def insert(self, value, index):
		if index > self.length:
			print("Index out of range")
			return

		if index == 0:
			self.prepend(value)
		elif index == self.length:
			self.append(value)
		else:
			count = 0
			current_node = self.head
			while current_node:
				if count == index-1:
					new_node = Node(value)
					next_node = current_node.next
					current_node.next = new_node
					new_node.next = next_node
					self.length += 1
					return
				current_node = current_node.next
				count += 1


	def search(self, target):

		if self.length == 0:
			print("Singly linked list is Empty")
			return

		current_node = self.head
		index = 0
		while current_node:
			if current_node.value == target:
				print(f"Found {target} at index {index}!")
				return
			current_node = current_node.next
			index += 1
		else:
			print(f"{target} not found in Singly linked list.")


	def get(self, index):

		if 0 < index >= self.length:
			print("Index is out of range!")
		elif index == 0:
			print(self.head.value)
			return self.head
		elif index == self.length-1 or index == -1:
			print(self.tail.value)
			return self.tail
		else:
			current_node = self.head
			index = index if index > 0 else self.length + index
			current_index = 0
			while current_node:
				if index == current_index:
					print(current_node.value)
					return current_node
				current_node = current_node.next
				current_index += 1

	def set_value(self, index, value):
		if 0 < index >= self.length:
			print("Index out of range!")
		elif self.length == 1 and index == 0:
			new_node = Node(value)
			self.head = new_node
			self.tail = new_node
		elif self.length > 1 and index == -1:
			self.tail.value = value
		else:
			current_node = self.head
			current_index = 0
			while current_node:
				if current_index == index:
					current_node.value = value
					print(f"Updated value!")
					return
				current_node = current_node.next
				current_index += 1


	def pop_first(self):
		if self.length == 0:
			return None 
		elif self.length == 1:
			self.head = None
			self.tail = None
		else:
			new_head = self.head.next 
			self.head = new_head
		self.length -= 1

	def pop(self):
		if self.length == 0:
			return None 
		elif self.length == 1:
			self.head = None
			self.tail = None
		else:
			new_tail = self.get(-2)
			new_tail.next = None
			self.tail = new_tail
		self.length -= 1

	def remove(self, index):
		if self.length == 0:
			return None 
		if self.length == 1 and index == 0:
			self.head = None
			self.tail = None
		else:
			prev_node = self.get(index-1)
			new_next_node = prev_node.next.next
			prev_node.next = new_next_node

		self.length -= 1


	def delete_all(self):
		self.head = None 
		self.tail = None 
		self.length = 0 

	def __str__(self):

		if self.length == 0:
			return("Singly linked list is empty!")

		vals = []
		current_node = self.head
		while current_node:
			vals.append(current_node.value)
			current_node = current_node.next

		return " -> ".join(map(str, vals))

sll = SinglyLinkedList(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.prepend(00)
print(sll)
sll.insert(90, 6)
print(sll)
sll.search(90)
print(sll.length)
sll.get(-2)
sll.set_value(-1, 100)
print(sll)
sll.pop_first()
print(sll)
sll.pop()
print(sll)
sll.remove(3)
print(sll)
sll.delete_all()
print(sll)

