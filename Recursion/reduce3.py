import functools 

L = [2,3,4]

#print(functools.reduce(lambda a,b:a*b,L))
#output -- 24

print(functools.reduce(lambda a,b:a*b,L,10))
# here 10 is the initializer and the multiplication starts with 10 and then proceeds 
#10 is called accumilator and the next element is 2
#output -- 240
