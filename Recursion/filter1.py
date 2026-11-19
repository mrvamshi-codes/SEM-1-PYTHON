a = lambda n:True if n>=0 else False

L = [1,-4,9,-2,10,-8,0]

b = list(filter(a,L)) 
#syntax of filter -- filter(function, iterable)
#purpose of filter -- Selects elements satisfying a condition
#Result -- Iterator of selected values

print(b,type(b))