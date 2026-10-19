#find the absolute difference btw succesive elements of a given list and this difference must ne stored in the new list.Display the new list
L1=[57,63,128,79]
L2=[]
for i in range(0,len(L1)-1):
    L2.append(abs(L1[i]-L1[i+1]))
print(L2)
