def double(n):
    return n*2

def add_five(n):
    return n+5

num = [1,2,3,4,5,6]

def apply_operation(func,lst):
    return(list(map(func,lst)))


print(apply_operation(double,num))
print(apply_operation(add_five,num))