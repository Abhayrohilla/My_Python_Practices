# 8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.

a = [1, 2, 3, 4]
b = (0, 1, 2, 3)
c = list(map(lambda x: str(x), a))
d = tuple(map(lambda x: str(x), b))
print(c)
print(d)
