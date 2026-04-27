class Node:
    """
    Represent a node in a Doubly Circular Linked List.
    Each node points to both the previous and next nodes.
    """
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return f"Node({self.data})"
