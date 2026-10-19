#to count words in a sentence
n=input("enter the sentence:")
count=0
ch=n
while ch in n.split():
        count+=1
print(count)
