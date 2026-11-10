#count the occurance of the given element in the tuple
t1= (1, 2, 3, 4, 5, 1, 2, 1)
n=int(input("enter the element to search for:"))
count=0
for i in t1:
    if n==i:
        count+=1
print("the occurance of the given element is:",count)