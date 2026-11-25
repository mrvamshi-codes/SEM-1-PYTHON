# Given a list of strings, use map() to return a list of Boolean
# values indicating whether each string is a palindrome, ignoring case.

lst = ["Racecar", "hello", "Level"]

a = list(map(lambda s: s.lower() == s[::-1].lower(),lst )) 
 # == operator itself gives true or false,
 #hence no need to mention it using if-else statement  

print(a)

#output --[True, False, True]