# Using a deep copy:
import copy
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

d = copy.deepcopy(c)

print(id(c) == id(d))        # False - d is now a new object
print(id(c[0]) == id(d[0]))    # False - d[0] is now a new object
print(id(c))
print(id(d))