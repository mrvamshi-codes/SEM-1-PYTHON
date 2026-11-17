a = ["apple","mango","pears"]
b = map(str.upper,a)  
print(type(b))
print(list(b))



#when i don't use list it just shows map object and class as map
#map is a lazy function so using list cuzz it's a eager function
'''can use list in two ways 
1)b=list(map())
['APPLE', 'MANGO', 'PEARS']
<class 'list'>



2)print(list(b))
<class 'map'>
['APPLE', 'MANGO', 'PEARS']'''




