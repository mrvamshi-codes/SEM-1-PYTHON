'''matrix = [[1,2,3],[4,5,6]]

transpose = [[row[i] for row in matrix] for i in range(3)]
#transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
#gpt suggested to use this 2nd one but i did not get how it works

print(transpose)'''
#[[1, 4], [2, 5], [3, 6]]


'''matrix = [[10, 20], [30, 40], [50, 60]]

result = [[row[i] for row in matrix] for i in range(2)]
print(result)'''
#[[10,30,50],[20,40,60]]
