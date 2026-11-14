#Calculate the sum of the first n natural numbers using recursion

def sum_n(n):
    if n==0:
        return 0        #logic was right except 0 (should have included it becz it returns none)
    add = n+sum_n(n-1)
    return add


print(sum_n(90))