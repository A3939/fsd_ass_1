import tkinter as tk

class EnrolmentView(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.configure(bg="#e6e9f8")
        self.pack(fill="both", expand=True)

        tk.Label(self, text="Subject Enrolment", font=("Segoe UI", 20, "bold"), fg="#1635CC", bg="#e6e9f8").pack(pady=20)

        btn_enrol = tk.Button(self, text="Enroll in Subject", command=self.controller.enrol_subject,
                             bg="#5973F7", fg="white", relief="flat", borderwidth=0, highlightthickness=0, cursor="hand2")
        btn_enrol.pack(pady=10, ipadx=20, ipady=10)

        btn_drop = tk.Button(self, text="Drop Subject", command=self.controller.drop_subject,
                             bg="#5973F7", fg="white", relief="flat", borderwidth=0, highlightthickness=0, cursor="hand2")
        btn_drop.pack(pady=10, ipadx=20, ipady=10)

        btn_view = tk.Button(self, text="View Enrolments", command=self.controller.view_enrolments,
                             bg="#5973F7", fg="white", relief="flat", borderwidth=0, highlightthickness=0, cursor="hand2")
        btn_view.pack(pady=10, ipadx=20, ipady=10)

        btn_back = tk.Button(self, text="Back to Dashboard", command=self.controller.back_to_dashboard,
                             bg="#5973F7", fg="white", relief="flat", borderwidth=0, highlightthickness=0, cursor="hand2")
        btn_back.pack(pady=10, ipadx=20, ipady=10)

    def refresh(self):
        pass
