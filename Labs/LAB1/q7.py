studentGrades = {}
for i in range(1, 6):
    name = input(f"Enter #{i} student name: ")
    grade = int(input(f"Enter marks of {name}: "))
    studentGrades.update({name:grade})
print("Students who scored more than 60:")
for k, v in studentGrades.items():
    if v > 60:
        print(k)