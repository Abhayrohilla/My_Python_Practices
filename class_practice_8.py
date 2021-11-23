# 8. Write a Python class to reverse a string word by word. Go to the editor
# Input string : 'hello .py'
# Expected Output : '.py hello'
class Find_sting:
    def Hello(self, find_s):
        return f"{find_s[-3:]} {find_s[:5]}"

a = Find_sting()
print(a.Hello('hello .py'))