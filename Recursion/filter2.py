#use filter function to filter vowels from list of characters

def filtering(char):
    return char.lower() in 'aeiou'


#OR


'''def filtering(lst):
    for item in lst:
        if item.lower() in 'aeiou':
            return item'''

characters = ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd', 'A', 'i', 'U']
vowels = list(filter(filtering,characters))

print(vowels,type(vowels))

