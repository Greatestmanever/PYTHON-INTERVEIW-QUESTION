# Write a Python program to print Fibonacci Series

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

for i in range(0,10):
    print(F(i))
