class BinaryTree:

	def __init__(self, size):
		self.custom_list = [None]*size
		self.last_used_index = 0
		self.size = size

	def insert_node(self, value):
		if self.last_used_index + 1 == self.size:
			return "Tree is full!"
		else:
			self.custom_list[self.last_used_index+1] = value
			self.last_used_index += 1
			return "Inserted node succefully!"

	def search_node(self, value):
		for i in range(self.size):
			if self.custom_list[i] == value:
				return f"Found node at index {i}!"
		else:
			return "Node not found!"

	def pre_order_traversal(self, index=1):
		if index > self.last_used_index:
			return
		print(self.custom_list[index])
		self.pre_order_traversal(index*2)
		self.pre_order_traversal((index*2) + 1)

	def in_order_traversal(self, index=1):
		if index > self.last_used_index:
			return
		self.in_order_traversal(index*2)
		print(self.custom_list[index])
		self.in_order_traversal((index*2) + 1)

	def post_order_traversal(self, index=1):
		if index > self.last_used_index:
			return
		self.post_order_traversal(index*2)
		self.post_order_traversal((index*2) + 1)
		print(self.custom_list[index])

	def level_order_traversal(self, index=1):
		for i in range(index, self.last_used_index+1):
			print(self.custom_list[i])

	def delete_node(self, value):
		if self.last_used_index == 0:
			print("Empty tree!")
			return
		for i in range(1, self.last_used_index+1):
			if self.custom_list[i] == value:
				self.custom_list[i] = self.custom_list[self.last_used_index]
				self.custom_list[self.last_used_index] = None
				self.last_used_index -= 1
				print("Node deleted!")
				return self.level_order_traversal()
		else:
			print("Node not found!")

	def delete_tree(self):
		self.custom_list = None 
		self.last_used_index = None
		self.size = None
		print("Deleted binary tree!")


tree = BinaryTree(8)
print(tree.insert_node("Drinks"))
print(tree.insert_node("Hot"))
print(tree.insert_node("Cold"))
print(tree.insert_node("Tea"))
print(tree.insert_node("Coffee"))
print("--------------------------")
print(tree.search_node("Tea"))
print(tree.search_node("Cola"))
print("--------------------------")
tree.pre_order_traversal()
print("--------------------------")
tree.in_order_traversal()
print("--------------------------")
tree.post_order_traversal()
print("--------------------------")
tree.level_order_traversal()
print("--------------------------")
tree.delete_node("Cold")
print("--------------------------")
tree.delete_tree()
