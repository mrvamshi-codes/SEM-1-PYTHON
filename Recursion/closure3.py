#4
'''def f1():
    def f2():
        print("Hello world")
    return f2

c = f1()
del f1 
c()
f1()'''    
#this is the output after deleting 
#NameError: name 'f1' is not defined


#6 
def outerfunc(x):
    def innerfunc():
        print(x)           # x is a free variable from the outer function
    return innerfunc

a = outerfunc(7)
a()
del outerfunc
a()                      # Closure retains the value of x even after deletion

# Unlike program 4, the inner function depends on
# a variable belonging to the outer function.
# Hence, this is a closure.