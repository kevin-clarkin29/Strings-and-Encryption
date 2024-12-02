from graph import Graph

# Initialize the graph
graph = Graph()
graph.add_node("Alice")
graph.add_node("Bob")
graph.add_edge("Alice", "Bob")

# Send a message from Alice to Bob
message_body = "Hello, RSA!"
print("Original Message:", message_body)

# Simulate message exchange
decrypted_message = graph.send_message("Alice", "Bob", message_body, use_compression=False)
print("Decrypted Message:", decrypted_message)
