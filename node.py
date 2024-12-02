from algorithms.rsa import generate_keys, encrypt_message, decrypt_message
from algorithms.rle import run_length_encode, run_length_decode
from message import Message

class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.connections = set()  # Connections to other nodes
        self.private_key, self.public_key = generate_keys()  # RSA keys

    def send_message(self, receiver, body, use_compression=False):
        """
        Send a message to another node.
        :param receiver: The Node receiving the message.
        :param body: The message content (string).
        :param use_compression: Placeholder for future compression support.
        :return: The encrypted message.
        """
        # Debug: Check the body of the message
        print(f"Original Message Body: {body}")
    
        # Directly encrypt the message (no compression for now)
        encrypted_body = encrypt_message(receiver.public_key, body)
        print(f"Encrypted Message Body: {encrypted_body}")
    
        # Create a message object
        metadata = {"encryption": "RSA", "method": "PLAIN"}  # Add method here
        message = Message(sender_id=self.id, receiver_id=receiver.id, body=encrypted_body, metadata=metadata)
        return message



    def receive_message(self, message):
        """
        Receive and decrypt a message.
        :param message: The received Message object.
        :return: The original message content (string).
        """
        # Debug: Print received message metadata
        print(f"Received Message Metadata: {message.metadata}")

        # Decrypt the message
        decrypted_body = decrypt_message(self.private_key, message.body)

        # Process based on the method in metadata
        if message.metadata["method"] == "RLE":
        # Handle decompression (placeholder for future functionality)
            pass
        elif message.metadata["method"] == "PLAIN":
        # No decompression needed
            return decrypted_body
        else:
            raise ValueError(f"Unsupported method: {message.metadata['method']}")
