#Take a input string from the user and display the unique words in it line by line
Str1='python is easy and python is useful and easy to learn'
S=set(Str1.split())  #have to include .split() to get unique words or else will get unique characters
print("Unique words are:",S)
