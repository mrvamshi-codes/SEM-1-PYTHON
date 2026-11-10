'''Unique Common Elements Using Tuple and Sets'''
t1=('aryan','rohan','sai','rohan','yash')
t2=('yash','aryan','rohan')
s1=set(t1)
s2=set(t2)

only_event1=s1-s2
all_students=s1 | s2
both_events=s1 & s2
print("students participated in event 1:",only_event1)
print("students participated in event 2:",all_students)
print("students participated in both the events:",both_events)