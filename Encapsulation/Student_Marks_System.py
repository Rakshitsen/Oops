class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # Private attribute

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print(f"Marks updated successfully for {self.name}. New marks: {self.__marks}")
        else:
            print("Invalid marks! Marks should be between 0 and 100.")

# Test the class
s1 = Student("Rahul", 80)
print(s1.get_marks())  # Expected: 80
s1.set_marks(95)
print(s1.get_marks())  # Expected: 95
s1.set_marks(-10)  # Should print a warning message

