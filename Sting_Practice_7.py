# 8. Write a Python function that takes a list of words and returns the longest word and the length of the longest one. Go to the editor
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9
largest_word = ["funnyboy", "soun", "abhyrohilla", "sony", "abhi", "python"]
a = []
for i in largest_word:
    a.append(len(i))
z = list(tuple(zip(a,largest_word)))
z.sort()
print("Longest word: ", str(z[-1][-1]))
print("Length of the longest word: ", str(max(a)))
