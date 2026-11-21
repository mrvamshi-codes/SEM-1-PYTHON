#calculate maximum temperature
import functools

temperature = [22.5, 24.6, 26, 32, 27.5]

a = lambda a,b:a if a>b else b

#print(functools.reduce(a,temperature))


#calculate avg temperature

b = lambda a,b:(a+b)

print(functools.reduce(b,temperature)/len(temperature))

