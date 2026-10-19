#Given a non-decreasing array of integers, remove every value that appears more than once consecutively.
if __name__ == '__main__':
    n = int(input().strip())

    if n <= 0:
        print("ERROR")
    else:
        arr = list(map(int, input().rstrip().split()))
# Write your solution here
result=[]
i=0
l=len(arr)
while i<l:
    count=1
    
    while i<l-1 and arr[i]==arr[i+1]:
        count+=1
        i+=1
    if count==1:
        result.append(arr[i])
    i+=1
if len(result)==0:
        print("EMPTY")
else:
        for j in result:
            print(j,end=" ")
'''/0/https://www.hackerrank.com/rest/contests/week4-wednesday-challenge-1-rr-and-ec-campus-07-09-26-1790915778/testcases/603408testcaseinput'''
