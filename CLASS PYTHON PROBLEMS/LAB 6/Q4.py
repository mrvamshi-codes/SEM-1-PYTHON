'''Count the Frequency of Each Word in a Text File'''

with open("words.txt","w") as f:
    f.write("python is easy python is useful")

file_name=input("Enter the file name: ")

f = open(file_name, "r")
text = f.read()
f.close()

words = text.split()
frequency = {}

for word in words:  
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequency:")

for word in frequency:
    print(word , ":", frequency[word])


