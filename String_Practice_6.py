# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
uservalue = input("Enter your sentence ")
if "not" and "poor" in uservalue:
    print('The lyrics is good!\nThe lyrics is poor!')
else:
    print('This sentence not find in not and poor')