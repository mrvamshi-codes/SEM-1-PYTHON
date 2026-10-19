import csv

with open("matches.csv","r") as f1:
	reader=csv.DictReader(f1)

	for row in reader:
		print(row["season"],":",row["winner"])

