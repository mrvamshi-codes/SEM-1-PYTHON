#create an empty set and add n tuples to it each having 3 elements in a tuple and display the set
S=set()
n=int(input("enter the number of tuples in the set:"))
for i in range(0,n):
    a=int(input("enter the element:"))
    b=int(input("enter the element:"))
    c=int(input("enter the element:"))

    t=(a,b,c)
    S.add(t)
print("Set of tuples:",S)

