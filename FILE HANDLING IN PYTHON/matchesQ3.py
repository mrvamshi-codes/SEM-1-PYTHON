import csv

count=0

with open("matches.csv","r") as f1:
	reader=csv.DictReader(f1)

	for row in reader:
		if row["toss_winner"]==row["winner"]:
			count+=1
print("Number of matches in which toss winner is same as the match winners are:",count)

		
	