# 1. Write a Python class to convert an integer to a roman numeral.
class Num:
    def Num_R(self, b):
        a = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V",
             4: "IV", 1: "I"}
        return a.get(b, "MMMM")


a = Num()
print(a.Num_R(1))
print(a.Num_R(4000))
