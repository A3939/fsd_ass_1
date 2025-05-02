from model.database import Database

class AdminController:
    def __init__(self):
        self.database = Database()
        self.students = self.database.load_students()

    def admin_menu(self):
        while True:
            print("\n--- Admin System Menu ---")
            print("(1) Remove a Student")
            print("(2) Partition PASS/FAIL Students")
            print("(3) Group Students by Grade")
            print("(4) View All Students")
            print("(5) Clear All Students")
            print("(x) Exit Admin Menu")
            choice = input("Choose an option: ").lower()

            if choice == '1':
                self.remove_student()
            elif choice == '2':
                self.partition_pass_fail()
            elif choice == '3':
                self.group_by_grade()
            elif choice == '4':
                self.view_all_students()
            elif choice == '5':
                self.clear_all_students()
            elif choice == 'x':
                print("Exiting Admin Menu...")
                break
            else:
                print("Invalid option. Try again.")

    def remove_student(self):
        email = input("Enter the student's email to remove: ").strip()
        before_count = len(self.students)
        self.students = [s for s in self.students if s.email != email]
        after_count = len(self.students)

        if before_count == after_count:
            print("No student found with that email.")
        else:
            self.database.save_students(self.students)
            print(f"Student {email} removed successfully.")

    def partition_pass_fail(self):
        pass_students = [s for s in self.students if s.has_passed()]
        fail_students = [s for s in self.students if not s.has_passed()]

        print(f"\n--- PASS Students ({len(pass_students)}) ---")
        for s in pass_students:
            print(f"{s.name} ({s.email}) - Average Mark: {s.average_mark():.2f}")

        print(f"\n--- FAIL Students ({len(fail_students)}) ---")
        for s in fail_students:
            print(f"{s.name} ({s.email}) - Average Mark: {s.average_mark():.2f}")

    def group_by_grade(self):
        grade_groups = {'HD': [], 'D': [], 'C': [], 'P': [], 'F': []}

        for student in self.students:
            for subject in student.subjects:
                grade_groups.get(subject.grade, []).append((student.name, subject.name, subject.mark))

        print("\n--- Students Grouped by Grade ---")
        for grade, entries in grade_groups.items():
            print(f"\nGrade {grade}:")
            if entries:
                for entry in entries:
                    print(f"{entry[0]} - {entry[1]} (Mark: {entry[2]})")
            else:
                print("No students.")

    def view_all_students(self):
        if not self.students:
            print("No students registered.")
            return

        print("\n--- All Students ---")
        for student in self.students:
            print(f"{student.name} ({student.email}) - Enrolled Subjects: {len(student.subjects)}")

    def clear_all_students(self):
        confirmation = input("Are you sure you want to clear ALL students? (yes/no): ").lower()
        if confirmation == 'yes':
            self.students = []
            self.database.clear_students()
            print("All students cleared successfully.")
        else:
            print("Operation cancelled.")
