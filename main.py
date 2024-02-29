from criptro import *
import tkinter as tk

cipher = generate_key_from_password("1")

def assignCipher(entry_widget):
    text = entry_widget.get()
    # Perform operations with the text (replace this with your actual logic)
    cipher = generate_key_from_password(text)

def decryptPasswords(cipher):
    return leer(cipher)

def main():

    # cipher = generate_key_from_password(password)  
    root = tk.Tk()
    root.title("Encriptador y Decriptador de contraseñas")

    # Left side widgets
    left_frame = tk.Frame(root)
    left_frame.grid(row=0, column=0, padx=10, pady=10)

    tk.Label(left_frame, text="Añadir contraseña").grid(row=0, column=0, columnspan=2)

    password_label_left = tk.Label(left_frame, text="Contraseña:")
    password_label_left.grid(row=1, column=0, sticky="E")
    password_entry_left = tk.Entry(left_frame, show="*")
    password_entry_left.grid(row=1, column=1)

    app_label_left = tk.Label(left_frame, text="Aplicacion:")
    app_label_left.grid(row=2, column=0, sticky="E")
    app_entry_left = tk.Entry(left_frame)
    app_entry_left.grid(row=2, column=1)

    email_label_left = tk.Label(left_frame, text="Correo/Nombre:")
    email_label_left.grid(row=3, column=0, sticky="E")
    email_entry_left = tk.Entry(left_frame)
    email_entry_left.grid(row=3, column=1)

    accept_button_left = tk.Button(left_frame, text="OK",)
    accept_button_left.grid(row=4, column=0, columnspan=2, pady=10)

    # Right side widgets
    right_frame = tk.Frame(root)
    right_frame.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(right_frame, text="").grid(row=0, column=0, columnspan=2)

    password_label_right = tk.Label(right_frame, text="Llave de encriptacion:")
    password_label_right.grid(row=1, column=0, sticky="E")
    password_entry_right = tk.Entry(right_frame, show="*")
    password_entry_right.grid(row=1, column=1)

    accept_button_right = tk.Button(right_frame, text="OK",command=assignCipher(password_entry_right))
    accept_button_right.grid(row=2, column=0, columnspan=2, pady=10)

    # Text widget on the right side
    result_text = tk.Text(right_frame, height=10, width=30)
    result_text.grid(row=3, column=0, columnspan=2)
    result_text.config(state=tk.DISABLED)

    refresh_text = tk.Button(right_frame,text="Actualizar", command=decryptPasswords(cipher=cipher))
    refresh_text.grid(row=4, column=0, columnspan=2)
    

    root.mainloop()

if __name__ == "__main__":
    main()


