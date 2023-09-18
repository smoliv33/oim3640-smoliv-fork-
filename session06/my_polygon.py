import turtle

leo = turtle.Turtle()


def triangle(t, length):
    """ Draw a triangle with given side length"""
    for i in range(3):
        t.fd(length)
        t.lt(120)


triangle(leo, 200)

turtle.mainloop()
