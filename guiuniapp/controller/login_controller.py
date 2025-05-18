from model.user_model import UserModel
from view.login_view import LoginView
from model.student_model import StudentModel  # Import your student model

class LoginController:
    def __init__(self, root, app):
        from view.login_view import LoginView
        from model.user_model import UserModel

        self.root = root              # ✅ Add this line
        self.app = app
        self.model = UserModel()
        self.view = LoginView(root, self)


    def handle_login(self):
        email = self.view.get_email()
        password = self.view.get_password()

        if not self.model.validate_email(email):
            self.view.show_error("Invalid email format.\nUse: firstname.lastname@university.com")
            return

        # Password validation if needed

        try:
            if self.model.authenticate(email, password):
                self.view.show_success("Login successful!")
                self.view.pack_forget()

                # Load all students (your data)
                all_students = StudentModel.load_all_students()

                # Find the logged-in student object by email
                logged_in_student = next((s for s in all_students if s.email == email), None)

                if not logged_in_student:
                    self.view.show_error("User data not found after login.")
                    return

                from controller.dashboard_controller import DashboardController
                DashboardController(self.root, self.app, logged_in_student, all_students)

            else:
                self.view.show_error("Login Failed. Incorrect email or password.")
        except Exception as e:
            self.view.show_error(str(e))
