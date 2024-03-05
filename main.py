try:
    from criptro import *
    import tkinter as tk
    from tkinter import ttk
    import sv_ttk
    from PIL import ImageTk, Image
except:
    import subprocess
    subprocess.call("pip install criptro")
    subprocess.call("pip install tkinter")
    subprocess.call("pip install sv_ttk")
    subprocess.call("pip install Pillow")

    from criptro import *
    import tkinter as tk
    from tkinter import ttk
    import sv_ttk
    from PIL import ImageTk, Image
cipher = generate_key_from_password("1")
result_label = None  # Declare result_label globally

def configure_styles():
    style = ttk.Style()
    # Configure a style for buttons
    style.configure(
        "TButton",
        font=("Helvetica", 12),
        padding=(10, 5),
        background="#4CAF50",
        foreground="#000000",
    )

    # Configure a style for labels
    style.configure(
        "TLabel",
        font=("Helvetica", 12),
        background="#feffe6",
        foreground="#000000",

    )

    # Configure a style for entries
    style.configure(
        "TEntry",
        font=("Helvetica", 12),
        background="#feffe6",
        foreground="#000000",
        
    )

    # Configure a style for frames
    style.configure(
        "TFrame",
        font=("Helvetica", 12),
        background="#feffe6",
        foreground="#000000",
    )

    style.configure(
        "TText",
        font=("Helvetica", 12),
        background="#feffe6",
        foreground="#000000",
    )

    style.configure(
        "TFrame",
        font=("Helvetica", 12),
        background="#feffe6",
        foreground="#000000",
        
    )

def establecerLlave():
    global cipher
    global password_entry_right
    contraseña = password_entry_right.get()
    cipher = generate_key_from_password(contraseña)
    print("Llave establecida: ", contraseña)


def refresh_result_label():
    global result_label, cipher

    decrypted_entries = leer(cipher)

    if not decrypted_entries:
        return None
    
    result_label.config(text=decrypted_entries)

    print(decrypted_entries)

def añadirContraseña():
    global app_entry_left, email_entry_left, result_label, cipher, password_entry_left
    app = app_entry_left.get()
    correo = email_entry_left.get()
    contraseña = password_entry_left.get()
    if "" in [app,correo,contraseña]: return
    escribir(app, correo, contraseña, cipher)
    print(app, correo, contraseña, cipher)
    refresh_result_label()


def main():
    global app_entry_left, email_entry_left, result_label, cipher, password_entry_right, password_entry_left

    root = tk.Tk()
    root.title("Administrador de contraseñas encriptadas")
    root.configure(background="#000000")
    configure_styles()

    # Left side widgets
    left_frame = ttk.Frame(root,)
    left_frame.grid(row=0, column=0, padx=100, pady=100, )

    ImageTk.PhotoImage(Image.open())

    ttk.Label(left_frame, text="Añadir contraseña").grid(
        row=0,
        column=0,
        columnspan=2,
        padx=20,
        pady=20,
    )

    password_label_left = ttk.Label(left_frame, text="Contraseña:")
    password_label_left.grid(row=1, column=0, sticky="E",padx=20,
        pady=20,)
    password_entry_left = ttk.Entry(left_frame)
    password_entry_left.grid(row=1, column=1,padx=20,
        pady=20,)

    app_label_left = ttk.Label(left_frame, text="Aplicacion:")
    app_label_left.grid(row=2, column=0, sticky="E",padx=20,
        pady=20,)
    app_entry_left = ttk.Entry(left_frame)
    app_entry_left.grid(
        row=2,
        column=1,
        padx=20,
        pady=20,
    )

    email_label_left = ttk.Label(left_frame, text="Correo/Nombre:")
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

    accept_button_left = ttk.Button(left_frame, text="OK",command=añadirContraseña)
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

    password_label_right = ttk.Label(right_frame, text="Llave de encriptacion:")
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

    accept_button_right = ttk.Button(right_frame, text="Establecer llave",command=establecerLlave)
    accept_button_right.grid(
        row=2,
        column=0,
        columnspan=2,
        padx=20,
        pady=20,
    )

    # Text widget on the right side
    result_label = tk.Label(right_frame,height=20, width=50)
    result_label.grid(
        row=3,
        column=0,
        columnspan=2,
        padx=20,
        pady=20,
    )
    result_label.config(state=tk.DISABLED)

    refresh_button_right = ttk.Button(right_frame, text="Refrescar", command=refresh_result_label)
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
