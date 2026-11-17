'''numbers = [1, 2, 3, 4]
squared = []
for num in numbers:
    result = (lambda x: x ** 2)(num)
    squared.append(result)
print(squared)'''

def double(n):          #double and triple are callback functions
    return n*2
def triple(n):
    return n*3

def apply_twice(fun,num):   #apply_twice is higher order function 
    return fun(fun(num))    

print(apply_twice(double,5))
print(apply_twice(triple,5))

#Defines apply_twice(func, num) that applies the given function twice to the number.
#the mistake i did was used fun(num) instead of the present code so only the output 
#was 10 and 15 instead of expected output 20 and 45