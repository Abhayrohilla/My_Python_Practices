# 7. Write a Python program to add two given lists and find the difference between lists. Use map() function.
def List(x, y):
    return x + y, x - y


x = [5, 7, 3, 73, 6, 3]
y = [5, 3, 6, 3, 37, 5]
r = list(map(List, x, y))
print(r)
