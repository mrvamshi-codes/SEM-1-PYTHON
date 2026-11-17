#WAP that doubles the even numbers present in the list using map function

num = [1,2,3,4,5,6]

def double(n):
    if n%2==0:
        return n*2
    else:
        return n

a = map(double,num)

print(list(a))

#mistake was i did not use return statement and used uneccesary for loop 
#after that I used return n*=2 which is symantically wrong 

#print(next(a))     output -- 1
#print(next(a))     output -- 4