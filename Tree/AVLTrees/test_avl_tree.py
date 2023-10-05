import pytest
from AVL_Tree import AVLNode, insert_node, delete_node, in_order_traversal

class TestAVLTree:
    @pytest.fixture
    def sample_avl_tree(self):
        # Create a sample AVL tree for testing
        root = AVLNode(10)
        root = insert_node(root, 5)
        root = insert_node(root, 15)
        root = insert_node(root, 3)
        root = insert_node(root, 8)
        return root

    def test_insert_node(self, sample_avl_tree):
        # Test inserting a node
        assert in_order_traversal(sample_avl_tree) == [3, 5, 8, 10, 15]

    def test_delete_node(self, sample_avl_tree):
        # Test deleting a node
        root = delete_node(sample_avl_tree, 5)
        assert in_order_traversal(root) == [3, 8, 10, 15]

        root = delete_node(root, 10)
        assert in_order_traversal(root) == [3, 8, 15]

    def test_delete_nonexistent_node(self, sample_avl_tree):
        # Test deleting a node that doesn't exist
        root = delete_node(sample_avl_tree, 20)
        assert in_order_traversal(root) == [3, 5, 8, 10, 15]

if __name__ == "__main__":
    pytest.main()
