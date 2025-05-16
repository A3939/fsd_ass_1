import json
import os

class Admin:
    def __init__(self, filename='student.data'):
        self.filename = filename
        self.students = []
        self.load_students()
    
    def load_students(self):
        """Load student data from file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    content = file.read()
                    if content.strip():
                        self.students = json.loads(content)
                    else:
                        self.students = []
            else:
                with open(self.filename, 'w') as file:
                    file.write('[]')
                self.students = []
        except json.JSONDecodeError:
            print("Error: Corrupted data file. Starting with empty database.")
            self.students = []
        except Exception as e:
            print(f"Error loading student data: {e}")
            self.students = []
    
    def save_students(self):
        """Save student data to file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.students, file)
        except Exception as e:
            print(f"Error saving student data: {e}")
    
    def add_student(self, student_id, name, grade):
        """Add a new student"""
        try:
            if not student_id or not name:
                raise ValueError("Student ID and name cannot be empty")
            
            if any(s['student_id'] == student_id for s in self.students):
                raise ValueError(f"Student with ID {student_id} already exists")
            
            self.students.append({
                'student_id': student_id,
                'name': name,
                'grade': float(grade)
            })
            self.save_students()
            print(f"Student {name} added successfully.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def liststudents(self):  # Fixed method name (with underscore)
        """List all students"""
        if not self.students:
            print("No students in the system.")
            return
        
        print("\nStudent List:")
        print("-" * 40)
        print(f"{'ID':<10}{'Name':<20}{'Grade':<10}")
        print("-" * 40)
        for student in sorted(self.students, key=lambda x: x['student_id']):
            print(f"{student['student_id']:<10}{student['name']:<20}{student['grade']:<10.2f}")
        print("-" * 40)
        print(f"Total students: {len(self.students)}\n")
    
    def group_by_grade(self):
        """Group students by their grade"""
        if not self.students:
            print("No students in the system.")
            return
        
        grade_groups = {}
        for student in self.students:
            grade = student['grade']
            grade_group = f"{int(grade//10)*10}-{int(grade//10)*10+9}"
            if grade_group not in grade_groups:
                grade_groups[grade_group] = []
            grade_groups[grade_group].append(student)
        
        print("\nStudents Grouped by Grade:")
        print("-" * 40)
        for group, students in sorted(grade_groups.items()):
            print(f"Grade Range {group}:")
            for student in students:
                print(f"  {student['student_id']} - {student['name']}: {student['grade']:.2f}")
        print("-" * 40)
    
    def partition_pass_fail(self, passing_grade=50):
        """Partition students into pass/fail categories"""
        if not self.students:
            print("No students in the system.")
            return
        
        pass_students = [s for s in self.students if s['grade'] >= passing_grade]
        fail_students = [s for s in self.students if s['grade'] < passing_grade]
        
        print("\nPass/Fail Partition:")
        print("-" * 40)
        print("PASSING STUDENTS:")
        for student in sorted(pass_students, key=lambda x: -x['grade']):
            print(f"  {student['student_id']} - {student['name']}: {student['grade']:.2f}")
        
        print("\nFAILING STUDENTS:")
        for student in sorted(fail_students, key=lambda x: x['grade']):
            print(f"  {student['student_id']} - {student['name']}: {student['grade']:.2f}")
        print("-" * 40)
    
    def remove_student(self, student_id):
        """Remove a student by ID"""
        try:
            if not student_id:
                raise ValueError("Student ID cannot be empty")
            
            original_count = len(self.students)
            self.students = [s for s in self.students if s['student_id'] != student_id]
            
            if len(self.students) < original_count:
                self.save_students()
                print(f"Student with ID {student_id} removed successfully.")
            else:
                print(f"No student found with ID {student_id}.")
        except Exception as e:
            print(f"Error removing student: {e}")
    
    def clear_file(self):
        """Clear all student data"""
        confirmation = input("Are you sure you want to clear all student data? (yes/no): ").lower()
        if confirmation == 'yes':
            self.students = []
            self.save_students()
            print("All student data has been cleared.")
        else:
            print("Operation cancelled.")

def display_menu():
    print("\nAdmin System")
    print("1. List all students")
    print("2. Add a new student")
    print("3. Group students by grade")
    print("4. Partition students into Pass/Fail")
    print("5. Remove a student")
    print("6. Clear all student data")
    print("7. Exit")

def main():
    admin = Admin()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")
        
        try:
            match choice:
                case '1':
                    admin.liststudents()
                case '2':
                    student_id = input("Enter student ID: ")
                    name = input("Enter student name: ")
                    grade = input("Enter student grade: ")
                    admin.add_student(student_id, name, grade)
                case '3':
                    admin.group_by_grade()
                case '4':
                    admin.partition_pass_fail()
                case '5':
                    student_id = input("Enter student ID to remove: ")
                    admin.remove_student(student_id)
                case '6':
                    admin.clear_file()
                case '7':
                    print("Exiting the system. Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1-7.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()