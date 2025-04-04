import csv

with open("students.csv", mode="r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        if row[2] == "A":
            print(row[0])  # Print only the name

