r1 = 20
r2 = 9
r3 = 13

# area_1 = 3.14159 * r1 * r1
# area_2 = 3.14159 * r2 * r2
# area_3 = 3.14159 * r3 * r3

# print(area_1, area_2, area_3)

# radius is parameter variable
def compute_area(radius):
    """
    (docstring, which is the description of this function)

    return the area of a circle with a given radius
    """
    pi = 3.14159
    area = pi * radius ** 2 
    # print(area) # just a side effect
    # if the function does not explicitly return value(s), it will return None
    return area

# area_1 = compute_area() 
area_1 = compute_area(r1) # r1 is called arguments
# print(pi)

area_2 = compute_area(r2)
area_3 = compute_area(r3)
print(f'Area of circle with radius {r1} is {area_1}.')

print(f'The sum is {area_1 + area_2 + area_3}.')



# Define a function that returns the double of any given number
# Then call the function

def get_double(x):
    """
    Return the double of given x
    """
    return x * 2

print(get_double(10))

# Calcuate the area of the circle with double of a given number 3

# new_radius = get_double(3)
# new_area = compute_area(new_radius)
# print(new_area)

print(compute_area(get_double(3)))