import unittest
import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.dcll import DoublyCircularLinkedList

class TestDCLL(unittest.TestCase):
    def setUp(self):
        self.list = DoublyCircularLinkedList()

    def test_insertion(self):
        self.list.insert_at_end("Clock 1")
        self.list.insert_at_end("Clock 2")
        self.list.insert_at_beginning("Clock 0")
        
        items = self.list.to_list()
        self.assertEqual(items, ["Clock 0", "Clock 1", "Clock 2"])
        self.assertEqual(self.list.size, 3)

    def test_circularity(self):
        self.list.insert_at_end("A")
        self.list.insert_at_end("B")
        
        # Check B.next points to A
        self.assertEqual(self.list.head.next.next, self.list.head)
        # Check A.prev points to B
        self.assertEqual(self.list.head.prev, self.list.head.next)

    def test_deletion(self):
        self.list.insert_at_end("1")
        self.list.insert_at_end("2")
        self.list.insert_at_end("3")
        
        self.list.delete("2")
        self.assertEqual(self.list.to_list(), ["1", "3"])
        
        self.list.delete("1")
        self.assertEqual(self.list.to_list(), ["3"])
        self.assertEqual(self.list.head.data, "3")

    def test_search(self):
        self.list.insert_at_end("X")
        node = self.list.search("X")
        self.assertIsNotNone(node)
        self.assertEqual(node.data, "X")

if __name__ == "__main__":
    unittest.main()
