# 9. Write a Python program to create a new list taking specific elements from a tuple and convert a string value to integer.

Student_data = [('Alberto Franco', '15/05/2002', '35kg'), ('Gino Mcneill', '17/05/2002', '37kg'),
                ('Ryan Parkes', '16/02/1999', '39kg'), ('Eesha Hinton', '25/09/1998', '35kg')]

a = list(map(lambda x: x[0], Student_data))
b = list(map(lambda x: x[1], Student_data))
c = list(map(lambda x: x[2], Student_data))
print(a)
print(b)
print(c)
