# i = 0
# # n = int(input("Enter: "))

# while i < 3: # as long as this is True
#     print('Hi')
#     i += 1


# for i in range(3):
#     print('Hi')

# Calculate the sum of all the integers from 0 to 10


def sum_up(n):
    total = 0

    for i in range(n + 1):
        print(f'Iteration {i}:')
        print(f'  before adding {i}, the current total is {total}')
        total += i  # The only useful line here
        print(f'  after adding {i}, the total becomes {total}')
        print()

    print(total)


# sum_up(10)


def sum_up_while(n):
    total = 0
    i = 0

    while i < n + 1:
        total += i
        i += 1

    print(total)


# sum_up_while(10)



while True:
    password = input('Please enter password: ')
    if password == '123456':
        print('Welcome!')
        break
    else:
        print('Try one more time!')