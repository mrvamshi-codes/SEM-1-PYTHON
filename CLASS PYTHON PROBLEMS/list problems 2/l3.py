#given a list , create a new list consisting of squares of all elements in the list
L1=[1,2,3,4]
L2=[]
for i in range(0,len(L1)):
    s=L1[i]**2
    L2.append(s)
print(L2)
    
