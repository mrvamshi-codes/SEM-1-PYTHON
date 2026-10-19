'''Wite a Python program to accept the working hours of 7 employees from the user and store Them in a tuple. Display the working hours of employees who worked more than 8 hours and count the number of employees who worked more than 8 hours.'''

T1=()
for i in range(7):
    hours = int(input("Enter working hours: "))
    T1+=(hours,)
print("Working hours of employees who worked more than 8 hours:")
count=0
for i in T1:
    if i>8:
        print(i)
        count+=1
print("Number of employees who worked more than 8 hours:",count)