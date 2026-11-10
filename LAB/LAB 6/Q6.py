#Merge Two Dictionaries Containing Student Marks

s1 = {}
s2 = {}

n1 = int(input("Enter the number of students in first dictionary:"))

for i in range(n1):
    name = input("Enter the name of student:")
    marks = int(input("Enter the marks of student:"))
    s1[name] = marks

n2 = int(input("Enter the number of students in second dictionary:"))

for i in range(n2):
    name = input("Enter the name of student:")
    marks = int(input("Enter the marks of student:"))
    s2[name] = marks

# Merge the two dictionaries
s1.update(s2)

print("Merged dictionary of student marks:", s1)