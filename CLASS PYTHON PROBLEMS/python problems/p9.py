#to check if a given number is palindrome or not
num=int(input("enter the number:"))
rev_num=0
temp=num
while temp>0:
    digit=temp%10
    rev_num=rev_num*10+digit
    temp=temp//10
if num==rev_num:
    print("the given number is palindrome")
else:
    print("the given number is not a palindrome")
    
