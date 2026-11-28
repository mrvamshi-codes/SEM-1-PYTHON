import math

def calculate(f):
    def inner1(*args):         #Collects positional arguments into a tuple
#using *args cuz it can accept variable number of arguments
        print("Decorators")
        f(*args)       #Unpacks the tuple and passes the arguments to the original function
        print("**********")
    return inner1


@calculate
def fact(num):
    print(math.factorial(num))

@calculate
def squareroot(num):
    print(math.sqrt(num))

@calculate
def maximum(*num):
    print(max(num[0],num[1],num[2]))


fact(5)
squareroot(16)
maximum(6,23,41)