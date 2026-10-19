#enter a number and reverse it
num=int(input("enter the number:"))
rev_num=0
temp=num
while temp>0:
    digit=temp%10
    rev_num=rev_num*10+digit
    temp=temp//10
print(rev_num)
