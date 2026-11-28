#3
'''def division(y):
    def divide(x):
        return x/y
    return divide


a = division(2)    #refers to divide
#a is a function that always divides by 2 as it remembers y as 2

b = division(3)    #refers to divide

print(a(20))       #20 is the input for x 
print(b(30))'''

# why did we use closure here ??

#Instead of passing both numbers every time we want to perform division,
#we can fix one number beforehand and reuse the function.



#7
def f1():
    x = 0
    def f2():
        nonlocal x  #Without nonlocal x, this program would raise an UnboundLocalError.
        x+=1
        return x
    return f2

func = f1()
result = func()
print("x=",result)
result = func()
print("x=",result)




#print(func()) -- 1
#print(func()) -- 2
#print(func()) -- 3

#a = f1()   (creates a new closure)
#print(a())        --  1