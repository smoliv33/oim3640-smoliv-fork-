import math

# print(math.pi)
# print(math.e)
# print(math.log(10))

import random

# print('I\'m \"ok\".') 
# print('\\\t\\')
# print(r'\\\t\\')


"""
This is another way to write large block of comments
"""

def my_add(a, b):
    """
    Return the sum of two values. (docstring)
    """
    return a + b


# print(my_add(5, 4))


# name = input('Please enter your name: ')
# password = input('Please enter your password: ')

# if name == 'admin' or password == 'admin':
#     print('Hi, welcome!')
# else:
#     print('Get out of here, hacker!')


age = int(input('How old are you? '))
# print(age, type(age))
# age = int(age)

if age >= 21:
    print('Yes, you can.')
else:
    print('Sorry.')