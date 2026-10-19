#create a set of numbers from 2 to n(inclusive). Print the squares of every number on the terminal
S=set()
n=int(input("enter the number:"))
for i in range(2,n+1):
    S.add(i)

print("Squares:")
for x in S:
    print(x*x)
   
