#create a set by adding n elements from the user. If the user has not added any element to the set, how to check whether the set is empty or not.Print accordingly.
S=set()
n=int(input("enter the number of elements:"))
for i in range(0,n):
    x=int(input("enter the element:"))
    S.add(x)
if len(S)==0:
    print("The set is empty")
else:
    print("The set is not empty")
    print("Set is:",S)
