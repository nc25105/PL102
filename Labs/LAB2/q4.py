class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def check_pass(self):
        if self.marks >= 50:
            print("Pass")
        else:
            print("Fail")

student = Student("labubu", 45)
student.check_pass()