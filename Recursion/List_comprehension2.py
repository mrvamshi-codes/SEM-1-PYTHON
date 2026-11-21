'''a = [1, 2, 3]
b = [2, 3, 4]

result = [x*y for x in a for y in b if x*y>6]
print(result)'''
#[8, 9, 12]

'''numbers = [1, 2, 3, 4, 5, 6]

result = [n**2 if n%2==0 else n for n in numbers]

print(result)'''
#[1, 4, 3, 16, 5, 36]


words = ["Python", "AI", "Programming", "Code", "ML"]

result = [len(n) for n in words if len(n)>4]
print(result)
#[6, 11]

# 1. FILTERING (if only)
# Syntax: [expression for variable in iterable if condition]
# The 'if' comes AFTER the for loop.
# Used to select only elements satisfying a condition.


# 2. CONDITIONAL TRANSFORMATION (if-else)
# Syntax: [expression_if_true if condition else expression_if_false for variable in iterable]
# The 'if-else' comes BEFORE the for loop.
# Used to modify elements based on a condition.
