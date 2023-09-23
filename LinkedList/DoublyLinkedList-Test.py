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
        print(f"insert_beginning of {data} Succefull")

    def insert_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        print(f"insert_last of {data} Succefull")

    def insert_after(self, key, data):
        if self.is_empty():
            # return None
            pirnt("Empty List")
        else:
            current_node = self.head
            while current_node:
                if current_node.data == key:
                    if current_node == self.tail:
                        self.insert_last(data)
                    else:
                        new_node = Node(data)
                        new_node.prev = current_node
                        new_node.next = current_node.next
                        current_node.next.prev = new_node
                        current_node.next = new_node
                        print(f"insert_after of {data} after {key} Succefull")
                        return
                else:
                    current_node = current_node.next
            print(f"Key - {key} not found")

    def delete_beginning(self):
        if self.is_empty():
            # return None 
            pirnt("Empty List")
        data = self.head.data
        if self.head == self.tail:
            self.head = None 
            self.tail = None 
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def delete_last(self):
        if self.is_empty():
            # return None
            pirnt("Empty List")
        data = self.head.tail
        if self.head == self.tail:
            self.head = None 
            self.tail = None 
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data

    def delete(self, key):
        if self.is_empty():
            # return None
            pirnt("Empty List")
        else:
            current_node = self.head
            while current_node:
                if current_node.data == key:
                    if current_node == self.head:
                        return self.delete_beginning()
                    elif current_node == self.tail:
                        return self.delete_last()
                    else:
                        current_node.prev.next = current_node.next
                        current_node.next.prev = current_node.prev
                        print(f"deletetion of {key} Succefull")
                        return
                else:
                    current_node = current_node.next
            print(f"Key - {key} not found")
            return


    def display_forward(self):
        if self.is_empty():
            pirnt("Empty List")
        else:
            items = []
            current_node = self.head
            while current_node:
                items += [current_node.data]
                current_node = current_node.next
            print("Forward display")
            print(" --> ".join(map(str, items)))


    def display_backward(self):
        if self.is_empty():
            pirnt("Empty List")
        else:
            items = []
            current_node = self.head
            while current_node:
                items = [current_node.data] + items
                # print(current_node.data)
                current_node = current_node.next
            print("Backword display")
            print(" --> ".join(map(str, items)))


# Example usage:
if __name__ == "__main__":
    linked_list = DoublyLinkedList()

    linked_list.insert_beginning(3)
    linked_list.display_forward() 
    linked_list.insert_beginning(2)
    linked_list.display_forward() 
    linked_list.insert_beginning(1)
    linked_list.display_forward() 
    linked_list.insert_last(4)
    linked_list.display_forward() 
    linked_list.insert_last(5)
    linked_list.display_forward() 
    linked_list.insert_after(2, 7)
    linked_list.display_forward() 
    linked_list.delete(4)
    linked_list.display_forward()  # Output: 1 -> 2 -> 7 -> 3 -> 5 -> None
    linked_list.display_backward()  # Output: 5 -> 3 -> 7 -> 2 -> 1 -> None




