import random

class Subject:
    def __init__(self, name):
        self.id = f"{random.randint(1, 999):03d}"
        self.name = name
        self.mark = random.randint(25, 100)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.mark >= 85:
            return 'HD'
        elif self.mark >= 75:
            return 'D'
        elif self.mark >= 65:
            return 'C'
        elif self.mark >= 50:
            return 'P'
        else:
            return 'F'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'mark': self.mark,
            'grade': self.grade
        }

    @staticmethod
    def from_dict(data):
        subj = Subject(data['name'])
        subj.id = data['id']
        subj.mark = data['mark']
        subj.grade = data['grade']
        return subj
