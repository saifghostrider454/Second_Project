# import random
# random_list = []
#
# randoms = random.randint(10, 200)
#
# for number in range(20):
#     randoms = random.randint(10, 200)
#     random_list.append(randoms)
#
#
# print(random_list)


# my_list = [1, 2, 3, 4]
# a=[]
# for i in my_list:
#     if i == 1:
#       continue
#     if i == 4:
#       break
#     a.append(i)
# print(a).


# my_tuple = (1, 2, 3, 4)
# for i in range(len(my_tuple)):
#     print(my_tuple[i])


# my_tuple = (1, 2, 3, 4)
# for i in my_tuple:
#    if i == 3:
#      break
#    print(i)


"""
A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime
number. 2, 3, 5, 7 etc. are prime numbers as they do not have any other factors. But 6 is not prime (it is composite)
since, 2 x 3 = 6
"""
import random

# num = input()

string = "The quick brown fox jumps over the lazy dog."


# string = string.split(" ")
#
# for num in string:
#     if len(num) > 1:
#         if len(num) % 2 != 0 and len(num) % len(num) == 0:
#             print(num, end=" ")


# para = "( ()) ((()()())) (()) ()"
#
# new_para = para.strip()
#
# print(new_para)
#


# n = int(input())
#
# emp_lst = []
# for i in range(0, n):
#     emp_lst.append(i)
#
# print(emp_lst)


# def is_leap(year):
#     leap = False
#
#     # Write your logic here
#     if year % 4 == 0:
#         if year % 100 != 0 or year % 400 == 0:
#             leap = True
#
#     return leap
#
#
# year = int(input())
# print(is_leap(year))


# a = input()
# b = input()
#
# try:
#     int(a) / int(b)
# except ZeroDivisionError as e:
#     print("Error Code:", e)
# except ValueError as e:
#     print("Error Code:", e)
# except Exception as e:
#     print("Error Code:", e)


# a = 5
# b = [2, 3, 6, 6, 5, 7]
#
#
# c = max(b)
# for i in range(b.count(c)):
#     if c in b:
#         b.remove(c)
#
#
# d = sorted(b)
#
# print(d[-1])


# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#
#     arr = list(arr)
#     c = max(arr)
#     for i in range(arr.count(c)):
#         if c in arr:
#             arr.remove(c)
#
#     d = sorted(arr)
#
#     print(d[-1])

# user_number_A = int(input("Enter a Number: "))
# user_number_B = int(input("Enter a Number: "))
#
#
# system = random.randint(user_number_A, user_number_B)
#
# user_count = True
#
# while user_count:
#     user_guess = int(input("Guess The number: "))
#     if user_guess == system:
#         print("You Guessed it right")
#         user_count = False
#     else:
#         print("Try Again")


# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#
#     lst = student_marks[query_name]
#     print('{:.2f}'.format(sum(lst) / len(lst)))
#
#
# def add(number):
#     """
#     :param number: 4, 5, 6 or 4, 2, -3
#     :return: 15 or 3
#     """
#     arr = map(int, number.split(", "))
#     return sum(arr)
#
#
# user_input = input("Enter Here: ")
# print(add(user_input))


# if __name__ == '__main__':
#     N = int(input())
#     arr = []
#
#     arr.index(N, 0)
#     print(arr)
#
#     arr.remove(N)
#
#     arr.append(N)
#
#     arr.sort()


# Write code here
# ask_value_x = int(input("Enter X Value: "))
# ask_value_y = int(input("Enter Y Value: "))
# ask_value_operator = input("Enter Operator (+, -, *, or /): ")
#
#
# def calculator(number_x: int, number_y: int, operation: str) -> int or float:
#     try:
#         if operation == '+':
#             return number_x + number_y
#         elif operation == '-':
#             return number_x - number_y
#         elif operation == '*':
#             return number_x * number_y
#         elif operation == '/':
#             return number_x / number_y
#         else:
#             print('Invalid Operator')
#     except Exception as error:
#         print(error)
#
#
# print(calculator(ask_value_x, ask_value_y, ask_value_operator))


# import random


# Generate a random number between 1 and 100


# Write code here
#
# def guessing_game() -> int or float:
#     system_guess = random.randint(1, 100)
#     user_guess = int(input("Guess the number: "))
#     user_count = False
#     while not user_count:
#         if user_guess == system_guess:
#             print("You Guessed it right")
#             user_count = True
#         elif user_guess > system_guess:
#             print("Hint: Your Guess is higher than guessing value")
#             user_guess = int(input("Guess the number again: "))
#         elif user_guess < system_guess:
#             print("Hint: Your Guess is lesser than guessing value")
#             user_guess = int(input("Guess the number again: "))
#
#
# guessing_game()


# emp_list = []
#
# counter = 0
# for number in range(100, 151):
#     number = str(number)
#     emp_list.append(number)
#
# for digits in emp_list:
#     for digit in digits:
#         if digit == '5':
#             counter += 1
# print(counter)


# a = input()
# b = input()
#
# print(f"{b[0:2]}{a[2:]} {a[0:2]}{b[2:]}")


# lst = eval(input())
# n = int(input())
#
# print(lst[0::2])


# set1 = set(input().split(' '))
# set2 = set(input().split(' '))
#
# print(set1.intersection(set2))

def bottle(size=5, color='red'):
    return f"{size}: {color}"


def appropriate_dictionary(words):
    dicts = {}
    for word in words:
        dicts[word] = words.count(word)

    return dicts


# print(appropriate_dictionary('hello world'))


def list_of_even_numbers(numbers: list) -> list:
    list1 = []
    for number in numbers:
        if number % 2 == 0:
            list1.append(number)
        else:
            continue

    return list1


# print(list_of_even_numbers([2, 5, 7, 8, 6, 2, 3]))

a = 10
b = 11


def sums():
    global a
    global b
    return a + b


# recursion
def factorial(number: int) -> int:
    if number == 0:
        return 1
    return number * factorial(number - 1)


# print(factorial(5))


def fibonacci_sequence(number):
    if number <= 1:
        return number
    else:
        return fibonacci_sequence(number - 1) + fibonacci_sequence(number - 2)


# print(fibonacci_sequence(9))

import time

Rules = """
Rules:

The Persons Name written in this note will die within 10 seconds
if no cause of death written then the person will die with heart attack
else the cause of death will be done that is written

Note: if the person name is not in list then it will not happen.
"""

list_of_persons = ['ghost', 'x-men', 'hulk', 'kira', 'dust man', 'killer man',
                   'bandit', 'spider man']
death_list = {}


# def deathnote(name_of_the_person: str, cause_of_death=''):
#     if cause_of_death == '':
#         cause_of_death = 'Heart Attack'
#     if name_of_the_person in list_of_persons:
#         print("Wait...")
#         time.sleep(10)
#         death_list[name_of_the_person] = cause_of_death
#         list_of_persons.remove(name_of_the_person)
#         print(f"{name_of_the_person} is Killed, Cause of Death: {cause_of_death}")
#     else:
#         print("Violation of Rule")
#
# 
# ask_name = input("Enter Persons Name Here: ").lower()
# death_cause = input("Enter Cause of Death: ").title()
# deathnote(ask_name, death_cause)
# print(death_list)
# print(list_of_persons)


temperatures_w1 = [32, 34, 31, 30, 29, 28, 33]
temperatures_w2 = [31, 34, 35, 28, 29]


def calculate_average_temperature(temperature: list) -> int:
    return sum(temperature) / len(temperature)


print(calculate_average_temperature(temperatures_w1))