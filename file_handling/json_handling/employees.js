import csv

with open("employees.csv", mode="r") as file:
    reader = csv.DictReader(file)
    next(reader)
    for row in reader:
        print(f"{{row[0]} works in {row[1]} and earns {row[2]}}")
