try:
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))
    print(n1 / n2)
except ZeroDivisionError:
    print("You cannot divide by Zero.")