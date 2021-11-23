# 3. Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid
class Check:
    def dict(self, *args):
        self.args = args
        c = []
        a = {'(': ')', '{': '}', '[': ']'}
        for i in a:
            if i in self.args:
                c.append(i, a[i])

b = Check()
print(b.dict("(){}[]"))
print(b.dict("){]"))

