# i = 0

# while i < 3:  # as long as this condition is True
#     print('Hi')
#     i += 1

# for i in range(3):
#     print('Hi')


# Calculate the sum of integers from 0 to 10


def sum_up(n):
    """return the sum of integers from 0 to n"""
    total = 0

    for i in range(n + 1):
        print(f'Iteration {i}:')
        print(f'  before adding {i}, the current total is {total}')
        total += i  # this is the only useful line
        print(f'  after adding {i}, the total becomes {total}')
        print()

    # print(total)
    return total


# print(sum_up(10))


# repeat asking user to enter their password until it is correct

while True:
    password = input('Enter your password: ')
    if password == '123456':
        print('Welcome!')
        break
    else:
        print('Wrong! Please enter again.')