#2. 

'''lst= [1,2,3,4,5]
Chars= ['a','b','c','d','e']
print(list(zip(Chars,lst)))'''

#output -- [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]


#3. 

'''scores = [65, 82, 74, 91, 76, 55, 88]
a = list(filter(lambda n:n>75,scores))
print(a)'''

#output -- [82, 91, 76, 88]

#4. 

Lst = ['Orange', 'Apple', 'Mango', 'Apricot']
'''new_lst = []
for item in Lst:
    if item.startswith('A'):
        new_lst.append(item)

print(new_lst)'''

#easy method 

result = map(lambda n:n if n.startswith('A') else None,Lst)
print(list(filter(lambda n:n is not None , result)))


