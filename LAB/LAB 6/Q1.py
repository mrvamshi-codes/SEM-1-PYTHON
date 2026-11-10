#Question 1 : Display lines starting with a given letter

filename = input("Enter file name: ")
letter = input("Enter starting letter: ")

with open(filename, "r") as file:
    for line in file:
        if line.startswith(letter):
            print(line.strip())


#output
'''Enter file name: L6Q1.txt
Enter starting letter: A
Apple is red
Ant is small
mrvamshi@Ms-MacBook-Air LAB 6 % python Q1.py
Enter file name: L6Q1.txt            
Enter starting letter: B
Banana is yellow'''