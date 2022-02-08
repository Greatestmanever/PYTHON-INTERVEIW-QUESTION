# Write a sorting function without using the list.sort function

lis = [24, 55, 78, 64, 25, 12, 33, 22, 11, 1, 2, 44, 3, 122, 23, 34]
new_list = []

# Using while loop
while lis:
     # arbitrary number in list
    minimum = lis[0]
    # Using for loop
    for x in lis:
        if  x > minimum:
            minimum = x
    new_list.append(minimum)
    lis.remove(minimum)
print(new_list)
print(lis)