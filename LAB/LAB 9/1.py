#Write power(base, exp=2) using a loop without **,
#accept user input and demonstrate the default exponent.


base = int(input("enter base:"))
exp = int(input("enter exponent:"))
def power(base,exp=2):
    ans = 1
    for i in range(exp):
        ans*=base
    return ans
    
print(power(base))
print(power(base,exp))
    