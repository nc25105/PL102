class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, student_id, name):
        super().__init__(name)
        self.student_id = student_id

    def display_student(self):
        print(f"ID: {self.student_id}, Name: {self.name}")

Student1 = Student("NC30000", "Ali")
Student1.display_student()