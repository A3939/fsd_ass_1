from model.student import Student
from model.database import Database
import utils

class StudentController:
    def __init__(self):
        self.database = Database()
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
        email = input("Enter your email (must be firstname.lastname@university.com): ").strip()
        if not utils.validate_email(email):
            print("Invalid email format.")
            return

        if self.database.find_student_by_email(email) is not None:
            print("A student with this email already exists.")
            return

        password = input("Enter your password (start with uppercase, 5+ letters, 3+ digits): ").strip()
        if not utils.validate_password(password):
            print("Invalid password format.")
            return

        name = input("Enter your name: ").strip()

        new_student = Student.create_with_password(name, email, password)
        self.database.save_or_update_student(new_student)
        print(f"Registration successful! Welcome, {name}.")

    def login(self):
        print("\n--- Student Login ---")
        email = input("Enter your email: ").strip()
        student = self.database.find_student_by_email(email)

        if student and student.verify_password(input("Enter your password: ").strip()):
            print(f"Welcome {student.name}!")
            self.logged_in_student = student
            self.subject_enrolment_menu()
        else:
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
                break
            else:
                print("Invalid option.")

    def enrol_subject(self):
        if len(self.logged_in_student.subjects) >= 4:
            print("Student are allow to entroll in 4 subjects only.")
            return

        self.logged_in_student.enrol_subject()
        self.database.save_or_update_student(self.logged_in_student)

    def drop_subject(self):
        subject_id = input("Enter subject id to drop: ").strip()
        self.logged_in_student.drop_subject(subject_id)
        self.database.save_or_update_student(self.logged_in_student)

    def view_enrolments(self):
        subjects = self.logged_in_student.subjects
        if not subjects:
            print("You are not enrolled in any subjects.")
            return

        print("\n--- Enrolled Subjects ---")
        print(f"{'Subject ID':<12} {'Mark':<6} {'Grade':<6}")
        print("-" * 30)
        for s in subjects:
            print(f"{s.id:<12} {s.mark:<6} {s.grade:<6}")

        avg = self.logged_in_student.average_mark()
        status = "PASS" if self.logged_in_student.has_passed() else "FAIL"
        print("-" * 30)
        print(f"{'Average Mark:':<12} {avg:.2f}")
        print(f"{'Status:':<12} {status}")

    def change_password(self):
        new_password = input("Enter new password: ").strip()
        if not utils.validate_password(new_password):
            print("Invalid password format.")
            return
        self.logged_in_student.change_password(new_password)
        self.database.save_or_update_student(self.logged_in_student)
