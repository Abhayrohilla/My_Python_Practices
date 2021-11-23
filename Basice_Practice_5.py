#6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
a = (input("Enter went your number"))
list = a.split(",")
tuple = tuple(list)
print(list)
print(tuple)