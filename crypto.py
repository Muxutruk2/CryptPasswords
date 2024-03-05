import os
from cryptography.fernet import Fernet
from genKey import *


def encrypt(text: str, cipher: Fernet) -> str:
    """Inputs text as string and Returns encripted text as a string using Fernet cipher"""
    return str(cipher.encrypt(text.encode()))


def write(app:str, email:str, password: str, cipher: Fernet) -> None:
    """Saves the encrypted password in th passwords.txt file"""

    # Concatenate the data into a single string
    text = f"{app},{email},{password}"
    print(f"Writing: {text}")

    # Encrypt the concatenated string
    encrypted_text = encrypt(text, cipher)
    print(f"Encrypted: {encrypted_text}")

    # Append the encrypted string to the file
    with open("passwords.txt", "wb") as file:
        file.write(encrypted_text + b"\n")
        print("Successfully wrote to the file")

    with open("passwords.txt", "rb") as file:
        print(file.read())


def decrypt(encrypted_text, cipher:Fernet.Key):
    try:
        # Decrypt the encrypted string
        decrypted_text = cipher.decrypt(encrypted_text).decode()
        return decrypted_text
    except Exception as e:
        return None


def read(cipher:Fernet.Key) -> str|None:
    """
    Inputs a Fernet.Key as cipher and outputs str if the cipher is correct, None otherwise
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
