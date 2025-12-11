# Project : Simple Bank account 
# o Create a simple bank account class that allows deposite and withdraw 
# o Implement methods for depositing and withdrawing money 

class BankAccount:
    bank_name = "ABC Bank"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.balance}")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")


acc1 = BankAccount("Denish", 1000)

acc1.deposit(500)
acc1.withdraw(300)
acc1.show_balance()
