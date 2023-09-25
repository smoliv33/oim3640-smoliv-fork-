def f(a, b, c=0):
    return a * 100 + b*10 + c


# result = f(3, 4, 5)
# print(result)

# result_2 = f(a=3, b=4)
# print(result_2)

# result_3 = f(c=4, b=3)
# print(result_3)


# print('hi', 'Hardik', sep='###')

score = 95


def check(score):
    if score >= 60:
        return 'hi'
        print("Pass")
    elif score >= 90:
        print("A")
    else:
        print("Fail")

# print(check(90))

def f1(a, b):
    print(a * b)

def f2():
    a = int(input('Enter: '))
    b = int(input('Enter: '))
    return f1(a, b)

# result = f2()
# print(result)


score =90
if score >= 60:
    print("Pass")

    
if score >= 90:
    print("A")
else:
    print("Fail")