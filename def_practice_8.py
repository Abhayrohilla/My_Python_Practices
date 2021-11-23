# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list. Go to the editor
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
Sample_List = [1, 2, 3, 3, 3, 3, 4, 5]
def fun(x):
    print(list(set(x)))
fun(Sample_List)

