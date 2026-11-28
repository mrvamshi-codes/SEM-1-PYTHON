# similar to *args but using only 2 arguments
# Unlike *args, this wrapper uses a fixed number of parameters.
import math

def compute(f):
    def inner(a,b):         # Wrapper accepts two arguments
        print("Computing hypotenuse")
        f(a,b)         # Passes the received arguments to the original function
        print("**************")
    return inner

@compute
def h(a,b):
    result = math.sqrt(a**2+b**2)
    print(result)

h(4,3)



#another program which i tried myself
'''def outer(f):
    def inner(*args):
        print("performing addition operation")
        f(*args)
        print("addition completed")
    return inner

@outer
def addition(a,b):
    result = a+b
    print(result)

addition(2,3)'''