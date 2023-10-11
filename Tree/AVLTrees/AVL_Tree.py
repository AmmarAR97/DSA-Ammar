import QueueNoSize as q


class AVLNode:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1


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


def get_height(root_node):
    if not root_node:
        return 0

    return root_node.height


def get_balance(root_node):
    if not root_node:
        return 0

    return get_height(root_node.left_child) - get_height(root_node.right_child)


def right_rotate(imbalanced_node):
    print("Right rotation")
    new_root = imbalanced_node.left_child
    imbalanced_node.left_child = imbalanced_node.left_child.right_child
    new_root.right_child = imbalanced_node
    imbalanced_node.height = 1 + max(
        get_height(imbalanced_node.left_child),
        get_height(imbalanced_node.right_child)
    )
    new_root.height = 1 + max(
        get_height(new_root.left_child),
        get_height(new_root.right_child)
    )
    return new_root


def left_rotate(imbalanced_node):
    print("Left rotation")
    new_root = imbalanced_node.right_child
    imbalanced_node.right_child = imbalanced_node.right_child.left_child
    new_root.left_child = imbalanced_node
    imbalanced_node.height = 1 + max(
        get_height(imbalanced_node.left_child),
        get_height(imbalanced_node.right_child)
    )
    new_root.height = 1 + max(
        get_height(new_root.left_child),
        get_height(new_root.right_child)
    )
    return new_root


def get_minimum_value_node(root_node):
    if root_node is None or root_node.left_child is None:
        return root_node
    else:
        return get_minimum_value_node(root_node.left_child)


def insert_node(root_node, node_value):
    if not root_node:
        return AVLNode(node_value)
    elif node_value < root_node.data:
        root_node.left_child = insert_node(root_node.left_child, node_value)
    else:
        root_node.right_child = insert_node(root_node.right_child, node_value)

    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)

    # Left-Left case (LL): Single Right Rotation
    if balance > 1 and node_value < root_node.left_child.data:
        print("Left-Left case (LL): Single Right Rotation")
        return right_rotate(root_node)

    # Right-Right case (RR): Single Left Rotation
    if balance < -1 and node_value > root_node.right_child.data:
        print("Right-Right case (RR): Single Left Rotation")
        return left_rotate(root_node)

    # Left-Right case (LR): Double Rotation (Left Right)
    if balance > 1 and node_value > root_node.left_child.data:
        print("Left-Right case (LR): Double Rotation (Left Right)")
        root_node.left_child = left_rotate(root_node.left_child)
        return right_rotate(root_node)

    # Right-Left case (RL): Double Rotation (Right Left)
    if balance < -1 and node_value < root_node.right_child.data:
        print("Right-Left case (RL): Double Rotation (Right Left)")
        root_node.right_child = right_rotate(root_node.right_child)
        return left_rotate(root_node)

    return root_node


def delete_node(root_node, node_value):
    if not root_node:
        return root_node
    elif node_value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, node_value)
    elif node_value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, node_value)
    else:
        if root_node.left_child is None:
            temp_node = root_node.right_child
            root_node = None
            return temp_node

        if root_node.right_child is None:
            temp_node = root_node.left_child
            root_node = None
            return temp_node

        # Case where the node has 2 childs, we need get the successor of the node. (smallest in the right sub tree)
        successor_node = get_minimum_value_node(root_node.right_child)
        root_node.data = successor_node.data
        root_node.right_child = delete_node(root_node.right_child, successor_node.data)

    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)

    # Left-Left case (LL): Single Right Rotation
    if balance > 1 and get_balance(root_node.left_child) >= 0:
        print("Left-Left case (LL): Single Right Rotation")
        return right_rotate(root_node)

    # Right-Right case (RR): Single Left Rotation
    if balance < -1 and  get_balance(root_node.right_child) <= 0:
        print("Right-Right case (RR): Single Left Rotation")
        return left_rotate(root_node)

    # Left-Right case (LR): Double Rotation (Left Right)
    if balance > 1 and get_balance(root_node.left_child) < 0:
        print("Left-Right case (LR): Double Rotation (Left Right)")
        root_node.left_child = left_rotate(root_node.left_child)
        return right_rotate(root_node)

    # Right-Left case (RL): Double Rotation (Right Left)
    if balance < -1 and get_balance(root_node.left_child) > 0:
        print("Right-Left case (RL): Double Rotation (Right Left)")
        root_node.right_child = right_rotate(root_node.right_child)
        return left_rotate(root_node)

    return root_node

def delete_avl_tree(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "Avl tree has been deleted succefully"

print("==========================================")
# Test inserting a node
root = AVLNode(10)
root = insert_node(root, 5)
root = insert_node(root, 15)
root = insert_node(root, 3)
root = insert_node(root, 8)
# in_order_traversal(root)
# # assert in_order_traversal(sample_avl_tree) == [3, 5, 8, 10, 15]
# print("==========================================")

# # # Test deleting a node
# root = delete_node(root, 5)
# in_order_traversal(root)
# # assert in_order_traversal(root) == [3, 8, 10, 15]
# print("==========================================")

# root = delete_node(root, 10)
# in_order_traversal(root)
# # assert in_order_traversal(root) == [3, 8, 15]
# print("==========================================")

# # Test deleting a node that doesn't exist
root = delete_node(root, 20)
in_order_traversal(root)
# assert in_order_traversal(root) == [3, 5, 8, 10, 15]
print("==========================================")

delete_avl_tree(root)
in_order_traversal(root)
