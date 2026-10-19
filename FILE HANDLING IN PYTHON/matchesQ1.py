import csv

count=0

with open("matches.csv","r") as f1:
	reader=csv.DictReader(f1)

	for row in reader:
		if row["season"]=="2009":
			count+=1

print("Number of matches played in 2009 =",count)

