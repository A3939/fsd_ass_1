import tkinter as tk
from controller.login_controller import LoginController

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("University Login App")
        self.root.geometry("420x380")
        self.root.resizable(False, False)
        self.show_login_view()

    def show_login_view(self):
        LoginController(self.root, self)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
