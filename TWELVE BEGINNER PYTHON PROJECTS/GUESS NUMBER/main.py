# import random

# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'Guess a number between 1 and {x}: '))
#         if guess < random_number:
#             print('Sorry, guess again. Too low.')
#         elif guess > random_number:
#             print('Sorry, guess again. Too high.')

#     print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

#     def computer_guess(x):
#         low = 1
#         high = x
#         feedback = ''
#         while feedback != 'c': 
#             if low != high:
#                 guess = random.randint(low, high)
#             else:
#                 guess = low # could also be high b/c low = high

#             feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ')
#             if feedback == 'h':
#                 high = guess - 1
#             elif feedback == 'l':
#                 low = guess + 1

#         print(f'Yay! The computer guessed your number, {guess}, corrctly!')
            



# guess(10)



# To tell python where to stop use break
# from itertools import count, cycle, repeat

# for i in count(10):
#     print(i)
#     if i == 20:
#         break


# Using repeat function
# from itertools import repeat
# a = [1, 2, 3]
#  # 5  reps the no of repititions it would make.
# for i in repeat(1, 5):
#     print(i)

# To get the size of the objects in bytes.
import sys
# Generator expressions
mygenerator = (i for i in range(10) if i  % 2 ==0)
print(sys.getsizeof(mygenerator))

# list comprehension
mylist = [i for i in range(10) if i % 2 == 0]
print(sys.getsizeof(mylist))