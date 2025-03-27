class User:
    def __init__(self, username, password):
        self.username = username
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
        
    def login(self, usernameL, pass_L):
        if usernameL == self.username and pass_L == self.__password:
            print("Login successful!")
        else:
            print("Invalid username or password")

# Test cases
user1 = User("Rakshit", "Pass@123")  # Initially set a password
user1.set_password("Hello123")  # Weak password (no special character)
user1.set_password("Strong@123")  # Password updated successfully

user1.login("Rakshit", "Wrong@123")  # Invalid credentials
user1.login("Rakshit", "Strong@123")  # Login successful!

