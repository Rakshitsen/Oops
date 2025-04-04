import csv

data = [
  ["Name", "Age", "Grade"],
  ["David", 21, "B"],
  ["Emma", 22, "A"],
  ["John", 20, "C"],
  ["Sophia", 23, "A"],
  ["Michael", 21, "B"],
  ["Olivia", 22, "A"],
  ["James", 20, "C"],
  ["Isabella", 23, "A"],
  ["Liam", 21, "B"]
]

with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)


print("CSV file written successfully!")
