#Write a Python function to calculate the factorial of a number n

def fact(n):
    fact = 1     #firstly introduced fact outside the function
    while n>0:
        fact*=n
        n-=1      #did not use this statement and missed the main logic
    return fact   #did not use return statement so output was none


print(fact(5))