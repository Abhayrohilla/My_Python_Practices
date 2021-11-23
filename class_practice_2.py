# 2. Write a Python class to convert a roman numeral to an integer.
class Num:
    def Num_R(self, b):
        a = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5,
             "IV": 4, "I": 1}
        return a.setdefault(b, "MMM")


a = Num()
print(a.Num_R('M'))
print(a.Num_R('I'))
