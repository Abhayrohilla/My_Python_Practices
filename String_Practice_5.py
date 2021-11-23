# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Go to the editor
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

uservalue = input("Enter your letter: ")
a = len(uservalue)
if 3<=a:
    print(f"{uservalue}" + "ing")
elif "ing" in uservalue:
    print(f"{uservalue}" + "ly")
else:
    print(f"{uservalue} " + "leave it unchanged")
