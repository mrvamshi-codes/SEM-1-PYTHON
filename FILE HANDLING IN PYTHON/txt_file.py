#this is used for .txt files only

#file handling using command line arguments

#addition of two numbers

'''import sys
print(sys.argv[1],sys.argv[2])
x=int(sys.argv[1])
y=int(sys.argv[2])
print("sum=",x+y)'''


#to work with larger amount of data we need a file as there will be less errors.


'''Files
1)binary.      2)text. ''' 





#opening a file

'''f1=open("t1.txt","r") # .txt and .py resides in the path
print(f1)

#readline() -- reads one line in a file

f1=open("t1.txt","r")
hi=f1.readline()
hi.strip()
print(hi,end=' ')


#read() -- reads entire file

f1=open("t1.txt","r")
hi=f1.read()
hi.strip()
print(hi)

 #readlines -- reads everything but just splits it into a list

f1=open("t1.txt","r")
hi=f1.readlines()
print(hi)'''


#write to a file
'''f1=open("t1.txt","w")
print("hello world",file=f1)
f1.close()'''

#another method for the same
#professional way to write a file

with open("t1.txt","w") as f1:
	print("HELLO WORLD",file=f1)

#this is used because no close line is needed; as python does it.
