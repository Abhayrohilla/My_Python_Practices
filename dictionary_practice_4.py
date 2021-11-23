# 4. Write a Python script to check whether a given key already exists in a dictionary.
a = {7: "abhay", 9: "sonu", 1: "sonuy", 6: "python", 2: "deepak"}
def fun(x):
    if x in a:
        print("This key is exist in dictionary")
    else:
        print("This key not exist in dictionary")
fun(6)
fun(0)