from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def generate_keys():
    """
    Generate a public/private key pair.
    :return: Tuple (private_key, public_key)
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,  # Common value
        key_size=2048,          # Key size in bits
    )
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_message(public_key, message):
    """
    Encrypt a message using the public key.
    :param public_key: RSA public key for encryption.
    :param message: Message to encrypt (string).
    :return: Encrypted message (bytes).
    """
    if message is None:
        raise ValueError("Cannot encrypt a NoneType message!")
    
    print(f"Encrypting Message: {message}")  # Debug statement
    
    encrypted = public_key.encrypt(
        message.encode(),  # Convert message to bytes
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return encrypted


def decrypt_message(private_key, encrypted_message):
    """
    Decrypt an encrypted message using the private key.
    :param private_key: RSA private key for decryption.
    :param encrypted_message: Encrypted message (bytes).
    :return: Decrypted message (string).
    """
    decrypted = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return decrypted.decode()  # Convert bytes back to string

def serialize_keys(private_key, public_key):
    """
    Serialize keys to PEM format for storage or sharing.
    :param private_key: RSA private key.
    :param public_key: RSA public key.
    :return: Tuple (private_key_pem, public_key_pem).
    """
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    return private_pem, public_pem

def deserialize_keys(private_pem, public_pem):
    """
    Deserialize PEM-formatted keys back into RSA key objects.
    :param private_pem: Serialized private key in PEM format.
    :param public_pem: Serialized public key in PEM format.
    :return: Tuple (private_key, public_key).
    """
    private_key = serialization.load_pem_private_key(private_pem, password=None)
    public_key = serialization.load_pem_public_key(public_pem)
    return private_key, public_key
