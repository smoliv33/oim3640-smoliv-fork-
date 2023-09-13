# import random


# print(random.random())

# print(random.randint(0, 9))


r1 = 20.23
r2 = 9
r3 = 13

# area_1 = 3.14159 * r1 * r1
# area_2 = 3.14159 * r2 * r2
# area_3 = 3.14159 * r3 * r3

# print(area_1, area_2, area_3)


def compute_area(radius):
    """
    Return the area of a circle with radius given.

    (This is a docstring, which is the description of this function)
    """
    # radius is the parameter variable, we should treat them as given inside of the function
    result = 3.14159 * radius * radius
    # print(result)  # print is like side effect
    # if the function does not explicitly return any value, it will return None as the default return value
    return result


area_1 = compute_area(r1)  # r1 is called arguments
area_2 = compute_area(
    r2
)  # this is how we call a function, and assign the returned value to a variable
area_3 = compute_area(r3)

# print(area_1 + area_2 + area_3)


# Create a function that returns the double of an input value


def get_double(x):
    """return the double of x"""
    return x * 2
    # print(x * 2)


# print(get_double(100))

# calculate the area of a circle with radius that is double of r1

# new_radius = get_double(r1)
# new_area = compute_area(new_radius)
# print(new_area)

print(compute_area(get_double(r1)))
