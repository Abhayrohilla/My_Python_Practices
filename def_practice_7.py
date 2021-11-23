# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
Sample_String = 'The quick Brow Fox'
a = []
b = []


def fun(x):
    for i in x:
        for j in i:
            if j.isupper():
                a.append(j)
            elif j.isspace():
                pass
            else:
                b.append(j)


fun(Sample_String)
print("No. of Upper case characters :", len(a))
print("No. of Lower case Characters :", len(b))
