my_list = [4, 7, 0, 3]
my_iter = iter(my_list)
# iterate through it using next()
print(next(my_iter))
print(next(my_iter))
# next(obj) is same as obj.__next__()
print(my_iter.__next__())
print(my_iter.__next__())
# This will raise error, no items left

