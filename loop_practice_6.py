# 6. Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4
a = []
b = []
for i in range(1, 10):
    if i % 2 == 0:
        a.append(i)
    else:
        b.append(i)
print("Number of even numbers :", len(b))
print("Number of odd numbers :", len(a))
