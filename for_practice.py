# Write a Python program to check if a number is positive, negative or zero.
from typing import Tuple

# def check_number_sign(number: int) -> str:
#     if number > 0:
#         return 'It is positive number'
#     elif number < 0:
#         return 'It is a negative number'
#     else:
#         return 'It is a zero number'
#
#
# # Write a Python program to compute and print sum of two given integers (more than or equal to zero).
# # If given integers or the sum have more than 80 digits, print "overflow".
#
# def check_sum(number1, number2):
#     if number1 >= 0 and number2 >= 0:
#         if number1 + number2 > 10**80 or number1 > 10**80 or number2 > 10**80:
#             return 'overflow'
#         else:
#             return number1 + number2
#     else:
#         pass


# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements

# Input:
# ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#
# Output:
# ['Green', 'White', 'Black']


# Numbers below threshold
# Easy
# Write a Python program to find the indexes of numbers of a given list below a given threshold.
#
# Example 1:
# Input:
# [0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
#
# 100
#
# Output:
# [0, 1, 2, 3, 7, 8, 9, 10]

# lst = eval(input())
#
# n = int(input())
# lst1 = []
# for index, value in enumerate(lst):
#     if value < n:
#         lst1.append(index)
#
# print(lst1)


"""Write a Python program to remove None value from a given list. (Using list comprehension)

Example 1:
Input:
[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

Output:
[12, 0, 23, -55, 234, 89, 0, 6, -12]"""

# lst = eval(input())
#
# lst = [int(x) for x in lst if x is not None]
#
# print(lst)


# lst = eval(input())
#
# lst1 = []
#
# for index, value in enumerate(lst):
#     if value is None:
#         lst1.append(index)
#
# print(lst1)


"""
Remove specific word
Easy
Write a Python program to remove specific words from a given list. (Using List comprehension)

Example 1:
Input:
['red', 'green', 'blue', 'white', 'black', 'orange']

['white', 'orange']

Output:
['red', 'green', 'blue', 'black']
"""

# lst = eval(input())
# lst1 = eval(input())
#
# lst = [x for x in lst if x not in lst1]
#
# print(lst)


# x_1, y_1 = int(input()), int(input())
#
# x_2, y_2 = int(input()), int(input())
#
# number = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5
#
# print("The Euclidean Distance between the above given two points 'PQ'=" + str(number))


# str1 = input()
# ch = input()
#
# str1 = str1.replace(ch, ' ')
#
# print(str1)


# str1 = input()
# sub = input()
#
# print(f"Last occurrence of Emma starts at index {str1.rindex(sub)}")


# a = int(input())
# b = int(input())
#
#
# print(f"value of a is : {a}")
#
# print(f"value of b is : {b}")
#
# a = a + b
# b = a - b
# a = a - b
#
# print(f"value of a is : {a}")
#
# print(f"value of b is : {b}")


"""
Write a python program to check a given number is perfect or not.

Note: A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.

Lets understand it with example

6 is a positive number and its divisor is 1,2,3 and 6 itself.

But we should not include 6 as by the definition of perfect number.

Lets add its divisor excluding itself

1+2+3 = 6 which is equal to number itself.

It means 6 is a Perfect Number.

Example 1:
Input:
28

Output:
It is Perfect Number

Example 2:
Input:
1256488

Output:
It is not Perfect Number
"""

# num = int(input())
#
# emp = []
#
# for i in range(1, num+1):
#     if i != num:
#         if num % i == 0:
#             emp.append(i)
#         else:
#             continue
#
#
# if sum(emp) == num:
#     print("It is Perfect Number")
# else:
#     print("It is not Perfect Number")
#
# print(emp)


test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
d = [set()]


def connect(data):
    n = len(data)
    position = 0
    while position < n - 1:
        if data[position][0] == data[position + 1][0]:
            d[0].update((data[position] + data[position + 1]))
            position += 1
        elif data[position][0] != data[position + 1][0]:
            #     d.insert(1, (data[position]))
            return 1


connect(test_list)
print(d)
