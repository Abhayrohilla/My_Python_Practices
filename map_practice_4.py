# 4. Write a Python program to create a "list" containing the power of said number in bases raised to the corresponding number in the index using Python map.
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = list(map(lambda x, y: x ** y, a, b))
print(c)
