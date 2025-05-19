from model.user_model import UserModel

class LoginController:
    def __init__(self, root, app):
        from view.login_view import LoginView

        self.root = root
        self.app = app
        self.model = UserModel()
        self.view = LoginView(root, self)

    def handle_login(self):
        email = self.view.get_email()
        password = self.view.get_password()

        # Validate email & password format first
        if not self.model.validate_email(email):
            self.view.show_error("Invalid email format.\nUse firstname.lastname@university.com")
            return

        if not self.model.validate_password(password):
            self.view.show_error("Invalid password format.\nPassword must start with uppercase, have at least 5 letters, followed by 3+ digits.")
            return

        # Authenticate credentials
        user = self.model.authenticate(email, password)
        if user:
            self.view.show_success(f"Welcome {user['name']}!")
            self.view.pack_forget()
            from controller.dashboard_controller import DashboardController
            DashboardController(self.root, self.app, user['name'])
        else:
            self.view.show_error("Email or password incorrect.")
