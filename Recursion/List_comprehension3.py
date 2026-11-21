'''numbers = [2, 5, 10, 12, 15, 20]

result = [n for n in numbers if n%2==0 if n>10]
print(result)'''
#[12, 20]


'''L1 = [n for n in range(100) if n%2==0 if n%5==0]
print(L1)'''
#[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

#SYNTAX  ---  [n for n in numbers if condition1 if condition2]


'''numbers = [12, 36, 45, 60, 78, 96, 123, 6]
result = [n for n in numbers if '6' in str(n)]
print(result)'''
#[36, 60, 96, 6]

#I used str(n) in '6' so the output was [6] then corrected it 




sentence = "Python is a powerful language"

#1. 
'''result = [ch for ch in sentence if ch == " "]
print(len(result))'''
#output -- 4

#2. 
'''result = [ch for ch in sentence if ch.lower() not in 'aeiou']
print('' .join(result))'''

# join() combines list elements into a string.
# ''.join(result) joins characters without adding extra spaces.



#example
'''letters = ['P', 'y', 't', 'h', 'n']
print(''.join(letters))   # Pythn
print('-'.join(letters))  # P-y-t-h-n'''