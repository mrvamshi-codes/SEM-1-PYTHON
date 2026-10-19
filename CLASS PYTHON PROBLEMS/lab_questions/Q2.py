''' write a python program to create a tuple containing the marks of 5 students.Aceept a student position and a new mark from the user. Since tuples are immutable , convert the tuple into list,update the marks at specified position , and convert it back into a tuple. Display the original tuple and the updated tuple.'''
marks = (85, 92, 78, 96, 88)
print("original marks tuple:", marks)
position = int(input("enter the position of the student from(0-4):"))

new_marks=int(input("enter the new marks:"))
marks_list=list(marks)
marks_list[position]=new_marks

updated_marks=tuple(marks_list)
print("updated marks tuple:",updated_marks)
