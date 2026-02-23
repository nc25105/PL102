#Q1
student = {"name": "Riya", "age": 15, "grade": 10}
print(student)

#Q2
marks = {"Math": 85, "Science": 90, "English": 78}
print(marks["Science"])

#Q3
student = {"name": "Riya", "age": 15}
student['city'] = 'Delhi'

#Q4
student = {"name": "Riya", "age": 15}
student["age"] = 16

#Q5
student = {"name": "Riya", "age": 15, "grade": 10}
del student['grade']

#Q6
marks = {"Math": 85, "Science": 90, "English": 78}
for i, v in marks.items():
    print(f"{i}: {v}")

#Q7
subjects = {"Math": 85, "Science": 90, "English": 78}
print("English" in subjects)

#Q8
items = {"pen": 10, "pencil": 20, "eraser": 5}
print(sum(items.values()))

#Q9
prices = {"apple": 2, "banana": 1, "orange": 3}
for v in prices:
    print(prices[v])

#Q10
subjectMarks = {"English":100,"Arabic":83,"Networking":79}
for i in subjectMarks:
    print(f"{i}: {subjectMarks[i]}")
subjectMarks["Math"] = 96
subjectMarks["Arabic"] = 84
del subjectMarks["Networking"]