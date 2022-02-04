#Using for loop
# for i in range(10, 21):
#     print (i)

#Using while loop
# i = 10
# while i <= 20:
#     print (i)
#     i += 1

#Using if statement
# a = 10
# i = 5
# if i > a:
#     print (i)
# else:
#     print ("There is error in your code!")
#     print ("Look carefully and debug it..")

#Using if statement
# a = 30
# b = 20
# if a < b:
#     print ("{} is less than {}".format(a, b))
# elif a == 20:
#     print ("{} is equal to {}".format(a, b))
# else:
#     print ("{} is greater than {}".format(a, b))

# Fiz Buzz
# for num in range(1, 30):
#     if num % 5 ==0 and num % 3 == 0:
#         print("FizzBuzz")
#     elif num % 3 ==0:
#         print("Fizz")
#     else:
#         print("Buzz")

# Fibonnacci Seq
# a, b = 0, 1
# for i in range(0, 10):
#     print (a)
#     a, b = b, a + b

# #Lists
# my_list = [10, 20, 30, 40, 50]
# for i in my_list:
#     print (i)

# #Tuples
# my_tup = [10, 20, 30, 40, 50]
# for s in my_tup:
#     print (s)

# #Dict
# my_dict = {'name': 'Spirit', 'age': '22', 'occupation': "Python Developer"}
# for key,val in my_dict:
#     print ("My {} is {}".format(key,val))

# #Set
# my_set = [10, 20, 30, 40, 50]
# for b in my_set:
#     print (b)

#List Comprehension
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Give me each number in a list squared
# squares = [num*num for num in my_list]
# print (squares)

# Fibonacci Generator
# def fib(num):
#     a,b = 0,1
#     for i in range(0, num):
#         yield "{}: {}".format(i+1, a)
#         a, b = b, a + b

# for item in fib(10):
#     print (item)

def high_and_low(numbers):
    numbers = ["1 2 3 4 5"]
    #    split numbers based on space     v
    numbers = [int(x) for x in numbers.split()]
    #           ^ type-cast each element to `int`
    print (max(numbers), min(numbers))