#check if the number is a palindrome or not
num=int(input("enter the number:"))
rev_num=0
temp=num
while temp>0:
    rev_num=rev_num*10+temp%10
    temp//=10
if num==rev_num:
    print("The given number is palindrome")
else:
    print("The given number is not a palindrome")