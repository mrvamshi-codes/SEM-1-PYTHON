#a program to check whether a given number is palindrome or not
n=int(input("enter the number:"))
rev_n=0
temp=n
while temp>0:
    digit=temp%10
    rev_n=rev_n*10+digit
    temp//=10
if n==rev_n:
    print("Given number is palindrome")
else:
    print("Given number is not palindrome")
