# 1
'''numbers = [2, 3, 4, 5]

def square(n):
    return n**2

def process(func,lst):
    return list(map(func,lst))    #use list here only instead of using it in the print statement

a = lambda n:n**3

print(process(square,numbers))
print(process(a,numbers))'''

#2
'''num = int(input("enter:"))

a = lambda n:n+5

b = lambda n:n*2

def combine(f1,f2,num):
    return f2(f1(num))

print(combine(a,b,num))
print(combine(b,a,num))'''


#3
numbers = [1, 2, 3, 4, 5, 6]

a = lambda n: n*2 if n%2!=0 else n    #missing the syntax of lambda function
                                       #value_if_true if condition else value_if_false
def transform(func,lst):
    return list(map(func,lst))

print(transform(a,numbers))




