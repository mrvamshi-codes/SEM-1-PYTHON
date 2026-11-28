# Chaining decorators applies multiple decorators
# to the same function.


def dedcorator_x(f):
    def inner():
        print("X"*20)
        f()
        print("X"*20)
    return inner


def dedcorator_y(f):
    def inner():
        print("Y"*20)
        f()
        print("Y"*20)
    return inner


'''def func():
    print("Hello world")

result = dedcorator_y(dedcorator_x(func))
# decorator_x wraps the original function first.
# decorator_y then wraps the function returned by decorator_x.
result()'''

#same program using @
@dedcorator_x
@dedcorator_y
def func():
    print("HELLO WORLD")

func()
