# 5. Write a Python program that accepts a word from the user and reverse it.
word_list = input("Enter your word : ")
for i in range(len(word_list) - 1, -1, -1):
    print(word_list[i], end="")
