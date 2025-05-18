import json
import os
from model.subject_model import Subject

class StudentModel:
    DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "student.data")

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.password = data['password']
        self.subjects = [Subject.from_dict(s) for s in data.get('subjects', [])]

    def enrol_subject(self):
        if len(self.subjects) >= 4:
            return False
        new_subject = Subject()
        self.subjects.append(new_subject)
        return True

    def drop_subject(self, subject_id):
        before_count = len(self.subjects)
        self.subjects = [s for s in self.subjects if s.id != subject_id]
        return len(self.subjects) < before_count

    def average_mark(self):
        if not self.subjects:
            return 0.0
        return sum(s.mark for s in self.subjects) / len(self.subjects)

    def has_passed(self):
        return all(s.grade != 'F' for s in self.subjects)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'subjects': [s.to_dict() for s in self.subjects]
        }

    @staticmethod
    def load_all_students():
        with open(StudentModel.DATA_FILE, 'r') as f:
            data = json.load(f)
            return [StudentModel(d) for d in data]

    @staticmethod
    def save_all_students(students):
        with open(StudentModel.DATA_FILE, 'w') as f:
            json.dump([s.to_dict() for s in students], f, indent=4)
