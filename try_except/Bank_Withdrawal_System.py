class InvalidTransactionError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidTransactionError("Invalid transaction: Amount must be greater than zero.")
        elif amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! Remaining balance: {self.balance}")

# Main program
try:
    account = BankAccount(50000)
    withdraw_amount = int(input("Enter the withdrawal amount: "))
    account.withdraw(withdraw_amount)

except InvalidTransactionError as e:
    print("Transaction Error:", e)
except InsufficientBalanceError as e:
    print("Balance Error:", e)
except ValueError:
    print("Error: Please enter a valid number.")
except Exception as e:
    print("Unexpected Error:", e)

