# class Time:
#     """
#     What's the time? ⌚⌚
#     Create a class Time which takes two inputs: hours and minutes to instantiate.
#
#     Construct a method DisplayTime() which displays the time in AM/PM formats.
#
#     For example if the input is 14 hours and 45 mins, then this method will print 'The time is 2:45 PM'.
#     If the inputted hours exceeds 23 then print the message "The input hours should be less than 24" and if the inputted
#     minutes exceeds 59 then print the message 'The input minutes should be less than 60.'
#     Also if the input is 12 hours 30 minutes, then the displayed time would be 12:30 PM
#     Construct a method DisplayRatio() which should display the ratio of minutes to hours.
#
#     For example, (8 hours and 16 mins) should display 2. Use try, except block to account for ZeroDivisionError.
#     """
#
#     def __init__(self):
#         self.parameter = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10,
#                           11: 11, 12: 12, 13: 1, 14: 2, 15: 3, 16: 4, 17: 5, 18: 6, 19: 7,
#                           20: 8, 21: 9, 22: 10, 23: 11, 24: 00}
#         self.__hour = 0
#         self.__minute = 0
#
#     def display_time(self, hour, minute):
#         try:
#             self.__hour = hour
#             self.__minute = minute
#             if self.__hour > 24:
#                 raise ValueError('The input hours should be less than 24" and if the inputted minutes')
#             if self.__minute > 59:
#                 raise ValueError('The input minutes should be less than 60')
#             if 12 < self.__hour < 24:
#                 return f"The time is {self.parameter[self.__hour]}:{self.__minute}PM"
#             else:
#                 return f"The time is {self.parameter[self.__hour]}:{self.__minute}AM"
#         except Exception as error:
#             return error
#
#     def display_ratio(self):
#         try:
#             if self.__hour == 0 or self.__minute == 0:
#                 raise ZeroDivisionError('Cant Divide by zero')
#             return self.__minute // self.__hour
#         except Exception as error:
#             return error
#
#
# hour_min_list = [(23, 45), (34, 50), (12, 34), (14, 67), (19, 20), (2, 15), (0, 10)]
#
# time = Time()
#
# for hm in hour_min_list:
#     print(time.display_time(hm[0], hm[1]))
#     print(time.display_ratio())


# User function Template for python3

# Function to find a continuous sub-array which adds up to a given number.
# class Solution:
#     def subArraySum(self, arr, n, s):
#         arr1 = []
#         arr1.extend(arr[n: s])
#         return sum(arr1)
#
#
# s = Solution()
# print(s.subArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 12))


# n = eval(input())
# new_str = ''
# for key in n.keys():
#     new_str += key*n[key]
#
# new_str = ' '.join(new_str)
# print(new_str)


# Write Your Code Here
# players = ['Alice', 'Bob', 'Charlie', 'Diana']

# emp_dict = []
#
# for player_x in players:
#     for i in range(1, len(players)):
#         for player_y in players[i:]:
#             if player_x == player_y:
#                 continue
#             elif player_x != player_y:
#                 emp_dict.append((player_x, player_y))
#
# print(set(emp_dict))


# for i in range(0, len(players)):
#     for j in range(i, len(players)):
#         if players[i] == players[j]:
#             continue
#         elif players[i] != players[j]:
#             print(players[i], players[j])


# for i in range(0, len(players)):
#     for j in range(i, len(players)):
#         print(i, j)


"""Write a program that will determine weather when the value of temperature and humidity is provided by the user.
TEMPERATURE(C) HUMIDITY(%) WEATHER
>= 30 >=90 Hot and Humid
>= 30 < 90 Hot
<30 >= 90 Cool and Humid
<30 <90 Cool"""

# def weather(temperature, humidity):
#     if temperature >= 30 and humidity >= 90:
#         return 'Hot and Humid'
#     elif temperature >= 30 and humidity < 90:
#         return 'Hot'
#     elif temperature < 30 and humidity >= 90:
#         return 'Cool and Humid'
#     elif temperature < 30 and humidity < 90:
#         return 'Cool'
#     else:
#         return 'Dont Understand'


# def in_hand_salary(ctc_salary):
#     common_deduction = {'hra': (ctc_salary * 10) / 100, 'da': (ctc_salary * 5) / 100,
#                         'pf': (ctc_salary * 3) / 100}
#     gross_salary = ctc_salary - common_deduction['hra'] - common_deduction['da'] - common_deduction['pf']
#
#     if ctc_salary >= 500000 or ctc_salary <= 1000000:
#         return gross_salary - (ctc_salary * 10 / 100)
#     elif ctc_salary >= 1100000 or ctc_salary <= 2000000:
#         return gross_salary - (ctc_salary * 20 / 100)
#     elif ctc_salary > 2000000:
#         return gross_salary - (ctc_salary * 30 / 100)
#     else:
#         return gross_salary
#
#
# print(in_hand_salary(1000000))


# def driven(value):
#     ask_user = input("""
#           1. cm to ft
#           2. kl to miles
#           3. usd to inr
#           4. exit
#           Enter Here: """)

# class Driven:
#     def __init__(self):
#         self.menu = input("""
#           1. cm to ft
#           2. kl to miles
#           3. usd to inr
#           4. exit
#           Enter Here: """)
#         if self.menu == '1':
#             self.__cm_to_ft()
#         elif self.menu == '2':
#             self.__kl_to_miles()
#         elif self.menu == '3':
#             self.__usd_to_inr()
#         elif self.menu == '4':
#             exit()
#         else:
#             print("Invalid Input")
#
#     def __cm_to_ft(self):
#         self.__value = int(input("Enter Cm: "))
#         print(self.__value * 0.032808, 'ft')
#
#     def __kl_to_miles(self):
#         self.__value = int(input("Enter kl: "))
#         print(self.__value * 0.62137, 'miles')
#
#     def __usd_to_inr(self):
#         self.__value = int(input("Enter usd: "))
#         print(self.__value * 80, 'inr')
#
#
# d = Driven()


# write your code here
# Write a Python program to find the sum of two given integers. However, if the sum is between 15 to 20 it will return
# 20.

n1 = int(input())
n2 = int(input())


def sums(num1, num2):
    total = num1 + num2
    if 15 <= total <= 20:
        return 20
    else:
        return total


def test_happy_path_positive_integers(self):
    assert sums(5, 10) == 15


def test_happy_path_negative_integers(self):
    assert sums(-5, -10) == -15


def test_happy_path_mixed_integers(self):
    assert sums(5, -10) == -5


def test_edge_case_smallest_integers(self):
    assert sums(-2147483648, 2147483647) == -1
