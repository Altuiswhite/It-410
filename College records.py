import re

# Validator class with static methods for various input validations
class Validator:

    @staticmethod
    def validate_name(name):
        return re.fullmatch(r"[A-Za-z\s\-']+", name) is not None

    @staticmethod
    def validate_email(email):
        return re.fullmatch(r"[A-Za-z0-9._\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", email) is not None

    @staticmethod
    def validate_student_id(sid):
        return sid.isdigit() and len(sid) <= 7

    @staticmethod
    def validate_instructor_id(iid):
        return iid.isdigit() and len(iid) <= 5

    @staticmethod
    def validate_required_field(field):
        return field.strip() != ""


# Base class for Person
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def displayInformation(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")


# Student class inheriting from Person
class Student(Person):
    def __init__(self, name, email, student_id, program):
        super().__init__(name, email)
        self.student_id = student_id
        self.program = program

    def displayInformation(self):
        super().displayInformation()
        print(f"Role: Student")
        print(f"Student ID: {self.student_id}")
        print(f"Program: {self.program}")


# Instructor class inheriting from Person
class Instructor(Person):
    def __init__(self, name, email, instructor_id, institution, degree):
        super().__init__(name, email)
        self.instructor_id = instructor_id
        self.institution = institution
        self.degree = degree

    def displayInformation(self):
        super().displayInformation()
        print(f"Role: Instructor")
        print(f"Instructor ID: {self.instructor_id}")
        print(f"Graduated From: {self.institution}")
        print(f"Highest Degree: {self.degree}")


# Main program logic
college_records = []

print("Welcome to the College Records System!\n")

while True:
    role = input("Is this individual a Student or an Instructor? (Enter 'student' or 'instructor'): ").strip().lower()
    while role not in ["student", "instructor"]:
        role = input("Invalid entry. Please enter 'student' or 'instructor': ").strip().lower()

    # Get and validate name
    name = input("Enter individual's name: ").strip()
    while not Validator.validate_name(name):
        name = input("Invalid name. Please enter again (letters, spaces, hyphens only): ").strip()

    # Get and validate email
    email = input("Enter individual's email address: ").strip()
    while not Validator.validate_email(email):
        email = input("Invalid email. Please enter again (basic email format only): ").strip()

    if role == "student":
        student_id = input("Enter Student ID (max 7 digits): ").strip()
        while not Validator.validate_student_id(student_id):
            student_id = input("Invalid Student ID. Please enter a numeric ID with max 7 digits: ").strip()

        program = input("Enter Program of Study: ").strip()
        while not Validator.validate_required_field(program):
            program = input("This field is required. Enter Program of Study: ").strip()

        student = Student(name, email, student_id, program)
        college_records.append(student)

    else:  # Instructor
        instructor_id = input("Enter Instructor ID (max 5 digits): ").strip()
        while not Validator.validate_instructor_id(instructor_id):
            instructor_id = input("Invalid Instructor ID. Please enter a numeric ID with max 5 digits: ").strip()

        institution = input("Enter name of last institution graduated from: ").strip()
        while not Validator.validate_required_field(institution):
            institution = input("This field is required. Enter name of institution: ").strip()

        degree = input("Enter highest degree earned: ").strip()
        while not Validator.validate_required_field(degree):
            degree = input("This field is required. Enter highest degree: ").strip()

        instructor = Instructor(name, email, instructor_id, institution, degree)
        college_records.append(instructor)

    # Continue or not
    cont = input("Would you like to enter another individual? (yes/no): ").strip().lower()
    while cont not in ['yes', 'no']:
        cont = input("Please enter 'yes' or 'no': ").strip().lower()

    if cont == "no":
        break

# Display all records
print("\n--- College Records Summary ---\n")
for record in college_records:
    record.displayInformation()
    print("-" * 40)
