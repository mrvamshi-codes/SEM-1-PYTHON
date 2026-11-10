#find largest of 3 numbers
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))    
c=int(input("enter the third number:"))

largest = a

if b>largest:
    largest = b
if c>largest:
    largest = c
print("The largest number is:",largest)