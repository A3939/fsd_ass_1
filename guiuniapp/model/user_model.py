import json
import re
import os

class UserModel:
    DATA_FILE = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "students.data"))

    EMAIL_PATTERN = r'^[a-z]+\.[a-z]+@university\.com$'
    PASSWORD_PATTERN = r'^[A-Z][a-zA-Z]{5,}\d{3,}$'

    @staticmethod
    def validate_email(email):
        return re.match(UserModel.EMAIL_PATTERN, email)

    @staticmethod
    def validate_password(password):
        return re.match(UserModel.PASSWORD_PATTERN, password)

    def authenticate(self, email, password):
        try:
            with open(self.DATA_FILE, 'r') as file:
                users = json.load(file)
                for user in users:
                    if user["email"] == email and user["password"] == '123':
                        return True
            return False
        except FileNotFoundError:
            raise Exception("User data file not found.")
        except json.JSONDecodeError:
            raise Exception("Invalid JSON format in student.data.")
