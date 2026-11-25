#Write a function is_palindrome(s) to check whether a user-entered string is a palindrome, 
#ignoring case, and display the result.



def is_palindrome(s):
    s = s.lower().replace(" ","")
    return s == s[::-1]



#Main program
text = input("enter:")
if is_palindrome(text):
    print(f'"{text}" is a palindrome')
else:
    print(f'"{text}" is not a palindrome')