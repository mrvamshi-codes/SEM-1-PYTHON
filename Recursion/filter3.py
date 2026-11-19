#function to check whether a number is a multiple of 3 using lambda function in filter function

a = lambda n:True if n%3==0 else False    

num = [3,4,6,8,12]

b = list(filter(a,num))

print(b,type(b))

#num = [3, 4, 6, 8, 12]
#b = list(filter(lambda n: n % 3 == 0, num))
#print(b)