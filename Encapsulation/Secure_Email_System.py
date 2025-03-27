class Email:
    def __init__(self, email, password):
        self.email = email
        self.__password = password  # Private attribute

    def get_password(self):
        print("Access Denied")  # Prevent direct access to password

    def set_password(self, new_pass):
        special_chars = "!@#$%^&*()"
        
        if (
            any(char.isdigit() for char in new_pass) and
            any(char in special_chars for char in new_pass) and
            len(new_pass) >= 8
        ):
            self.__password = new_pass
            print("Password updated successfully")
        else:
            print("Weak password! Password not updated")

# Test cases
e1 = Email("myemail@example.com", "Strong@123")
print(e1.get_password())  # Access Denied

e1.set_password("weak")  # Weak password
e1.set_password("New@Pass1")  # Password updated successfully

