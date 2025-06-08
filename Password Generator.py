import tkinter as tk
from tkinter import messagebox
import random
import string

class SecurePassMaker:
    def __init__(self, window):
        self.window = window
        self.window.title("Secure Password Creator")
        self.window.geometry("420x360")
        self.window.configure(bg="#f0f0f0")
        self.window.resizable(False, False)

        self._build_interface()

    def _build_interface(self):
        title = tk.Label(self.window, text="Secure Password Creator", font=("Arial", 17, "bold"), bg="#f0f0f0")
        title.pack(pady=12)

        self.length_val = tk.IntVar(value=10)
        length_frame = tk.Frame(self.window, bg="#f0f0f0")
        length_frame.pack()
        tk.Label(length_frame, text="Length:", bg="#f0f0f0").pack(side=tk.LEFT)
        tk.Entry(length_frame, textvariable=self.length_val, width=4).pack(side=tk.LEFT)

        # Options Frame
        self.opt_vars = {
            "upper": tk.BooleanVar(value=True),
            "lower": tk.BooleanVar(value=True),
            "num": tk.BooleanVar(value=True),
            "symbol": tk.BooleanVar(value=True)
        }

        opt_frame = tk.LabelFrame(self.window, text="Include in Password", padx=10, pady=5, bg="#f0f0f0")
        opt_frame.pack(pady=10)

        tk.Checkbutton(opt_frame, text="Uppercase (A-Z)", variable=self.opt_vars["upper"], bg="#f0f0f0").grid(sticky="w")
        tk.Checkbutton(opt_frame, text="Lowercase (a-z)", variable=self.opt_vars["lower"], bg="#f0f0f0").grid(sticky="w")
        tk.Checkbutton(opt_frame, text="Numbers (0-9)", variable=self.opt_vars["num"], bg="#f0f0f0").grid(sticky="w")
        tk.Checkbutton(opt_frame, text="Symbols [@#&*]", variable=self.opt_vars["symbol"], bg="#f0f0f0").grid(sticky="w")

        # Button to generate
        tk.Button(self.window, text="Create Password", command=self.create_password, bg="#4caf50", fg="white", padx=10).pack(pady=10)

        # Result Display
        self.pass_entry = tk.Entry(self.window, font=("Courier", 14), justify="center", width=30)
        self.pass_entry.pack(pady=5)

        # Copy Button
        tk.Button(self.window, text="Copy", command=self.copy_pass, bg="#2196f3", fg="white").pack(pady=5)

    def create_password(self):
        length = self.length_val.get()
        if length < 4:
            messagebox.showwarning("Invalid", "Length must be at least 4.")
            return

        groups = []
        if self.opt_vars["upper"].get():
            groups.append(string.ascii_uppercase)
        if self.opt_vars["lower"].get():
            groups.append(string.ascii_lowercase)
        if self.opt_vars["num"].get():
            groups.append(string.digits)
        if self.opt_vars["symbol"].get():
            groups.append("!@#$%^&*()_+=<>?/")

        if not groups:
            messagebox.showerror("Error", "Choose at least one option!")
            return

        password_chars = [random.choice(group) for group in groups]
        all_possible = ''.join(groups)
        password_chars += random.choices(all_possible, k=length - len(password_chars))
        random.shuffle(password_chars)

        final_password = ''.join(password_chars)
        self.pass_entry.delete(0, tk.END)
        self.pass_entry.insert(0, final_password)

    def copy_pass(self):
        password = self.pass_entry.get()
        if password:
            self.window.clipboard_clear()
            self.window.clipboard_append(password)
            messagebox.showinfo("Success", "Password copied!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SecurePassMaker(root)
    root.mainloop()
