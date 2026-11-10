''' Update a Tuple Element'''
marks = (85, 92, 78, 96, 88)
print("original marks tuple:", marks)
position = int(input("enter the position of the student from(1-5):"))

new_marks=int(input("enter the new marks:"))
marks_list=list(marks)
marks_list[position-1]=new_marks

updated_marks=tuple(marks_list)
print("updated marks tuple:",updated_marks)
