import unittest
from algorithms.rsa import generate_keys, encrypt_message, decrypt_message

class TestRSA(unittest.TestCase):
    def setUp(self):
        """Generate RSA keys for testing."""
        self.private_key, self.public_key = generate_keys()

    def test_encrypt_decrypt(self):
        """Test encryption and decryption of a message."""
        message = "Secure communication"
        encrypted = encrypt_message(self.public_key, message)
        decrypted = decrypt_message(self.private_key, encrypted)
        self.assertEqual(message, decrypted)

if __name__ == "__main__":
    unittest.main()
