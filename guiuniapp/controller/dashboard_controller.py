class DashboardController:
    def __init__(self, root, app, student, students):
        from view.dashboard_view import DashboardView
        self.root = root
        self.app = app
        self.student = student
        self.students = students
        self.view = DashboardView(root, self, student.name)

    def open_enrolment(self):
        self.view.pack_forget()
        from controller.enrolment_controller import EnrolmentController
        EnrolmentController(self.root, self.app, self.student, self.students)

    # Implement this later for subject window
    def open_subjects(self):
        self.view.pack_forget()
        from controller.subject_controller import SubjectController
        SubjectController(self.root, self.app, self.student, self.students)

    def logout(self):
        self.view.pack_forget()
        self.app.show_login_view()
