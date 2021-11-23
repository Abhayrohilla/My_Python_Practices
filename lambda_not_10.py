# 10. Write a Python program to create Fibonacci series upto n using Lambda. Go to the editor
# Fibonacci series upto 2:
# [0, 1]
# Fibonacci series upto 5:
# [0, 1, 1, 2, 3]
# Fibonacci series upto 6:
# [0, 1, 1, 2, 3, 5]
# Fibonacci series upto 9:
# [0, 1, 1, 2, 3, 5, 8, 13, 21]
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = list(map(lambda x: x + x, a))
print(b)
