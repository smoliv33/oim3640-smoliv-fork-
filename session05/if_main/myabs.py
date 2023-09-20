def my_abs(number):
    """
    Return the absolute value of a number

    number: an integer or a floating point number
    """
    if number < 0:
        return -number
    else:
        return number


def main():
    print(my_abs(-10))
    print(my_abs(-20))
    # print(__name__)


# To avoid executing this file when it is imported in another file
if __name__ == "__main__":
    main()
