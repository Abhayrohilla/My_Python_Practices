# 8. Write a Python program to extract year, month, date and time using Lambda. Go to the editor
# Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178
import datetime
wv = lambda x: x
a = wv(datetime.datetime.now())
print(a)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(a))
print(month(a))
print(day(a))
print(t(a))