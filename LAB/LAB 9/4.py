#Write a function count_occurrences(lst, item) to count the frequency
#of a target integer in a user-entered list without using .count().

def count_occurences(lst,item):
    count = 0
    for i in lst:
        if i==item:
            count+=1
    return count


#Main program
L = list(map(int,input("enter the numbers:").split()))

item_to_search = int(input("enter the element to search for:"))

print(count_occurences(L,item_to_search))

#output 
#enter the numbers:10 20 10 30 10 40 20 10 50 60
#enter the element to search for:10
#4       