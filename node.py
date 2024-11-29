# node.py
class Node:
    def __init__(self, node_id):
        """
        Initialize a node.
        :param node_id: Unique identifier for the node (e.g., a name or ID).
        """
        self.id = node_id
        self.connections = set()  # Stores IDs of connected nodes
        self.metadata = {}        # Dictionary for additional metadata

    def add_connection(self, other_node_id):
        """
        Add a connection to another node.
        :param other_node_id: ID of the other node to connect to.
        """
        self.connections.add(other_node_id)

    def __repr__(self):
        return f"Node({self.id}, Connections: {list(self.connections)})"
