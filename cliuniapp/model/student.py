import random
import hashlib
from model.subject import Subject

class Student:
    def __init__(self, name, email, password_hash):
        self.id = f"{random.randint(1, 999999):06d}"
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.subjects = []

    @classmethod
    def create_with_password(cls, name, email, raw_password):
        password_hash = cls.hash_password(raw_password)
        return cls(name, email, password_hash)

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, raw_password):
        return self.hash_password(raw_password) == self.password_hash
    
    def enrol_subject(self):
        if len(self.subjects) >= 4:
            print("You cannot enrol in more than 4 subjects.")
            return
        subject = Subject()
        self.subjects.append(subject)
        print(f"Enrolled in {subject.id} with mark {subject.mark} and grade {subject.grade}.")

    def drop_subject(self, subject_id):
        self.subjects = [s for s in self.subjects if s.id != subject_id]
        print(f"Dropped subject {subject_id:}.")

    def change_password(self, new_password):
        self.password_hash = self.hash_password(new_password)
        print("Password updated successfully.")

    def average_mark(self):
        if not self.subjects:
            return 0
        return sum(subject.mark for subject in self.subjects) / len(self.subjects)

    def has_passed(self):
        return self.average_mark() >= 50

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password_hash': self.password_hash,
            'subjects': [subject.to_dict() for subject in self.subjects]
        }

    @staticmethod
    def from_dict(data):
        student = Student(data['name'], data['email'], data['password_hash'])
        student.id = data['id']
        student.subjects = [Subject.from_dict(subj) for subj in data.get('subjects', [])]
        return student
