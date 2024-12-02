import sys
import os

# Add the project root directory to the Python path
sys.path.append(r"C:\Users\kevin\Desktop\Github\Strings-and-Encryption")

# Now import from the algorithms package
from algorithms.rsa import generate_keys, encrypt_message, decrypt_message, serialize_keys, deserialize_keys


# Step 1: Generate keys
private_key, public_key = generate_keys()

# Step 2: Serialize keys
private_pem, public_pem = serialize_keys(private_key, public_key)

# Step 3: Deserialize keys
private_key, public_key = deserialize_keys(private_pem, public_pem)

# Step 4: Encrypt a message
message = "Hello, RSA!"
encrypted = encrypt_message(public_key, message)
print("Encrypted message:", encrypted)

# Step 5: Decrypt the message
decrypted = decrypt_message(private_key, encrypted)
print("Decrypted message:", decrypted)
