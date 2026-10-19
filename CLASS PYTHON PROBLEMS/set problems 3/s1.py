#create an empty set and add n integers to it and display the set
S1=set()
n=int(input("enter the number of elements:"))
for i in range(0,n):
    num=int(input("enter the number:"))
    S1.add(num)
print(S1)
