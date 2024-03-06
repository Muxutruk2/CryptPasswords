import sys

sys.dont_write_bytecode = True

from crypto import *
import tkinter as tk
from tkinter import ttk
import sv_ttk

# Global variable to store the encryption key
cipher = generate_key_from_password("1")

# Global variable to store the result label widget
result_label = None

def setKey():
    """
    Sets the encryption key based on the password entered in the right side Entry widget.

    Input:
    - None

    Output:
    - None
    """
    global cipher
    global password_entry_right
    
    password = password_entry_right.get()
    cipher = generate_key_from_password(password)

def refresh_result_label():
    """
    Refreshes the result label widget with decrypted entries from the storage.

    Input:
    - None

    Output:
    - None
    """
    global result_label, cipher

    decrypted_entries = read(cipher)

    if not decrypted_entries:
        return None

    result_label.config(text=decrypted_entries)

def addPassword():
    """
    Adds a new password entry to the storage and refreshes the result label widget.

    Input:
    - None

    Output:
    - None
    """
    global app_entry_left, email_entry_left, result_label, cipher, password_entry_left
    
    app = app_entry_left.get()
    email = email_entry_left.get()
    password = password_entry_left.get()
    
    # Check if any of the fields are empty
    if "" in [app, email, password]:
        return
    
    write(app, email, password, cipher)
    refresh_result_label()

def changeLanguage():
    """
    Changes the language of the left side labels.

    Input:
    - None

    Output:
    - None
    """
    
    global add_password_label_left, password_label_left, app_label_left, email_label_left, accept_button_left, language_button_left, password_label_right, accept_button_right, refresh_button_right
    add_password_label_left.configure(text="Añadir contraseña")
    password_label_left.configure(text="Contraseña: ")
    app_label_left.configure(text="Aplicación: ")
    email_label_left.configure(text="Email/Nombre de usuario: ")
    language_button_left.configure(text="")
    password_label_right.configure(text="Llave de encriptacion")
    accept_button_right.configure(text="Establecer Llave")
    refresh_button_right.configure(text="Refrescar")

def main():
    global app_entry_left, email_entry_left, result_label, cipher, password_entry_right, password_entry_left
    global add_password_label_left, password_label_left, app_label_left, email_label_left, accept_button_left, language_button_left, password_label_right, accept_button_right, refresh_button_right

    root = tk.Tk()
    root.rowconfigure(0,weight=1)
    root.columnconfigure(0,weight=1)
    root.geometry("1000x652")
    root.title("Encrypted Password Manager")
    root.configure(background="#000000")
    root.resizable(False, False)

    tk.Grid.rowconfigure(root,0,weight=1)
    tk.Grid.rowconfigure(root,1,weight=1)
    tk.Grid.rowconfigure(root,2,weight=1)
    tk.Grid.rowconfigure(root,3,weight=1)
    tk.Grid.rowconfigure(root,4,weight=1)
    tk.Grid.rowconfigure(root,5,weight=1)
    tk.Grid.columnconfigure(root,0,weight=1)
    tk.Grid.columnconfigure(root,1,weight=1)

    # Left side widgets
    left_frame = ttk.Frame(root)
    left_frame.grid(
        sticky="NSEW",
        row=0,
        column=0,
        padx=100,
        pady=100,
    )

    add_password_label_left = ttk.Label(left_frame, text="Add Password")
    add_password_label_left.grid(
        sticky="NSEW",
        row=0,
        column=0,
        columnspan=2,
        padx=20,
        pady=20,
    )

    password_label_left = ttk.Label(left_frame, text="Password:")
    password_label_left.grid(
        row=1,
        column=0,
        sticky="NSEW",
        padx=20,
        pady=20,
    )
    password_entry_left = ttk.Entry(left_frame)
    password_entry_left.grid(
        sticky="NSEW",
        row=1,
        column=1,
        padx=20,
        pady=20,
    )

    app_label_left = ttk.Label(left_frame, text="Application:")
    app_label_left.grid(
        row=2,
        column=0,
        sticky="NSEW",
        padx=20,
        pady=20,
    )
    app_entry_left = ttk.Entry(left_frame)
    app_entry_left.grid(
        sticky="NSEW",
        row=2,
        column=1,
        padx=20,
        pady=20,
    )

    email_label_left = ttk.Label(left_frame, text="Email/Username:")
    email_label_left.grid(
        sticky="NSEW",
        row=3,
        column=0,
        padx=20,
        pady=20,
    )
    email_entry_left = ttk.Entry(left_frame)
    email_entry_left.grid(
        sticky="NSEW",
        row=3,
        column=1,
        padx=20,
        pady=20,
    )

    accept_button_left = ttk.Button(left_frame, text="OK", command=addPassword)
    accept_button_left.grid(
        sticky="NSEW",
        row=4,
        column=0,
        columnspan=2,
        padx=20,
        pady=20,
    )

    language_button_left = ttk.Button(left_frame, text="Español", command=changeLanguage)
    language_button_left.grid(
        sticky="NSEW",
        row=5,
        column=0,
        columnspan=2,
        padx=20,
        pady=20)

    # Right side widgets
    right_frame = ttk.Frame(root)
    right_frame.grid(
        row=0,
        column=1,
        padx=20,
        pady=20,
        sticky="NSEW",
    )

    ttk.Label(right_frame, text="").grid(
        row=0,
        column=0,
        columnspan=2,
        padx=20,
        pady=20,
        sticky="NSEW",
    )

    password_label_right = ttk.Label(right_frame, text="Encryption Key:")
    password_label_right.grid(
        sticky="NSEW",
        row=1,
        column=0,
        padx=20,
        pady=20,
    )
    password_entry_right = ttk.Entry(right_frame)
    password_entry_right.grid(
        sticky="NSEW",
        row=1,
        column=1,
        padx=20,
        pady=20,
    )

    accept_button_right = ttk.Button(right_frame, text="Set Key", command=setKey)
    accept_button_right.grid(
        sticky="NSEW",
        row=2,
        column=0,
        columnspan=2,
        padx=20,
        pady=20,
    )

    # Text widget on the right side
    result_label = tk.Label(right_frame, height=20)
    result_label.grid(
        sticky="SE",
        row=3,
        column=0,
        columnspan=2,
        padx=20,
        pady=20,
    )
    result_label.config(state=tk.DISABLED)

    refresh_button_right = ttk.Button(
        right_frame, text="Refresh", command=refresh_result_label
    )
    refresh_button_right.grid(
        sticky="NSEW",
        row=4,
        column=0,
        columnspan=2,
        padx=20,
        pady=20,
    )
    sv_ttk.set_theme("dark")
    root.mainloop()

if __name__ == "__main__":
    main()
