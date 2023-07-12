# Write a Python program to check if a number is positive, negative or zero.
from typing import Tuple


def check_number_sign(number: int) -> str:
    if number > 0:
        return 'It is positive number'
    elif number < 0:
        return 'It is a negative number'
    else:
        return 'It is a zero number'


# Write a Python program to compute and print sum of two given integers (more than or equal to zero).
# If given integers or the sum have more than 80 digits, print "overflow".

def check_sum(number1, number2):
    if number1 >= 0 and number2 >= 0:
        if number1 + number2 > 10**80 or number1 > 10**80 or number2 > 10**80:
            return 'overflow'
        else:
            return number1 + number2
    else:
        pass
