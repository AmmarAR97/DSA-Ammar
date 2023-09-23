class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_beginning(self):
        if self.is_empty():
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def insert_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_last(self):
        if self.is_empty():
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data

    def insert_after(self, key, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == key:
                if current == self.tail:
                    self.insert_last(data)
                else:
                    new_node.next = current.next
                    new_node.prev = current
                    current.next.prev = new_node
                    current.next = new_node
                return True
            current = current.next
        return False

    def delete(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current == self.head:
                    return self.delete_beginning()
                elif current == self.tail:
                    return self.delete_last()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    return current.data
            current = current.next
        return None

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

# Example usage:
if __name__ == "__main__":
    linked_list = DoublyLinkedList()

    linked_list.insert_beginning(3)
    linked_list.insert_beginning(2)
    linked_list.insert_beginning(1)
    linked_list.insert_last(4)
    linked_list.insert_last(5)
    linked_list.insert_after(2, 7)
    linked_list.delete(4)

    linked_list.display_forward()  # Output: 1 -> 2 -> 7 -> 3 -> 5 -> None
    linked_list.display_backward()  # Output: 5 -> 3 -> 7 -> 2 -> 1 -> None
