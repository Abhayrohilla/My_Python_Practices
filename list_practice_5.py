# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
Sample_List = ['abc', 'xyz', 'aba', '1221']
for i in Sample_List:
    if 3 < len(i):
        if i[0] == i[-1]:
            print(i[2])
