# # """words = input().lower()
# #
# # emp_dict = {}
# #
# # for word in words:
# #     number_of_char = {word: words.count(word)}
# #     emp_dict.update(number_of_char)
# #
# # print(emp_dict)
# # """
# #
# # '''
# # Let's take 153 for an example
# #
# # First calculate the cube of its each digits
# #
# # 1^3 = (1 * 1 * 1) = 1
# #
# # 5^3 = (5 * 5 * 5) = 125
# #
# # 3^3= (3 * 3 * 3) = 27
# #
# # Now add the cube
# #
# # 1+125+27 = 153
# #
# # It means 153 is an Armstrong Number.
# # '''
# import sys
#
# # number = 450
# # convert_to_str = str(number)
# # list_of_numbers = []
# # for num in convert_to_str:
# #     new_number = int(num)
# #     cube = new_number * new_number * new_number
# #     list_of_numbers.append(cube)
# #
# # if sum(list_of_numbers) == number:
# #     print("Number is Armstrong")
# # elif sum(list_of_numbers) != number:
# #     print("Number is not Armstrong")
# # # '''
# # '''
# # m = int(input())
# # n = int(input())
# #
# # print(f"Biggest even number between {m} and {n}")
# #
# # if (n-1) % 2 == 0:
# #     print(n-1)
# # else:
# #     print(n)'''
# #
# # """
# #
# # emp = []
# #
# #
# # def func(numbers):
# #     if len(numbers) > 1:
# #         for number in numbers:
# #             emp.append(int(number))
# #         total = sum(emp)
# #         print(f'Step-1 Sum: {total}')
# #         if len(str(total)) > 1:
# #             emp_list = []
# #             for t in str(total):
# #                 emp_list.append(int(t))
# #             print(f'Step-2 Sum: {sum(emp_list)}')
# #         elif len(str(total)) < 2:
# #             print(total)
# #     elif len(numbers) < 1:
# #         print(numbers)
# #
# #
# # func(str(n))"""
# #
# # songs = ("American Pie", "Bohemian Rhapsody", "Come Sail Away", "Dream On", "Enter Sandman", "Free Bird",
# #          "Gimme Shelter", "Hotel California", "Imagine", "Jungleland", "Keep on Loving You", "Like a Rolling Stone",
# #          "Man in the Mirror", "November Rain", "One (U2)", "Purple Haze", "Questions 67 & 68", "Respect",
# #          "Stairway to Heaven", "Tears in Heaven", "Unity", "Viva la Vida", "When Doves Cry", "Xanadu", "Your Song",
# #          "Zombie")
# #
# # ask_name = input("Enter Your Name Here: ").title()
# #
# # for song in songs:
# #     if song[0] == ask_name[0]:
# #         print(song)
# #
# # for song in songs:
# #     if song[0] == ask_name[-1].title():
# #         print(song)
# #         break
#
# # strs = input()
# #
# # new_str = strs.split(' ')
# #
# # for string in new_str:
# #     if len(string) > 1:
# #         if (len(string) % 2) == 0:
# #             continue
# #         elif (len(string) % 2) != 0:
# #             print(string, end=' ')
#
# # my_list = [1, 2, 3, 4, 5]
# # print(my_list[1:4:2])
#
#
# # statement = "anas eagerly recommended 'the shawshank redemption' to his friends. He described the movie as a " \
# #             "captivating and emotional story of hope and friendship. His friends decided to watch it together the " \
# #             "following weekend. "
# #
# # new_value = "Arnav"
# #
# # statement = statement.replace("anas", new_value)
# # print(statement)
#
#
# # # Define sets for fruits in each basket
# # basket1 = {'apple', 'banana', 'grape', 'orange'}
# # basket2 = {'banana', 'mango', 'pineapple', 'orange'}
# #
# # # Find the total number of fruits available
# #
# # both_baskets = list(basket1) + list(basket2)
# # total_fruits = len(set(both_baskets))
# # print("Total number of fruits available:", total_fruits)
# #
# # # Find fruits available in both baskets
# # print("All the available fruits:", set(both_baskets))
# #
# # # Find only the common fruits in both baskets
# # common_fruits = basket1 & basket2   # Replace x with appropriate method
# # print("Common fruits in both baskets:", common_fruits)
# #
# # # # Find fruits unique to each basket
# # unique_basket1 = basket1.union(basket2)    # Replace x with appropriate method
# # unique_basket2 = basket2.union(basket1)    # Replace x with appropriate method
# # print("Fruits unique to basket 1:", unique_basket1)
# # print("Fruits unique to basket 2:", unique_basket2)
#
#
# # alice_gpa = 0
# #
# # mathematics_grade = 5
# # mathematics_hours = 4
# #
# # history_grade = 2
# # history_hours = 2
# #
# # science_grade = 5
# # science_hours = 3
# #
# # art_grade = 3
# # art_hours = 2
# #
# # english_grade = 2
# # english_hours = 3
# #
# #
# # multiply_grade_hour = (mathematics_grade * mathematics_hours + history_grade * history_hours + science_grade *
# #                        science_hours + art_grade * art_hours + english_grade * english_hours)
# #
# # total_hours = (mathematics_hours + history_hours + science_hours + art_hours + english_hours)
# #
# # gpa = multiply_grade_hour / total_hours
# #
# # alice_gpa += gpa
# #
# # print("%.2f" % alice_gpa)
#
#
# # stars = ""
# # emp_list = []
# #
# # for _ in range(128):
# #     emp_list.append('*')
# #
# # new = stars.join(emp_list)
# # stars = new
# # print(stars)
#
#
# # seconds = 48600
# #
# # # Write your answer below
# #
# # hour = 48600 // 60 // 60
# #
# # minute = (48600 // 60) - (hour * 60)
# #
# # print(hour)
# # print(minute)
#
#
# # n = 5
# # total = 0
# # for i in range(n + 1):
# #     total += i
# # print(total)
#
# # n = 7
# # s = 0.0
# #
# # for i in range(1, n):
# #     s = s + 1.0 / (i * i)
# # print(s)
#
# # print(bool("abc"))
#
#
# # fruits = {"apple", "banana", "cherry"}
# # more_fruits = ["orange", "mango", "grapes"]
# # more_fruits = set(more_fruits)
# # fruits.update(more_fruits)
# # print(fruits)
#
#
# # lst = [1, 2, 34, 4, 5]
# # print(sum(lst))
#
#
# class Calculator:
#     """
#     This Class Will Do Simple Ar-thematic Operations,
#     Like Calculator Does in Simple ways.
#     """
#
#     def add(self, x_number: int, y_number: int) -> float:
#         """
#         This Function can add two numbers
#         :param x_number: 2
#         :param y_number: 4
#         :return: 6
#         """
#         return x_number + y_number
#
#     def add_multiple(self, *numbers: int or float) -> int:
#         """
#         This Function will take any number of int values and return
#         the added value of your numbers
#         :param numbers: 10, 20, 30
#         :return: 60
#
#         Note: This Function cannot take user input as an argument and add rather than
#                 you have to insert value manually like add(2, 4, 6) and it will return
#             --> 12
#         """
#         total = 0
#         try:
#             for number in numbers:
#                 total += number
#         except Exception as error:
#             print(error)
#         else:
#             return total
#
#     def subtract(self, x_number: int, y_number: int) -> float:
#         """
#         This is Subtracting Function That Takes,
#         :param x_number: 50
#         :param y_number: 40
#         :return: 10
#         """
#         return x_number - y_number
#
#     def multiply(self, x_number: int, y_number: int) -> float:
#         """
#         This Function can Multiply two numbers
#         :param x_number: 4
#         :param y_number: 2
#         :return: 8
#         """
#         return x_number * y_number
#
#     def divide(self, x_number: int, y_number: int) -> float:
#         """
#         This Function can divide two numbers and return float value
#         :param x_number: 4
#         :param y_number: 2
#         :return: 2.0
#         Note: You cannot divide a number with 0.
#         """
#         try:
#             division = x_number / y_number
#         except Exception as error:
#             print(f"[{error}]")
#         else:
#             return division
#
#     def quotient(self, x_number: int, y_number: int) -> int:
#         """
#         This Function can return Quotient of the division
#         :param x_number: 10
#         :param y_number: 4
#         :return: 2.0
#         """
#         return x_number // y_number
#
#     def remainder(self, x_number: int, y_number: int) -> int:
#         """
#         This function can return Remainder of the division
#         :param x_number: 10
#         :param y_number: 4
#         :return: 2.0
#         """
#         return x_number % y_number
#
#     def square(self, x_number: int) -> int:
#         """
#         This Function can return square of the number
#         :param x_number: 4
#         :return: 16
#         """
#         return x_number ** 2
#
#     def cube(self, x_number) -> int:
#         """
#         This Function can return cube of the number
#         :param x_number: 4
#         :return: 64
#         """
#         return x_number ** 3
#
#
#
#
#
# from tkinter import *
# from tkinter import messagebox
#
#
# class PokeCalculator(Frame):
#     pokedex = {
#         'pidgey': 12,
#         'caterpie': 12,
#         'weedle': 12,
#         'rattata': 25
#     }
#     choices = pokedex.keys()
#     screen_title = 'Pokemon evolve calculator'
#
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.master = master
#         self.make_window()
#
#     def make_window(self):
#         self.master.title(self.screen_title)
#
#         L1 = Label(self, text='Candies')
#         L1.grid(column=1, row=0)
#
#         L2 = Label(self, text='Pokemon amount in storage')
#         L2.grid(column=2, row=0)
#
#         self.var = StringVar()
#         self.var.set('Pokemon')
#         self.Pokemon = OptionMenu(self, self.var, *self.choices)
#         self.Pokemon.grid(column=0, row=1)
#
#         self.Candies = Entry(self)
#         self.Candies.grid(column=1, row=1)
#
#         self.Poke_amount = Entry(self)
#         self.Poke_amount.grid(column=2, row=1)
#
#         Calculate = Button(self, text='Calculate', command=self.get_and_check)
#         Calculate.grid(column=1, row=2)
#
#     def get_and_check(self):
#         self.get_values()
#         self.check_input()
#
#     def get_values(self):
#         self.poke = self.var.get()
#         self.candies_total = self.Candies.get()
#         self.p_amount = self.Poke_amount.get()
#
#     def check_input(self):
#         string1 = 'Please select a Pokemon from the dropdown menu'
#         string2 = 'Please only enter numbers'
#         if self.poke == 'Pokemon':
#             messagebox.showinfo(self.screen_title, string1)
#         elif not self.p_amount.isdigit() or not self.candies_total.isdigit():
#             messagebox.showinfo(self.screen_title, string2)
#         else:
#             self.too_few_pokemon()
#
#     def too_few_pokemon(self):
#         candies_total = int(self.candies_total)
#         p_amount = int(self.p_amount)
#         evolve = int((candies_total - 1) / (self.pokedex[self.poke] - 1))
#         candies_needed = (p_amount * (self.pokedex[self.poke] - 1)) + 1
#         if p_amount <= evolve:
#             n = 0
#             while candies_needed <= candies_total:
#                 n = n + 1
#                 p_amount = p_amount + 1
#                 candies_needed = ((p_amount) * (self.pokedex[self.poke] - 1)) + 1
#                 candies_total = candies_total + 3
#                 evolve2 = int((candies_total - 1) / (self.pokedex[self.poke] - 1))
#             string1 = '''            You have enough candies too evolve {0} {1},
#             but you only have {2} {1} in storage and thus can only
#             evolve {2} {1}.
#             If you catch {3} more {1} you can now evolve {4} {1}.'''
#             messagebox.showinfo(self.screen_title, string1.format(evolve, self.poke,
#                                                                   self.p_amount,
#                                                                   n, evolve2))
#         else:
#             self.too_much_pokemon()
#
#     def too_much_pokemon(self):
#         candies_total = int(self.candies_total)
#         p_amount = int(self.p_amount)
#         candies_needed = (p_amount * (self.pokedex[self.poke] - 1)) + 1
#         m = 0
#         while candies_total <= candies_needed:
#             m = m + 1
#             p_amount = p_amount - 1
#             candies_needed = ((p_amount) * (self.pokedex[self.poke] - 1)) + 1
#             candies_total = candies_total + 1
#             evolve = int((candies_total - 1) / (self.pokedex[self.poke] - 1))
#         string2 = 'Transfer {0} {1} so you can evolve a total of {2} {1}.'
#         messagebox.showinfo(self.screen_title, string2.format(m, self.poke, evolve))
#
#
# root = Tk()
# app = PokeCalculator(root)
# app.pack()
# root.mainloop()
#


class Calculator:

    def __init__(self, x_value: int, y_value: int) -> None:
        self.__x_value = x_value
        self.__y_value = y_value

    def add(self):
        return self.__x_value + self.__y_value

    def subtract(self):
        return self.__x_value - self.__y_value

    def multiply(self):
        return self.__x_value * self.__y_value

    def divide(self):
        return self.__x_value / self.__y_value

    def divmod(self):
        return self.__x_value % self.__y_value

    def truediv(self):
        return self.__x_value // self.__y_value

    def square(self):
        return self.__x_value ** 2

    def cube(self):
        return self.__x_value ** 3

