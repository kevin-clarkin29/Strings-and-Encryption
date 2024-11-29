# message.py
class Message:
    def __init__(self, sender_id, receiver_id, body, metadata=None):
        """
        Initialize a message.
        :param sender_id: ID of the sender.
        :param receiver_id: ID of the receiver.
        :param body: The message body (string).
        :param metadata: Dictionary with additional information (default: None).
        """
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.body = body
        self.metadata = metadata or {}

    def __repr__(self):
        return f"Message(from {self.sender_id} to {self.receiver_id}, Metadata: {self.metadata})"
