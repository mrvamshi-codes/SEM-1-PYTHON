'''num = [1,2,3,4,5]
squares =[n**2 for n in num]
print(squares)'''

#output --[1, 4, 9, 16, 25]

#there are two types of syntax for this 

#1. [expression for variable in iterable]

#2. [expression for variable in iterable if condition]


#
'''numbers = [3, 7, 10, 12, 15, 18, 21, 24]
result = [n**2 for n in numbers if n%3==0]
print(result)'''

# [9, 144, 225, 324, 441, 576]


'''a = [2, 4]
b = [3, 5, 7]

result = [x*y for x in a for y in b]    #nested for loops (mistake i made was i used "and" instead of for 2nd time)

print(result)'''
#[6, 10, 14, 12, 20, 28]



