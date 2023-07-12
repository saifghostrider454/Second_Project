# Write a Python program to check if a number is positive, negative or zero.
from typing import Tuple


def check_number_sign(number: int) -> str:
    if number > 0:
        return 'It is positive number'
    elif number < 0:
        return 'It is a negative number'
    else:
        return 'It is a zero number'


def round(number: float) -> str:
    return ("{:.2f}".format(number))


print(round(22.5652))

n = 22.5685
n.__round__()
print(n)
