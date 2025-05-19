import tkinter as tk

class DashboardView(tk.Frame):
    def __init__(self, root, controller, username):
        super().__init__(root)
        self.controller = controller
        self.root = root

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
            bg="#5973F7", fg="white",
            activebackground="#3A51C7",
            width=22, height=2,
            command=command,
            relief="flat"
        ).pack(pady=12)
