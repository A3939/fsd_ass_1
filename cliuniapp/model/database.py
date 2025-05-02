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
