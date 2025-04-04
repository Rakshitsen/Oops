import csv

with open("students.csv",mode= "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
