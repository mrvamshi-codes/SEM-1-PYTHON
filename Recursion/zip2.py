areas = [3.14159, 12.56637, 28.27433, 50.26548, 78.53982]
new_lst = []

def rounding(lst):
    for i in range(0,len(lst)):
        a = round(lst[i],i+1)         #mainly did not get the logic of i+1
        new_lst.append(a)
    print(new_lst)


rounding(areas)

#output -- [3.1, 12.57, 28.274, 50.2655, 78.53982]