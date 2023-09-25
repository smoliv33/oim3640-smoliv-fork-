def f(a, b, c=0):
    return a * 100 + b * 10 + c


# res = f(3, 4)
# print(res)

# res_2 = f(c=5, a=3, b=4)
# print(res_2)

# res_3 = f(3, c=4, b=6)
# print(res_3)


# print('hi', end=' ')
# print('hi')

# print('Hi', 'Larry')


def check():
    score = 95
    if score >= 60:
        print("Pass")
    elif score >= 90:
        print("A")
    else:
        print("Fail")

    return 'good'


# print(check())


def f():
    print('hi')

def f2():
    """return something"""
    return f()


res = f2()
print(res)
