fruts = ["aple", "magno", "banan", "ornage", "carrot"]
print(fruts)
print(fruts[0], fruts[-1])
fruts[1] = "garpe"
print(fruts)

nums = [10,20,30,40,50]
print(nums)
del nums[2]
nums.insert(2, 25)
print(nums)

nums2 = []
for i in range(5):
    nums2.append(int(input("Enter number: ")))
print(nums2)

marks = [65, 72, 80, 90, 55]
print("highest mark: ", max(marks))
print("lowest mark: ", min(marks))
print("marks average: ", sum(marks) / len(marks))

students = ["abdul", "hamood", "beebo", "canary", "dwingleberry", "pradesh"]
students.sort()
print(students)

items = ["pen", "pencil", "eraser", "ruler"]
items[1] = "notebook"
print(items)

noms = [1, 2, 3, 4, 5, 6 ,7 ,8]
for i in noms:
    if i%2==0:
        del noms[noms.index(i)]

nums3 = [3, 6, 9, 12, 15]
newNums3 = []
for i in nums3:
    if i > 8:
        newNums3.append(i)

numpersList = [67, 21, 69]
inp = int(input("enter nomber: "))
if inp in numpersList: print("habibi yo nomper is in the list")