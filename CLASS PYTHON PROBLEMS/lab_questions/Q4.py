'''Write a Python program to create two tuples containing the names of students who participated in Event 1 and Event 2. Some students may appear more than once in a tuple. Convert both tuples into sets and display'''
t1=('aryan','rohan','sai','rohan','yash')
t2=('sai','yash','aryan','rohan','sai')
s1=set(t1)
s2=set(t2)
print("students participated in event 1:",s1)
print("students participated in event 2:",s2)
print("students participated in both the events:",s1.intersection(s2))