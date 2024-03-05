import os

try:
    import base64
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.fernet import Fernet

except:
    os.system("pip install cryptography")

def generate_key_from_password(password: str) -> Fernet:
    """
    Generates a Fernet key from a password.

    Parameters:
    - password (str): The password used to generate the key.

    Returns:
    Fernet: The generated Fernet key.
    """
    # Convert the password to bytes
    password_bytes = password.encode()

    # Generate a salt (random value)
    salt = b'0972376093247698234najdiajfgjoijqj40934i'

    # Create a PBKDF2HMAC key derivation function
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,  # You can adjust the number of iterations for security
        salt=salt,
        length=32  # The length of the key
    )

    # Derive the key from the password
    key = Fernet(base64.urlsafe_b64encode(kdf.derive(password_bytes)))

    return key
