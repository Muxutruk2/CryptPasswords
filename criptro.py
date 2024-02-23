import os
from cryptography.fernet import Fernet
from genKey import *

def encriptar(texto, cipher):
    return cipher.encrypt(texto.encode())

def escribir(app, correo, contraseña, cipher):
    # Concatenate the data into a single string
    texto = f"{app},{correo},{contraseña}"

    # Encrypt the concatenated string
    textoEncriptado = encriptar(texto, cipher)

    # Append the encrypted string to the file
    with open("contraseñas.txt", "ab") as file:
        file.write(textoEncriptado + b'\n')  # Add a newline between entries


def desencriptar(texto_encriptado, cipher):
    try:
        # Decrypt the encrypted string
        texto_desencriptado = cipher.decrypt(texto_encriptado).decode()
        return texto_desencriptado
    except Exception as e:
        print(f"Error decrypting: {e}")
        return None

def leer(cipher):
    # Read all lines from the encrypted file
    with open("contraseñas.txt", "rb") as file:
        lines = file.readlines()

    decrypted_entries = []

    for line in lines:
        # Decrypt each line
        texto_desencriptado = desencriptar(line, cipher)

        if texto_desencriptado is not None:
            # Split the decrypted string into individual fields
            app, correo, contraseña = texto_desencriptado.split(",")
            decrypted_entries.append(f"App: {app}, Correo: {correo}, Contraseña: {contraseña}")

    return "\n".join(decrypted_entries)
    