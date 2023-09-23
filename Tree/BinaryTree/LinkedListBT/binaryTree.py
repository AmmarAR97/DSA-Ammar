class TreeNode:
	def __init__(self, data, children=[]):
		self.data = data
		self.children = children

	def add_child(self, TreeNode):
		self.children.append(TreeNode)

	def __str__(self, level=0):
		ret = "  " * level + str(self.data)  + "\n"
		for child in self.children:
			ret += child.__str__(level + 1)
		return ret

tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
tree.add_child(cold)
tree.add_child(hot)

print(tree)