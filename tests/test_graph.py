import unittest
import sys
import os

# Add the project root directory to Python's path
#sys.path.append(r"C:\Users\kevin\Desktop\Github\Strings-and-Encryption")
sys.path.append(r"C:\Users\harry\Documents\GitHub\Strings-and-Encryption")

from graph import Graph
from message import Message


class TestGraph(unittest.TestCase):
    def setUp(self):
        """Set up a sample graph for testing."""
        self.graph = Graph()
        self.graph.add_node("Alice")
        self.graph.add_node("Bob")
        self.graph.add_node("Charlie")
        self.graph.add_edge("Alice", "Bob")
        self.graph.add_edge("Bob", "Charlie")

    def test_add_node(self):
        """Test adding a node to the graph."""
        self.graph.add_node("Dave")
        self.assertIn("Dave", self.graph.nodes)
        self.assertEqual(len(self.graph.nodes), 4)

    def test_add_edge(self):
        """Test adding an edge between nodes."""
        self.assertIn("Bob", self.graph.nodes["Alice"].connections)
        self.assertIn("Alice", self.graph.nodes["Bob"].connections)

    def test_find_node(self):
        """Test finding a node in the graph."""
        node = self.graph.find_node("Alice")
        self.assertIsNotNone(node)
        self.assertEqual(node.id, "Alice")

if __name__ == "__main__":
    unittest.main()
