import os
from cryptography.fernet import Fernet
from genKey import *

def encrypt(text: str, cipher: Fernet) -> str:
    """
    Encrypts the input text using the provided Fernet cipher.

    Parameters:
    - text (str): The text to be encrypted.
    - cipher (Fernet): The Fernet cipher object used for encryption.

    Returns:
    str: The encrypted text as a string.
    """

    return str(cipher.encrypt(text.encode()))

def write(app: str, email: str, password: str, cipher: Fernet) -> None:
    """
    Saves the encrypted password in the passwords.txt file.

    Parameters:
    - app (str): The application name.
    - email (str): The email associated with the password.
    - password (str): The password to be encrypted and stored.
    - cipher (Fernet): The Fernet cipher object used for encryption.

    Returns:
    None
    """

    # Concatenate the data into a single string
    text = f"{app},{email},{password}"

    # Encrypt the concatenated string
    encrypted_text = encrypt(text, cipher)

    # Append the encrypted string to the file
    with open("passwords.txt", "ab") as file:
        file.write(encrypted_text.encode() + b"\n")

def decrypt(encrypted_text: bytes, cipher: Fernet) -> str|None:
    """
    Decrypts the input encrypted text using the provided Fernet cipher.

    Parameters:
    - encrypted_text (bytes): The encrypted text to be decrypted.
    - cipher (Fernet): The Fernet cipher object used for decryption.

    Returns:
    str|None: The decrypted text as a string if successful, None otherwise.
    """

    try:
        # Decrypt the encrypted string
        decrypted_text = cipher.decrypt(encrypted_text).decode()
        return decrypted_text
    except Exception as e:
        return None

def read(cipher: Fernet) -> str|None:
    """
    Reads and decrypts the contents of the passwords.txt file.

    Parameters:
    - cipher (Fernet): The Fernet cipher object used for decryption.

    Returns:
    str|None: The decrypted entries as a formatted string if successful, None otherwise.
    """

    with open("passwords.txt", "rb") as file:
        lines = file.readlines()

    decrypted_entries = []

    for line in lines:
        # Decrypt each line
        decrypted_text = decrypt(line, cipher)

        if decrypted_text is not None:
            # Split the decrypted string into individual fields
            app, email, password = decrypted_text.split(",")
            decrypted_entries.append(
                f"App: {app}, Email: {email}, Password: {password}"
            )
        else:
            return None

    return "\n".join(decrypted_entries)
