class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Check if the linked list is empty."""
        return self.head is None

    def append(self, data):
        """Add a new node with the given data to the end of the linked list."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        """Add a new node with the given data to the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete the first occurrence of a node with the given data."""
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        """Search for the first occurrence of a node with the given data and return it."""
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def display(self):
        """Print the elements of the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))


# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    linked_list.display()  # Output: 1 -> 2 -> 3 -> 4

    linked_list.prepend(0)

    linked_list.display()  # Output: 0 -> 1 -> 2 -> 3 -> 4

    linked_list.delete(2)

    linked_list.display()  # Output: 0 -> 1 -> 3 -> 4

    node = linked_list.search(4)
    if node:
        print("Found:", node.data)  # Output: Found: 3
    else:
        print("Not Found")
