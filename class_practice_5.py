# 5. Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number. Go to the editor
# Input: numbers= [10,20,10,40,50,60,70], target=50
# Output: 3, 4
class Target:
    def find_index(self, add_no):
        n = len(add_no)
        for i in range(n):
            if add_no[i] + add_no[i + 1] == 50:
                print("Index1=", i + 1, "Index=", i + 2)
                break


j = Target()
j.find_index([10, 20, 10, 40, 50, 60, 70])
