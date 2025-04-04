import csv
records = [
  {"Name": "Karan", "Score": 85},
  {"Name": "Isha", "Score": 92},
  {"Name": "Manav", "Score": 78}
]

with open("scores.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Score"])
    writer.writeheader()
    for record in records:
        writer.writerow(record)

print("Data written successfully")
