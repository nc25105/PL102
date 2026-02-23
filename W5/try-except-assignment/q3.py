try:
    n = int(input("Enter number: "))
    if n >= 18:
        print("You're eligible to vote.")
    else:
        print("You're ineligible to vote.")
except ValueError:
    print("Input must be in numbers.")