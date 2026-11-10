#Lowest digit in a given number
n=int(input("enter the number:"))
lowest=0
while n>0:
    digit=n%10
    if digit<lowest:
        lowest=digit
    n//=10
print("The Lowest digit is :",lowest)
    
