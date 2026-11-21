#Write a Python program using reduce() and lambda to find the sum of only the even numbers in the list

'''import functools
numbers = [3, 8, 5, 12, 7, 4, 9]
a = lambda a,b:a+b if b%2==0 else a
print(functools.reduce(a,numbers,0))'''

#Write a Python program using functools.reduce() and lambda to find the smallest number in this list

'''from functools import reduce

numbers = [45, 12, 78, 3, 29, 8]
a = lambda a,b:a if a<b else b
print(reduce(a,numbers))'''