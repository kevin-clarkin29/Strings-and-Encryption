from node import Node

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node_id):
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id)

    def add_edge(self, node1_id, node2_id):
        if node1_id in self.nodes and node2_id in self.nodes:
            self.nodes[node1_id].connections.add(node2_id)
            self.nodes[node2_id].connections.add(node1_id)

    def send_message(self, sender_id, receiver_id, body, use_compression=True):
        """
        Simulate sending a message between nodes.
        :param sender_id: ID of the sender.
        :param receiver_id: ID of the receiver.
        :param body: The message content (string).
        :param use_compression: Whether to use RLE compression.
        :return: The decrypted message content.
        """
        sender = self.nodes[sender_id]
        receiver = self.nodes[receiver_id]

        # Sender creates and sends the message
        message = sender.send_message(receiver, body, use_compression)

        # Receiver processes the message
        return receiver.receive_message(message)
