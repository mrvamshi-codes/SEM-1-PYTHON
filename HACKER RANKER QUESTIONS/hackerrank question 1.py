#hackerrank question 1
if __name__ == '__main__':
    try:
        s = input()
    except EOFError:
        s = ""

    # Write your code here
result=list(s)
i=0
l=len(result)
found=false
while i<l-1:
    a=result[i]
    b=result[i+1]
    
    if a==b:
       found=True
       break
       
    i+=1
if found:
    print("YES")
else:
    print("NO")
