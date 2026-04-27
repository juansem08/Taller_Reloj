from app.core.dcll import DoublyCircularLinkedList
from app.models.clock_data import ClockData

class ClockManager:
    """
    Service to manage multiple world clocks using a Doubly Circular Linked List.
    """
    def __init__(self):
        self.clocks_list = DoublyCircularLinkedList()
        self.current_node = None
        
        # Initialize with a default clock (Local)
        self.add_clock("Hora Local", "America/Bogota") # Default as per user context (Colombia)

    def add_clock(self, city, timezone):
        """Add a new clock to the system. O(1)"""
        new_clock = ClockData(city, timezone)
        self.clocks_list.insert_at_end(new_clock)
        
        # Set head as current if it's the first clock
        if self.current_node is None:
            self.current_node = self.clocks_list.head

    def remove_current_clock(self):
        """Remove the currently displayed clock. O(n) due to search in DCLL delete"""
        if self.clocks_list.is_empty():
            return False
        
        data_to_remove = self.current_node.data
        next_node = self.current_node.next
        
        if self.clocks_list.delete(data_to_remove):
            if self.clocks_list.is_empty():
                self.current_node = None
            else:
                self.current_node = next_node
            return True
        return False

    def next_clock(self):
        """Navigate to the next clock in the circular list. O(1)"""
        if self.current_node:
            self.current_node = self.current_node.next
        return self.get_current_clock()

    def previous_clock(self):
        """Navigate to the previous clock in the circular list. O(1)"""
        if self.current_node:
            self.current_node = self.current_node.prev
        return self.get_current_clock()

    def get_current_clock(self):
        """Return the data of the current clock."""
        return self.current_node.data if self.current_node else None

    def get_all_clocks(self):
        """Return a list of all clock names for UI display."""
        return [c.city_name for c in self.clocks_list.to_list()]
