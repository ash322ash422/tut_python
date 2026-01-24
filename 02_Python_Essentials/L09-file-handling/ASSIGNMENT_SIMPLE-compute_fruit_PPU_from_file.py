import csv

file_name = "data_fruits.csv"

with open(file_name, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        fruit = row["fruit"]
        total_price = float(row["total_price"])
        qty = int(row["qty"])

        price_per_unit = total_price / qty
        print(f"Fruit: {fruit} | Price per unit: {price_per_unit}")