# 4. Write a Python program to construct the following pattern, using a nested for loop.
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(6):
    print("* " * i)
    if 5 == i:
        for j in range(i-1, 0, -1):
            print("* " * j)


