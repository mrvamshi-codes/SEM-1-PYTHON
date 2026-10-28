#Question 2 : Find the student with highest marks


students={}

n=int(input("enter the number of students:"))

for i in range(n):
    name= input("Enter the name of student:")
    marks=int(input("Enter the marks of student:"))
    students[name]=marks

topper = max(students,key=students.get)
print("Student with highest marks is:",topper)
print("Marks:",students[topper])



#output 
'''enter the number of students:2
Enter the name of student:Aryan
Enter the marks of student:95
Enter the name of student:Hardik
Enter the marks of student:87
Student with highest marks is: Aryan
Marks: 95'''