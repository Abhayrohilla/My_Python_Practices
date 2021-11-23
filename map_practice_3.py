# 3. Write a Python program to listify the list of given strings individually using Python map.
a = ['Red', 'Blue', 'Black', 'White', 'Pink']
b = list(map(lambda x:x, a))
print(b)
result = list(map(list, a))
print(result)