import QueueNoSize as Queue

class TreeNode:
	def __init__(self, data):
		self.data = data
		self.left_child = None
		self.right_child = None

tree = TreeNode('Drinks')
cold = TreeNode('Cold')
hot = TreeNode('Hot')
tree.left_child = cold
tree.right_child = hot
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
cola = TreeNode('Cola')
fanta = TreeNode('Fanta')
cold.left_child = cola
cold.right_child = fanta
hot.left_child = tea
hot.right_child = coffee


# Root node -> Left sub-tree -> Right sub-tree
def pre_order_traversal(root_node):
	if not root_node:
		return
	print(root_node.data)
	pre_order_traversal(root_node.left_child)
	pre_order_traversal(root_node.right_child)

# print("\nPrinting pre_order_traversal:")
# pre_order_traversal(tree)


# Left sub-tree -> Root node  -> Right sub-tree
def in_order_traversal(root_node):
	if not root_node:
		return
	in_order_traversal(root_node.left_child)
	print(root_node.data)
	in_order_traversal(root_node.right_child)

# print("\nPrinting in_order_traversal:")
# in_order_traversal(tree)


# Left sub-tree -> Right sub-tree -> Root node
def post_order_traversal(root_node):
	if not root_node:
		return
	post_order_traversal(root_node.left_child)
	post_order_traversal(root_node.right_child)
	print(root_node.data)

# print("\nPrinting post_order_traversal:")
# post_order_traversal(tree)


# Go level by level print all nodes from root
def level_order_traversal(root_node):
	if not root_node:
		return
	custom_queue = Queue.Queue()
	custom_queue.enqueue(root_node)
	while custom_queue.isEmpty() is False:
		current_node = custom_queue.dequeue()
		print(current_node.data)
		if current_node.left_child:
			custom_queue.enqueue(current_node.left_child)
		if current_node.right_child:
			custom_queue.enqueue(current_node.right_child)

# print("\nPrinting level_order_traversal:")
# level_order_traversal(tree)

# Go level by level print all nodes from root
def searchBT(root_node, value):
	if not root_node:
		return "Binary tree does not exist" 
	custom_queue = Queue.Queue()
	custom_queue.enqueue(root_node)
	while custom_queue.isEmpty() is False:
		current_node = custom_queue.dequeue()
		if current_node.data == value:
			return f"Found {value}!"
		if current_node.left_child:
			custom_queue.enqueue(current_node.left_child)
		if current_node.right_child:
			custom_queue.enqueue(current_node.right_child)
	else:
		return f"{value} not found!"
			
# print(searchBT(tree, "Fanta"))


# Go level by level print all nodes from root
def insert_node_to_BT(root_node, new_node):
	if not root_node:
		return new_node
	custom_queue = Queue.Queue()
	custom_queue.enqueue(root_node)
	while custom_queue.isEmpty() is False:
		current_node = custom_queue.dequeue()
		if current_node.left_child:
			custom_queue.enqueue(current_node.left_child)
		else:
			current_node.left_child = new_node
			return "Added New node!"
		if current_node.right_child:
			custom_queue.enqueue(current_node.right_child)
		else:
			current_node.left_child = new_node
			return "Added New node!"
			
# print(insert_node_to_BT(tree, TreeNode('CocaCola')))
# level_order_traversal(tree)


""" 
To delete a node:
1. Get the deepest(last) node from the three.
2. Find the node you want to delete.
3. replace the deepest node with node you want to delete.
4. delete the deepest node
"""

def get_deepest_node(root_node):
	if not root_node:
		return "Binary tree does not exist" 
	custom_queue = Queue.Queue()
	custom_queue.enqueue(root_node)
	while custom_queue.isEmpty() is False:
		deepest_node = custom_queue.dequeue()
		if deepest_node.left_child:
			custom_queue.enqueue(deepest_node.left_child)
		if deepest_node.right_child:
			custom_queue.enqueue(deepest_node.right_child)
	return deepest_node

# deepest_node = get_deepest_node(tree)
# print(deepest_node.data)
# level_order_traversal(tree)

def delete_deepest_node(root_node, deepest_node):
	if not root_node:
		return "Binary tree does not exist"
	custom_queue = Queue.Queue()
	custom_queue.enqueue(root_node)
	while custom_queue.isEmpty() is False:
		current_node = custom_queue.dequeue()
		if current_node is deepest_node:
			current_node = None
			return
		if current_node.left_child:
			if current_node.left_child is deepest_node:
				current_node.left_child = None
				return
			else:
				custom_queue.enqueue(current_node.left_child)
		if current_node.right_child:
			if current_node.right_child is deepest_node:
				current_node.right_child = None
				return
			else:
				custom_queue.enqueue(current_node.right_child)

def delete_node_bt(root_node, node_value):
	if not root_node:
		return "Binary tree does not exist"
	custom_queue = Queue.Queue()
	custom_queue.enqueue(root_node)
	while custom_queue.isEmpty() is False:
		current_node = custom_queue.dequeue()
		if current_node.data == node_value:
			deepest_node = get_deepest_node(root_node)
			current_node.data = deepest_node.data
			delete_deepest_node(root_node, deepest_node)
			return "Node deleted!"
		if current_node.left_child:
			custom_queue.enqueue(current_node.left_child)
		if current_node.right_child:
			custom_queue.enqueue(current_node.right_child)

# level_order_traversal(tree)
level_order_traversal(tree)
delete_node_bt(tree, 'Hot')
print("---------------------")
level_order_traversal(tree)

def delete_bt(root_node):
	if root_node:
		root_node.data = None 
		root_node.left_child = None 
		root_node. right_child = None
	else:
		print("Empty Tree!")

delete_bt(tree)
level_order_traversal(tree)
delete_bt(tree)
