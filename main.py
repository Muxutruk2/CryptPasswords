import sys

sys.dont_write_bytecode = True

from crypto import *
import tkinter as tk
from tkinter import ttk
import sv_ttk

cipher = generate_key_from_password("1")
result_label = None


def setKey():
    global cipher
    global password_entry_right
    password = password_entry_right.get()
    cipher = generate_key_from_password(password)
    print("Key set: ", password)


def refresh_result_label():
    global result_label, cipher

    decrypted_entries = read(cipher)

    if not decrypted_entries:
        return None

    result_label.config(text=decrypted_entries)

    print(decrypted_entries)


def addPassword():
    global app_entry_left, email_entry_left, result_label, cipher, password_entry_left
    app = app_entry_left.get()
    email = email_entry_left.get()
    password = password_entry_left.get()
    if "" in [app, email, password]:
        return
    write(app, email, password, cipher)
    print(app, email, password, cipher)
    refresh_result_label()


def main():
    global app_entry_left, email_entry_left, result_label, cipher, password_entry_right, password_entry_left

    root = tk.Tk()

    root.title("Encrypted Password Manager")
    root.configure(background="#000000")

    # Left side widgets
    left_frame = ttk.Frame(root)
    left_frame.grid(
        row=0,
        column=0,
        padx=100,
        pady=100,
    )

    ttk.Label(left_frame, text="Add Password").grid(
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
        sticky="E",
        padx=20,
        pady=20,
    )
    password_entry_left = ttk.Entry(left_frame)
    password_entry_left.grid(
        row=1,
        column=1,
        padx=20,
        pady=20,
    )

    app_label_left = ttk.Label(left_frame, text="Application:")
    app_label_left.grid(
        row=2,
        column=0,
        sticky="E",
        padx=20,
        pady=20,
    )
    app_entry_left = ttk.Entry(left_frame)
    app_entry_left.grid(
        row=2,
        column=1,
        padx=20,
        pady=20,
    )

    email_label_left = ttk.Label(left_frame, text="Email/Username:")
    email_label_left.grid(
        row=3,
        column=0,
        sticky="E",
        padx=20,
        pady=20,
    )
    email_entry_left = ttk.Entry(left_frame)
    email_entry_left.grid(
        row=3,
        column=1,
        padx=20,
        pady=20,
    )

    accept_button_left = ttk.Button(left_frame, text="OK", command=addPassword)
    accept_button_left.grid(
        row=4,
        column=0,
        columnspan=2,
        padx=20,
        pady=20,
    )

    # Right side widgets
    right_frame = ttk.Frame(root)
    right_frame.grid(
        row=0,
        column=1,
        padx=20,
        pady=20,
    )

    ttk.Label(right_frame, text="").grid(
        row=0,
        column=0,
        columnspan=2,
        padx=20,
        pady=20,
    )

    password_label_right = ttk.Label(right_frame, text="Encryption Key:")
    password_label_right.grid(
        row=1,
        column=0,
        sticky="E",
        padx=20,
        pady=20,
    )
    password_entry_right = ttk.Entry(right_frame)
    password_entry_right.grid(
        row=1,
        column=1,
        padx=20,
        pady=20,
    )

    accept_button_right = ttk.Button(right_frame, text="Set Key", command=setKey)
    accept_button_right.grid(
        row=2,
        column=0,
        columnspan=2,
        padx=20,
        pady=20,
    )

    # Text widget on the right side
    result_label = tk.Label(right_frame, height=20, width=50)
    result_label.grid(
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
