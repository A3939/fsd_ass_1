from model.student import Student
from model.database import Database
import utils

class StudentController:
    def __init__(self):
        self.database = Database()
        self.students = self.database.load_students()
        self.logged_in_student = None

    def student_menu(self):
        while True:
            print("\n--- Student System Menu ---")
            print("(l) Login")
            print("(r) Register")
            print("(x) Exit")
            choice = input("Choose an option: ").lower()

            if choice == 'l':
                self.login()
            elif choice == 'r':
                self.register()
            elif choice == 'x':
                break
            else:
                print("Invalid option. Try again.")

    def register(self):
        print("\n--- Register New Student ---")
        name = input("Enter your name: ").strip()
        email = input("Enter your email (must be firstname.lastname@university.com): ").strip()
        password = input("Enter your password (start with uppercase, 5+ letters, 3+ digits): ").strip()

        if not utils.validate_email(email):
            print("Invalid email format.")
            return
        if not utils.validate_password(password):
            print("Invalid password format.")
            return

        if any(student.email == email for student in self.students):
            print("A student with this email already exists.")
            return

        new_student = Student(name, email, password)
        self.students.append(new_student)
        self.database.save_students(self.students)
        print(f"Registration successful! Welcome, {name}.")

    def login(self):
        print("\n--- Student Login ---")
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()

        for student in self.students:
            if student.email == email and student.password == password:
                print(f"Welcome {student.name}!")
                self.logged_in_student = student
                self.subject_enrolment_menu()
                return
        
        print("Invalid email or password.")

    def subject_enrolment_menu(self):
        while True:
            print("\n--- Subject Enrolment Menu ---")
            print("(1) Enrol in a subject")
            print("(2) Drop a subject")
            print("(3) View enrolments")
            print("(4) Change password")
            print("(x) Logout")
            choice = input("Choose an option: ").lower()

            if choice == '1':
                self.enrol_subject()
            elif choice == '2':
                self.drop_subject()
            elif choice == '3':
                self.view_enrolments()
            elif choice == '4':
                self.change_password()
            elif choice == 'x':
                print("Logging out...")
                self.logged_in_student = None
                self.database.save_students(self.students)
                break
            else:
                print("Invalid option.")

    def enrol_subject(self):
        if len(self.logged_in_student.subjects) >= 4:
            print("Maximum 4 subjects allowed.")
            return

        subject_name = input("Enter subject name to enrol: ").strip()
        self.logged_in_student.enrol_subject(subject_name)
        self.database.save_students(self.students)

    def drop_subject(self):
        subject_name = input("Enter subject name to drop: ").strip()
        self.logged_in_student.drop_subject(subject_name)
        self.database.save_students(self.students)

    def view_enrolments(self):
        if not self.logged_in_student.subjects:
            print("No subjects enrolled.")
            return
        print("\nEnrolled Subjects:")
        for subject in self.logged_in_student.subjects:
            print(f"- {subject.name} (Mark: {subject.mark}, Grade: {subject.grade})")
        print(f"Average Mark: {self.logged_in_student.average_mark():.2f}")
        print(f"Status: {'PASS' if self.logged_in_student.has_passed() else 'FAIL'}")

    def change_password(self):
        new_password = input("Enter new password: ").strip()
        if not utils.validate_password(new_password):
            print("Invalid password format.")
            return
        self.logged_in_student.change_password(new_password)
        self.database.save_students(self.students)
