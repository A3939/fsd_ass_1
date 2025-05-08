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
        id = input("Enter the student's id to remove: ").strip()
        before_count = len(self.students)
        self.students = [s for s in self.students if s.id != id]
        after_count = len(self.students)

        if before_count == after_count:
            print("No student found with that email.")
        else:
            self.database.save_students(self.students)
            print(f"Student {id} removed successfully.")

    def partition_pass_fail(self):
        pass_students = [s for s in self.students if s.has_passed()]
        fail_students = [s for s in self.students if not s.has_passed()]

        def print_group(title, students):
            print(f"\n--- {title} Students ({len(students)}) ---")
            print(f"{'Name':<20} {'Email':<35} {'Avg Mark':<10}")
            print("-" * 70)
            for s in students:
                print(f"{s.name:<20} {s.email:<35} {s.average_mark():<10.2f}")

        print_group("PASS", pass_students)
        print_group("FAIL", fail_students)

    def group_by_grade(self):
        grade_groups = {'HD': [], 'D': [], 'C': [], 'P': [], 'F': []}

        for student in self.students:
            for subject in student.subjects:
                grade_groups.get(subject.grade, []).append((student.name, subject.id, subject.mark))

        print("\n--- Students Grouped by Grade ---")
        for grade, entries in grade_groups.items():
            print(f"\nGrade {grade}:")
            if entries:
                print(f"{'Name':<20} {'Subject ID':<12} {'Mark':<5}")
                print("-" * 40)
                for entry in entries:
                    print(f"{entry[0]:<20} {entry[1]:<12} {entry[2]:<5}")
            else:
                print("No students.")

    def view_all_students(self):
        if not self.students:
            print("No students registered.")
            return

        print("\n--- All Students ---")
        print(f"{'ID':<8} {'Name':<20} {'Email':<35} {'Subjects':<10} {'Avg Mark':<10} {'Status':<6}")
        print("-" * 90)

        for student in self.students:
            avg_mark = student.average_mark()
            status = 'PASS' if student.has_passed() else 'FAIL'
            print(f"{student.id:<8} {student.name:<20} {student.email:<35} {len(student.subjects):<10} {avg_mark:<10.2f} {status:<6}")

    def clear_all_students(self):
        confirmation = input("Are you sure you want to clear ALL students? (yes/no): ").lower()
        if confirmation == 'yes':
            self.students = []
            self.database.clear_students()
            print("All students cleared successfully.")
        else:
            print("Operation cancelled.")
