'''write a python program to create a tuple containing names of five students and another tuple containing their corresponding marks. Create s drt containing the marks if students who scored above 75.
Display the set of qualifying marks and number of students who scored above 75.'''
students=('a','b','c','d','e')
TM=(85, 90, 70, 78, 88)

Set_of_qualifying_marks = set()
for x in TM:
    if x in TM:
        if x>75:
            Set_of_qualifying_marks.add(x)

print("Set of qualifying marks:", Set_of_qualifying_marks)
print("Number of students who scored above 75:", len(Set_of_qualifying_marks))
