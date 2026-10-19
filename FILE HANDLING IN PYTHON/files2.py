#this is used for .csv files only.

import csv

 
#csv.reader()  -- gives lists

#don't forget writing import.csv before starting anything in csv files 

'''with open("t2.csv","r") as f1:
	reader=csv.reader(f1)


	for row in reader:
		print(row)'''
#Name,Age(input for reading rows)
#Vamshi,18
#Rahul,19

#don't forget writing import.csv before starting anything in csv files 

'''with open("t2.csv","r") as f1:
	reader=csv.reader(f1)

	next(reader) #skipping the header row using this function


	for row in reader:
		print(row)'''

#accesing particular columns

#don't forget writing import.csv before starting anything in csv files 

'''with open("t2.csv","r") as f1:
	reader=csv.reader(f1)

	next(reader)


	for row in reader:
		print("Name:",row[0])
		print("Age:",row[1])'''



#csv.writer()

#lines in t2.csv for this is
'''Name,Age,Branch
Vamshi,18,CSE
Rahul,19,ECE'''

#don't forget writing import.csv before starting anything in csv files 

'''with open("t2.csv","w",newline="") as f1:
	wt=csv.writer(f1)


	wt.writerow(["Name", "Age", "Branch"])
	wt.writerow(["Vamshi", 18, "CSE"])
	wt.writerow(["Rahul", 19, "ECE"])'''


#csv.DictReader()  -- gives dictionaries

#don't forget writing import.csv before starting anything in csv files 

'''with open("t2.csv","r") as f1:
	reader=csv.DictReader(f1)

	for row in reader:
		print(row)'''

#accesing individual fields/columns

#don't forget writing import.csv before starting anything in csv files 


'''with open("t2.csv","r") as f1:
	reader=csv.DictReader(f1)

	for row in reader:
		print("Name:",row["Name"])
		print("Age:",row["Age"])	 
		print("Branch:",row["Branch"])'''


#csv.DictWriter() 

#don't forget writing import.csv before starting anything in csv files

with open("new.csv","w",newline="") as f1:
	fields=["Name","Age","Branch"]
	

	writer=csv.DictWriter(f1,fieldnames=fields)

	writer.writeheader()


	writer.writerow({"Name":"Vamshi","Age": 18,"Branch":"CSE"})
        

	writer.writerow({"Name":"Rahul","Age":19,"Branch":"ECE"})





