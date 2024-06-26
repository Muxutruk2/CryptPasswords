#!/usr/bin/env python3
import os

try:
    import base64
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.fernet import Fernet

except:
    os.system("pip install cryptography")

def generate_key_from_password(password:str) -> Fernet:
    # Convert the password to bytes
    password_bytes = password.encode()

    # Generate a salt (random value)
    salt = b'salt_value_here'

    # Create a PBKDF2HMAC key derivation function
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,  # You can adjust the number of iterations for security
        salt=salt,
        length=32  # The length of the key
    )

    try:
        # Derive the key from the password
        key = Fernet(base64.urlsafe_b64encode(kdf.derive(password_bytes)))
    except Exception as e:
        print(f"ERROR WHEN GENERATING FERNET KEY FROM str:{password} kdf: {kdf} : ", e)

    return key

if __name__ == "__main__":
    print("Generated key from 123: ", generate_key_from_password("123"))
# end main