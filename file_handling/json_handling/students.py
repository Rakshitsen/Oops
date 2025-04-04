import csv

# Open the CSV file
with open("students.csv", mode="r") as file:
    reader = csv.reader(file)  # Create a CSV reader object
    for row in reader:  # Iterate through rows
        print(row)

