#reduce() applies a function repeatedly to the elements of an iterable, combining them into a single value.
#Unlike map() and filter(), reduce() must be imported from the functools module.



#import functools → Use functools.reduce().    -- method used by ma'am
#from functools import reduce → Use reduce() directly.   --gpt method


import functools 

a = lambda x,y:x*y
L = [1,2,3,4,5,6]
b = functools.reduce(a,L)
print(b,type(b)) 


#other method 
'''from functools import reduce
a = lambda x,y:x*y
L = [1,2,3,4,5,6]
b = reduce(a,L)
print(b,type(b)) '''



