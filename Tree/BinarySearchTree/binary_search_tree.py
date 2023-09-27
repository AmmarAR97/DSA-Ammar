import QueueNoSize as Queue

class BSTNode:

	def __init__(self, data):
		self.data = data
		self.left_child = None 
		self.right_child = None 

def insert_node(root_node, node_value):
	if not root_node.data:
		root_node.data = node_value
	elif node_value <= root_node.data:
		if not root_node.left_child:
			root_node.left_child = BSTNode(node_value)
		else:
			insert_node(root_node.left_child, node_value)
	else:
		if not root_node.right_child:
			root_node.right_child = BSTNode(node_value)
		else:
			insert_node(root_node.right_child, node_value)
	print("inserted node successfully!")

def pre_order_traversal(root_node):
	if not root_node:
		return
	print(root_node.data)
	pre_order_traversal(root_node.left_child)
	pre_order_traversal(root_node.right_child)

def in_order_traversal(root_node):
	if not root_node:
		return
	in_order_traversal(root_node.left_child)
	print(root_node.data)
	in_order_traversal(root_node.right_child)

def post_order_traversal(root_node):
	if not root_node:
		return
	post_order_traversal(root_node.left_child)
	post_order_traversal(root_node.right_child)
	print(root_node.data)

def level_order_traversal(root_node):
	if not root_node:
		return
	custom_queue = Queue.Queue()
	custom_queue.enqueue(root_node)
	while not custom_queue.isEmpty():
		current_node = custom_queue.dequeue()
		print(current_node.data)
		if current_node.left_child:
			custom_queue.enqueue(current_node.left_child)
		if current_node.right_child:
			custom_queue.enqueue(current_node.right_child)


def search_node(root_node, node_value):
	if root_node.data == node_value:
		print("The value is found")
	elif node_value < root_node.data:
		if root_node.left_child.data == node_value:
			print("The value is found")
		else:
			search_node(root_node.left_child, node_value)
	else:
		if root_node.right_child.data == node_value:
			print("The value is found")
		else:
			search_node(root_node.right_child, node_value)


def min_value_node(root_node):
	current_node = root_node
	while current_node.left_child:
		current_node = current_node.left_child
	return current_node


def delete_node(root_node, node_value):
	if not root_node:
		return
	if node_value < root_node.data:
		root_node.left_child = delete_node(root_node.left_child, node_value)
	elif node_value > root_node.data:
		root_node.right_child = delete_node(root_node.right_child, node_value)
	else:
		# Node with the key to be deleted found

        # Case 1: Node with only one child or no child
		if root_node.left_child is None:
			temp_node = root_node.right_child
			root_node = None
			return temp_node

		if root_node.right_child is None:
			temp_node = root_node.left_child
			root_node = None 
			return temp_node

		# Case 2: Node with two children
        # Find the inorder successor (the smallest node in the right subtree)
		temp_node = min_value_node(root_node)
		root_node.data = temp_node.data

		# Delete the inorder successor
		root_node.right_child = delete_node(root_node.right_child, temp_node.data)

	return root_node


def delete_bst(root_node):
	root_node.data = None 
	root_node.left_child = None 
	root_node.right_child = None
	return "BST is deleted succefully!"


tree = BSTNode(None)
insert_node(tree, 70)
insert_node(tree, 50)
insert_node(tree, 90)
insert_node(tree, 30)
insert_node(tree, 60)
insert_node(tree, 80)
insert_node(tree, 100)
insert_node(tree, 20)
insert_node(tree, 40)
print("--------------------------")
pre_order_traversal(tree)
print("--------------------------")
in_order_traversal(tree)
print("--------------------------")
post_order_traversal(tree)
print("--------------------------")
level_order_traversal(tree)
print("--------------------------")
search_node(tree, 100)
print("--------------------------")
min = min_value_node(tree)
print(min.data)
print("--------------------------")
delete_node(tree, 200)
level_order_traversal(tree)
print("--------------------------")
print(delete_bst(tree))
print("--------------------------")
level_order_traversal(tree)

