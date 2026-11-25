#Given a 2D matrix and an integer multiplier, 
#use map() to multiply every element in the matrix by the multiplier.

matrix = [[1, 2], [3, 4]]
multiplier = 10

def multiply_row(row):
    return list(map(lambda x:x*multiplier,row))

result = list(map(multiply_row,matrix))
print(result)

#output -- [[10, 20], [30, 40]]