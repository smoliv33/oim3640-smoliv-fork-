# age = 20
# if age >= 6:
#     print('teenager')
# elif age >= 18:
#     print('adult')
# else:
#     print('kid')


# def recursion():
#     print('Do you mean "recursion"?')
#     import time
#     time.sleep(0.5)
#     recursion()


# recursion()
import time


def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n, end='\r')
        time.sleep(1)
        countdown(n - 1)

countdown(5)
