class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def solve(self):
        return f"Area of rectangle:- {length*breadth}"

length = int(input("Enter your rectangle length:-"))
breadth = int(input("Enter your rectangle breadth:-"))
re_sol = Rectangle(length, breadth)
print(re_sol.solve())
