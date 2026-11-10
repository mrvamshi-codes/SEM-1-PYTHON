#print all amstrong numbers from 1 to n
n=int(input("enter the number:"))
for i in range(1,n+1):
    total=0
    temp=i
    count=len(str(i))
    while temp>0:
        digit=temp%10
        total+=digit**count
        temp=temp//10
    if i==total:
        print(i,end=" ")
    
