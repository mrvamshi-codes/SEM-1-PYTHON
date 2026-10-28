#Question 3 : Calculate total amount for each order from a CSV file


import csv

with open("L6Q3.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["PRODUCT"]
        quantity = int(row["QUANTITY"])
        price = float(row["PRICE"])

        total = quantity * price

        print(product, ":", total)



#output
'''PEN : 50.0
BOOK : 100.0
PENICL : 15.0'''
