#create two empty sets . Take m and n as input from the user as the number of elements to be added to both the sets respectively.Add m integers to set 1 and add n integrs to set2.Find the cartesian product of two sets and display it.
S1=set()
S2=set()
m=int(input("Enter the number of elements to be added to set 1: "))
n=int(input("Enter the number of elements to be added to set 2: "))

for i in range(m):
    S1.add(int(input("Enter the element to be added to set 1: ")))

for i in range(n):
    S2.add(int(input("Enter the element to be added to set 2: ")))

# Cartesian product of two sets (using a set comprehension)
cartesian_product = {(x, y) for x in S1 for y in S2}

print("Cartesian product of two sets is: ",cartesian_product)