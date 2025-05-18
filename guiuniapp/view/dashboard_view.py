import tkinter as tk

class DashboardView(tk.Frame):
    def __init__(self, root, controller, username):
        super().__init__(root)
        self.controller = controller
        self.root = root
        self.bg_color = "#e6e9f8"       # Soft bluish background (not white)
        self.primary_color = "#1635CC"  # Title text color
        self.button_color = "#5973F7"
        self.button_active = "#3A51C7"
        self.label_color = "#0A30F0"
        self.configure(bg="#e6e9f8")
        self.pack(fill="both", expand=True)

        tk.Label(
            self,
            text=f"Welcome, {username} 👋",
            font=("Segoe UI", 20, "bold"),
            fg="#1635CC", bg="#e6e9f8"
        ).pack(pady=(40, 20))

        self._create_button("📝 Enrolment Window", self.controller.open_enrolment)
        self._create_button("📚 Subject Window", self.controller.open_subjects)
        self._create_button("🚪 Logout", self.controller.logout)

    def _create_button(self, text, command):
        tk.Button(
            self,
            text=text,
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
            command=command
        ).pack(pady=30)
