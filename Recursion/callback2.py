def square(n):
    return n**2

def cube(n):
    return n**3


num = [1,2,3,4,5]


def apply(func,lst):
    return list(map(func,lst))

print(apply(square,num))
print(apply(cube,num))


#alternate simpler method 
'''a = map(square,num)
   b = map(cube,num)'''
#print(list(a)) and also for b