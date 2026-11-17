n1 = [1,2,3,4]
n2 = [6,5,4]

a = map(lambda x,y:x+y,n1,n2)

print(list(a))

#if i use strict = True 
# output is (ValueError: map() argument 2 is shorter than argument 1 )

#default value of strict is False

