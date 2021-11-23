# 5. Write a Python program to filter a list of integers using Lambda. Go to the editor
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]
m = []
for q in range(1, 1000):
    m.append(q)
result = list(filter(lambda x: x % 2 == 0, m))
print(f"Even numbers from the said list:\n{result}")
a = []
for j in m:
    result1 = list(filter(lambda x: j % x == 0, m))
    a.append(result1)
c = []
for k in a:
    if len(k) == 2:
        c.append(k)
p = []
for l in c:
    p.append(l[-1])
print(f"Odd numbers from the said list:\n{p}")