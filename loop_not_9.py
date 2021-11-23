# 9. Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34
b = []
for i in range(22):
    b.append(i)
print(b)
d = []
c = 0
for j in range(len(b)):
    print(b[c] + b[j], end=" ")
    if j == 1:
        c += 1
        j += 1
