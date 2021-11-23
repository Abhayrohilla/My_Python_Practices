# 6. Write a Python program to convert "all" the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence. Use map() function.

def Uppercase(a):
    return str(a).upper(), str(a).lower()


a = {"q", "w", "e", "r", "t", "y", "u", "i", "g"}
b = set(map(Uppercase, a))
print(b)
