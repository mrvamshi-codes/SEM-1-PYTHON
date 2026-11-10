#write a program to count vowels in a string
n=input("enter the string:")
count=0
for ch in n.lower():
    if ch in "aeiou":
        count+=1
print("Number of vowels are:",count)
