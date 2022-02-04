# How to merge two dictionaries
# in python 3.5+
x = {"a": 1, "b": 2}
y = {"b": 3, "c": 4}

z = {**x, **y}

z

# In python 2.x you could
# use this:
z = dict(x, **y)
z
# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting 
# duplicates from left to right.
