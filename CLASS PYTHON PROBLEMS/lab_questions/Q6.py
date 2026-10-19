'''write a python program to acccept the names and grades of five students from the user and store them in two tuples
1. Create a set containing the unique grades obtained by the students.
2. Count the number of students who received grade A
3. If no student received grade "A', display an appropriate message
4. Display the student names, grades, unique grades, and the appropriate result for grade'''

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

