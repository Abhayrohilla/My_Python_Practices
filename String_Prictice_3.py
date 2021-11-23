# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
# Sample String : 'restart'
# Expected Result : 'resta$t'



Sample_String = 'restart'
# a = Sample_String[0]
# c = Sample_String[1:].replace('r', '$')
# print(Sample_String[0]+ Sample_String[1:].replace('r', '$'))
# print(x)
# c[0]='r'
# print(c)
# c = a + Sample_String[1:]
# print(Sample_String[1:])

a= 5
a=7
print(a)
str1 = 'restart'
print(str1)
char = str1[0]

str1 = str1.replace(char, '$')
print(str1)
str1 = char + str1[1:]

print(str1)
