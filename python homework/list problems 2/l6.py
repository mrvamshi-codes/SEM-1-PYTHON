#given a list of integers , add the number n to each element of the list and print the same list
L1=[5,6,7,8]
n=int(input("enter the number to add in the list:"))
for i in range(0,len(L1)):
    L1[i]+=n
print(L1)
    
