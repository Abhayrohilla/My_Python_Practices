# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. Go to the editor
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
print('w3resource')
Sample_String = input('enter your word')
if 10 == len(Sample_String):
    print(Sample_String[:2]+Sample_String[8:10])
elif 2 == len(Sample_String):
    print(Sample_String[:2]+Sample_String[:2])
else:
    print("Empty String")
