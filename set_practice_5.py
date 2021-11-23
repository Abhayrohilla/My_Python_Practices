# 5. Write a Python program to remove an item from a set if it is present in the set.
Set = {1, 2, 3, 4, 5, 6, 87, 8, 9, 5, 4, 3, 9999999999999}
Set.discard(9999999999999)
print(Set)