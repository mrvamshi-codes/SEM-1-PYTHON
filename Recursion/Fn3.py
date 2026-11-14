#Write a Python function that accepts an amount in USD and converts it into INR.

def converter1(USD):     #did not use the parameter in the starting
    INR = USD*94.24 
    return INR 

print(converter1(999))




#Write a Python function that accepts an amount in INR and converts it into USD.

def converter2(INR):
    USD = INR*0.01061
    return USD

print(converter2(94145.76))