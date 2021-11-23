class Formula:
    def __init__(self, length, width, height, base):
        self.length = length
        self.width = width
        self.base = base
        self.height = height
    def Square(self):
        return self.length*self.length
    def Rectangle(self):
        return self.length*self.width
    def Triangle(self):
        return self.base*self.height/2

class Fun(Formula):
    def __init__(self, length, width, height, base):
        super().__init__(length, width, height, base)
a = Fun(1,2,3,4)
print(a.Rectangle())