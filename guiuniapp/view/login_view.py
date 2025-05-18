import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.root = root

        self.bg_color = "#e6e9f8"       # Soft bluish background (not white)
        self.primary_color = "#1635CC"  # Title text color
        self.button_color = "#5973F7"
        self.button_active = "#3A51C7"
        self.label_color = "#0A30F0"

        self.configure(bg=self.bg_color)
        self.pack(fill="both", expand=True)

        # Title
        tk.Label(self, text="University Login", font=("Segoe UI", 22, "bold"),
                 fg=self.primary_color, bg=self.bg_color).pack(pady=(30, 20))

        # Email Entry
        self._create_label_entry("Email ID", "email_entry")
        # Password Entry
        self._create_label_entry("Password", "password_entry", show="*")

        # Login Button
        login_button = tk.Button(
            self,
            text="Login",
            font=("Segoe UI", 12, "bold"),
            bg=self.button_color,         # "#5973F7"
            fg=self.button_active,
            activebackground=self.button_active,  # "#3A51C7"
            activeforeground=self.button_color,     # Ensure text stays white on active
            padx=15,
            pady=8,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,         # Remove border highlight on focus
            cursor="hand2",               # Mouse pointer changes to hand on hover
            command=self.controller.handle_login
        )
        login_button.pack(pady=30)


    def _create_label_entry(self, label_text, attr_name, show=None):
        frame = tk.Frame(self, bg=self.bg_color)
        frame.pack(pady=10)

        label = tk.Label(frame, text=label_text, font=("Segoe UI", 11),
                         fg=self.label_color, bg=self.bg_color, anchor="w", width=30)
        label.pack(anchor="w")

        entry = tk.Entry(frame, font=("Segoe UI", 11), width=32,
                         relief="flat", borderwidth=1,
                         bg="black", fg="white", insertbackground="white", show=show)
        entry.pack()
        setattr(self, attr_name, entry)

    def get_email(self):
        return self.email_entry.get()

    def get_password(self):
        return self.password_entry.get()

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def show_success(self, message):
        messagebox.showinfo("Success", message)
