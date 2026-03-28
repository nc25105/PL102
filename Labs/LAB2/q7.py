class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_topper(self):
        return self.marks > 75

students = []
for i in range(5):
    students.append(Student(input("Enter student name: "), int(input("Enter student marks: "))))

for student in students:
    if student.is_topper():
        print(student.name)