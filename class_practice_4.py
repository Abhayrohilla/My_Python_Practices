# 4. Write a Python class to get all possible unique subsets from a set of distinct integers. Go to the editor
# Input : [4, 5, 6]
# Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
a = []


# class Subset:
#     def
#
#
# b = Subset([4, 5, 6])
# b.set1()

# a = [4, 5, 6]
# n = len(a)
# b = []
# for i in range(n):
#     b.append([a[i]])
#     if [4] in b:
#         print([4],
# print(b)

class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))

    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]


print(py_solution().sub_sets([4, 5, 6]))