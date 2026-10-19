#check if a given number is even or odd until the user says stop
while True:
    val=input("Enter a number or stop:")
    if val=="stop":
        break
    num=int(val)
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")
