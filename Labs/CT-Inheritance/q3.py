class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining: {self.balance}")
        else:
            print("Insufficient funds!")

class SavingsAccount(Account):
    def calculate_interest(self, rate=0.05):
        interest = self.balance * rate
        print(f"Interest earned: {interest}")

class FixedDeposit(Account):
    def lock_period(self, months):
        print(f"This account is locked for {months} months.")

personal_acc = SavingsAccount(1000)
personal_acc.calculate_interest(0.1)