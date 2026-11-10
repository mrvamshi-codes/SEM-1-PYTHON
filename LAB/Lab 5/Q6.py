'''Student Grade Management Using Tuple and Set'''

grades=('A', 'B', 'C', 'A', 'D')
names=('John', 'Alice', 'Bob', 'Eve', 'Charlie')

unique_grades=set(grades)
count_Agrades=grades.count('A')
if count_Agrades==0:
    print("No student recieved grade A")

print("Student Names:",names)
print("Grades:",grades)
print("Unique Gradese:",unique_grades)
print("Number of students who received grade A:",count_Agrades)

