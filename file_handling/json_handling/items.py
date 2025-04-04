import csv

data = [
  ["Product", "Price", "Quantity"],
  ["Pen", 10, 5],
  ["Book", 50, 2],
  ["Pencil", 5, 10]
]

with open("items.csv", mode="w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data written successfully")
