from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def get_balance(self):
        pass  # Abstract method (must be implemented in child classes)

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        print(f"Your savings account balance is: {self.balance}")

class CurrentAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance
    
    def get_balance(self):
        print(f"Your current account balance is: {self.balance}")

# Creating objects and calling the abstract method
s1 = SavingsAccount(5000000)
s1.get_balance()  # Output: Your savings account balance is: 5000000

c1 = CurrentAccount(6000000)
c1.get_balance()  # Output: Your current account balance is: 6000000

