try:
    n = int(input("Enter number: "))
    print(n**2)
except ValueError:
    print("Input must be in numbers.")