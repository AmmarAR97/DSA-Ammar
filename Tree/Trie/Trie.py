# TrieNode class represents a single node in the Trie data structure.
class TrieNode:
	def __init__(self):
		# Dictionary to store child nodes, where keys are characters and values are TrieNode objects.
		self.children = {}
		# Flag to indicate if this node marks the end of a complete word.
		self.end_of_string = False

# Trie class represents the Trie data structure.
class Trie:
	def __init__(self):
		# Initialize the Trie with a root node that has no character and no end_of_string flag.
		self.root = TrieNode()

	# Method to insert a string into the Trie.
	def insert_string(self, word):
		current = self.root
		for ch in word:
			# Check if the character exists as a child of the current node.
			node = current.children.get(ch)
			if node is None:
				# If not, create a new node and add it as a child.
				node = TrieNode()
				current.children.update({ch: node})
			# Move to the next node.
			current = node
		# Mark the end of the inserted string.
		current.end_of_string = True
		print("Successfully inserted the node!")

	# Method to search for a string in the Trie.
	def search_string(self, word):
		current = self.root
		for ch in word:
			# Check if the character exists as a child of the current node.
			node = current.children.get(ch)
			if node is None:
				# If not found, the string is not in the Trie.
				return False
			# Move to the next node.
			current = node
		# If the end_of_string flag is set, the string is in the Trie.
		if current.end_of_string:
			return True
		else:
			return False

# Recursive function to delete a string from the Trie.
def delete_string(root_node, word, index):
	ch = word[index]
	current_node = root_node.children.get(ch)
	can_delete_this_node = False

	# If the current node has more than one child, we cannot delete it, so we recursively check its children.
	if len(current_node.children) > 1:
		delete_string(current_node, word, index + 1)
		return False

	# If we have reached the end of the word.
	if index == len(word) - 1:
		# If the current node has other children, just unset the end_of_string flag.
		if len(current_node.children) >= 1:
			current_node.end_of_string = False
			return False
		else:
			# If it has no other children, remove it from the parent node's children.
			root_node.children.pop(ch)

	# If the current node marks the end of a string, we recursively check its children.
	if current_node.end_of_string:
		delete_string(current_node, word, index + 1)
		return False

	# Recursively check if we can delete the current node.
	can_delete_this_node = delete_string(current_node, word, index + 1)
	if can_delete_this_node:
		# If we can delete the current node, remove it from the parent node's children.
		root_node.children.pop(ch)
		return True
	else:
		return False



new_trie = Trie()
new_trie.insert_string("App")
new_trie.insert_string("Apple")
delete_string(new_trie.root, "App", 0)
new_trie.insert_string("BSD")
print(new_trie.search_string("App"))