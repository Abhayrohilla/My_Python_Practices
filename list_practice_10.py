# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
largest_word = ["funnyboy", "soun", "abhyrohilla", "sony", "abhi", "python"]
a = []
for i in largest_word:
    a.append(len(i))
z = list(tuple(zip(a,largest_word)))
z.sort()
print(z[-1][-1])
