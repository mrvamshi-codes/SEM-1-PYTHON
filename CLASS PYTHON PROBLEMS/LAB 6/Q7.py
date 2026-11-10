#Find the Longest Word in a Text File

with open("story.txt","w") as file:
    file.write("Python programming develops logical thinking skills")

with open("story.txt","r") as file:
    content = file.read().split()

longest =""
for word in content:
    if len(word) > len(longest):
        longest = word

if len(content) > 0:
    print("The longest word in the file is:", longest)  
    print("The length of the longest word is:", len(longest))
else:
    print("The file is empty.")


