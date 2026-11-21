
#5. 
from functools import reduce
'''n ='1729'
result = reduce(lambda a,b:a+b,map(int,n))               #missed the main logic map(function,iterable)
print(result)'''


#6. 
nums = [45, 12, 78, 34, 9, 56, 23, 67, 5, 41]
print(reduce(min,nums))     
#instead of min 
#lambda a,b:a if a<b else b or min(a,b)
