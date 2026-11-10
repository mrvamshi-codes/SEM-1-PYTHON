#Find Products Within a Given Price Range from a CSV File

import csv

with open("L6Q5.csv", "r") as file:
    reader = csv.DictReader(file)

    minimum = float(input("Enter minimum price: "))
    maximum = float(input("Enter maximum price: "))

    for row in reader:
        name = row["Product Name"]
        price = float(row["Price"])

        if minimum <= price <= maximum:
            print(name , ":" , price)