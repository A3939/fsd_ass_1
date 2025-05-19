class DashboardController:
    def __init__(self, root, app, username):
        from view.dashboard_view import DashboardView
        self.root = root
        self.app = app
        self.view = DashboardView(root, self, username)

    def open_enrolment(self):
        # Placeholder for enrolment window
        print("Open Enrolment Window - to be implemented")

    def open_subjects(self):
        # Placeholder for subject window
        print("Open Subject Window - to be implemented")

    def logout(self):
        self.view.pack_forget()
        self.app.show_login_view()
