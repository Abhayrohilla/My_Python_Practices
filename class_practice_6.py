# 6. Write a Python class to find the three elements that sum to zero from a set of n real numbers. Go to the editor
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]
a = [-25, -10, -7, 10, 2, 4, 8, -3]
a.sort()
n = len(a)
for i in range(n):
    if 10 + (a[i]+a[i]) == 0:
        print([a[i], a[i+1], 10])
        break

print(a)





        
