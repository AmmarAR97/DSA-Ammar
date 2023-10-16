class Heap:
	def __init__(self, size):
		self.max_size = size + 1
		self.custom_list = self.max_size * [None]
		self.heap_size = 0


# Function to get the root (minimum/maximum value) of the heap
def peep_of_heap(root_node):
	if not root_node or root_node.heap_size == 0 or root_node.custom_list is None:
		return None
	else:
		return root_node.custom_list[1]


# Function to get the size of the heap
def size_of_heap(root_node):
	if not root_node or root_node.heap_size == 0 or root_node.custom_list is None:
		return 0
	else:
		return root_node.heap_size


# Function to perform level-order traversal of the heap
def level_order_traversal(root_node):
	if not root_node or root_node.heap_size == 0 or root_node.custom_list is None:
		print("Heap is empty.")
		return
	else:
		for i in range(1, root_node.heap_size+1):
			print(root_node.custom_list[i], end=" ")


# Function to heapify after inserting a new node
def heapify_tree_insert(root_node, index, heap_type):
	if index <= 1:
		return

	parent_index = index // 2

	if heap_type == "Min":
		if root_node.custom_list[parent_index] > root_node.custom_list[index]:
			temp = root_node.custom_list[index]
			root_node.custom_list[index] = root_node.custom_list[parent_index]
			root_node.custom_list[parent_index] = temp
			print(f"Swapped: {temp} <-> {root_node.custom_list[index]}")
		heapify_tree_insert(root_node, parent_index, heap_type)
	else:
		if root_node.custom_list[parent_index] < root_node.custom_list[index]:
			temp = root_node.custom_list[index]
			root_node.custom_list[index] = root_node.custom_list[parent_index]
			root_node.custom_list[parent_index] = temp
			print(f"Swapped: {temp} <-> {root_node.custom_list[index]}")
		heapify_tree_insert(root_node, parent_index, heap_type)


def insert_node(root_node, node_value, heap_type):
	if root_node.heap_size + 1 == root_node.max_size:
		return "The Binary Heap is Full"

	root_node.custom_list[root_node.heap_size + 1] = node_value
	root_node.heap_size += 1
	heapify_tree_insert(root_node, root_node.heap_size, heap_type)
	return "The value has been successfully inserted"


# Function to heapify after extracting the root node
def heapify_tree_extract(root_node, index, heap_type):
	left_index = index*2
	right_index = index*2 + 1
	swap_child = 0

	if root_node.heap_size < left_index:
		return # If there are no children, stop
	elif root_node.heap_size == left_index: # when a node has only a left child
		if heap_type == "Min":
			if root_node.custom_list[left_index] < root_node.custom_list[index]:
				temp = root_node.custom_list[index]
				root_node.custom_list[index] = root_node.custom_list[left_index]
				root_node.custom_list[left_index] = temp
			return
		else:
			if root_node.custom_list[left_index] > root_node.custom_list[index]:
				temp = root_node.custom_list[index]
				root_node.custom_list[index] = root_node.custom_list[left_index]
				root_node.custom_list[left_index] = temp
			return
	else:
		if heap_type == "Min":
			if root_node.custom_list[left_index] > root_node.custom_list[right_index]:
				swap_child = right_index
			else:
				swap_child = left_index

			if root_node.custom_list[swap_child] < root_node.custom_list[index]:
				temp = root_node.custom_list[index]
				root_node.custom_list[index] = root_node.custom_list[left_index]
				root_node.custom_list[left_index] = temp
			return
		else:
			if root_node.custom_list[left_index] < root_node.custom_list[right_index]:
				swap_child = right_index
			else:
				swap_child = left_index

			if root_node.custom_list[swap_child] > root_node.custom_list[index]:
				temp = root_node.custom_list[index]
				root_node.custom_list[index] = root_node.custom_list[left_index]
				root_node.custom_list[left_index] = temp

	heapify_tree_extract(root_node, swap_child, heap_type)


# Function to extract the root node from the heap
def extract_node(root_node, heap_type):
	if root_node.heap_size == 0:
		return
	else:
		extracted_node = root_node.custom_list[1]
		root_node.custom_list[1] = root_node.custom_list[root_node.heap_size]
		root_node.custom_list[root_node.heap_size] = None
		root_node.heap_size -= 1
		heapify_tree_extract(root_node, 1, heap_type)
		return extracted_node


# Function to delete all elements and reset the heap
def delete_entire_heap(root_node):
	root_node.custom_list = None



newHeap = Heap(5)
insert_node(newHeap, 4, "Min")
insert_node(newHeap, 5, "Min")
insert_node(newHeap, 2, "Min")
insert_node(newHeap, 1, "Min")
insert_node(newHeap, 3, "Min")
extract_node(newHeap, "Min")
# delete_entire_heap(newHeap)
level_order_traversal(newHeap)

