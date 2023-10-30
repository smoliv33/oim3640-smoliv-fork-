while True:
    try:
        number = input('Enter a number: ')
        number = int(number)
        result = 2023 / number
        print(result)
        break
    except ValueError as e:
        print('You should enter an integer!')
        print(e)
    except ZeroDivisionError:
        print('You just entered 0.')


print('Hello, world!')  # I want to print this no matter what
