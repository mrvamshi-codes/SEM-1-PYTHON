#Largest digit in a given number
n=int(input("enter the number:"))
largest=0
while n>0:
    digit=n%10
    if digit>largest:
        largest=digit
    n//=10
print("The Largest digit is :",largest)
    
