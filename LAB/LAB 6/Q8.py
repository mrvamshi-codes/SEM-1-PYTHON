#Store City Names and Populations in a CSV File

import csv

cities = []

for i in range(3):
    city = input("Enter the name of the city: ")
    population = int(input("Enter the population of the city: "))
    cities.append([city, population])

with open("L6Q8.csv" , "w" , newline = "") as file:
    writer = csv.writer(file)

    writer.writerow(["City" , "Population"])
    writer.writerows(cities)

print("City names and populations have been stored in the CSV file.")

with open("L6Q8.csv" , "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row[0],":",row[1])