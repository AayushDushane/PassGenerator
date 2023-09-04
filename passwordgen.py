import tkinter as tk
import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_password_button_clicked():
    try:
        length = int(entry_password_length.get())
        if length <= 0:
            result_label.config(text="Password length must be greater than 0.")
        else:
            password = generate_password(length)
            result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        result_label.config(
            text="Invalid input. Please enter a valid number for the password length.")


def clear_password():
    entry_password_length.delete(0, 'end')
    result_label.config(text="")


def clear_username():
    entry_username.delete(0, 'end')


window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")

username_label = tk.Label(window, text="Username:",
                          bg="lightblue", font=("Helvetica", 12))
entry_username = tk.Entry(window, font=("Helvetica", 12))
password_label = tk.Label(window, text="Password Length:",
                          bg="lightgreen", font=("Helvetica", 12))
entry_password_length = tk.Entry(window, font=("Helvetica", 12))
generate_password_button = tk.Button(window, text="Generate Password",
                                     command=generate_password_button_clicked, bg="lightcoral", font=("Helvetica", 12))
clear_password_button = tk.Button(
    window, text="Clear Password", command=clear_password, bg="lightcoral", font=("Helvetica", 12))
clear_username_button = tk.Button(
    window, text="Clear Username", command=clear_username, bg="lightcoral", font=("Helvetica", 12))
result_label = tk.Label(window, text="", wraplength=300, font=(
    "Helvetica", 12), padx=10, pady=10, bg="lightgray")

username_label.grid(row=0, column=0, padx=10, pady=10)
entry_username.grid(row=0, column=1, padx=10, pady=10)
password_label.grid(row=1, column=0, padx=10, pady=10)
entry_password_length.grid(row=1, column=1, padx=10, pady=10)
generate_password_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
clear_password_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
clear_username_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

developer_label = tk.Label(
    window, text="Developed by Aayush Dushane", font=("Helvetica", 10))
developer_label.grid(row=6, column=0, columnspan=2, pady=10)

window.mainloop()
