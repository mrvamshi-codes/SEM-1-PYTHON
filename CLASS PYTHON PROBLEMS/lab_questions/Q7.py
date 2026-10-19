'''write a program to create two sets of integers and determine whethere the sets are equal or disjoint, or one is a subsest of other '''
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
if set1==set2:
    print("sets are equal")
elif set1.isdisjoint(set2):
    print("sets are disjoint")
elif set1.issubset(set2):
    print("set1 is a subset of set2")  
elif set2.issubset(set1):
    print("set2 is a subset of set1")
else:
    print("sets overlap, but neither is a subset of the other")