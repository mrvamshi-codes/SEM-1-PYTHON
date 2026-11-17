

def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"



print(check(10))

#lambda function for the same 

var1 = lambda n:"true" if n%2==0 else "false"
print(var1(6))