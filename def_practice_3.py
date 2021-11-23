# 3. Write a Python function to multiply all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
Sample_List = (8, 2, 3, -1, 7)


def fun(x):
    a = 1
    for i in x:
        a *= i
    print(a)


fun(Sample_List)
