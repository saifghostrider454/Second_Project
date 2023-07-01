class Atm:

    def __init__(self):
        self.__pin = ''
        self.__balance = 0
        # self.menu()

    # Getter
    def get_pin(self):
        return self.__pin

    # Setter
    def set_pin(self, new_pin: str):
        if type(new_pin) == str:
            self.__pin = new_pin
        else:
            print("Invalid Pin Type")

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, new_balance: int):
        if type(new_balance) == int:
            self.__balance = new_balance
        else:
            print("Invalid balance type")

    def menu(self):
        user_input = input("""
                        Hello how can i help you?
                        1. Press 1 to create pin
                        2. Press 2 to change pin
                        3. Press 3 to check Balance
                        4. Press 4 to withdraw
                        5. Anything else to exists
                        """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input("Enter a Pin: ")
        self.__pin = user_pin

        user_balance = int(input("Enter Your Balance: "))
        self.__balance = user_balance

        print("Pin Created Successfully")
        self.menu()

    def change_pin(self):
        old_pin = input("Enter Your Old Pin: ")
        if old_pin == self.__pin:
            new_pin = input("Enter Your New Pin: ")
            self.__pin = new_pin
            print("pin changed")
            self.menu()
        else:
            print("Invalid Pin")
            self.menu()

    def check_balance(self):
        user_pin = input("Enter Your Pin: ")
        if user_pin == self.__pin:
            print(self.__balance)
            self.menu()
        else:
            print("Invalid Pin")
            self.menu()

    def withdraw(self):
        user_pin = input("Enter Your Pin: ")
        if user_pin == self.__pin:
            amount = int(input("Enter Amount: "))
            if amount <= self.__balance:
                print("withdrawn successfully")
                self.__balance -= amount
            else:
                print("Insufficient Balancee")
        else:
            print("Invalid Pin")
        self.menu()


class Fraction:

    def __init__(self, numerator: int or float, denominator: int or float) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.numerator * other.denominator

        return f"{new_numerator}/{new_denominator}"

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.numerator * other.denominator

        return f"{new_numerator}/{new_denominator}"

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.numerator * other.denominator

        return f"{new_numerator}/{new_denominator}"

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator

        return f"{new_numerator}/{new_denominator}"


class Point:

    def __init__(self, x, y):
        self.x_cod = x
        self.y_cod = y

    def __repr__(self):
        return f"<{self.x_cod},{self.y_cod}>"

    def euclidean_distance(self, other):
        return ((self.x_cod - other.x_cod) ** 2 + (self.y_cod - other.y_cod) ** 2) ** 0.5

    def distance_from_origin(self):
        return self.euclidean_distance(Point(0, 0))


class Line:

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __repr__(self):
        return f"{self.A}x + {self.B}y + {self.C} = 0"

    def point_on_line(line, point) -> str:
        if line.A * point.x_cod + line.B * point.y_cod + line.C == 0:
            return "lies on the line"
        else:
            return "does not lies on the line"

    def shortest_distance(line, point):
        return abs(line.A * point.x_cod + line.B * point.y_cod + line.C) / (line.A ** 2 + line.B ** 2) ** 0.5


# Pass by reference

class Person:

    __counter = 100

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
        self.__pid = Person.__counter
        Person.__counter += 1

    # getter
    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    @staticmethod
    def get_counter():
        return Person.__counter

    def __repr__(self):
        return f"{self.__pid, self.__name, self.__gender}"


p1 = Person('saif', 'male')
p2 = Person('kaif', 'male')
p3 = Person('merry', 'female')
p4 = Person('ghost', 'male')

# l1 = [p1, p2, p3]
#
# for i in l1:
#     print(i.get_name(), i.get_gender())
#
#
# d = {'p1': p1, 'p2': p2, 'p3': p3}
#
# for i in d:
#     print(d[i].get_name())

# print([p1, p2, p3, p4])
# print(Person.get_counter())














