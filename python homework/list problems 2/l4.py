#given a list , create a new list consisting of square  roots of all elements in the list
L1=[1,4,9,16,25]
L2=[]
for x in L1:
    L2.append(x**(1/2)) '''cannot use x**1/2'''
print(L2)
