import QueueNoSize as q


class AVLNode:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1

    def get_height(self, root_node):
        if not root_node:
            return 0

        return root_node.height

    def get_balance(self, root_node):
        if not root_node:
            return 0

        return self.get_height(root_node.left_child) - self.get_height(root_node.right_child)

    def right_rotate(self, imbalanced_node):
        print("Right rotation")
        new_root = imbalanced_node.left_child
        imbalanced_node.left_child = imbalanced_node.left_child.right_child
        new_root.right_child = imbalanced_node
        imbalanced_node.height = 1 + max(
            self.get_height(imbalanced_node.left_child),
            self.get_height(imbalanced_node.right_child)
        )
        new_root.height = 1 + max(
            self.get_height(new_root.left_child),
            self.get_height(new_root.right_child)
        )
        return new_root

    def left_rotate(self, imbalanced_node):
        print("Left rotation")
        new_root = imbalanced_node.right_child
        imbalanced_node.right_child = imbalanced_node.right_child.left_child
        new_root.left_child = imbalanced_node
        imbalanced_node.height = 1 + max(
            self.get_height(imbalanced_node.left_child),
            self.get_height(imbalanced_node.right_child)
        )
        new_root.height = 1 + max(
            self.get_height(new_root.left_child),
            self.get_height(new_root.right_child)
        )
        return new_root

    def insert_node(self, root_node, node_value):
        if not root_node:
            return AVLNode(node_value)
        elif node_value < root_node.data:
            root_node.left_child = self.insert_node(root_node.left_child, node_value)
        else:
            root_node.right_child = self.insert_node(root_node.right_child, node_value)

        root_node.height = 1 + max(self.get_height(root_node.left_child), self.get_height(root_node.right_child))
        balance = self.get_balance(root_node)

        # Left-Left case (LL): Single Right Rotation
        if balance > 1 and node_value < root_node.left_child.data:
            print("Left-Left case (LL): Single Right Rotation")
            return self.right_rotate(root_node)

        # Right-Right case (RR): Single Left Rotation
        if balance < -1 and node_value > root_node.right_child.data:
            print("Right-Right case (RR): Single Left Rotation")
            return self.left_rotate(root_node)

        # Left-Right case (LR): Double Rotation (Left Right)
        if balance > 1 and node_value > root_node.left_child.data:
            print("Left-Right case (LR): Double Rotation (Left Right)")
            root_node.left_child = self.left_rotate(root_node.left_child)
            return self.right_rotate(root_node)

        # Right-Left case (RL): Double Rotation (Right Left)
        if balance < -1 and node_value < root_node.right_child.data:
            print("Right-Left case (RL): Double Rotation (Right Left)")
            root_node.right_child = self.right_rotate(root_node.right_child)
            return self.left_rotate(root_node)

        return root_node

def pre_order_traversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)


def in_order_traversal(root_node: AVLNode):
    if not root_node:
        return
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)


def post_order_traversal(root_node: AVLNode):
    if not root_node:
        return
    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.data)


def level_order_traversal(root_node):
    if not root_node:
        return
    custom_queue = q.Queue()
    custom_queue.enqueue(root_node)

    while not custom_queue.isEmpty():
        current_node = custom_queue.dequeue()
        print(current_node.data)

        if current_node.left_child:
            custom_queue.enqueue(current_node.left_child)

        if current_node.right_child:
            custom_queue.enqueue(current_node.right_child)


def search_avl_tree(root_node, node_value):
    if not root_node:
        print("Not found")
        return
    if root_node.data == node_value:
        print("The value is found")
    elif node_value < root_node.data:
        if root_node.left_child.data == node_value:
            print("The value is found")
        else:
            search_avl_tree(root_node.left_child, node_value)
    else:
        if root_node.right_child.data == node_value:
            print("The value is found")
        else:
            search_avl_tree(root_node.right_child, node_value)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = q.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.data)
            if root.left_child is not None:
                customQueue.enqueue(root.left_child)
            if root.right_child is not None:
                customQueue.enqueue(root.right_child)

avl_tree = AVLNode(5)
levelOrderTraversal(avl_tree)
print("--------------------------------")
avl_tree = avl_tree.insert_node(avl_tree, 10)
levelOrderTraversal(avl_tree)
print("--------------------------------")
# avl_tree.insert_node(avl_tree, 1)
# levelOrderTraversal(avl_tree)
# print("--------------------------------")
avl_tree = avl_tree.insert_node(avl_tree, 15)
levelOrderTraversal(avl_tree)
print("--------------------------------")
avl_tree = avl_tree.insert_node(avl_tree, 20)
levelOrderTraversal(avl_tree)
print("--------------------------------")
avl_tree = avl_tree.insert_node(avl_tree, 25)
# level_order_traversal(avl_tree)
levelOrderTraversal(avl_tree)

