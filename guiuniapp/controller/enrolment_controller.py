import tkinter as tk
from tkinter import simpledialog, messagebox
from model.student_model import StudentModel

class EnrolmentController:
    def __init__(self, root, app, student, students):
        from view.enrolment_view import EnrolmentView
        self.root = root
        self.app = app
        self.student = student
        self.students = students
        self.view = EnrolmentView(root, self)

    def enrol_subject(self):
        if len(self.student.subjects) >= 4:
            messagebox.showerror("Limit reached", "You can only enrol in 4 subjects.")
            return
        self.student.enrol_subject()
        self.save_and_refresh()
        messagebox.showinfo("Success", "Subject enrolled successfully!")

    def drop_subject(self):
        subject_id = simpledialog.askstring("Drop Subject", "Enter subject ID to drop:")
        if not subject_id:
            return
        if self.student.drop_subject(subject_id):
            self.save_and_refresh()
            messagebox.showinfo("Success", f"Subject {subject_id} dropped.")
        else:
            messagebox.showerror("Error", f"No subject with ID {subject_id} found.")

    def view_enrolments(self):
        enrolled = self.student.subjects
        if not enrolled:
            messagebox.showinfo("Enrolments", "You are not enrolled in any subjects.")
            return
        msg = "\n".join([f"ID: {s.id}, Mark: {s.mark}, Grade: {s.grade}" for s in enrolled])
        avg = self.student.average_mark()
        status = "PASS" if self.student.has_passed() else "FAIL"
        msg += f"\n\nAverage Mark: {avg:.2f}\nStatus: {status}"
        messagebox.showinfo("Enrolled Subjects", msg)

    def save_and_refresh(self):
        StudentModel.save_all_students(self.students)
        self.view.refresh()

    def back_to_dashboard(self):
        self.view.pack_forget()
        from controller.dashboard_controller import DashboardController
        DashboardController(self.root, self.app, self.student, self.students)
