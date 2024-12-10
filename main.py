import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip


def generate_password():
    length = length_var.get()
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_numbers = numbers_var.get()
    use_special = special_var.get()

    if not (use_uppercase or use_lowercase or use_numbers or use_special):
        messagebox.showerror("Error", "At least one character type must be selected")
        return

    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    check_password_strength(password)


def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    strength = "Weak"
    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        strength = "Strong"
    elif length >= 6 and ((has_upper and has_lower) or (has_upper and has_digit) or (has_lower and has_digit)):
        strength = "Medium"

    strength_label.config(text=strength)
    if strength == "Strong":
        strength_label.config(fg="green")
    elif strength == "Medium":
        strength_label.config(fg="orange")
    else:
        strength_label.config(fg="red")


def copy_password():
    password = password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("Password Generator", "Password copied to clipboard")


# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.configure(bg="#ADD8E6")

# Set up variables
length_var = tk.IntVar(value=9)
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar()
special_var = tk.BooleanVar()

# Set up the layout
frame = tk.Frame(root, padx=10, pady=10, bg="#ADD8E6")
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Password Generator", font=("Arial", 18), bg="#ADD8E6").grid(row=0, column=0, columnspan=2,
                                                                                  pady=(0, 20))

password_frame = tk.Frame(frame, bg="#ADD8E6")
password_frame.grid(row=1, column=0, columnspan=2)

password_entry = tk.Entry(password_frame, width=21, font=("Arial", 14))
password_entry.pack(side="left", pady=(0, 10))

copy_button = tk.Button(password_frame, text="Copy", command=copy_password, bg="#008080", fg="white",
                        font=("Arial", 10), width=5)
copy_button.pack(side="left", padx=(10, 0), pady=(0, 10))

strength_label = tk.Label(frame, text="Weak", fg="red", bg="#ADD8E6", font=("Arial", 10))
strength_label.grid(row=2, column=0, columnspan=2)

tk.Label(frame, text="Password Length:", bg="#ADD8E6", font=("Arial", 10)).grid(row=3, column=0, sticky="w")
length_label = tk.Label(frame, textvariable=length_var, bg="#ADD8E6", font=("Arial", 10))
length_label.grid(row=3, column=1, sticky="e")
length_slider = tk.Scale(frame, from_=6, to_=20, orient="horizontal", variable=length_var, bg="#ADD8E6",
                         font=("Arial", 10), length=200)
length_slider.grid(row=4, column=0, columnspan=2, pady=(0, 10))

tk.Checkbutton(frame, text="Uppercase", variable=uppercase_var, bg="#ADD8E6", font=("Arial", 10)).grid(row=5, column=0,
                                                                                                       sticky="w")
tk.Checkbutton(frame, text="Lowercase", variable=lowercase_var, bg="#ADD8E6", font=("Arial", 10)).grid(row=6, column=0,
                                                                                                       sticky="w")
tk.Checkbutton(frame, text="Numbers", variable=numbers_var, bg="#ADD8E6", font=("Arial", 10)).grid(row=7, column=0,
                                                                                                   sticky="w")
tk.Checkbutton(frame, text="Special Characters", variable=special_var, bg="#ADD8E6", font=("Arial", 10)).grid(row=8,
                                                                                                              column=0,
                                                                                                              sticky="w")

generate_button = tk.Button(frame, text="Generate Password", command=generate_password, bg="#008080", fg="white",
                            font=("Arial", 12))
generate_button.grid(row=9, column=0, columnspan=2, pady=(20, 0), ipadx=10)

# Run the application
root.mainloop()
