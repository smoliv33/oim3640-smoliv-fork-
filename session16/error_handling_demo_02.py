while True:
    try:
        number = int(input('Enter a number:'))
        result = 2023 / number
        print(result)
        break
    except ValueError as e:
        print('You should enter an integer!')
        print(e)
    except ZeroDivisionError:
        print('You just entered 0!')
    except:
        print("I don't know what's wrong. ")
    finally:
        print('No matter what happens, we will get here finnaly.')

print('Hello, world!') # I still want to print this no matter what