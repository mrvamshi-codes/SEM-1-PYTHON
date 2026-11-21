#write a program to find factorial a number using reduce function
from functools import reduce

n = 0

numbers = range(1,n+1)        
#this is the main logic I missed and used recursion in this . 

print(reduce(lambda x,y:x*y,numbers,1))    
#here 1 is the initializer which helps to avoid type error when n=0 as range(1,1) is empty