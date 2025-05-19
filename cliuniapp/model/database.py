import json
import os
from model.student import Student

class Database:
    FILE_PATH = "students.data"

    def __init__(self):
        if not os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, 'w') as f:
                json.dump([], f)

    def load_students(self):
        with open(self.FILE_PATH, 'r') as f:
            data = json.load(f)
            return [Student.from_dict(item) for item in data]

    def save_students(self, students):
        with open(self.FILE_PATH, 'w') as f:
            json.dump([student.to_dict() for student in students], f, indent=4)

    def clear_students(self):
        with open(self.FILE_PATH, 'w') as f:
            json.dump([], f)

    def find_student_by_email(self, email):
        with open(self.FILE_PATH, 'r') as f:
            data = json.load(f)
            for item in data:
                if item['email'] == email:
                    return Student.from_dict(item)
        return None
    
    def save_or_update_student(self, student):
        with open(self.FILE_PATH, 'r') as f:
            data = json.load(f)

        # Find student index by email if exists
        for i, item in enumerate(data):
            if item['email'] == student.email:
                data[i] = student.to_dict()
                break
        else:
            data.append(student.to_dict())

        with open(self.FILE_PATH, 'w') as f:
            json.dump(data, f, indent=4)
