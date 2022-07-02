from player import logo
import math
from extra import Calculator

cal = Calculator()
print(logo)


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multi(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def exp(n1, n2):
    return n1 ** n2


def factorial(n1):
    return math.factorial(n1)


operator_dict = {
    '+': add,
    '-': sub,
    '*': multi,
    '/': div,
    'pow': exp,
    '!': factorial
}
cal.first_cal(operator_dict)
