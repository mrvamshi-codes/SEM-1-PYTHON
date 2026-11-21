
# zip() pairs corresponding elements from two or more iterables.
# If the iterables have unequal lengths, zip() stops at the shortest.
# Extra elements in longer iterables are ignored.
# zip() returns a lazy iterator containing tuples.



'''a = [1,2,3]
b = [4,5,6]

print(list(zip(a,b)))
#[(1, 4), (2, 5), (3, 6)]
print(zip(a,b))
#<zip object at 0x105447f80>'''


'''names = ["Ram", "Sam", "John"]
marks = [85, 90, 78]

result = zip(names, marks)

print(type(result))         #<class 'zip'> 
print(list(result))          #[('Ram', 85), ('Sam', 90), ('John', 78)]'''



'''names = ["Ram", "Sam", "John"]
marks = [85, 90, 78]

print(list(zip(names, marks)))        #[('Ram', 85), ('Sam', 90), ('John', 78)]
print(dict(zip(names, marks)))        #{'Ram': 85, 'Sam': 90, 'John': 78}
print(set(zip(names, marks)))         #{('John', 78), ('Sam', 90), ('Ram', 85)}'''


'''a = [1,2,3]
b = list(map(lambda n:n**3,a))
print(a)
print(b)
print(list(zip(a,b)))'''

#[1, 2, 3]
#[1, 8, 27]
#[(1, 1), (2, 8), (3, 27)]

L1 = [1,2,3]
L2 = [4,5,6,7]

result = {k:v for k,v in zip(L1,L2)}    #this is same as print(dict(zip(L1,L2)))
print(result)
#{1: 4, 2: 5, 3: 6}



