#given a list of heterogeneous elements , create a different lists based on the type of elements in the list
L=[10, 3.5, "Python", True]
integers=[]
floats=[]
booleans=[]
strings=[]
for x in L:
    if type(x)==int:
        integers.append(x)
    elif type(x)==float:
        floats.append(x)
    elif type(x)==bool:
        booleans.append(x)
    elif type(x)==str:
        strings.append(x)
print("Integers:",integers)
print("Bool:",booleans)
print("Float:",floats)
print("Strings:",strings)
