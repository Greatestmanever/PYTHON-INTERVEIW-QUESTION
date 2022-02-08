# Write a Python program to print a list in reverse

lis = [24, 55, 78, 64, 25, 12, 33, 22, 11, 1, 2, 44, 3, 122, 23, 34]

lis.reverse()
print(lis)

# Alternatively

def reverse(li):
    # Using splice method
    return li[::-1]

reverse(lis)