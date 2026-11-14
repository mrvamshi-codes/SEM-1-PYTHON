#Write a function to print the length of a list.

numbers = [1,2,3,4,5]

def check_len(list):
    return len(list)


length = print(check_len(numbers))

#mistake was did not use print statement

#Write a function to print all elements of a list in a single line.

def p(list):
    for item in list:
        print(item,end = " ")     #firstly used list[item] which was a logical mistake
    print()
        

p(numbers)           #used print(p(numbers)) so got none value 


#print() → Displays something on the screen.



#return → Sends a value back to the caller.



#A function without an explicit return returns None.


