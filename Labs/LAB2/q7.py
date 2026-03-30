class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_topper(self):
        return self.marks > 75

students = []
for i in range(1,6):
    name = input(f"Enter student {i}: ")
    marks = int(input(f"Enter marks of {name}: "))
    students.append(Student(name, marks))

print("Top performing students:")
for student in students:
    if student.is_topper():
        print(student.name)