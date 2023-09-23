class Heap:
	def __init__(self, size):
		self.custom_list = (size+1) * [None]  # Since we're not using index of 0 for ease
		self.heap_size = 0
		self.max_size = size + 1


def peek_of_heap(root_node=None):
	if not root_node:
		print("Heap does not exist!")
		return
	else:
		return root_node.custom_list[1]  # Since root is stored at 1 always


def size_of_heap(root_node=None):
	if not root_node:
		print("Heap does not exist!")
		return
	else:
		return root_node.heap_size  # Since root is stored at 1 always


def level_order_traversal(root_node):
	if not root_node:
		print("Heap does not exist!")
		return
	else:
		for i in range(1, root_node.heap_size+1):
			print(root_node.custom_list[i])


def heapify_insertion(root_node, index, heap_type):
	"""

	"""
	parent_index = index // 2
	if index <= 1:
		return
	if heap_type == "Min":
		if root_node.custom_list[index] < root_node.custom_list[parent_index]:
			temp_node = root_node.custom_list[index]
			root_node.custom_list[index] = root_node.custom_list[parent_index]
			root_node.custom_list[parent_index] = temp_node
		heapify_insertion(root_node, parent_index, heap_type)
	elif heap_type == "Max":
		if root_node.custom_list[index] > root_node.custom_list[parent_index]:
			temp_node = root_node.custom_list[index]
			root_node.custom_list[index] = root_node.custom_list[parent_index]
			root_node.custom_list[parent_index] = temp_node
		heapify_insertion(root_node, parent_index, heap_type)
	else:
		print(f"Invalid heap type {heap_type} \n It should be either 'Min' or 'Max'")


def insert_node(root_node, node_value, heap_type):
    if root_node.heap_size + 1 == root_node.max_size:
    	print("The Binary Heap is Full")
    	return
    root_node.custom_list[root_node.heap_size + 1] = node_value
    root_node.heap_size += 1
    heapify_insertion(root_node, root_node.heap_size, heap_type)
    print("The value has been successfully inserted")
    return


new_heap = Heap(5)
insert_node(new_heap, 5, 'Max')
insert_node(new_heap, 3, 'Max')
insert_node(new_heap, 2, 'Max')
insert_node(new_heap, 4, 'Max')
insert_node(new_heap, 1, 'Max')
insert_node(new_heap, 0, 'Max')
print("----------------------------------")
level_order_traversal(new_heap)
