# graph.py
from node import Node

class Graph:
    def __init__(self):
        """
        Initialize an empty graph.
        """
        self.nodes = {}  # Dictionary to store nodes by their IDs

    def add_node(self, node_id):
        """
        Add a new node to the graph.
        :param node_id: Unique identifier for the new node.
        """
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id)

    def add_edge(self, node1_id, node2_id):
        """
        Create an undirected edge between two nodes.
        :param node1_id: ID of the first node.
        :param node2_id: ID of the second node.
        """
        if node1_id in self.nodes and node2_id in self.nodes:
            self.nodes[node1_id].connections.add(node2_id)
            self.nodes[node2_id].connections.add(node1_id)

    def find_node(self, node_id):
        """
        Find and return a node by its ID.
        :param node_id: ID of the node to find.
        :return: Node object or None if not found.
        """
        return self.nodes.get(node_id)
