from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def get_balance(self):
        pass  # Abstract method

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Encapsulated balance (private variable)

    def get_balance(self):
        print(f"Dear {self.account_holder}, your savings account balance is {self.__balance}")

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.__balance}")

# Creating a savings account object
s1 = SavingsAccount("Rakshit", 5000)
s1.get_balance()  # Output: Your balance is 5000

s1.deposit(2000)  # Deposit money
s1.withdraw(1000)  # Withdraw money
s1.get_balance()  # Output: Your balance is updated

