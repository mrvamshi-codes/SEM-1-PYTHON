#1
'''def outer(msg):
    def inner():
        print(msg)
    return inner

a = outer("this is the first program of closure fucntion")
a()'''

#2
'''def f1():
    def f2():
        print("Hello")
        print("World")
    print("f2=",id(f2))
    return f2

c = f1()
c()
print(id(c))'''


#5
def outer(n):
    text = n**2         #text is having the scope of outer function
    def inner():
        print(text)    #calling the non-local variable text
    return inner 

func = outer(5)
func()