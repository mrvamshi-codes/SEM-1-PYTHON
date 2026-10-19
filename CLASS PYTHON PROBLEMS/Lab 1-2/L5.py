#to reverse a given number
n=int(input("enter the number:"))
rev_num=0
temp=n
while temp>0:
    digit=temp%10
    rev_num=rev_num*10+digit
    temp//=10
print("The reverse of the given number is: ",rev_num)
