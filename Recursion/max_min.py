#1

'''numbers = [10, 25, 15, 40, 5]

print(max(numbers))  # 40
print(min(numbers))  # 5'''

#2 
'''words = ["apple","banana","orange"]
print(max(words,key = len)) '''   #banana
#Here, Python compares the lengths of the words instead of comparing them alphabetically.

#3

numbers = []

print(max(numbers, default=0))  # 0   it's fallback
#Python returns the default value 0 instead of raising an error.
#also if the iterable have some elements then the default does'nt work

#4
'''words = ["apple", "zebra", "banana"]

print(max(words))            #zebra
print(max(words, key=len))'''   #banana


# max(words)          -> Returns the alphabetically largest word.
#                        Output: zebra

# max(words, key=len) -> Returns the word with the greatest length.
#                        Output: banana

# min(words)          -> Returns the alphabetically smallest word.
#                        Output: apple

# min(words, key=len) -> Returns the word with the shortest length.
#                        Output: apple
