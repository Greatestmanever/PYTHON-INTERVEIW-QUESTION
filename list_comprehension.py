first = [1, 2, 3, 4, 5, 6, 7]

even_first = [ x for x in first if x % 2 == 0] # even numbers
print(even_first)

square_first = [ x ** 2 for x in first] # squared numbers
print(square_first)