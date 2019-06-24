def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def square(x, y):
    return x ** y


def square_root(x):
    if x >= 0:
        return x**(.5)
    else:
        return "ValueError: negative number cannot be raised to a fractional power."
