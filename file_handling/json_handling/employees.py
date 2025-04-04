import csv

with open("employees.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} - {row['Department']} - {row['Salary']}")
