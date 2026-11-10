'''Student Marks Analysis Using Tuple and Set.'''
students=('a','b','c','d','e')
TM=(85, 90, 70, 78, 88)

Set_of_qualifying_marks = set()
for x in TM:
    if x in TM:
        if x>75:
            Set_of_qualifying_marks.add(x)

print("Set of qualifying marks:", Set_of_qualifying_marks)
print("Number of students who scored above 75:", len(Set_of_qualifying_marks))
