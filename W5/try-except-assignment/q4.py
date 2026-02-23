list = [21,63,32,79,30]
try:
    indx = int(input("Enter index to get: "))
    print(list[indx])
except IndexError:
    print("Number out of range.")