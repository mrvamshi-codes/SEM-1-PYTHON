#Write a recursive function to print all elements of a list, using the list and index as parameters.

def print_elements(list,index):
    
    if index==len(list):
        return
    print(list[index],end =" ")    #did not print the element before increasing the index
    return print_elements(list,index+1)

numbers=[1,2,3,4,5]
print_elements(numbers,0)        #did not use 0 for index rather used 4 as index 
print()                          #if i had used 2 as index then my output will be 3 4 5


    