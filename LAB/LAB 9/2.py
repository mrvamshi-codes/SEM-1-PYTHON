#Write sum_of_digits(n) to return the sum of digits 
#of a positive integer and display its digit count.

num = int(input("enter the number:"))


def sum_of_digits(n):
    total = 0

    while n>0:
        total += n%10
        n //= 10
    return total

print("sum of the digits are:",sum_of_digits(num))
print("number of digits are:",len(str(num)))