from app.core.node import Node

class DoublyCircularLinkedList:
    """
    A Doubly Circular Linked List implementation.
    The last node points to the head, and the head's previous points to the last node.
    """
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the list. O(1)"""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last = self.head.prev
            new_node.next = self.head
            new_node.prev = last
            last.next = new_node
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        """Insert a node at the end of the list. O(1)"""
        if self.is_empty():
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        last = self.head.prev
        
        new_node.next = self.head
        new_node.prev = last
        last.next = new_node
        self.head.prev = new_node
        self.size += 1

    def delete(self, data):
        """Delete a node containing the specified data. O(n)"""
        if self.is_empty():
            return False

        current = self.head
        found = False

        # Search for the node
        while True:
            if current.data == data:
                found = True
                break
            current = current.next
            if current == self.head:
                break

        if not found:
            return False

        # If it's the only node
        if current.next == current:
            self.head = None
        else:
            # Re-link surrounding nodes
            current.prev.next = current.next
            current.next.prev = current.prev
            if current == self.head:
                self.head = current.next

        self.size -= 1
        return True

    def search(self, data):
        """Search for a node containing data. O(n)"""
        if self.is_empty():
            return None
        
        current = self.head
        while True:
            if current.data == data:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    def to_list(self):
        """Convert the DCLL to a standard Python list. O(n)"""
        result = []
        if self.is_empty():
            return result
        
        current = self.head
        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:
                break
        return result

    def __len__(self):
        return self.size
