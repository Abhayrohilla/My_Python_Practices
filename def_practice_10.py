# 10. Write a Python program to print the even numbers from a given list. Go to the editor
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
Sample_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = []
def fun(x):
    for i in x:
        if i % 2 == 0:
            a.append(i)


fun(Sample_List)
print(a)
