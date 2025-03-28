class NegativeNumberError(Exception):
    pass


try:
    num=int(input("Enter a number which not  -ve : "))
    if num < 0:
        raise NegativeNumberError("Number cannot be negative!")
    print(f"Square of you give number {num} is {num**2}")
except ValueError:
    print("Error: Please enter a number!")
except Exception as e:
    print("Unexpected Error:", e)
