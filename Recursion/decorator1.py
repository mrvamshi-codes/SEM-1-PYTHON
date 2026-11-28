#1
def func_decorator(func):
    def inner_func():  # Wrapper function
        print("Hello, before the function is called")
        func()  # Executes the original function
        print("Hello, after the function is called")
    return inner_func

'''def func_hello():
    print("Inside Hello function")

hello = func_decorator(func_hello)
hello()'''

# A decorator adds functionality to an existing
# function without modifying its original code.

#2
#same with using @
@func_decorator     # Automatically applies the decorator
def func_hello():
    print("Inside Hello function")

func_hello()      # Now executes the decorated function

